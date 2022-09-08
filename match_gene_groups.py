from build_ontology_term_list import build_ontology_term_list

def match_gene_groups(file_name):
    term_list = build_ontology_term_list(file_name)

    search_term = "MP:0000001"

    matching_category_list = []

    for term in term_list:
        if term.parent == search_term:
            matching_category_list.append(term)

    return matching_category_list


