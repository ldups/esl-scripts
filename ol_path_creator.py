class Term:
    def __init__(self, id, name, is_a):
        self.id = id
        self.name = name
        self.parent = is_a

# reads tree file and splits lines into a list
treeFile = open('MPheno_OBO.ontology.txt', 'r')
treeContent = treeFile.read().splitlines()
treeFile.close()

searchTerm = 'is_a: MP:0000001'
#lines = treeFile.readlines()

# removes empty and whitespace lines from list
for line in treeContent:
    if not line or line.isspace():
        treeContent.remove(line)

# finds indeces of all occurences of '[Term]' in list
termIndexList = []
for i in range(len(treeContent)):
    if treeContent[i].find('[Term]') != -1:
        termIndexList.append(i)

termList = []
for i in range(len(termIndexList)):
    termIndex = termIndexList[i]
    # excludes top level group
    if treeContent[termIndex + 1] != "id: MP:0000001":
        id = treeContent[termIndex+1]
        name = treeContent[termIndex+2]
        if termIndex == len(termList) - 1:
            is_a = treeContent[len(treeContent) - 1]
        else:
            is_a = treeContent[termIndexList[i+1]-1]
        termList.append(Term(id, name, is_a))

print(termList[1].id)

#print(treeContent)


# too slow
'''regEx = re.compile("\[Term\]\n([\s\S]+is_a: MP:0000001)")
searchMatches = re.findall(regEx, treeContent)'''