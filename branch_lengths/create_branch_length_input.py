from pathlib import Path

def create_branch_length_input(rate_file_path, output_file_base_name, positive_char, negative_char, threshold):
    '''function creates an input file for ESL with branch length data coded as a fasta file
    argument 1: path for file containing rates or rate shifts between species
    argument 2: base name for fasta output file
    argument 3: character to be used as code for greater rate shift
    argument 4: character to be used as code for lower rate shift
    argument 5: threshold percentage difference to assign one rate a positive character
    outputs fasta file with sequence for each species containing only positive and negative characters'''

    #TO DO: only works in directory I'm in, change to accepting full path + base name
    output_file_path = 'branch_lengths\\' + output_file_base_name + '.fasta'

    rate_file = open(rate_file_path, 'r')
    output_file = open(output_file_path, 'w')

    at_rate_shift = False
    at_end = False
    while not at_rate_shift:
        line = rate_file.readline()
        if line.startswith('RATE SHIFTS'):
            at_rate_shift = True
            #skips header line
            rate_file.readline()
            while not at_end:
                line = rate_file.readline().strip()
                if not line: 
                    at_end = True
                    break
                species1 = line
                species2 = rate_file.readline().strip()
                species1_name = species1.split('\t')[0]
                species1_rates = species1.split('\t')[1:]
                species2_name = species2.split('\t')[0]
                species2_rates = species2.split('\t')[1:]
                species2_symbol_list = []
                output_file.write('>' + species1_name + '\n')
                for i in range(0, len(species1_rates)):
                    if float(species1_rates[i]) / float(species2_rates[i]) - 1 > threshold:
                        output_file.write(positive_char)
                        species2_symbol_list.append(negative_char)
                    elif float(species2_rates[i]) / float(species1_rates[i]) - 1 > threshold:
                        output_file.write(negative_char)
                        species2_symbol_list.append(positive_char)
                    else:
                        output_file.write(negative_char)
                        species2_symbol_list.append(negative_char)
                output_file.write('\n')
                output_file.write('>' + species2_name + '\n')
                for symbol in species2_symbol_list:
                    output_file.write(symbol)
                output_file.write('\n')
            
    print('Output fasta file written successfully.\nFasta file path: ', output_file_path)
    rate_file.close()
    output_file.close()

def create_branch_length_input_ol(rate_file_path, output_file_base_name, positive_char, negative_char, threshold):
    '''function creates input files for overlapping ESL with branch length data coded fasta files
    argument 1: path for file containing rates or rate shifts between species
    argument 2: base name for fasta output file
    argument 3: character to be used as code for greater rate shift
    argument 4: character to be used as code for lower rate shift
    argument 5: threshold percentage difference to assign one rate a positive character
    outputs 1 fasta file per gene and 1 master path file containing list of fasta file paths'''


    rate_file = open(rate_file_path, 'r')
    all_path_file_path = output_file_base_name + 'all_paths.txt'
    all_path_file = open(all_path_file_path, 'w')

    at_rate_shift = False
    at_end = False
    while not at_rate_shift:
        line = rate_file.readline()
        if line.startswith('RATE SHIFTS'):
            at_rate_shift = True
            gene_names = rate_file.readline().strip().split('\t')[1:]
            while not at_end:
                line = rate_file.readline().strip()
                if not line: 
                    at_end = True
                    break
                species1 = line
                species2 = rate_file.readline().strip()
                species1_name = species1.split('\t')[0]
                species1_rates = species1.split('\t')[1:]
                species2_name = species2.split('\t')[0]
                species2_rates = species2.split('\t')[1:]
                
                for i in range(0, len(species1_rates)):
                    gene_name = gene_names[i]
                    output_path = output_file_base_name + gene_name + '.fasta'
                    
                    # won't work if file already exists and has stuff in it -> add error
                    output_file_object = Path(output_path)
                    if not output_file_object.is_file():
                        all_path_file.write(output_path)
                        if not i == len(species1_rates) - 1:
                            all_path_file.write('\n')
                    output_file = open(output_path, 'a')
                    
                    print('Writing to: '+ output_path)

                    output_file.write('>' + species1_name + '\n')

                    if float(species1_rates[i]) / float(species2_rates[i]) - 1 > threshold:
                        output_file.write(positive_char + '\n')
                        output_file.write('>' + species2_name + '\n')
                        output_file.write(negative_char + '\n')
                    elif float(species2_rates[i]) / float(species1_rates[i]) - 1 > threshold:
                        output_file.write(negative_char + '\n')
                        output_file.write('>' + species2_name + '\n')
                        output_file.write(positive_char + '\n')
                    else:
                        output_file.write(negative_char + '\n')
                        output_file.write('>' + species2_name + '\n')
                        output_file.write(negative_char + '\n')
                    output_file.close()
                

    print('Output fasta files written successfully.')
    all_path_file.close()
    rate_file.close()

create_branch_length_input_ol('branch_lengths/echo_molec_rates.txt', 'branch_lengths/echo_ol_thresh2/', 'A', 'T', 2)