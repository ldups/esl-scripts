from datetime import date, timedelta
from Bio import SeqIO
from random import sample
from math import floor 

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

def generate_test_indices(matching_id_list, percent_test):
    id_list = []
    for i in range(len(matching_id_list)):
        whole_id = matching_id_list[i]
        id = whole_id.rsplit('_', 1)[0]
        if id not in id_list:
            id_list.append(id)

    num_test_seqs = floor(percent_test * len(id_list))
    test_list = sample(id_list, k=num_test_seqs)
    return test_list

def write_input_files(pheno_file_path, fasta_file_path, output_base_name, min_difference, percent_test = 0):
    matching_id_list = match_ids_by_date(pheno_file_path, min_difference)
    #output_fasta_path = output_base_name + '.fas'
    output_response_path = output_base_name + '_response.txt'

    pheno_file = open(pheno_file_path, 'r')

    num_records = 0

    test_list = generate_test_indices(matching_id_list, percent_test)

    
    # can use to make separate fasta file- shouldn't be necessary
    """ sequences_to_write = []
    for record in SeqIO.parse(fasta_file_path, 'fasta'):
        if record.id in matching_id_list:
            sequences_to_write.append(record)
            num_records += 1 

    with open(output_fasta_path, 'w') as output_handle:
        SeqIO.write(sequences_to_write, output_handle, 'fasta-2line') """

    with open(output_response_path, 'w') as output_response:
        for line in pheno_file:
            # converts line from csv file to format needed for response matrix
            id = line.strip().split(',')[0]
            response = line.strip().split(',')[1]
            if id in matching_id_list:
                if id.rsplit('_', 1)[0] in test_list:
                    output_response.write(id + '\t0\n')
                else:
                    output_response.write(id + '\t' + response + '\n')

    #print(str(num_records) + ' records written to output fasta file.')
    print('Wrote response matrix for ' + str(min_difference) +' days or more with ' + '{:.2%}'.format(percent_test) + ' of matching pairs included in test set.')

    pheno_file.close()

pheno_file_path = 'hiv_dates\hiv_phenos.txt'
write_input_files(pheno_file_path, 'hiv_dates\hivb_pre_post_rti_realigned.fas', 'hiv_365', 365)
