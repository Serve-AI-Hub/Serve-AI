# Serve-AI

Welcome to the Serve-AI GitHub repository! Serve-AI is a project under the broader Serve-IT initiative at Indiana University, and is funded by the Public Interest Technology University Network (PIT-UN). Serve-AI focuses on developing AI-driven solutions to empower small, resource-constrained nonprofit organizations. Our goal is to create accessible and ethical AI tools, along with training materials, educational resources, and best practices that enhance the efficiency and impact of these nonprofits. In doing so, we further the mission of PIT-UN and Serve-AI to apply technology in the service of the public interest.

## Repository Structure

This repository is organized into two key sections:

### 1. Deliverables

All final deliverables created by students are organized by topic within the `deliverables/` directory. Each topic may contain multiple individual project directories, and each project includes specific deliverables (such as presentations, software tools, training materials, videos, and white papers).

For example, the directory structure blueprint is as follows:
- **deliverables/**
  - **topic/**
    - **project/**
      - **presentations/**
      - **software_tools/**
      - **training_materials/**
      - **videos/**
      - **white_papers/**

And the actual structure may look like this (depending on the topics and projects):

- **deliverables/**
  - **ai_ethics/**
    - **project_1/**
      - **software_tools/**
      - **training_materials/**
    - **project_2/**
      - **presentations/**
      - **training_materials/**
      - **videos/**
      - **white_papers/**

### 2. Documentation

Supporting documents, research notes, and meeting notes are similarly organized by topic within the `documentation/` directory. Each topic may contain multiple individual project directories, with each project including relevant research notes and software documentation.

For example, the directory structure blueprint is as follows:
- **documentation/**
  - **topic/**
    - **project/**
      - **research_notes/**
      - **software_docs/**

## How to Contribute

Thank you for your interest in contributing to the Serve-AI project! Below are the detailed steps to guide you through the process of contributing effectively:

### 1. **Forking the Repository and Cloning Your Fork**

1. **Fork the Repository**: Go to the Serve-AI repository on GitHub and click the "Fork" button to create your own copy of the repository under your GitHub account.

2. **Clone Your Fork**: Once you've forked the repository, clone your fork to your local machine. 
   ```bash
   git clone https://github.com/your-username/serve-ai.git
   ```
   **NOTE:** You'll run commands in your terminal or command prompt.

   **NOTE:** Replace `your-username` with your GitHub username. You can also copy the URL from your forked repository on GitHub.
3. **Navigate to the Repository**: Move into the `serve-ai` directory to start working on your local copy of the repository.
    ```bash
    cd serve-ai
    ```

### 2. **Creating a New Branch**

1. **Create a New Branch**: Before making any changes, create a new branch to keep your work organized.
   ```bash
   git checkout -b my_feature_branch
   ```
   Replace `my_feature_branch` with a descriptive name for your branch (something related to your project or the changes you're making | e.g., `add_training_materials`, or `social_media_and_ai`).

### 3. **Creating a New Project Using the Project Creation Program**

If you are creating a new project, follow these steps. **Otherwise skip to step 4.**:
1. **Run the Program**: Start by running the provided Python script `create_project.py` to create the directory structure for your new project.

**NOTE:** Make sure you're within the `serve-ai` directory before running the script.
   ```bash
   python create_project.py
   ```
2. **Input Project Name**: The program will prompt you to enter a project name. Ensure the name is in snake_case (e.g., `my_project_name`).
3. **Select or Create a Topic**: The program will list existing topics. You can select one using the numeric input or create a new topic by entering the name in snake_case.
4. **Directory Creation**: The program will automatically create the necessary file structure for your new project.

### 4. **Making Changes**

1. **Work on Your Branch**: Make your changes within the appropriate directories. If you are creating or modifying files, ensure that everything is correctly placed within the `deliverables/` or `documentation/` directories.
   
2. **Avoid Large Files**: Do not include large files like `.pptx` or video files directly in the repository. Instead:
   - Upload these files to an external hosting service (e.g., Serve-IT YouTube channel or a cloud storage service).
   - Create a markdown file within the appropriate directory with descriptions of the files and links to where they are hosted.

3. **Commit Your Changes**: After making changes, commit them to your branch. For example, if you want to add files `file1` and `file2` which are either new files or modified files, you can commit them using:

   ```bash
   git add path/to/your/file1 path/to/your/file2
   git commit -m "A short description of your changes"
   ```

   Replace `path/to/your/file1` and `path/to/your/file2` with the actual paths to the files you want to commit.

### 5. **Merging Changes and Syncing Your Fork**

1. **Sync Your Fork** (In your browser - remote):
    1. Go to your forked repository on GitHub.
    2. Make sure you are on the main page of your forked repository.
    3. Select the `main` or `master` branch from the dropdown (whatever is your default branch).
    4. Click on "Sync Fork".
    5. Click on "Update branch".

2. **Ensure Your Branch Is Up-to-Date** (On your local machine): 
   - Before merging, make sure your local branch is up-to-date with the main branch.
   ```bash
    git checkout main
    git pull origin main
    git checkout my_feature_branch
    git merge main
    ```

3. **Resolve Conflicts**: If there are any conflicts, resolve them before proceeding.

### 6. **Submitting a Pull Request**

1. **Push Your Branch to GitHub**: Push your local branch to your remote GitHub fork.
   ```bash
   git push origin my_feature_branch
   ```

2. **Create a Pull Request**: On GitHub, go to your forked repository:
    1. Select the branch you just pushed from the dropdown. (top left - would be `my_feature_branch` in our example)
    2. Click on "Contribute"
    3. Then click "Open Pull Request"
    4. Select the main branch of the Serve-AI repository as the base branch.
    5. Select your branch as the compare branch (`my_feature_branch` in our example).
    6. Add a title and detailed description for your pull request.
    7. Select "Create Pull Request".

3. **Wait for Review**: Your pull request will be reviewed by the project maintainers. They may ask for changes or approve your request. Ensure you address any feedback promptly.

### Some Additional Tips

- **Regularly Sync your Fork:** Keep your fork up-to-date with the main repository by syncing it regularly. This helps prevent conflicts and ensures that your fork has the latest changes.
- **Regularly Update your Branch:** If you're working on a long-term project, regularly update your branch with the latest changes from the main branch to avoid conflicts later on.
- **Save Your Work Frequently:** Commit your changes frequently to save your progress and avoid losing work in case of unexpected issues.
- **Use Descriptive Commit Messages:** Write clear and concise commit messages that describe the changes you've made. This helps maintainers understand your contributions.
- **Don't Submit a Pull Request with Unrelated Changes:** If you're working on multiple features or fixes, create separate branches and pull requests for each set of changes.
- **Don't Submit a Pull Request with Unfinished Work:** Ensure your project is complete, tested, and ready for review before submitting a pull request (if not fully complete, at least something ready for review).
- **Ask for Help:** If you're stuck or need assistance at any point, don't hesitate to ask for help from a mentor, team/project lead, or the project maintainers.

By following these steps, you'll ensure that your contributions are well-organized, compatible with the rest of the project, and easy for maintainers to review. If you're new to Git or encounter any issues, don't hesitate to ask for help from a mentor or consult online resources.

Thank you for contributing to Serve-AI! Your efforts are crucial in advancing our mission to create impactful and accessible AI tools for nonprofits.