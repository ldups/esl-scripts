# esl-scripts

## overlapping_paths
### Function: creates path file organized into GO groups, used in ESL overlapping input
#### File inputs required:
 1) OBO ontology file (MPheno_OBO.ontology.txt in main)
    - Contains list of GO terms and details like ID, name, and parents
    - Can include different properties than example, like is_obsolete or synonyms
    - Required properties: id, name, is_a
    - Example format:
```
[Term]
id: MP:0000015
name: abnormal ear pigmentation
def: "anomaly in the coloration of the skin of the outer ear due to changes in the amount, shape, or distribution of cells producing pigment" [MGI:cwg, MGI:llw2]
is_a: MP:0002095 ! abnormal skin pigmentation
is_a: MP:0030530 ! abnormal outer ear skin morphology
```

2) MGI_Gene_Pheno rpt file (MGI_GenePheno.rpt.txt in main)
    - Each line contains MGI ID and one lowest-level MP ID MGI ID is associated with
    - Script reads column 5 (MP ID) and column 7 (MGI ID)
    - More details about format can be found on [MGI site](http://www.informatics.jax.org/downloads/reports/index.html#go) under Alleles and Phenotypes heading (number 9)
    - Example format:

```
Rb1<tm1Tyj>/Rb1<tm1Tyj>	Rb1<tm1Tyj>	MGI:1857242	involves: 129S2/SvPas	MP:0000600	12529408	MGI:97874	MGI:2166359
```

3) MGI_phenotype_ontology file (MGI_phenotype_ontology_data.txt in main)
    - Relates gene name, MGI ID, and list of highest-level MP IDs associated with gene (comma-delimited)
    - More details about format can be found on [MGI site](http://www.informatics.jax.org/downloads/reports/index.html#go) under Alleles and Phenotypes heading (number 2)
    - Example format:

```
Human_Marker_Symbol	Human_Entrez_Gene_ID	Mouse_Marker_Symbol	MGI_Marker_Accession_ID	High-level_Mammalian_Phenotype_ID	empty_col
A2ML1	144568	Mug1	MGI:99837	MP:0005370, MP:0005376, MP:0005384, MP:0005387, MP:0010768	
```

4) Path file (overlapping_paths\all_orthomam_alignment_paths.txt in main)
    - File containing all paths to be considered for inclusion in final output path file
    - Path should contain \_GeneName\_ before file extension