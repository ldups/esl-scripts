import re

def find_term_by_id(id, term_dict): 
    '''finds a term by id from a list of terms'''
    for term in term_dict:
        if id == term.id:
            return term
    return None

def parse_full_path_file(all_paths_file):
    '''from path file, creates a dictionary in form {gene name: path}'''
    path_dictionary = {}

    all_paths_file = open(all_paths_file, 'r')
    full_path_content = all_paths_file.read().splitlines()
    all_paths_file.close()

    for path in full_path_content:
        if path.find('null') == -1:
            # regex searching for GeneName_AA.fas, captures GeneName
            gene_match = re.search('(?<=_)([A-Za-z0-9\-]+)(?=_AA\.fas)', path)
            if gene_match:
                gene_name = gene_match.group(0)
                path_dictionary[gene_name] = path

    return path_dictionary
             

def create_path_file(all_paths_file_name, gene_mp_dictionary, term_list, min_gene_num, max_gene_num, output_file_base_name):
    '''writes two files: 
    1) overlapping path file to be used as ESL input
    2) key file with list of MP categories included in path file and details
    argument 1: file name of file containing all individual paths on separate lines
    argument 2: dictionary relating each gene to list of MPs it is included in
    argument 3: list of all term objects in tree
    argument 4: minimum number of genes in MP group for group to be included in output
    argument 5: base name for output files'''

    print('in create_path_file')
    path_dictionary = parse_full_path_file(all_paths_file_name)
    final_path_file_name = 'output_path_file_' + output_file_base_name + '.txt'
    group_key_file_name = 'output_key_file_' + output_file_base_name + '.txt'
    final_path_file = open(final_path_file_name, 'w')
    group_key_file = open(group_key_file_name, 'w')
    print('files opened')

    group_dictionary = {}
    for group_list in gene_mp_dictionary.values():
        for group in group_list:
            if group not in group_dictionary:
                group_dictionary[group] = []

    for gene_name in path_dictionary:
        if gene_name in gene_mp_dictionary:
            groups = gene_mp_dictionary[gene_name]
            for group in groups:
                path = path_dictionary[gene_name]
                if path not in group_dictionary[group]:
                    group_dictionary[group].append(path)

    print('writing to file')

    group_key_file.write('Id\tName\tNumber of paths\n')
    num_groups_written = 0
    num_groups_in_dict = len(group_dictionary)
    for group in group_dictionary:
        term = find_term_by_id(group, term_list)
        id = group
        name = term.name
        num_paths = len(group_dictionary[group])
        if num_paths >= min_gene_num and num_paths <= max_gene_num:
            group_key_file.write(id + '\t' + name + '\t' + str(num_paths) + '\n')

            for path in group_dictionary[group]:
                if group_dictionary[group].index(path) != len(group_dictionary[group]) - 1:
                    final_path_file.write(path + ',')
                else:
                    final_path_file.write(path)
            if num_groups_written < num_groups_in_dict - 1:
                final_path_file.write('\n')
        num_groups_written += 1

    group_key_file.close()
    final_path_file.close()

# function used when searching for top level MPs- faster than recursion from bottom of tree
def read_gene_data_file_top_level(gene_data_file_name):
    '''from phenotype ontology data file, creates dictionary in form {gene name: [top level phenotype ids]}'''
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


