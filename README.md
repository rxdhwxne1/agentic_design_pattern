# Agentic Design Patterns Using Ollama

This repository contains my implementation of agentic design patterns using Ollama, showcasing how these patterns enhance interactive systems and user experiences.

## Table of Contents

- [Introduction](#introduction)
- [Agentic Design Patterns](#agentic-design-patterns)
  - [Reflection](#reflection)
  - [Tools](#tools)
  - [Planning](#planning) (planned for future implementation)
  - [Multi-agent](#multi-agent) (planned for future implementation)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Introduction

The agentic design pattern focuses on creating systems that empower users to take actions and make decisions in an interactive environment. This implementation leverages Ollama for language processing to enhance dialogue systems and improve user interactions. 

By working on these agentic design patterns, I have developed a deeper understanding of AI-driven communication, which has enriched my skills in natural language processing and system design. This experience has also enhanced my problem-solving abilities, as I navigate the complexities of integrating various functionalities into a cohesive system. Moreover, collaborating on these projects has strengthened my teamwork and project management skills, preparing me for real-world applications in the rapidly evolving field of artificial intelligence.

## Agentic Design Patterns

### Reflection

The 'Reflection' pattern enables the model to evaluate and refine its responses in real-time, improving dialogue coherence and accuracy.

### Tools

The 'Tools' pattern integrates external functionalities, allowing the model to call specific functions and access information beyond its initial training, thereby enhancing its versatility.

### Planning

Currently under development, the 'Planning' pattern will support task sequencing and long-term interaction strategies, enabling the model to approach complex tasks systematically.

### Multi-agent

The 'Multi-agent' pattern is planned for future implementation to facilitate collaboration among multiple agents, enhancing adaptability and diversity in multi-turn dialogues.

## Installation

To set up the project, clone the repository and install the required dependencies:

```bash
git clone https://github.com/rxdhwxne1/agentic_design_pattern.git
cd agentic_design_pattern
```

## Create a virtual environment (optional):

```bash
python -m venv env
source env/bin/activate  # For macOS/Linux
.\env\Scripts\activate   # For Windows
```

## Install dependencies:

```bash
pip install -r requirements.txt
```

Install and configure Ollama: Ollama is used to manage text generation models (LLMs) like Llama 3.2. Ensure that Ollama is installed: Download and install Ollama from Ollama.com.

## Usage

To run the chosen design pattern, use the following command (for example, to run 'Reflection'):
```bash
streamlit run reflection_design_pattern/reflection.py
```

This will start the Streamlit server and open the application in your web browser.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request to propose changes.


### Points à personnaliser :
- Assurez-vous que les liens et les commandes correspondent à votre configuration.
- Ajoutez des sections ou des détails supplémentaires si nécessaire, en fonction de votre projet et de votre audience.
- Vérifiez que les noms de fichiers et de répertoires dans la section **Usage** sont corrects.
