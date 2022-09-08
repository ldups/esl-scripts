import re
from match_gene_groups import match_gene_groups

file_name = 'MPheno_OBO.ontology.txt'

matching_gene_cats = match_gene_groups(file_name)

full_file_path = 'all_orthomam_alignment_paths.txt'


def parse_full_path_file(full_file_path):
    path_dictionary = {}

    full_file_path = open(full_file_path, 'r')
    full_path_content = full_file_path.read().splitlines()
    full_file_path.close()

    for path in full_path_content:
        if path.find('null') != -1:
            print('this one is null')
        else:
            gene_name = re.search('(?<=_)[A-Z0-9]+(?=_AA\.fas)', path)
            print(gene_name)

parse_full_path_file(full_file_path)
