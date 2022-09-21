def read_MGI_GenePheno(geno_pheno_name, pheno_ont_name):
    ''' 
    reads geno_pheno file and pheno_ontology file and creates dictionary relating gene name and lowest level mammalian phenotype ids
    argument 1: geno_pheno_name: file name for file relating MGI and lowest level MP
    argument 2: pheno_ont_name: file name for file relating MGI and gene name
    returns dictionary in form {gene name: [list of lowest level MPs]}
    '''
    # in current case, gene_pheno_file = MGI_GenePheno.rpt.txt
    gene_pheno_file = open(geno_pheno_name, 'r')
    # in current case, pheno_ont_file = MGI_phenotype_ontology_data.txt
    pheno_ont_file = open(pheno_ont_name, 'r')

    # creates dictionary from gene_pheno file in form {mgi:[mp]}
    mgi_mp_dictionary = {}
    for line in gene_pheno_file:
        mp = line.split('\t')[4]
        mgis = line.split('\t')[6].split('|')
        for mgi in mgis:
            if mgi not in mgi_mp_dictionary:
                mgi_mp_dictionary[mgi] = []
            mgi_mp_dictionary[mgi].append(mp)

    mgi_name_dictionary = {}
    # skips header line
    next(pheno_ont_file)
    # creates dictionary in form {mgi: gene name}
    for line in pheno_ont_file:
        gene_name = line.split('\t')[0]
        mgi = line.split('\t')[3]
        mgi_name_dictionary[mgi] = gene_name

    # creates dictionary in form {gene name: [lowest level mps]}
    gene_mp_dictionary = {}
    for mgi in mgi_mp_dictionary:
        if mgi in mgi_name_dictionary:
            gene_name = mgi_name_dictionary[mgi]
            mp = mgi_mp_dictionary[mgi]
            if gene_name not in gene_mp_dictionary:
                gene_mp_dictionary[gene_name] = []
            gene_mp_dictionary[gene_name].extend(mp)

    gene_pheno_file.close()
    pheno_ont_file.close()

    return gene_mp_dictionary

