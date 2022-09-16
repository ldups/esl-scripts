import matplotlib.pyplot as plt
import numpy as np

def make_full_gene_mpi_plot(gene_mp_dictionary):
    num_mps = create_list_num_mps(gene_mp_dictionary)
    num_bins = 50
    plt.hist(num_mps, density=False, bins=num_bins, color = '#33CEFF')
    plt.ylabel('Number of Genes')
    plt.xlabel('Number of Lowest Level MPs')
    plt.title('All genes vs. number of low level MPs')
    plt.show()

def make_low_gene_mpi_plot(gene_mp_dictionary):
    num_mps = create_list_num_mps(gene_mp_dictionary, max_val=50)
    num_bins = 25
    plt.hist(num_mps, density=False, bins=num_bins, color = '#33CEFF')
    plt.ylabel('Number of Genes')
    plt.xlabel('Number of Lowest Level MPs')
    plt.title('Genes with under 50 low level MPs vs. number of low level MPs')
    plt.show()

def make_high_gene_mpi_plot(gene_mp_dictionary):
    num_mps = create_list_num_mps(gene_mp_dictionary, min_val=100)
    num_bins = 25
    plt.hist(num_mps, density=False, bins=num_bins, color = '#33CEFF')
    plt.ylabel('Number of Genes')
    plt.xlabel('Number of Lowest Level MPs')
    plt.title('Genes with over 100 low level MPs vs. number of low level MPs')
    plt.show()

def calculate_num_bins(num_mp_list):
    mp_array = np.asarray(num_mp_list)
    q25, q75 = np.percentile(mp_array, [25, 75])
    bin_width = 2 * (q75-q25) * len(mp_array) ** (-1/3)
    bins = round((mp_array.max() - mp_array.min()) / bin_width)
    return bins

def calculate_avg_num_mps(gene_mp_dictionary):
    num_genes = 0
    num_mps = 0
    for gene in gene_mp_dictionary:
        num_genes += 1
        num_mps += len(gene_mp_dictionary[gene])
    return num_mps // num_genes
    
def calculate_max_num_mps(gene_mp_dictionary):
    mps = list(gene_mp_dictionary.values())
    max_mps = len(mps[0])
    for i in range(1, len(mps)):
        num_mps = len(mps[i])
        if num_mps > max_mps:
            max_mps = num_mps
    return max_mps

def create_list_num_mps(gene_mp_dictionary, min_val=None, max_val=None):
    mps = list(gene_mp_dictionary.values())
    num_mp_list = []
    for mp_list in mps:
        num_mps = len(mp_list)
        if min_val is not None and num_mps > min_val:
            num_mp_list.append(num_mps)
        if max_val is not None and num_mps < max_val:
            num_mp_list.append(num_mps)
        if max_val is None and min_val is None:
            num_mp_list.append(num_mps)
    return num_mp_list