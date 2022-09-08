# represents a term in ontology file with id, name, and 'is_a' info
from re import I


class Term:
    def __init__(self, id, name, is_a):
        self.id = id
        self.name = name
        self.parent = is_a

def parse_ID(id_text):
    return id_text[4:]

def parse_name(name_text):
    return name_text[6:]

def parse_inheritance(is_a_text):
    return is_a_text[6:16]

def extract_terms(tree_content, term_index_list):
    term_list = []
    for i in range(len(term_index_list)):
        term_index = term_index_list[i]
        # if statement excludes top level group
        if tree_content[term_index + 1] != 'id: MP:0000001':
            is_obsolete = False
            id = tree_content[term_index+1]
            name = tree_content[term_index+2]

            # parses term to find obsolescence and is_a line
            start_index = term_index + 3
            if i == len(term_index_list) - 1:
                end_index = len(tree_content) - 1
            else:
                end_index = term_index_list[i+1]

            for j in range(start_index, end_index):
                line = tree_content[j]
                if line.find('is_obsolete: true') != -1:
                    is_obsolete = True
                    break
                elif line.startswith('is_a'):
                    is_a = line
            
            if not is_obsolete:
                # creates term object representing term with id, name, and is_a
                term_list.append(Term(parse_ID(id), parse_name(name), parse_inheritance(is_a)))
    
    # returns a list of term objects
    return term_list

# parses ontology file and converts terms in file into list of Term objects
def build_ontology_term_list(file_path):
    # reads tree file and splits lines into a list
    tree_file = open(file_path, 'r')
    tree_content = tree_file.read().splitlines()
    tree_file.close()

    # removes empty and whitespace lines from list
    for line in tree_content:
        if not line or line.isspace():
            tree_content.remove(line)

    # finds indices of all occurences of '[Term]' in list
    term_index_list = []
    for i in range(len(tree_content)):
        if tree_content[i].find('[Term]') != -1:
            term_index_list.append(i)

    # calls function that creates list of term objects from content of tree
    return extract_terms(tree_content, term_index_list)






""" # if last term, selects overall last item to avoid index out of bounds error
            if i == len(term_index_list) - 1:
                is_a = tree_content[len(tree_content) - 1]
            else:
                is_a = tree_content[term_index_list[i+1]-1]
            #removes obsolete terms """