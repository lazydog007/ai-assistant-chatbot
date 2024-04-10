<p align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" alt="project-logo">
</p>
<p align="center">
    <h1 align="center">.</h1>
</p>
<p align="center">
    <em>Empowering conversations, one line at a time.</em>
</p>
<p align="center">
	<!-- local repository, no metadata badges. -->
<p>
<p align="center">
		<em>Developed with the software and tools below.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/Streamlit-FF4B4B.svg?style=default&logo=Streamlit&logoColor=white" alt="Streamlit">
	<img src="https://img.shields.io/badge/OpenAI-412991.svg?style=default&logo=OpenAI&logoColor=white" alt="OpenAI">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=default&logo=Python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/badge/AIOHTTP-2C5BB4.svg?style=default&logo=AIOHTTP&logoColor=white" alt="AIOHTTP">
	<img src="https://img.shields.io/badge/Flask-000000.svg?style=default&logo=Flask&logoColor=white" alt="Flask">
</p>

<br><!-- TABLE OF CONTENTS -->

<details>
  <summary>Table of Contents</summary><br>

- [ Overview](#-overview)
- [ Features](#-features)
- [ Repository Structure](#-repository-structure)
- [ Modules](#-modules)
- [ Getting Started](#-getting-started)
  - [ Installation](#-installation)
  - [ Usage](#-usage)
  - [ Tests](#-tests)
- [ Project Roadmap](#-project-roadmap)
- [ Contributing](#-contributing)
- [ License](#-license)
- [ Acknowledgments](#-acknowledgments)
</details>
<hr>

## Overview

The project, named AI Chatbot Assistant, leverages OpenAI API to create engaging chat experiences. Users interact with GPT-based AI to hold conversations and receive personalized responses. The application includes features like customizable page configurations, user thread management, and dynamic dialogue handling.

---

## Repository Structure

```sh
└── ./
    ├── Pipfile
    ├── Pipfile.lock
    ├── README.md
    ├── app
    │   ├── assistant.py
    │   ├── home.py
    │   └── pages
    ├── example.env
    ├── run.py
    └── threads_db.db
```

---

## Modules

<details closed><summary>.</summary>

| File               | Summary                                                                                                                                                                                                                   |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [run.py](run.py)   | Initializes Flask app, logs start-up, and runs server on host and port.                                                                                                                                                   |
| [Pipfile](Pipfile) | Manages dependencies and specifies Python version for the project. Contains URLs, packages, and versions for libraries like requests, flask, and openai. Ensures compatibility and smooth functioning of the application. |

</details>

<details closed><summary>app</summary>

| File                             | Summary                                                                                                                                                                                                            |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [home.py](app/home.py)           | Engage users with an AI chatbot powered by OpenAI API. Customizable page config and built with Python and Streamlit. Created for Christian C.s Bot Examples in the repository.                                     |
| [assistant.py](app/assistant.py) | Implements chat assistant functionality using OpenAI API. Utilizes shelve for user thread storage. Manages thread creation, message handling, and assistant interaction to generate responses based on user input. |

</details>

<details closed><summary>app.pages</summary>

| File                                               | Summary                                                                                                                                                                                                                                     |
| -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [1_chatgpt.py](app/pages/1_chatgpt.py)             | Enables conversational chat with GPT-based AI. Manages user inputs and AI responses, ensuring a dynamic dialogue within a streamlit interface. Handles session state, user messages, and AI model selection for a seamless chat experience. |
| [2_gym_assistant.py](app/pages/2_gym_assistant.py) | Implements a customer support chat feature integrating OpenAI API for Fuerza Gym. Tracks user interactions, generates AI responses, and displays conversation in a chat-like interface. The session stores a maximum of 10 messages.        |

</details>

---

## Getting Started

**System Requirements:**

- **Python**: `version ^3.12`

### Installation

<h4>From <code>source</code></h4>

> 1. Clone the . repository:
>
> ```console
> $ git clone ../.
> ```
>
> 2. Change to the project directory:
>
> ```console
> $ cd .
> ```
>
> 3. Install the dependencies:
>
> ```console
> $ pipenv install
> ```

### Usage

<h4>From <code>source</code></h4>

> Run . using the command below:
>
> ```console
> $ streamlit run app/home.py
> ```
