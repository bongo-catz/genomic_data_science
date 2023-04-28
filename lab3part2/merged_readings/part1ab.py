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

def countUniqueGeneID(inputRead):
    geneIDset = set()
    count = 0
    for line in inputRead:
        line = line.strip().split("\t")
        first_element = line[0]
        if ("#" in first_element) == False:
            list_of_ids = line[8]
            elements = list_of_ids.split(";")
            gene_id_element = elements[0]
            pattern = r'"(.*?)"'
            match = re.search(pattern, gene_id_element)
            gene_id = match.group(1)
            geneIDset.add(gene_id)
            count += 1  
    uniqueCount = len(geneIDset)     
    return count, uniqueCount

if __name__ == "__main__":
    inputRead = sys.stdin.read().strip().split("\n")
    count = countTranscripts(inputRead)
    geneCount, uniqueCount = countUniqueGeneID(inputRead)
    print("Total number of transcripts found: " + str(count))
    print("Total number of unique gene IDs found: " + str(uniqueCount))
    