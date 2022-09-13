from build_ontology_term_list import build_ontology_term_list

def match_gene_groups(file_name):
    term_list = build_ontology_term_list(file_name)

    search_term = 'MP:0000001'

    matching_category_list = []

    for term in term_list:
        if term.parent == search_term:
            matching_category_list.append(term)

    return matching_category_list

#finds level of term object
# top level = is_a 'MP0000001'
# second level = any group under top level
def find_group_level(group, term_list):
    parent_object = group

    if parent_object.parent == 'MP:0000001':
            return 1

    for term in term_list:
        if term.id == parent_object.parent:
            parent_object = term
            break
    
    return find_group_level(parent_object, term_list) + 1


term_list = build_ontology_term_list('MPheno_OBO.ontology.txt')
 
