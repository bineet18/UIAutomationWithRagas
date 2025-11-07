# UIAutomationWithRagas

## Overview

This project serves as a proof-of-concept (POC) for automating the evaluation of chatbot responses through user interface (UI) interactions. It leverages Playwright for browser automation to simulate user queries on platforms such as ChatGPT and employs the Ragas framework to assess response quality using a suite of predefined metrics. The primary intent is to demonstrate a streamlined method for testing and validating AI-generated outputs in a controlled, repeatable manner, focusing on aspects like factual accuracy, semantic alignment, safety, and overall response quality.

The system is designed to facilitate rapid prototyping and experimentation in AI response evaluation, enabling developers and researchers to integrate automated testing into their workflows without extensive manual intervention.

## Features

- **Browser Automation**: Utilizes Playwright to navigate web interfaces, submit queries, and capture responses from chatbots.
- **Response Evaluation**: Applies Ragas metrics including factual correctness, semantic similarity, harmfulness, maliciousness, coherence, correctness, and conciseness.
- **Asynchronous Handling**: Incorporates mechanisms to manage asynchronous operations, ensuring reliable execution of evaluation tasks.
- **Configurable Thresholds**: Allows assertions based on metric scores to validate response quality against predefined benchmarks.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/UIAutomationWithRagas.git
   cd UIAutomationWithRagas
   ```

2. Install dependencies using pip:
   ```
   pip install -r requirements.txt
   ```

   Note: The requirements include libraries such as Playwright, pytest, pytest-asyncio, Ragas, LangChain, and OpenAI.

3. Install Playwright browsers:
   ```
   playwright install
   ```

## Usage

1. Configure the evaluation metrics in `evaluators.py` as needed, ensuring the LLM and embeddings are properly set via `config.py`.

2. Run the tests using pytest:
   ```
   pytest test_chatbot_evaluation.py -v
   ```

   This executes the automated test suite, which interacts with ChatGPT, captures responses, and applies the defined metrics for validation.

## Project Structure

- `evaluators.py`: Defines asynchronous functions for various Ragas metrics.
- `test_chatbot_evaluation.py`: Contains the Playwright-based test for querying and evaluating chatbot responses.
- `config.py`: Manages configuration for the evaluator LLM and embeddings.
- `pytest.ini`: Pytest configuration file.
- `.gitignore`: Specifies files and directories to exclude from version control.

## Requirements

- Python 3.13+
- Dependencies as listed in `requirements.txt` (e.g., playwright==1.49.0, pytest==8.3.4, ragas==0.2.6, etc.)

## Limitations and Future Enhancements

As a POC, this project focuses on basic functionality and may require adjustments for production use, such as enhanced error handling, support for multiple chatbots, or dynamic query generation. Potential enhancements include integrating additional metrics, optimizing wait mechanisms for streaming responses, and expanding browser compatibility.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For inquiries or contributions, please contact [your-email@example.com].