import sys
import re

def generateTPMCountGene(inputRead):
    TPM_per_gene = {}
    for line in inputRead:
        inputLine = line.strip().split("\t")
        first_element = inputLine[0]
        if ("#" in first_element) == False:
            identifier = inputLine[2]
            if (identifier == "transcript"):
                important_elements = inputLine[8]
                elements = important_elements.split(";")
                TPM_element = elements[-2]
                gene_id_element = elements[0]
                if ("TPM" in TPM_element):
                    pattern = r'"(.*?)"'
                    match = re.search(pattern, TPM_element)
                    TPM = float(match.group(1))
                    match2 = re.search(pattern, gene_id_element)
                    gene_id = match2.group(1)
                    if gene_id in TPM_per_gene.keys():
                        TPM_per_gene[gene_id] += TPM
                    else:
                        TPM_per_gene[gene_id] = TPM
    sorted_TPM_per_gene = sorted(TPM_per_gene.items(), key = lambda x:x[1], reverse= True)
    return sorted_TPM_per_gene

if __name__ == "__main__":
    # store the names of the files to be searched through 
    files_to_read = ["SRR479052_aligned_reestimate.gtf", "SRR479054_aligned_reestimate.gtf"]
    inputRead = sys.stdin.read().strip().split("\n")
    TPM_per_gene = generateTPMCountGene(inputRead)
    
    # now report top ten
    print("The top 10 most-highly expressed genes")
    for i in range(0, 10):
        element = list(TPM_per_gene[i])
        print("Gene ID: " + element[0] + ", TPM Count: " + str(element[1]))