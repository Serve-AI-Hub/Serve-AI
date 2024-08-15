import os
import re

# Function to check if the name is in snake_case
def is_snake_case(name):
    return bool(re.match("^[a-z0-9_]+$", name))

# Function to create directories
def create_project_structure(base_dir, topic, project):
    paths = [
        os.path.join(base_dir, topic, project, 'presentations'),
        os.path.join(base_dir, topic, project, 'software_tools'),
        os.path.join(base_dir, topic, project, 'training_materials'),
        os.path.join(base_dir, topic, project, 'videos'),
        os.path.join(base_dir, topic, project, 'white_papers'),
        os.path.join(base_dir.replace('deliverables', 'documentation'), topic, project, 'research_notes'),
        os.path.join(base_dir.replace('deliverables', 'documentation'), topic, project, 'software_docs')
    ]
    for path in paths:
        os.makedirs(path, exist_ok=True)
        
    # Create and populate the Markdown file named after the project
    markdown_filename = f"{project}.md"
    markdown_path = os.path.join(base_dir, topic, project, markdown_filename)
    
    with open(markdown_path, 'w') as readme_file:
        # if the title includes ai by itself, but not as part of a word, capitalize it
        split_title = project.split('_')
        title = ' '.join(split_title).title()
        split_title = title.split(' ')
        if 'Ai' in split_title:
            split_title[split_title.index('Ai')] = 'AI'
        title = ' '.join(split_title)
        
        readme_file.write(f"# {title}\n\n")
        readme_file.write("## Description\n")
        readme_file.write("Provide a brief overview of the project. Describe the problem it addresses, the goals of the project, and the key features or functionalities it offers. This section should give a clear understanding of what the project is about and why it was created.\n\n")
        readme_file.write("## Authors/Contributors\n")
        readme_file.write("- [Name](https://github.com/username)\n")
        readme_file.write("- [Name](https://github.com/username)\n\n")
        readme_file.write("List all the people who contributed to the project, including their roles if relevant. You can link to their GitHub profiles or other professional profiles.\n\n")
        readme_file.write("## Ideal Audience\n")
        readme_file.write("Describe the target audience for this project. Who will benefit the most from using this project? This could include specific types of nonprofits, educators, students, or any other group that might find this project particularly useful.\n\n")
        readme_file.write("## Prerequisites\n")
        readme_file.write("List any prerequisites needed to use or understand the project. This might include knowledge of certain technologies, tools, or background information (Can be none! Or something as simple as familiarity with web browsing).\n\n")
        readme_file.write("- **Technical Prerequisites**: Mention any technical skills or tools needed.\n")
        readme_file.write("- **Knowledge Prerequisites**: List any specific knowledge or background information required.\n\n")
        readme_file.write("## Installation/Setup\n")
        readme_file.write("Provide step-by-step instructions on how to install or set up the project. This could include instructions for downloading, configuring, and running the project. (Section can be deleted if not applicable)\n\n")
        readme_file.write("## Resource Links\n")
        readme_file.write("Provide links to projects if they are hosted elsewhere (e.g. Serve-AI YouTube, or other cloud service) or to any other resources that are relevant to the project. (Section can be deleted if not applicable)")
    
    print(f"Project structure and description template created for '{project}' under topic '{topic}'.")

# Function to select a topic
def select_topic(existing_topics):
    print("\nSelect the topic for the project:")
    for idx, topic in enumerate(existing_topics, start=1):
        print(f"{idx}. {topic}")
    print(f"{len(existing_topics) + 1}. Create a new topic")

    while True:
        selection = input("Enter the number of your choice: ")
        if selection.isdigit():
            selection = int(selection)
            if 1 <= selection <= len(existing_topics):
                return existing_topics[selection - 1]
            elif selection == len(existing_topics) + 1:
                return "Create a new topic"
        print("Invalid selection. Please enter a valid number.")

# Main function
def main():
    base_dir = 'deliverables'

    # Get project name
    while True:
        project_name = input("Enter the new project name (in snake_case): ")
        if is_snake_case(project_name):
            break
        else:
            print("The project name must be in snake_case (e.g., 'my_project_name').")

    # Get topic name
    existing_topics = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]

    if existing_topics:
        topic_choice = select_topic(existing_topics)
    else:
        print("\nNo existing topics found.")
        topic_choice = "Create a new topic"

    if topic_choice == "Create a new topic":
        while True:
            topic_name = input("Enter the new topic name (in snake_case): ")
            if is_snake_case(topic_name):
                break
            else:
                print("The topic name must be in snake_case (e.g., 'my_topic_name').")
    else:
        topic_name = topic_choice

    # Create the directory structure
    create_project_structure(base_dir, topic_name, project_name)

if __name__ == "__main__":
    main()