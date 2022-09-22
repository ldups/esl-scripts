def create_branch_length_input(rate_file_path, output_file_base_name, positive_char, negative_char):
    '''function creates an input file for ESL with branch length data coded as a fasta file
    argument 1: path for file containing rates or rate shifts between species
    argument 2: base name for fasta output file
    argument 3: character to be used as code for greater rate shift
    argument 4: character to be used as code for lower rate shift
    outputs fasta file with sequence for each species containing only positive and negative characters'''
    
    rate_file_path = 'branch_lengths\echo_molec_rates.txt'
    output_file_base_name = 'output_branch_lenghts'
    output_file_path = 'branch_lengths\\' + output_file_base_name + '.fasta'
    positive_char = 'A'
    negative_char = 'T'

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
                    if species1_rates[i] > species2_rates[i]:
                        output_file.write(positive_char)
                        species2_symbol_list.append(negative_char)
                    else:
                        output_file.write(positive_char)
                        species2_symbol_list.append(negative_char)
                output_file.write('\n')
                output_file.write('>' + species2_name + '\n')
                for symbol in species2_symbol_list:
                    output_file.write(symbol)
                output_file.write('\n')
            
    print('Output fasta file written successfully.')
    rate_file.close()
    output_file.close()

