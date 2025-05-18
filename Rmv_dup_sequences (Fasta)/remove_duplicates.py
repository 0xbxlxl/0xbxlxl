# using argparse to allow the user to give input and output files when running the script
import argparse

# importing os because I want to auto-create the output file name if the user doesn’t provide one
import os

# This function takes a FASTA file, removes duplicate sequences (case-insensitive),
# and writes the cleaned sequences to a new file with modified headers
def clean_fasta(input_file, output_file=None):
    seq_dict = {}  # Dictionary to store sequences as keys and their header + count as values
    header = None  # Variable to temporarily hold the current header
    sequence = ""  # Variable to temporarily hold the current sequence
    total_sequences = 0  # Counter for total number of sequences in the input file

    # Opening the input FASTA file for reading
    with open(input_file, "r") as infile:
        for line in infile:
            line = line.strip()  # Remove any extra spaces or newline characters
            if line.startswith(">"):  # If the line is a header
                if sequence:
                    total_sequences += 1  # Count this sequence
                    seq_upper = sequence.upper()  # Convert sequence to uppercase to avoid case-sensitive duplicates
                    if seq_upper not in seq_dict:
                        seq_dict[seq_upper] = [header, 1]  # If new, store header and count 1
                    else:
                        seq_dict[seq_upper][1] += 1  # If duplicate, increase the count
                    sequence = ""  # Reset sequence holder for the next one
                header = line  # Store the new header
            else:
                sequence += line  # Add sequence lines together (can be multiline)

        # Handling the very last sequence in the file
        if sequence:
            total_sequences += 1
            seq_upper = sequence.upper()
            if seq_upper not in seq_dict:
                seq_dict[seq_upper] = [header, 1]
            else:
                seq_dict[seq_upper][1] += 1

    # Default output file if not provided by -o
    if output_file is None:
        base = os.path.splitext(input_file)[0]  # Get filename without extension
        output_file = base + "_nodup.fasta"  # Create output filename

    # Writing the cleaned sequences to the new output file
    with open(output_file, "w") as outfile:
        for seq, (original_header, count) in seq_dict.items():
            new_header = f"{original_header}_{count}x"  # I’m updating the header with how many times the sequence appeared
            outfile.write(f"{new_header}\n{seq}\n")  # Writing new header and sequence to file

    # Printing the summary so the user knows what happened
    print(f"File processed: {input_file}")
    print(f"Original sequences: {total_sequences}")
    print(f"Unique sequences: {len(seq_dict)}")
    print(f"Output written to: {output_file}")
    print("-" * 40)

# using argparse to handle command-line arguments when running the script
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Remove duplicate sequences from FASTA file.")
    parser.add_argument("-i", "--input", required=True, help="Input FASTA file")  # Input file is required
    parser.add_argument("-o", "--output", help="Output FASTA file (optional)")  # Output file is optional
    args = parser.parse_args()

    # Call my function using the arguments passed from the command line
    clean_fasta(args.input, args.output)