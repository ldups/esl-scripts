# zeroes out position in all sequences
# saves sequences to new fasta file

def remove_position(fasta_path, position):
    new_fasta_path = fasta_path.split('.')[0] + '_' + str(position) + '_removed.fas'
    new_fasta = open(new_fasta_path, 'w')
    with open(fasta_path, 'r') as fasta:
        for line in fasta:
            if line.startswith('>'):
                new_fasta.write(line)
            else:
                new_seq = line[:position] + '.' + line[position+1:]
                new_fasta.write(new_seq)
    new_fasta.close()
