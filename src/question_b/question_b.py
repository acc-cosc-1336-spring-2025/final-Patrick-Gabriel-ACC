#write functions here, don't add input('') statements here!

def get_most_likely_ancestor_consensus(dna_string1, dna_string2):
    positions = []
    len1 = len(dna_string1)
    len2 = len(dna_string2)

    for i in range(len1 - len2 + 1):
       
        if dna_string1[i:i+len2] == dna_string2:
            positions.append(i + 1)  # Add 1 for 1-based index

    return positions