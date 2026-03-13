# Project Context:
This project is based on identifying the happened accidents with the help of hardware (ESP32: Acts as the brain, processing sensor data and managing low-power modes.MPU6050 (Accel/Gyro): Constantly monitors g-force and tilt angles.NEO-6M GPS: Fetches latitude and longitude.SIM800L/A: Sends the SMS or HTTP request to your alert server). And here for the backend I am using python backend scripts to process the data received from the hardware and send alerts to the nearby hospitals and to the concerned family members via SMS. As said before the backend server is powered by the fastapi by python. 

And here the data collected from the accident will be stored in the database till the final senario weather it was a false alarm or not, weather the patient is alive or not, the severity of the accident and the type of the accident. This data will be used for future analysis and to improve the accuracy of the system.

(FUTURE IMPLEMENTATION: I am planning to train a model using the stored data to predict the accidents weather it is false or not and other details like the severity of the accident and the type of the accident.)


## 1. Follow Coding Standards
### 1.1 Naming Conventions
- Use consistent naming conventions for variables, functions, and classes.

### 1.2 Code Organization
- Organize code logically into modules and functions.
- Make sure to write tests for all new features and bug fixes.
- Make sure to write the code under 350-500 lines.
- If it exceeds more than 500 lines even after refactoring create a new file.
- Remember that when the code is split into multiple files make sure to maintain the connection between them. After splitting those files, update all imports and references accordingly.
- While splitting the files, ensure that the logic and functionality remain intact.
- It should not introduce any new bugs, issues or change the existing behavior.
- Make sure to add comments to refer the other split files, so it will not create any confusion.

### 1.3 Managing Connected and Dependent Files
- If you modify a file that is connected to or imported by other files (e.g., shared modules, APIs, or utility functions), ensure you update all dependent files accordingly. This includes updating imports, function calls, documentation, and any related logic to maintain consistency and prevent errors across the codebase.

### 1.4 Dependencies, Libraries & Frameworks
- Use appropriate libraries and frameworks to simplify tasks.
- Update all the dependencies, libraries & frameworks into the requirements.txt, documentation files.

## 2. Comment and Document
- Add clear, concise comments for complex logic for every line if possible.
- Document function inputs, outputs, and side effects.
- Make sure to write documentation and README files along with the code, without needing to be asked or delayed.
- If there are files which are interlinked with other files make sure at the end of the code to add comments explaining the relationships and dependencies.
- Remember that every single function, class, module & code logic must be explained properly by comments right within the code file itself.
- An example given below:
"def calculate_grade(score):
    """
    This function takes a numerical score and returns a letter grade.
    Logic: Uses conditional 'if-elif-else' statements to check 
    which range the score falls into.
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"

# A list of student scores to process
student_scores = [95, 82, 67, 45, 89]

# A loop to iterate through each item in the list
for score in student_scores:
    # Function Call: Passing the current score to the logic handler
    grade = calculate_grade(score)
    
    # Condition: Checking if the student passed or failed
    # Technical context: 'F' is our threshold for failure
    if grade == "F":
        status = "Needs Improvement"
    else:
        status = "Passed"
        
    print(f"Score: {score} | Grade: {grade} | Status: {status}")"

- As said before every line must be explained properly with comments, so that it will be easy for anyone to understand the code without needing to go through the entire code logic.

## 3. Error Handling
- Anticipate possible errors and handle exceptions gracefully.
- Validate inputs and outputs to prevent unexpected behavior.

## 5. Maintain Readability
- Prioritize clarity over cleverness; compact code should still be understandable.
- Avoid overly complex one-liners that hinder readability.

## 7. New chat session
- When the user is starting a new chat session, ensure to go through the entire context of the project, existing codebase, documentation, README files, requirements.txt, CHANGELOG.md and any other relevant files to understand the current state of the project.

## 8. About the files & folders: (documentation folder)
- Here the folder `documentation` is meant to document every changes made to the project. Which means if a file is changed or a new file is created or a folder is created, it must be documented properly in the documentation folder.
- Just need to make sure that the documentation files are not redundant or duplicate at the same time they must not be over crowded with information.
- Always remember that when you have documented about the new file or folder in the documentation folder, when the same file or folder is modified, make sure to study the modified file & the documented file and then update the documentation file accordingly. For this you should not create a new documentation file, instead you need to update the existing documentation file related to that modified file or folder. This is because if you create a new documentation file for the modified file or folder, it will create confusion and redundancy. 
### 8.1 README.md
- This README.md file must act like a project overview, setup guide.
- It must contain information about the project, how to set it up, how to contribute, coding standards, folder structure, and any other relevant information.
- Remember that this file should not act like a documentation file. So avoid adding too much detailed information here.
- Remember that in this file you need to mention each and every folder and file present in the project with a very short description of what it contains (Must complete within 2 lines) and its purpose in the project. Along with this I need you to mention the architectural flow of the project with the help of Mrakdown & using ASCI symbols to represent the flow. 
- Since the project evolves over time, make sure to update the README.md file whenever there are changes in the project structure, new features added, or any other relevant updates.
- For example if there is a file called `example.py` created or modified, then you need to update the README.md file, if the file is update or modified, delete the specific line describing and the diagram related to that file, study the modified file and then add a new line describing the modified file along with the updated diagram related to that file. 
### 8.4 requirements.txt:
- This requirements.txt file must contain all the dependencies, libraries & frameworks used in the project.
- Every single time a new dependency, library or framework is added to the project, it must be updated properly in this file.

### 8.5 frontend and backend folders:
- The frontend folder `frontend` contains all the code related to the user interface and user experience.
- The backend folder `backend` contains all the code related to server-side logic, database interactions, and API integrations and the core functionality of the project.

### 8.6 Git & Github:
- When ever the user types the word 'git --commands' in the chat you need to make sure to generate the necessary git commands along with the commit messages specifically tailored to the modified or newly created files.
- This ensures that all newly created or modified files are properly committed to the repository with clear and relevant messages.
- So here to get context about the modified or newly created files/folders, you need to execute the git status command to get the list of modified or newly created files/folders and then generate the necessary git commands along with the commit messages specifically tailored to those modified or newly created files/folders.
- Make sure that the commit messages are more descriptive rather than generic.
- If the chat is in the agent mode execute the git commands automatically.