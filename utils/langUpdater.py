import os

def find_and_update_lines(option):

    base_template = f"PluginTranslations\Templates\{option}_English.lang"
    translations_folder = f"PluginTranslations\Translations"

    with open(base_template, 'r', encoding="utf-8") as file1:
        lines_file1 = file1.readlines()

    def extract_text_before_colon(line):
        if ':' in line:
            text = line.split(':')[0].strip()
            return text.strip('#').strip()
        return None

    def fix_hash_lines(line):
        if ":" in line and line.startswith('#') and not line.startswith('# '):
            return f"# {line[1:]}"
        return line
    
    for file in os.listdir(translations_folder):
        if file.endswith(".lang") and option in file:
            with open(os.path.join(translations_folder, file), 'r', encoding="utf-8") as file2:
                lines_file2 = file2.readlines()

                lines_dict_file2 = {extract_text_before_colon(line): line for line in lines_file2}
                lines_to_add = []

                for line_file1 in lines_file1:
                    text_to_search = extract_text_before_colon(line_file1)
                    if text_to_search is not None:
                        if text_to_search not in lines_dict_file2:
                            # If the text is not found in file2, add it to the list of lines to add
                            lines_to_add.append((lines_file1.index(line_file1), f"# {line_file1.strip()}\n"))
                            print(f"[DEBUG] Adding line from file1: {line_file1.strip()}")
                        else:
                            # If the text is found in file2, remove the line from file2
                            line_to_move = lines_dict_file2[text_to_search]
                            lines_file2.remove(line_to_move)
                            # Add the line to the list of lines to add at its new position
                            lines_to_add.append((lines_file1.index(line_file1), line_to_move))
                            print(f"[DEBUG] Moving line from file2: {line_to_move.strip()}")

                # Sort the lines to add based on their original positions in file1
                lines_to_add.sort(key=lambda x: x[0])

                # Add the sorted lines to file2
                for line_to_add in lines_to_add:
                    index, line = line_to_add
                    lines_file2.insert(index, line)

                # Fix lines starting with '#'
                lines_file2 = [fix_hash_lines(line) for line in lines_file2]

                # Write the updated contents back to the second file
                with open(os.path.join(translations_folder, file), 'w', encoding="utf-8") as file2:
                    file2.writelines(lines_file2)

                print("[SUCCESS] Language update completed successfully.")


if __name__ == "__main__":
    # Ask for the two file paths
    options = ["UltraPermissions", "UltraScoreboards", "UltraPunishments", "UltraCustomizer", "UltraEconomy", "UltraRegions", "InsaneShops", "InsaneVaults", "InsaneAnnouncer"]

    plugin_name = input("Enter the name of the plugin: ")

    if plugin_name in options:
        find_and_update_lines(plugin_name)