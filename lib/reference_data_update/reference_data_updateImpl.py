# -*- coding: utf-8 -*-
#BEGIN_HEADER
import json
from utils import RefUtils
#END_HEADER


class reference_data_update:
    '''
    Module Name:
    reference_data_update

    Module Description:
    A KBase module: reference_data_update
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.1"
    GIT_URL = "https://github.com/JamesJeffryes/reference_data_update.git"
    GIT_COMMIT_HASH = "32c2e6869e1561d9a7a7f328efad730cf94d912b"

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.ref_utils = RefUtils(config)
        #END_CONSTRUCTOR
        pass


    def fix_genome_taxonomies(self, ctx, params):
        """
        :param params: instance of type "UpdateTaxaParams" -> structure:
           parameter "target_workspace" of String, parameter
           "selection_params" of String, parameter "bad_word" of String
        :returns: instance of type "UpdateTaxaResults" -> structure:
           parameter "results" of String
        """
        # ctx is the context object
        # return variables are: results
        #BEGIN fix_genome_taxonomies
        print(params)
        for req in {'target_workspace', 'selection_params', 'bad_word'}:
            if req not in params:
                raise ValueError("Must specify {}".format(req))
        selection_dict = json.loads(params["selection_params"])
        for req in {"before", "after"}:
            if req not in selection_dict:
                raise ValueError("Must specify {}".format(req))
        params.update(selection_dict)
        results = self.ref_utils.fix_taxonomy(params)
        #END fix_genome_taxonomies

        # At some point might do deeper type checking...
        if not isinstance(results, dict):
            raise ValueError('Method fix_genome_taxonomies return value ' +
                             'results is not type dict as required.')
        # return the results
        return [results]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
