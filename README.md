# ChatGPT4PCG 2 Competition: Prompt Engineering for Science Birds Level Generation

This repository contains the code and datasets for the paper "ChatGPT4PCG 2 Competition: Prompt Engineering for Science Birds Level Generation" accepted at [IEEE CoG 2024](https://2024.ieee-cog.org).

## Authors
Pittawat Taveekitworachai, Febri Abdullah, Mury F. Dewantoro, Yi Xia, Pratch Suntichaikul, Ruck Thawonmas, Julian Togelius, and Jochen Renz

## Abstract

This paper presents the second ChatGPT4PCG competition at the 2024 IEEE Conference on Games. In this edition of the competition, we follow the first edition, but make several improvements and changes. We introduce a new evaluation metric along with allowing a more flexible format for participants' submissions and making several improvements to the evaluation pipeline. Continuing from the first edition, we aim to foster and explore the realm of prompt engineering (PE) for procedural content generation (PCG). While the first competition saw success, it was hindered by various limitations; we aim to mitigate these limitations in this edition. We introduce diversity as a new metric to discourage submissions aimed at producing repetitive structures. Furthermore, we allow submission of a Python program instead of a prompt text file for greater flexibility in implementing advanced PE approaches, which may require control flow, including conditions and iterations. We also make several improvements to the evaluation pipeline with a better classifier for similarity evaluation and better-performing function signatures. We thoroughly evaluate the effectiveness of the new metric and the improved classifier. Additionally, we perform an ablation study to select a function signature to instruct ChatGPT for level generation. Finally, we provide implementation examples of various PE techniques in Python and evaluate their preliminary performance. We hope this competition serves as a resource and platform for learning about PE and PCG in general.
## File structure
```
.
├── 1-vit-classifier # This directory contains the dataset and the code for the classifier used in the competition.
│   ├── testing # This directory contains the testing dataset for testing the classifiers.
│   └── training # This directory contains the training dataset used to train the new classifier.
├── 2-diversity-effectiveness # This directory contains the dataset and the code for the diversity metric used in the competition.
│   ├── diversity-new-vit # This directory contains the output of the evaluation when using the diversity metric with the new classifier.
│   └── diversity-old-vit # This directory contains the output of the evaluation when using the diversity metric with the old classifier.
├── 3-function-signatures # This directory contains the dataset and the code for the function signatures used in the competition.
│   ├── gpt-3.5-turbo-1106-results # This directory contains the output of the experiment using the GPT-3.5-turbo-1106 model.
│   ├── prompts.zip # This file contains the prompts of each function signature used in the experiment.
│   ├── responses-gathering-script # This directory contains the script used to gather the responses of ChatGPT.
│   └── results.zip # This file contains the results of the experiment using the latest model.
└── 4-prompt-engineering # This directory contains the code for the prompt engineering experiment.
    ├── experiment_results.zip.001 # This file contains the results of the experiment.
    ├── experiment_results.zip.002 # This file contains the results of the experiment.
    ├── few_shot # This directory contains the code for the few-shot prompting experiment.
    ├── gpt-3.5-turbo-1106-results # This directory contains the output of the experiment using the GPT-3.5-turbo-1106 model.
    ├── null_shot # This directory contains the code for the null-shot prompting experiment.
    ├── null_shot_cot # This directory contains the code for the null-shot chain-of-thought prompting experiment with the classifier-on-top approach.
    ├── requirements.txt # This file contains the required libraries to run the code.
    ├── tot # This directory contains the code for the task-oriented prompting experiment.
    ├── zero_shot # This directory contains the code for the zero-shot prompting experiment.
    ├── zero_shot_cot # This directory contains the code for the zero-shot chain-of-thought prompting experiment with the classifier-on-top approach.
    └── zero_shot_multi_turn # This directory contains the code for the zero-shot multi-turn prompting experiment.
```

## Installation and Usage
0. Create a virtual environment (if needed):
```bash
conda create -n chatgpt4pcg2 python=3.12
```
and activate it:
```bash
conda activate chatgpt4pcg2
```
1. Copy `.env.example` and rename it to `.env.`. Follow instructions on [this page](https://platform.openai.com/docs/api-reference/authentication) to obtain your own OpenAI API key.
2. Install the requirements:
```bash
pip install -r requirements.txt
```
3. Run the code in the directories as needed.
