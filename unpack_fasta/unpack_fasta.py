def unpack_fasta(fasta_file_path):
    packed_fasta_file = open(fasta_file_path, 'r')
    unpacked_file_path = fasta_file_path.split('.fasta')[0] + '_unpacked' + '.fasta'
    unpacked_fasta_file = open(unpacked_file_path, 'w')
    lines = packed_fasta_file.readlines()
    for i in range(len(lines)):
        line = lines[i]
        if i == 0:
            unpacked_fasta_file.write(line)
        elif line.startswith('>'):
            unpacked_fasta_file.write('\n' + line)
        else:
            unpacked_fasta_file.write(line.strip())
    packed_fasta_file.close()
    unpacked_fasta_file.close()

unpack_fasta('unpack_fasta\\3TC_patients.fasta')