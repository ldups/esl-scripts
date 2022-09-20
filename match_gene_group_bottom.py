from distutils.command.build import build
from find_level_bottom import find_term_by_id
from build_ontology_term_list import build_ontology_term_list
from find_level_bottom import add_level_to_term_list

def match_gene_group_bottom(lowest_level, highest_level, term_list, gene_ll_mp_dictionary):
    ''' 
    creates dictionary relating gene name and nth level mammalian phenotype IDs that gene belongs to
    argument 1: integer representing lowest level (starting from top) desired (inclusive)
    argument 2: integer representing highest level (starting from top) desired (inclusive)
    (highest_level should be a lower number than lowest_level)
    argument 2: list of Term objects- term objects must have level property != None
    argument 3: dictionary in form {gene name: [list of lowest level MPs]}
    returns dictionary in form {gene name: [list of nth level MPs]}
    '''
    gene_n_level_dictionary = {}
    for gene in gene_ll_mp_dictionary:
        matching_group_list = []
        ll_mps = gene_ll_mp_dictionary[gene]
        for ll_mp in ll_mps:
            ll_mp_term = find_term_by_id(term_list, ll_mp)
            level = ll_mp_term.id
            """ while level < n:
                parent_ids = ll_mp_term.parents """



def find_n_levels(lowest_level, highest_level, term_list, term_id):
    '''recursive function that starts at a lowest level mp and travels up the tree until it reaches the nth level'''
    matching_groups = []
    term = find_term_by_id(term_list, term_id)
    if term.level <= lowest_level and term.level >= highest_level:
        if term.id not in matching_groups:
            matching_groups.append(term.id)
    
    if term.level > highest_level:
        for parent in term.parents:
                matching_terms = find_n_levels(lowest_level, highest_level, term_list, parent)
                for term in matching_terms:
                    if term not in matching_groups:
                        matching_groups.append(term)
    return matching_groups


term_list = build_ontology_term_list('MPheno_OBO.ontology.txt')
term_list = add_level_to_term_list(term_list)
print(find_n_levels(3, 2, term_list, 'MP:0020364')) 
 