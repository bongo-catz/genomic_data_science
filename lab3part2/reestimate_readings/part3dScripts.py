import sys
import re

def generateMaxTPM(files_to_read):
    TPM_per_transcript = {}
    for gtffileName in files_to_read:
        gtffile = open(gtffileName, "r")
        lines = gtffile.readlines()
        for line in lines:
            inputLine = line.strip().split("\t")
            first_element = inputLine[0]
            if ("#" in first_element) == False:
                identifier = inputLine[2]
                if (identifier == "transcript"):
                    gene_id_element = inputLine[8]
                    elements = gene_id_element.split(";")
                    TPM_element = elements[-2]
                    transcript_id_element = elements[1]
                    if ("TPM" in TPM_element):
                        pattern = r'"(.*?)"'
                        match = re.search(pattern, TPM_element)
                        TPM = float(match.group(1))
                        match2 = re.search(pattern, transcript_id_element)
                        transcript_id = match2.group(1)
                        if transcript_id in TPM_per_transcript.keys():
                            currentMaxTPM = TPM_per_transcript[transcript_id]
                            if (currentMaxTPM < TPM):
                                TPM_per_transcript[transcript_id] = TPM
                        else:
                            TPM_per_transcript[transcript_id] = TPM
    return TPM_per_transcript

def countTranscriptsWithTPMGreater50(TPM_per_transcript):
    count = 0
    for key, value in TPM_per_transcript.items():
        if value > 50:
            count += 1
    return count

if __name__ == "__main__":
    # store the names of the files to be searched through 
    files_to_read = ["SRR479052_aligned_reestimate.gtf", "SRR479054_aligned_reestimate.gtf", "SRR479056_aligned_reestimate.gtf", "SRR479058_aligned_reestimate.gtf", "SRR479061_aligned_reestimate.gtf", "SRR479064_aligned_reestimate.gtf", "SRR479066_aligned_reestimate.gtf", "SRR479068_aligned_reestimate.gtf", "SRR479070_aligned_reestimate.gtf", "SRR479073_aligned_reestimate.gtf", "SRR479076_aligned_reestimate.gtf"]
    TPM_per_transcript = generateMaxTPM(files_to_read)
    for key, value in TPM_per_transcript.items():
        print("Transcript ID: " + key + ", TPM: " + str(value))
    count = countTranscriptsWithTPMGreater50(TPM_per_transcript)
    print("Distinct Transcripts with TPM > 50: " + str(count))
    
    