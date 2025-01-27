#!/bin/bash

# Ensure the script exits on errors and undefined variables
set -e
set -u

# Function to display usage instructions
usage() {
    echo "Usage: $0 <input_directory> <output_directory> <num_cpus>"
    exit 1
}

# Check for correct number of arguments
if [ "$#" -ne 3 ]; then
    usage
fi

# Read user inputs
INPUT_DIR="$1"
OUTPUT_DIR="$2"
NUM_CPUS="$3"

# Check if input directory exists
if [ ! -d "$INPUT_DIR" ]; then
    echo "Error: Input directory '$INPUT_DIR' does not exist."
    exit 1
fi

# Create output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Function to process a single file
process_file() {
    local input_file="$1"
    local output_dir="$2"
    local base_name
    base_name=$(basename "$input_file" | sed 's/\.[^.]*$//') # Strip extension
    local output_file="${output_dir}/${base_name}.wav"

    # Convert audio file to WAV format with 16KHz sampling rate and mono channel
    ffmpeg -i "$input_file" -ar 16000 -ac 1 "$output_file" -y
}

# Export the function for parallel execution
export -f process_file

# Find all audio files in the input directory and process them in parallel
find "$INPUT_DIR" -type f -print0 | \
    xargs -0 -n 1 -P "$NUM_CPUS" -I {} bash -c 'process_file "$@"' _ {} "$OUTPUT_DIR"

echo "Processing completed. Processed files are saved in '$OUTPUT_DIR'."
