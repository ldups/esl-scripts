def match_gene_groups_top_level(term_list):
    '''finds top level groups within a term_list
    faster than recursive match_gene_group_bottom if looking for top level
    '''
    matching_category_list = []

    # top level groups have MP:0000001 as parent
    search_term = 'MP:0000001'

    for term in term_list:
        parents = term.parent
        for parent in parents:
            if parent == search_term:
                matching_category_list.append(term)

    return matching_category_list



 
