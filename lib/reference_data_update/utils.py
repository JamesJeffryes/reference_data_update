from collections import namedtuple
from datetime import timedelta
from dateutil import parser

from KBaseSearchEngine.KBaseSearchEngineClient import KBaseSearchEngine
from Workspace.WorkspaceClient import Workspace


class RefUtils:
    def __init__(self, config):
        self.ws = Workspace(config['workspace-url'])
        self.kbse = KBaseSearchEngine(config['search-url'])

    def retrieve_taxon(self, taxon_wsname, scientific_name):
        """
        _retrieve_taxon: retrieve taxonomy and taxon_reference

        """
        TaxTuple = namedtuple("TaxTuple",
                              ['taxonomy', 'taxon_reference', 'domain', 'genetic_code'])
        default = TaxTuple('Unconfirmed Organism: ' + scientific_name,
                           'ReferenceTaxons/unknown_taxon', 'Unknown', 11)

        def extract_values(search_obj):
            return TaxTuple(search_obj['data']['scientific_lineage'],
                            taxon_wsname + "/" + search_obj['object_name'],
                            search_obj['data']['domain'],
                            search_obj['data'].get('genetic_code', 11))

        search_params = {
            "object_types": ["taxon"],
            "match_filter": {
                "lookup_in_keys": {
                    "scientific_name": {"value": scientific_name}},
                "exclude_subobjects": 1
            },
            "access_filter": {
                "with_private": 0,
                "with_public": 1
            },
            "sorting_rules": [{
                "is_object_property": 0,
                "property": "timestamp",
                "ascending": 0
            }]
        }
        objects = self.kbse.search_objects(search_params)['objects']
        if len(objects):
            if len(objects) > 100000:
                raise RuntimeError("Too many matching taxons returned for {}. "
                                   "Potential issue with searchAPI.".format(scientific_name))
            return extract_values(objects[0])
        search_params['match_filter']['lookup_in_keys'] = {
            "aliases": {"value": scientific_name}
        }
        objects = self.kbse.search_objects(search_params)['objects']
        if len(objects):
            return extract_values(objects[0])
        return default

    def fix_taxonomy(self, params):
        workspace = params['target_workspace']
        bad_word = params['bad_word']
        after = params['after']
        before = params['before']
        ws = self.ws
        events = {
            "ok": 0,
            "fixed": 0,
            "unique": 0,
            "no_revert": 0,
            "error": 0
        }
        last_time = ""
        chunk = 0
        list_params = {'workspaces': [workspace], 'type': 'KBaseGenomes.Genome-9', 'after': after,
                       'before': before, 'limit': 1000, 'includeMetadata': 1}
        infos = ws.list_objects(list_params)
        while infos:
            print(len(infos))
            for info in infos:
                last_time = info[3]
                if bad_word not in info[-1]['Taxonomy']:
                    events["ok"] += 1
                    continue
                corrected_taxa = self.retrieve_taxon("ReferenceTaxons", info[-1]['Name'])
                curr_ref = str(info[6]) + '/' + str(info[0]) + '/' + str(info[4])
                try:
                    data = ws.get_objects2({'objects': [{'ref': curr_ref}]})['data'][0]['data']
                    data.update(corrected_taxa._asdict())
                    ws.save_objects({'workspace': workspace, 'objects': [
                        {'type': 'KBaseGenomes.Genome', 'data': data, 'objid': info[0]}]})
                    print(curr_ref, corrected_taxa)
                    events["fixed"] += 1
                except:
                    print('Failed to save: {}'.format(curr_ref))
                    events["error"] += 1
            list_params['after'] = (parser.parse(last_time) + timedelta(seconds=1)).strftime('%Y-%m-%dT%H:%M:%S+0000')
            infos = ws.list_objects(list_params)
            chunk += 1
            print("Finished chunk {}. Though {}".format(chunk, last_time))
        print(events)
        print(last_time)
        return {"events": events, "last_timepoint_processed": last_time}




