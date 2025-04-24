import pkg_resources
import os

def get_import_versions():
    with open("requirements.txt", "w") as f:
        for dist in pkg_resources.working_set:
            f.write(f"{dist.project_name}=={dist.version}\n")

if __name__ == "__main__":
    get_import_versions()
    print("requirements.txt généré avec les versions actuelles")