import os

def createLangFile(pluginName, lang):
    fileName = rf"PluginTranslations\Translations\{pluginName}_{lang}.lang"
    baseTemplate = rf"PluginTranslations\Templates\{pluginName}_English.lang"
    
    if os.path.exists(f"{fileName}"):
        return

    try:
        with open(baseTemplate, 'r') as fileBase:
            lines = fileBase.readlines()

        with open(fileName, 'w') as fileToFix:
            for line in lines:
                if ":" in line:
                    line = "# " + line
                fileToFix.write(line)

        print(f"File '{pluginName}_{lang}' created successfully.")
    except FileNotFoundError as e:
        print(f"[ERROR] File not found. {e}")
    except Exception as e:
        print(f"[ERROR] An error occurred: {e}")

pluginOptions = ["UltraPermissions", "UltraScoreboards", "UltraPunishments", "UltraCustomizer", "UltraEconomy", "UltraRegions", "UltraMotd", "InsaneShops", "InsaneVaults", "InsaneSpawners", "InsaneAnnouncer"] # 11 plugins
languageOptions = ["Czech", "Dutch", "Danish", "French", "German", "Hungarian", "Italian", "Korean", "Polish", "Portuguese", "Romanian", "Russian", "simplified-Chinese", "Slovak", "Spanish", "Taiwan"] # 15 languages 
pluginName = input("Enter the name of the plugin: ")

if pluginName == "all":
    for plugin in pluginOptions:
        for lang in languageOptions:
            createLangFile(plugin, lang)
else:            
    if pluginName in pluginOptions:
        for lang in languageOptions:
            createLangFile(pluginName, lang)
    else:
        print("[ERROR] Invalid plugin name.")
        print("Available plugins: " + ", ".join(pluginOptions))
        
