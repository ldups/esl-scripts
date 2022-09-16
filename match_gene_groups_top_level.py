from build_ontology_term_list import build_ontology_term_list

def match_gene_groups_top_level(file_name):
    term_list = build_ontology_term_list(file_name)
    matching_category_list = []

    search_term = 'MP:0000001'

    for term in term_list:
        parents = term.parent
        for parent in parents:
            if parent == search_term:
                matching_category_list.append(term)

    return matching_category_list



 
