
from build_ontology_term_list import build_ontology_term_list

def find_term_by_id(term_list, id):
    for term in term_list:
        if term.id == id:
            return term

def find_term_by_parent(term_list, parent_id):
    matching_term_list = []
    for term in term_list:
        for parent in term.parents:
            if parent == parent_id:
                matching_term_list.append(term)
    return matching_term_list


def find_level_bottom(term_list, mp):
    term = find_term_by_id(term_list, mp)
    term = find_term_by_parent(term_list, 'MP:0005168')
    print(term[0].name)
    

#finds level of term object
# top level = is_a 'MP0000001'
# second level = any group under top level

def find_group_level(group, term_list, id_level_dict):
    parent_object = group

    if parent_object.parents[0] == 'MP:0000001':
            return 1

    for term in term_list:
        if term.id == parent_object.parents[0]:
            parent_object = term
            break
    
    return find_group_level(parent_object, term_list) + 1 

id_level_dict = {}
term_list = build_ontology_term_list('MPheno_OBO.ontology.txt')
for term in term_list:
    level = find_group_level(term, term_list)
    term.level = level

""" print(term_list[92].level)
print(term_list[172].level)
print(term_list[905].level) """