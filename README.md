# Audio Preprocessing and Metadata Dashboard

This project focuses on preprocessing audio data, extracting and processing transcripts, generating metadata, and building a dashboard for analysis. The tasks include converting audio files to a uniform format, trimming unnecessary audio segments, processing text data, generating JSON manifests, and deploying a Flask web application for visualization.

---

# **How to Run the Project**

## **Task 1 - Task 4**

1. **Open the Notebook**:  
   - Open the `TASKS.ipynb` file in your Google Colab workspace.

2. **Notebook Structure**:  
   - The notebook is divided into tasks (`Task-1`, `Task-2`, and so on).
   - **Important**: Each task depends on the previous one. Make sure to run the cells sequentially, from top to bottom.

3. **Mount Google Drive**:  
   - At the start of the notebook, mount your Google Drive:
     ```python
     from google.colab import drive
     drive.mount('/content/drive')
     ```

4. **Preprocess Audios**:  
   - Place the `preprocess_audios.sh` file in the `Drive` folder of your Google Drive.
   - This script will be used in Task-1 to preprocess the audio files.

5. **Control File Count (`n_files`)**:  
   - Use the variable `n_files` to specify how many files to process:
     - Set `n_files = -1` to process all files.
     - Set `n_files = 1` to process a smaller subset for testing (e.g., 1–5 files).

6. **Outputs**:  
   - After completing all tasks, you will obtain:
     - `.txt` files for transcripts.
     - `.wav` files for audio.
     - `.json` files for analytics.

---

## **Task 5: Running the Flask App**

1. **Prepare Files**:  
   - Download the generated `.json` file and place it in the same directory as the `app.py` file.

2. **Set Up Virtual Environment**:  
   - Navigate to the project directory in your terminal.
   - Run the following commands to create and activate a virtual environment:
     ```bash
     python -m venv mvenv
     source venv/bin/activate    # On Windows, use `venv\Scripts\activate`
     ```

3. **Install Dependencies**:  
   - Install the required packages:
     ```bash
     pip install -r requirements.txt
     ```

