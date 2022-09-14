def read_MGI_GenePheno(geno_pheno_name, pheno_ont_name):

    gene_pheno_file = open(geno_pheno_name, 'r')
    pheno_ont_file = open(pheno_ont_name, 'r')
    mp_mgi_dictionary = {}
    for line in gene_pheno_file:
        mp = line.split('\t')[4]
        mgis = line.split('\t')[5].split('|')
        for mgi in mgis:
            mp_mgi_dictionary[mgi] = mp

    for line in pheno_ont_file:
        
    

        





    gene_pheno_file.close()
    pheno_ont_file.close()

read_MGI_GenePheno('MGI_GenePheno.rpt.txt', 'MGI_phenotype_ontology_data.txt')