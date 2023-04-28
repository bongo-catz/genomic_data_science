import sys
import re

def countMatchTranscripts(inputRead):
    partAcount = 0
    partBcount = 0
    partCcount = 0
    totalCount = 0
    for line in inputRead:
        line = line.strip().split("\t")
        first_element = line[0]
        if ("#" in first_element) == False:
            identifier = line[2]
            list_of_ids = line[8].split(";")
            if (identifier == "transcript"):
                totalCount += 1
                index = -1
                for element in list_of_ids:
                    if "class_code" in element:
                        index = list_of_ids.index(element)
                class_code = list_of_ids[index][-2]
                if (class_code == "="): # Predicted transcript has exactly the same introns as the reference transcript
                    partAcount += 1
                if (class_code != "u" and class_code != "="): # Look at transcripts without class code "u" and "="
                    partBcount += 1
                if (class_code == "u"):
                    partCcount += 1 
    print(totalCount)               
    return partAcount, partBcount, partCcount


if __name__ == "__main__":
    inputRead = sys.stdin.read().strip().split("\n")
    partAcount, partBcount, partCcount = countMatchTranscripts(inputRead)
    print("Total number of transcripts that match with introns from reference: " + str(partAcount))
    print("Total number of novel transcripts: " + str(partBcount))
    print("Total number of novel transcripts that occur at entirely novel locations : " + str(partCcount))
    