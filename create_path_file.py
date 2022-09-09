import re
from match_gene_groups import match_gene_groups

ontology_file_name = 'MPheno_OBO.ontology.txt'

matching_gene_cats = match_gene_groups(ontology_file_name)

all_paths_file_name = 'all_orthomam_alignment_paths.txt'

gene_data_file_name = 'MGI_phenotype_ontology_data.txt'

def parse_full_path_file(all_paths_file):
    path_dictionary = {}

    all_paths_file = open(all_paths_file, 'r')
    full_path_content = all_paths_file.read().splitlines()
    all_paths_file.close()

    for path in full_path_content:
        if path.find('null') == -1:
            gene_match = re.search('(?<=_)([A-Za-z0-9\-]+)(?=_AA\.fas)', path)
            if gene_match:
                gene_name = gene_match.group(0)
                path_dictionary[gene_name] = path

    return path_dictionary
             
def read_gene_data_file(gene_data_file_name):
    gene_data_file = open(gene_data_file_name, 'r')
    full_gene_content = gene_data_file.read().splitlines()
    gene_data_file.close()

    gene_dictionary = {}
    for line in full_gene_content:
        split_line = line.split('\t')
        gene_symbol = split_line[0]
        phenotype_ids = split_line[4]
        phenotype_id_list = phenotype_ids.split(', ')
        gene_dictionary[gene_symbol] = phenotype_id_list

    return gene_dictionary    
    
def create_path_file(all_paths_file_name, gene_data_file_name):
    path_dictionary = parse_full_path_file(all_paths_file_name)
    gene_dictionary = read_gene_data_file(gene_data_file_name)

    final_path_file = open('output_path_file.txt', 'w')
    group_key_file = open('output_key_file.txt', 'w')

    matching_groups = match_gene_groups('MPheno_OBO.ontology.txt')
    for group in matching_groups:
        group_key_file.write(group.id + '\n')

    """ for gene_id in path_dictionary:
        path = path_dictionary[gene_id]
        if gene_id in gene_dictionary:
            gene_groups = gene_dictionary[gene_id] """

    group_key_file.close()
    final_path_file.close()

create_path_file(all_paths_file_name, gene_data_file_name)

#print(read_gene_data_file(gene_data_file_name))
#parse_full_path_file(all_paths_file_name)
