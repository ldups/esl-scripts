from datetime import date, timedelta
from Bio import SeqIO

def extract_date(line):
    id = line.rsplit('_', 1)[0]
    date_only = line.rsplit('_', 1)[1]
    month = int(date_only.rsplit('-', 1)[-1])
    year = int(date_only.rsplit('-', 1)[-2])
    date_object = date(year, month, 1)
    return id, date_object

def match_ids_by_date(pheno_file_path, min_difference):
    pheno_file = open(pheno_file_path, 'r')
    min_difference = timedelta(min_difference)
    matching_id_list = []
    end_of_file = False

    while not end_of_file:
        line1 = pheno_file.readline().strip().split(',')[0]

        if line1:
            id, date1 = extract_date(line1)
            line2 = pheno_file.readline().strip().split(',')[0]
            date2 = extract_date(line2)[1]

            difference = date2 - date1
            if difference > min_difference:
                matching_id_list.append(line1)
                matching_id_list.append(line2)

        else:
            end_of_file = True

    pheno_file.close()
    return matching_id_list

def write_input_files(pheno_file_path, fasta_file_path, output_base_name, min_difference):
    matching_id_list = match_ids_by_date(pheno_file_path, min_difference)
    output_fasta_path = output_base_name + '.fas'
    output_response_path = output_base_name + '_response.txt'

    pheno_file = open(pheno_file_path, 'r')

    num_records = 0
    
    sequences_to_write = []
    for record in SeqIO.parse(fasta_file_path, 'fasta'):
        if record.id in matching_id_list:
            sequences_to_write.append(record)
            num_records += 1

    with open(output_fasta_path, 'w') as output_handle:
        SeqIO.write(sequences_to_write, output_handle, 'fasta-2line')

    with open(output_response_path, 'w') as output_response:
        for line in pheno_file:
            id = line.strip().split(',')[0]
            response = line.strip().split(',')[1]
            if id in matching_id_list:
                output_response.write(id + '\t' + response + '\n')

    print(str(num_records) + ' records written to output fasta file.')

    pheno_file.close()

pheno_file_path = 'hiv_dates\hiv_phenos.txt'
write_input_files(pheno_file_path, 'hiv_dates\hivb_pre_post_rti_realigned.fas', 'hiv_450', 450)
