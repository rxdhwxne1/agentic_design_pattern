# agentic_design_pattern
In this repository you will find my implementation of the agentic design pattern using ollama

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Introduction

The agentic design pattern focuses on creating systems that empower users to take actions and make decisions in an interactive environment. This implementation leverages Ollama for language processing and Streamlit for a user-friendly web interface.

## Installation

To set up the project, clone the repository and install the required dependencies:

```bash
git clone https://github.com/rxdhwxne1/agentic_design_pattern.git
cd agentic_design_pattern
```

## Créez un environnement virtuel (pas obligatoire):

```bash
python -m venv env
source env/bin/activate  # Pour macOS/Linux
.\env\Scripts\activate   # Pour Windows
```

## Installez les dépendances :
```bash
pip install -r requirements.txt
```

**Installez et configurez Ollama** : Ollama est utilisé pour gérer les modèles de génération de texte (LLM) comme llama3.2. 
Assurez-vous que ollama est installé :
Téléchargez et installez Ollama depuis Ollama.com.

## Usage

To run the chosen design pattern, use the following command (let's say you chose 'reflection'):
```bash
streamlit run reflection_design_pattern/reflection.py
```

This will start the Streamlit server and open the application in your web browser.

Contributions are welcome! Please open an issue or submit a pull request to propose changes.
