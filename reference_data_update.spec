/*
A KBase module: reference_data_update
*/

module reference_data_update {

    typedef structure {
        string target_workspace;
        string selection_params;
        string bad_word;
    } UpdateTaxaParams;

    typedef structure {
        string results;
    } UpdateTaxaResults;

    funcdef fix_genome_taxonomies(UpdateTaxaParams params) returns (UpdateTaxaResults results)  authentication required;
};
