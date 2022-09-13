import re
import time
from match_gene_groups import match_gene_groups
from match_gene_groups import Search_method

ontology_file_name = 'MPheno_OBO.ontology.txt'

all_paths_file_name = 'all_orthomam_alignment_paths.txt'

gene_data_file_name = 'MGI_phenotype_ontology_data.txt'

def find_term_by_id(id, term_dict):
    for term in term_dict:
        if id == term.id:
            return term
    return None

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

    final_path_file = open('output_path_file_level_4.txt', 'w')
    group_key_file = open('output_key_file.txt_level_4', 'w')

    matching_groups = match_gene_groups('MPheno_OBO.ontology.txt', Search_method.LEVEL, search_term = None, level = 4)
    group_dictionary = {}
    for group in matching_groups:
        group_dictionary[group.id] = []

    for gene_name in path_dictionary:
        if gene_name in gene_dictionary:
            groups = gene_dictionary[gene_name]
            for group in groups:
                if group in group_dictionary:
                    group_dictionary[group].append(path_dictionary[gene_name])

    group_key_file.write('Id\tName\tNumber of paths\n')
    for group in group_dictionary:
        term = find_term_by_id(group, matching_groups)
        id = group
        name = term.name
        num_paths = len(group_dictionary[group])
        if num_paths > 0:
            group_key_file.write(id + '\t' + name + '\t' + str(num_paths) + '\n')

            
            for path in group_dictionary[group]:
                if group_dictionary[group].index(path) != len(group_dictionary[group]) - 1:
                    final_path_file.write(path + ',')
                else:
                    final_path_file.write(path)
            final_path_file.write('\n')

    group_key_file.close()
    final_path_file.close()

start_time = time.time()
create_path_file(all_paths_file_name, gene_data_file_name)
print("--- %s seconds ---" % (time.time() - start_time))

