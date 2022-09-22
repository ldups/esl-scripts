rate_file = open('branch_lengths\echo_molec_rates.txt', 'r')
output_file = open('branch_lengths\output_branch_lengths_try2.fasta', 'w')
line_num = 0
at_rate_shift = False
at_end = False
while not at_rate_shift:
    line = rate_file.readline()
    if line.startswith('RATE SHIFTS'):
        at_rate_shift = True
        header_line = rate_file.readline()
        species_count = 0
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
                    output_file.write('A')
                    species2_symbol_list.append('T')
                else:
                    output_file.write('T')
                    species2_symbol_list.append('A')
            output_file.write('\n')
            output_file.write('>' + species2_name + '\n')
            for symbol in species2_symbol_list:
                output_file.write(symbol)
            output_file.write('\n')
            

rate_file.close()
output_file.close()