4. **Run the Flask Application**:  
   - Start the server by running:
     ```bash
     python app.py
     ```
   - Open your browser and navigate to:  
     [http://127.0.0.1:5000](http://127.0.0.1:5000)

5. **Dashboard**:  
   - The dashboard will display analytics for your project. It may look something like this:

     ![Dashboard Example](https://github.com/Mrsenjiii/project_AI/blob/main/examples/Capture.JPG)
     ![Dashboard Example2](https://github.com/Mrsenjiii/project_AI/blob/main/examples/Capture2.JPG)

---

## **Notes**

- Ensure all dependencies are installed before running the app.
- Replace `image-link-placeholder` with the appropriate link to the image of your dashboard.


## 📋 Project Overview

### Key Objectives:
#### Web Scrapping
- Loading URLs for lectures, and transcript pdf.
- downloading data for Analysis and Model Building.

#### Audio Preprocessing:
- Convert audio files to WAV format.
- Standardize sampling rates and channels.
- Trim unnecessary segments (e.g., the first 10 seconds and the last 30 seconds).

#### Text Extraction and Preprocessing:
- Extract text from PDFs.
- Perform cleaning operations:
  - Remove punctuation.
  - Convert text to lowercase.
  - Convert numbers into words.

#### Metadata Generation:
- Generate JSON manifest files linking audio files with their corresponding text transcripts and metadata.
- Include details such as file paths, audio durations, and processed transcript text.

#### Dashboard Development:
- Build a Flask application to analyze metadata.
- Visualize file statistics and language-specific data using a web-based dashboard.

---

## ⚙️ Workflow Details

### 1. **Downloading Data**
#### Working :
  -Using Python request We are fetching lectures and transcript pdf data.
  -Saving Each file into the structured folder which is easily understandable just by reading the code.


### 2. **Audio Preprocessing (`preprocess_audios.sh`)**
#### Purpose:
Processes raw audio files by:
- Converting them to WAV format.
- Standardizing the sampling rate to 16 kHz.
- Ensuring mono-channel output.

#### Steps:
1. Take inputs for:
   - Input directory of raw audio files (`<input_directory>`).
   - Output directory for processed audio files (`<output_directory>`).
   - Number of CPUs to utilize (`<num_cpus>`).
2. Validate input directories.
3. Convert audio files in parallel using `ffmpeg`.

#### Command Example:
```bash
./preprocess_audios.sh input_audios output_audios 4
```


### 3. Trimming Audio Files  

#### Purpose  
To remove irrelevant portions of audio files for better alignment with transcripts.

#### Key Steps  
- Remove the first 10 seconds and the last 30 seconds of each audio file.  
- Save the trimmed audio files to a new directory.
- In the future, I would like to use some other models to identify the section where we do not have speech audio so that we can silence the part where we have noise or some instrument sound.
- 

#### Implementation  
This task is implemented in Python using the **pydub** library. 

#### Output  
Trimmed audio files are stored in a designated directory.


### 4. Text Extraction and Preprocessing  

#### Purpose  
Extract text from PDF transcripts and clean it for further processing.

#### Steps  
1. Extract raw text from PDF files.  
2. Process the text by:  
   - Removing punctuation.  
   - Converting text to lowercase.  
   - Replacing numeric digits with their word equivalents using the **num2words** library.  
3. Save the cleaned text in `.txt` format.  

#### Key Features  
- Supports multiple languages.  
- Organizes processed text into separate directories based on language.  

#### Output  
Processed text files are saved in corresponding directories.

### 5. JSON Manifest Generation  

#### Purpose  
Link audio files with their corresponding cleaned transcripts and metadata for machine learning tasks.

#### Steps  
1. Extract metadata for each audio file, including:  
   - **File path**  
   - **Duration** (in seconds)  
   - **Cleaned transcript text**  
2. Create JSONL files, where each line represents one file in JSON format.

#### JSON Format Example  
```json
{
  "audio_filepath": "data/courses/106106184/audio/lec_1_2.wav",
  "duration": 824.4,
  "text": "Sample transcript text."
}
```
### 6. Flask Dashboard  

#### Purpose  
Provide an interactive web-based dashboard to analyze audio and text metadata.

#### Features  

- **Metadata Analysis Endpoint** (`/meta_data_analysis`):  
  Computes key statistics, including:  
  - Total word count.  
  - Unique characters used (alphabet size).  
  - Total duration (in hours).  
  - Vocabulary size.  

- **File Statistics Endpoint** (`/files_analysis`):  
  Lists metadata for each audio file, including:  
  - File name.  
  - Duration.  
  - Character and word counts.  
  Groups files by duration (minute buckets) for generating histograms.  

- **Dashboard** (`/`):  
  Serves an interactive HTML dashboard (customization required).  


### Dependencies  

#### Python Libraries  
- **Flask**: For building the web application.  
- **PyDub**: For audio processing.  
- **Num2Words**: For text processing.  
- **PyPDF2** or **PDFMiner**: For text extraction from PDFs.  
- **JSON** and **Math** modules: For metadata generation.  

#### Bash Utilities  
- **ffmpeg**: For audio conversion.  
- **xargs**: For parallel processing.  

---

### Execution Flow  

1. **Preprocess Audio Files**:  
   Run the `preprocess_audios.sh` script to convert raw audio files to WAV format.  

2. **Trim Audio Files**:  
   Use the Python script to remove unnecessary audio segments.  

3. **Extract and Process Transcripts**:  
   Extract text from PDFs, clean it, and save processed `.txt` files.  

4. **Generate JSON Manifests**:  
   Link audio files with cleaned transcripts in JSONL format.  

5. **Run Flask App**:  
   Start the Flask server to visualize metadata through the dashboard.



