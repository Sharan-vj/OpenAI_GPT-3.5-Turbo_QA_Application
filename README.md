# Question Answering Application Using OpenAI GPT-3.5

### Project Description
<p align='justify'>
This project is a Question Answering (QA) application built using OpenAI's GPT-3.5 Turbo model. The application allows users to input a question and receive an accurate and contextually relevant answer from the model. The main goal of this project is to demonstrate the capabilities of OpenAI's language model in understanding and generating human-like text responses, making it a useful tool for various QA tasks.
</p>

### ScreenShot
<img width="800" height="400" align="center" src="/screenshots/Screenshot 1.png">

### Technologies Used in This Project
* **Python** : Core programming language used for developing the model and application

* **openai** : Utilized for accessing OpenAI's GPT-3.5 Turbo model to generate responses based on user queries.

* **streamlit** : Used as the front-end framework for building a user-friendly web interface to interact with the QA model.

* **Git/Github** : For version control and hosting the project repository.

### Installation and Setup

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Sharan-vj/OpenAI_GPT-3.5-Turbo_QA_Application.git
    cd OpenAI_GPT-3.5-Turbo_QA_Application
    ```

2. **Create a Virtual Environment**:
    ```bash
    conda create --name <env name> python=3.10 -y
    ```
3. **Activate the Virtual Enviroment**
    ```bash
    conda activate <env name>
    ```
4. **Install the Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
5. **Set Up OPENAI API KEY in .ENV file**
    ```bash
    OPENAI_API_KEY="your_api_key"
    ```
6. **Run the Streamlit Application**:
    ```bash
    streamlit run app.py
    ```
    The application will be available at `http://127.0.0.1:8501/`.

### Usage
1. **Ask Your Question**: Input your question in the text box provided on the Streamlit app's interface.
2. **Get Answer**: The model will process your question and return a detailed, contextually accurate answer.

### Contributing
Contributions are welcome! Please open an issue or submit a pull request if you have any improvements or suggestions.

### License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

### Acknowledgments
* Special thanks to the open-source community for the libraries used in this project.
