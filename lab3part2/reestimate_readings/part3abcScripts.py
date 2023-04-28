import sys
import re

def countHighestTPM(inputRead):
    highestTPM = -1
    highestTranscriptLine = ""
    for line in inputRead:
        line = line.strip().split("\t")
        first_element = line[0]
        if ("#" in first_element) == False:
            identifier = line[2]
            if (identifier == "transcript"):
                gene_id_element = line[8]
                elements = gene_id_element.split(";")
                TPM_element = elements[-2]
                if ("TPM" in TPM_element):
                    pattern = r'"(.*?)"'
                    match = re.search(pattern, TPM_element)
                    TPM = float(match.group(1))
                    if (highestTPM < (TPM)):
                        highestTPM = TPM
                        highestTranscriptLine = line
    return highestTPM, highestTranscriptLine

def countDistinctTranscriptsGenesWIthTPMAboveZero(files_to_read):
    transcriptIDSet = set()
    geneIDSet = set()
    for gtffileName in files_to_read:
        gtffile = open(gtffileName, "r")
        lines = gtffile.readlines()
        for line in lines:
            inputLine = line.strip().split("\t")
            first_element = inputLine[0]
            if ("#" in first_element) == False:
                identifier = inputLine[2]
                if (identifier == "transcript"):
                    id_element = inputLine[8]
                    elements = id_element.split(";")
                    TPM_element = elements[-2]
                    if ("TPM" in TPM_element):
                        pattern = r'"(.*?)"'
                        match = re.search(pattern, TPM_element)
                        TPM = float(match.group(1))
                        if (TPM > 0):
                            transcript_id_element = elements[1]
                            match2 = re.search(pattern, transcript_id_element)
                            transcript_id = match2.group(1)
                            transcriptIDSet.add(transcript_id)
                            gene_id_element = elements[0]
                            match3 = re.search(pattern, gene_id_element)
                            gene_id = match3.group(1)
                            geneIDSet.add(gene_id)
    transcriptCount = len(transcriptIDSet)
    geneCount = len(geneIDSet)
    return transcriptCount, geneCount

if __name__ == "__main__":
    # store the names of the files to be searched through 
    files_to_read = ["SRR479052_aligned_reestimate.gtf", "SRR479054_aligned_reestimate.gtf", "SRR479056_aligned_reestimate.gtf", "SRR479058_aligned_reestimate.gtf", "SRR479061_aligned_reestimate.gtf", "SRR479064_aligned_reestimate.gtf", "SRR479066_aligned_reestimate.gtf", "SRR479068_aligned_reestimate.gtf", "SRR479070_aligned_reestimate.gtf", "SRR479073_aligned_reestimate.gtf", "SRR479076_aligned_reestimate.gtf"]
    highestTPM = -1
    highestTranscriptLine = ""
    TPM_per_file = {}
    Line_per_file = {}
    for gtffileName in files_to_read:
        gtffile = open(gtffileName, "r")
        lines = gtffile.readlines()
        TPM_file, Line_file = countHighestTPM(lines)
        Line_per_file[gtffileName] = Line_file
        TPM_per_file[gtffileName] = TPM_file
    assert (len(TPM_per_file) == 11)
    highestTPMFile = max(TPM_per_file, key = TPM_per_file.get)
    highestTPM = TPM_per_file[highestTPMFile]
    highestTranscriptLine = Line_per_file[highestTPMFile]
    
    # get the largest TPM in the list 3a
    print("File with Highest TPM: " + str(highestTPMFile))
    print("Highest TPM: " + str(highestTPM))
    print("Line with highest TPM: " + str(highestTranscriptLine))
    
    distinctTranscriptsWithTPMAboveZero, distinctGenesWithTPMAboveZero = countDistinctTranscriptsGenesWIthTPMAboveZero(files_to_read)
    # get the number of distinct transcripts with TPM > 0 3b
    print("Distinct transcripts with TPM > 0: " + str(distinctTranscriptsWithTPMAboveZero))
    
    # get the number of distinct transcripts with TPM > 0 3c
    print("Distinct genes with TPM > 0: " + str(distinctGenesWithTPMAboveZero))