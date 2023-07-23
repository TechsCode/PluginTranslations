import re

def add_hash_before_colon_in_file(pluginName):

    baseTemplate = f"PluginTranslations\Templates\{pluginName}_English.lang"

    try:
        with open(baseTemplate, 'r') as fileBase:
            lines = fileBase.readlines()

        with open(filePath, 'w') as fileToFix:
            for line in lines:
                if ":" in line:
                    line = "# " + line
                fileToFix.write(line)

        print("[SUCCESS] File successfully updated.")
    except FileNotFoundError as e:
        print(f"[ERROR] File not found. {e}")
    except Exception as e:
        print(f"[ERROR] An error occurred: {e}")

filePath = input("Enter the file path: ")

pattern = r"\\([^\\]+)_"
match = re.search(pattern, filePath)

if match:
    pluginName = match.group(1)
    add_hash_before_colon_in_file(pluginName)
