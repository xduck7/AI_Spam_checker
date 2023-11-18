# AI_Spam_checker

### AI for checking messages for spam

---
### 📂 Project structure
- [![Folder Badge](https://img.shields.io/badge/-Folder_"Data"-orange?)](https://github.com/xduck7/AI_Spam_checker/tree/main) **contains data in csv format for training AI**
- [![Folder Badge](https://img.shields.io/badge/-Folder_"Image"-orange?)](https://github.com/xduck7/AI_Spam_checker/tree/main) **contains images for application**
- [![Folder Badge](https://img.shields.io/badge/-Folder_"Model"-orange?)](https://github.com/xduck7/AI_Spam_checker/tree/main) **contains files with AI model, weights, files .pkl to transform numbers into matrices and back**
- [![Python Badge](https://img.shields.io/badge/-Learning.py-darkgreen?style=flat&logo=Python&logoColor=white)](https://github.com/xduck7/AI_Spam_checker/tree/main) **the file in which the AI is trained to recognize spam. AI takes the data for her training from the folder "Data"**
- [![Python Badge](https://img.shields.io/badge/-Predict.py-darkgreen?style=flat&logo=Python&logoColor=white)](https://github.com/xduck7/AI_Spam_checker/tree/main) **after AI training , the work goes to "Predict.py" a file that works with the same model and files from the folder "Model" that were received after execution "Learning.py"**
- [![Python Badge](https://img.shields.io/badge/-Rqst.py-darkgreen?style=flat&logo=Python&logoColor=white)](https://github.com/xduck7/AI_Spam_checker/tree/main)
  **the file that is responsible for adding data about the request to the program. That is, after executing the request, information about the request and the result of the request (spam or not) is added to our PostgreSQL DB "forspam"**
- [![Python Badge](https://img.shields.io/badge/-Start.py-darkgreen?style=flat&logo=Python&logoColor=white)](https://github.com/xduck7/AI_Spam_checker/tree/main)
  **a file that puts everything together and displays it all in the Tkinter interface. It is in it that we will create a request to our AI and get answers**

---

### ⚙️ Config
- 🐍 Python: **3.11.5**
- 🐘 PostgreSQL: **42.6.0**
- 🔶 Tensorflow: **2.15.0**
- 💠 Pandas: **2.1.3**

---

### 🔠 Structure of DB "forspam"
  | Id | Date_time | Author | Content | Class |
  |---------|----------|-----------|---------|----------|
  | Id 1    | Date_time 1  | Author 1   | Content 1 | Class 1 |
  | Id 2    | Date_time 2  | Author 2   | Content 2 | Class 2 |
  | Id 3    | Date_time 3  | Author 3   | Content 3 | Class 3 |

  - **Id - a column that is randomly generated and linked to the request**
  - **Date_time - the time when the request was made**
  - **Author - who made the request (in this case, the name is generated randomly)**
  - **Content - request content**
  - **Class - request result. Spam (1) or NOT spam (0)**

---

### 🗒️ Required modules
  - **Pandas**
  - **Numpy**
  - **Joblib**
  - **Tensorflow**
  - **Tkinter**
  - **Psycopg2**
  - **Names** <br />
  
**⚒️ To install the modules, enter the command in the terminal: 'pip install [module_name]' (without [])**
