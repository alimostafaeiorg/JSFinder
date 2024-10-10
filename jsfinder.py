import subprocess

def execute_command(command):
    """Execute a shell command and return the output."""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout

def main():
    print("\033[1;93mCreate By Ali Mostafaei \033[0m") 
    print("\033[1;32mWelcome to the program!\033[0m")  # \033[1;32m for bold green text

    # Step 1: Get a single URL from the user
    url = input("Enter the URL (e.g., https://dell.com): ").strip()

    # Step 2: Run katana on the URL directly
    katana_command = f"katana -u {url} -o katana_output.txt"  # Save Katana output to a file
    print("Running katana...")
    execute_command(katana_command)

    # Step 3: Check the Katana output
    with open('katana_output.txt', 'r') as f:
        katana_output = f.read()

    # Print Katana output for debugging
    print("Katana Output:")
    print(katana_output)

    # Step 4: Extract JavaScript links
    js_links = [line for line in katana_output.splitlines() if '.js' in line]

    # Step 5: Check for HTTP status code 200 using httpx
    if js_links:
        js_links_str = "\n".join(js_links)  # Join links into a single string for checking
        httpx_command = f"echo '{js_links_str}' | httpx -mc 200"
        print("Checking for HTTP 200 status...")
        valid_js_links = execute_command(httpx_command)

        # Step 6: Save results to js.txt
        with open('js.txt', 'w') as f:
            f.write(valid_js_links)

        # Step 7: Print results in green
        print("\033[92m" + valid_js_links + "\033[0m")  # ANSI escape code for green text
    else:
        print("No JavaScript links found.")

if __name__ == "__main__":
    main()
