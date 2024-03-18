# Clinical Trial IPD Classifier

## Overview
This repository contains the code and dataset used in the research for classifying Individual Participant Data (IPD) sharing statements in clinical trial records. The study focuses on leveraging BERT-based language models to automate the classification of IPD statements into "Yes", "No", and "Undecided" categories. Our work contributes to improving data management practices in medical research by facilitating the efficient and accurate classification of these statements.

## Research
The volume of clinical trials registered on platforms like ClinicalTrials.gov is vast and continuously growing. Manual evaluation of IPD sharing statements becomes increasingly impractical due to the scale. This research employs Natural Language Processing (NLP) and Transformer models, specifically BERT and its derivatives, to address the challenge of automating the classification process.

## Repository Structure

- `code/`: Contains the Python scripts and the requirements text file that were used for the project.
  - `requirements.txt`: Lists dependencies required to run the scripts.
  - `xml_parsing.py`: Parses XML files from ClinicalTrials.gov API.
  - `data_preprocessing.py`: Cleans and prepares data for processing.
  - `data_sampling.py`: Samples data from the larger dataset for model training.
  - `Manual Labeling.py`: GUI for manually labeling data.
  - `data_splitting.py`: Divides dataset into training, validation, and test sets.
  - `model_biobert_uncased_mlabel.py`: Evaluates BioBERT model using manual labels.
  - `model_biobert_uncased_ipd.py`: Evaluates BioBERT model on IPD status.
  - `model_bluebert_uncased_mlabel.py`: Evaluates BlueBERT model using manual labels.
  - `model_bluebert_uncased_ipd.py`: Evaluates BlueBERT model on IPD status.
  - `model_scibert_uncased_mlabel.py`: Evaluates SciBERT model using manual labels.
  - `model_scibert_uncased_ipd.py`: Evaluates SciBERT model on IPD status.

- `dataset/`: This directory holds the datasets used in the three model evaluations.
  - `Annotated_dataset/`: The folder contains 3 CSV files of training, validation, and test datasets with Manual labels.
    - `train_dataset_AD`
    - `validation_dataset_AD`
    - `test_dataset_AD`
  - `IPD_status_dataset/`: The folder contains 3 CSV files of training, validation, and test datasets with IPD status.
    - `train_dataset_ipd`
    - `validation_dataset_ipd`
    - `test_dataset_ipd`    

## Dataset Flowchart


![URL_of_the_image "Optional title"](https://github.com/sjelodari/ClinicalTrialIPDClassifier/blob/main/Datasets/Data%20Split%20Flowchart.png))

#### Due to data privacy, descriptions in the `dataset/` directory have been hashed, but are identifiable by their NCT numbers. In the `dataset/` directory, data has been processed and labeled with binary labels for analysis: "Yes" = 0, "Undecided" = 1, "No" = 2. This maintains privacy while ensuring data usability.

## Usage

Instructions on how to use the scripts to replicate the study or to apply the models to new data will be provided here.

## Contributing

We welcome contributions to this project.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## Citation

If you use the data or code in this repository in your research, please cite it as follows:
