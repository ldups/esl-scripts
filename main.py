'''file contains sample workflow to build overlapping path file'''

from build_ontology_term_list import build_ontology_term_list
from find_level_bottom import add_level_to_term_list
from read_MGI_GenePheno import read_MGI_GenePheno
from match_gene_group_bottom import match_gene_group_bottom
from create_path_file import create_path_file

print('starting main')
term_list = build_ontology_term_list('MPheno_OBO.ontology.txt')
print('term list created')
term_list = add_level_to_term_list(term_list)
print('levels added to term list')
gene_ll_mp_dictionary = read_MGI_GenePheno('MGI_GenePheno.rpt.txt', 'MGI_phenotype_ontology_data.txt')
print('gene_ll_mp_dict created')
gene_mp_dictionary = match_gene_group_bottom(1000, 4, term_list, gene_ll_mp_dictionary)
create_path_file('all_orthomam_alignment_paths.txt', gene_mp_dictionary, term_list, 5, 300, 'level_4_down_correct') 



