
def find_term_by_id(term_list, id):
    ''' finds a Term object in a list of terms by id'''
    for term in term_list:
        if term.id == id:
            return term

def find_term_by_parent(term_list, parent_id):
    ''' finds a Term object in a list of terms by parent id'''
    matching_term_list = []
    for term in term_list:
        for parent in term.parents:
            if parent == parent_id:
                matching_term_list.append(term)
    return matching_term_list
    

def find_group_level(group, term_list):
    ''' finds group level of Term object in list of terms recursively
        top level (1) = is_a 'MP0000001'
        second level (2) = any group under top level
    '''
    parent_object = group

    if parent_object.parents[0] == 'MP:0000001':
        return 1

    for term in term_list:
        if term.id == parent_object.parents[0]:
            parent_object = term
            break
    
    return find_group_level(parent_object, term_list) + 1 

def add_level_to_term_list(term_list):
    ''' calls find_group_level for each term in list and adds level as property of Term object'''
    for term in term_list:
        level = find_group_level(term, term_list)
        term.level = level
    return term_list

def find_term_by_level(term_list, level):
    matching_groups = []
    for term in term_list:
        if term.level == level:
            matching_groups.append(term)
    return matching_groups


