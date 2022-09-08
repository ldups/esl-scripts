from build_ontology_term_list import build_ontology_term_list

term_list = build_ontology_term_list('MPheno_OBO.ontology.txt')

search_term = "MP:0000001"

matching_category_list = []

for term in term_list:
    if term.parent == search_term:
        matching_category_list.append(term)


