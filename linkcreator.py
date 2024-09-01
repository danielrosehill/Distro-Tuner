import os

def create_symlink(repo_path, config_path, link_name=None):
    try:
        if not link_name:
            link_name = os.path.basename(config_path)
        symlink_path = os.path.join(repo_path, link_name)
        os.symlink(config_path, symlink_path)
        print(f"Symlink created: {symlink_path} -> {config_path}\n")
    except Exception as e:
        print(f"Error creating symlink: {e}\n")

def main():
    print("Hi! I'm your friendly Linux system distro tuner.")
    print("My job is to create symbolic links (symlinks) between config files you commonly access and this distro.\n")
    
    while True:
        repo_path = input("Please provide the full path of this repo on your local computer: ").strip()
        if not os.path.exists(repo_path):
            print("The path you provided does not exist. Please try again.\n")
            continue

        config_path = input("Please provide the full path of the configuration file you'd like to copy: ").strip()
        if not os.path.exists(config_path):
            print("The configuration file does not exist. Please try again.\n")
            continue
        
        use_same_name = input("Would you like to create the symlink with the same filename? (y/n): ").strip().lower()
        
        if use_same_name == 'y':
            link_name = None
        else:
            link_name = input("Please provide the new filename for the symlink: ").strip()
        
        create_symlink(repo_path, config_path, link_name)

if __name__ == "__main__":
    main()
