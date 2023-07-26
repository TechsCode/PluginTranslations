import os

def create_lang_file(plugin_name, language_list):
    filename = f"PluginTranslations\Translations\{plugin_name}_{language_list}.lang"
    baseTemplate = f"PluginTranslations\Templates\{plugin_name}_English.lang"
    
    if os.path.exists(f"{filename}"):
        return

    try:
        with open(baseTemplate, 'r') as fileBase:
            lines = fileBase.readlines()

        with open(filename, 'w') as fileToFix:
            for line in lines:
                if ":" in line:
                    line = "# " + line
                fileToFix.write(line)

        print(f"File '{filename}' created successfully.")
    except FileNotFoundError as e:
        print(f"[ERROR] File not found. {e}")
    except Exception as e:
        print(f"[ERROR] An error occurred: {e}")

options = ["UltraPermissions", "UltraScoreboards", "UltraPunishments", "UltraCustomizer", "UltraEconomy", "UltraRegions", "UltraMotd", "InsaneShops", "InsaneVaults", "InsaneSpawners", "InsaneAnnouncer"]
languages = ["Czech", "Dutch", "Danish", "French", "German", "Hungarian", "Italian", "Korean", "Polish", "Portuguese", "Romanian", "Russian", "simplified-Chinese", "Slovak", "Spanish", "Taiwan"]
plugin_name = input("Enter the name of the plugin: ")

if plugin_name == "all":
    for option in options:
        for lang in languages:
            create_lang_file(option, lang)
else:            
    if plugin_name in options:
        for lang in languages:
            create_lang_file(plugin_name, lang)
    else:
        print("Invalid plugin name.")
