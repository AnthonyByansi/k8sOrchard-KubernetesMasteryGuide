import os

def create_directory(path):
    os.makedirs(path, exist_ok=True)

def create_file(path, content=""):
    with open(path, 'w') as f:
        f.write(content)

# Create the root directory
create_directory("k8sOrchard-KubernetesMasteryGuide")

# Create subdirectories
sections = [
    "docs",
    ".github",
    "code-examples",
    "docs/getting-started",
    "docs/core-concepts",
    "docs/networking",
    "docs/storage",
    "docs/configuration",
    "docs/security",
    "docs/monitoring-and-logging",
    "docs/scaling-and-autoscaling",
    "docs/deployment-strategies",
    "docs/advanced-topics",
    "docs/troubleshooting",
    "docs/hands-on-labs",
    "docs/images/lab-screenshots",
    "docs/images/architecture-diagrams"
]

for section in sections:
    create_directory(section)

# Create Markdown files
markdown_files = [
    "docs/index.md",
    "docs/getting-started/introduction.md",
    # ... add more files here
]

for md_file in markdown_files:
    create_file(md_file)

# Create sub-section Markdown files
sub_sections = [
    "core-concepts",
    "networking",
    "storage",
    "configuration",
    "security",
    "monitoring-and-logging",
    "scaling-and-autoscaling",
    "deployment-strategies",
    "advanced-topics",
    "troubleshooting"
]

for sub_section in sub_sections:
    for i in range(1, 10):
        md_file = f"docs/{sub_section}/{str(i).zfill(2)}-placeholder.md"
        create_file(md_file)

# Create hands-on lab Markdown files
hands_on_labs = [
    "lab-01-deploying-microservices",
    "lab-02-multi-environment-cluster",
    "lab-03-rolling-updates",
    # ... add more labs here
]

for lab in hands_on_labs:
    md_file = f"docs/hands-on-labs/{lab}.md"
    create_file(md_file)

# Create code example directories and files
code_examples = [
    "lab-01-deploying-microservices",
    "lab-02-multi-environment-cluster"
    # ... add more labs here
]

for code_example in code_examples:
    create_directory(f"code-examples/{code_example}")
    create_file(f"code-examples/{code_example}/app-deployment.yaml")
    create_file(f"code-examples/{code_example}/service.yaml")

# Create GitHub-specific files
github_files = [
    ".github/ISSUE_TEMPLATE/bug_report.md",
    ".github/ISSUE_TEMPLATE/feature_request.md",
    ".github/ISSUE_TEMPLATE/question.md",
    ".github/workflows/build.yml",
    ".github/workflows/deploy.yml",
    ".github/CONTRIBUTING.md"
]

for github_file in github_files:
    create_file(github_file)

# Create images placeholder files
image_files = [
    "docs/images/lab-screenshots/lab-01/step-01.png",
    "docs/images/lab-screenshots/lab-01/step-02.png",
    # ... add more image files here
    "docs/images/architecture-diagrams/kubernetes-components.png",
    "docs/images/architecture-diagrams/network-policies.png"
    # ... add more image files here
]

for image_file in image_files:
    create_file(image_file, content="Placeholder content")

# Create root-level files
create_file("LICENSE")
create_file("README.md")
