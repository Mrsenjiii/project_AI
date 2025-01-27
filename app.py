from flask import Flask, jsonify, render_template
import json
import math
from collections import defaultdict

app = Flask(__name__)

# File Path to JSONL
path = r'english-Verified_transcripts_pdfs_txt_files_train_manifest (1).jsonl'

# Function to dynamically read JSONL file
def read_jsonl():
    with open(path, 'r') as json_file:
        return [json.loads(line) for line in json_file]  # Parse each line as JSON


# Compute Metadata for Dashboard
@app.route('/meta_data_analysis', methods=['GET'])
def meta_data():
    data = read_jsonl()  # Read the latest data from file
    total_words = 0
    char_used = set()
    total_duration = 0
    vocabulary = set()

    for item in data:
        total_words += len(item['text'].split())
        char_used.update(item['text'])
        total_duration += float(item['duration'])
        vocabulary.update(item['text'].split())

    # Convert total duration to hours
    total_hours = total_duration / 3600

    return jsonify({
        "total_words": total_words,
        "alphabet_size": len(char_used),
        "total_duration_hours": total_hours,
        "vocabulary_size": len(vocabulary),
    })


# File Statistics (For Histograms)
@app.route('/files_analysis', methods=['GET'])
def files_analysis():
    data = read_jsonl()  # Read the latest data from file
    answer = []
    minute_buckets = defaultdict(lambda: {"words": 0, "chars": 0})  # Group by minutes

    for item in data:
        file_name = item['audio_filepath'].split('/')[-1].split('.')[0]
        duration = item['duration']
        numbers_chars = len(item['text'])
        number_words = len(item['text'].split())

        # Add data to the response
        file_data = {
            "file_name": file_name,
            "duration": duration,
            "numbers_chars": numbers_chars,
            "number_words": number_words,
        }
        answer.append(file_data)

        # Group by minute buckets
        minute = math.floor(duration / 60)  # Calculate the minute bucket
        minute_buckets[minute]["words"] += number_words
        minute_buckets[minute]["chars"] += numbers_chars

    # Prepare data for histograms
    minute_buckets_data = {
        "minutes": list(minute_buckets.keys()),
        "words": [bucket["words"] for bucket in minute_buckets.values()],
        "chars": [bucket["chars"] for bucket in minute_buckets.values()],
    }

    return jsonify({"file_data": answer, "minute_buckets": minute_buckets_data})




# Serve the Dashboard
@app.route('/')
def index():
    return render_template('dashboard.html')  # Renders the HTML dashboard


@app.after_request
def add_header(response):
    response.headers["Cache-Control"] = "no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response

if __name__ == "__main__":
    app.run(debug=True, port=5000)
