# represents a term in ontology file with id, name, and 'is_a' info
class Term:
    def __init__(self, id, name, is_a):
        self.id = id
        self.name = name
        self.parent = is_a

def parse_ID(idText):
    return idText[4:]

def parse_name(nameText):
    return nameText[6:]

def parse_inheritance(is_a_text):
    return is_a_text[6:15]

#searchTerm = 'is_a: MP:0000001'

def extract_terms(treeContent, termIndexList):
    termList = []
    for i in range(len(termIndexList)):
        termIndex = termIndexList[i]
        # if statement excludes top level group
        if treeContent[termIndex + 1] != "id: MP:0000001":
            id = treeContent[termIndex+1]
            name = treeContent[termIndex+2]
            # if last term, selects overall last item to avoid index out of bounds error
            if i == len(termIndexList) - 1:
                is_a = treeContent[len(treeContent) - 1]
            else:
                is_a = treeContent[termIndexList[i+1]-1]
            #removes obsolete terms
            if not is_a.startswith("is_obsolete"):
                # creates term object representing term with id, name, and is_a
                termList.append(Term(parse_ID(id), parse_name(name), parse_inheritance(is_a)))
    # returns a list of term objects
    return termList

# parses ontology file and converts terms in file into list of Term objects
def build_ontology_term_list(filePath):
    # reads tree file and splits lines into a list
    treeFile = open(filePath, 'r')
    treeContent = treeFile.read().splitlines()
    treeFile.close()

    # removes empty and whitespace lines from list
    for line in treeContent:
        if not line or line.isspace():
            treeContent.remove(line)

    # finds indices of all occurences of '[Term]' in list
    termIndexList = []
    for i in range(len(treeContent)):
        if treeContent[i].find('[Term]') != -1:
            termIndexList.append(i)

    # calls function that creates list of term objects from content of tree
    return extract_terms(treeContent, termIndexList)

termList = build_ontology_term_list('MPheno_OBO.ontology.txt')