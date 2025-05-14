#add import

from question_b import get_most_likely_ancestor_consensus

def main():
    
    while True:
        print("--- DNA Substring Search ---")
        dna1 = input("Enter a DNA string (length 8 to 16): ").strip().upper()
        dna2 = input("Enter a DNA substring of length 4: ").strip().upper()

        if 8 <= len(dna1) <= 16 and len(dna2) == 4:
            break
        
        else:
            print("Invalid input. DNA string must be 8–16 characters and substring must be exactly 4 characters.")

    positions = get_most_likely_ancestor_consensus(dna1, dna2)

    if positions:
        print("Substring found at positions (1-based):", " ".join(map(str, positions)))
    
    else:
        print("No matches found.")


if __name__ == "__main__":
    main()