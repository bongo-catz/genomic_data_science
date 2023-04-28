import sys
import re

def countTranscripts(inputRead):
    count = 0
    for line in inputRead:
        line = line.strip().split("\t")
        first_element = line[0]
        if ("#" in first_element) == False:
            identifier = line[2]
            if (identifier == "transcript"):
                count += 1
    return count

def countUniqueGeneProteinID(inputRead):
    geneIDProteinset = set()
    for line in inputRead:
        line = line.strip().split("\t")
        first_element = line[0]
        if ("#" in first_element) == False:
            list_of_ids = line[8]
            elements = list_of_ids.split(";")
            gene_id_element = elements[1]
            if ("gene_id" in gene_id_element):
                pattern = r'"(.*?)"'
                match = re.search(pattern, gene_id_element)
                gene_id = match.group(1)
                if "protein_coding" in list_of_ids:
                    geneIDProteinset.add(gene_id)  
    uniqueCount = len(geneIDProteinset)     
    return uniqueCount

def countTranscriptProtein(inputRead):
    count = 0
    for line in inputRead:
        line = line.strip().split("\t")
        first_element = line[0]
        if ("#" in first_element) == False:
            list_of_ids = line[8]
            identifier = line[2]
            if ("protein_coding" in list_of_ids) and (identifier == "transcript"):
                count += 1   
    return count

if __name__ == "__main__":
    inputRead = sys.stdin.read().strip().split("\n")
    count = countTranscripts(inputRead)
    transcriptProteinCount = countTranscriptProtein(inputRead)
    uniqueCount = countUniqueGeneProteinID(inputRead)
    print("Total number of transcripts found: " + str(count))
    print("Total number of transcripts that correspond to protein_coding found: " + str(transcriptProteinCount))
    print("Total number of unique gene IDs that correspond to protein_coding found: " + str(uniqueCount))
    