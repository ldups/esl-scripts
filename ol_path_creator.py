class Term:
    def __init__(self, id, name, defin, is_a):
        self.id = id
        #self.name = name
        #self.defin = defin
        #self.parent = is_a

treeFile = open("MPheno_OBO.ontology.txt", "r")
searchTerm = "is_a: MP:0000001"
#lines = treeFile.readlines()
treeContent = treeFile.read().splitlines()
termList = []
for i in range(len(treeContent)):
    line = treeContent[i]
    if line.find("[Term]") != -1:
        id = treeContent[i+1]
        termList.append(Term(id))


#print(treeContent)
treeFile.close()

# too slow
'''regEx = re.compile("\[Term\]\n([\s\S]+is_a: MP:0000001)")
searchMatches = re.findall(regEx, treeContent)'''