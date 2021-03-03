# **Plugin Translations**

> A repository holding translations for our plugins.

- [Discord][discord]
- [Spigot][spigot]
- [Contributors][contributors]

---

## **Overview**
To make our plugins as convenient as possible, we provide global language files in this repository.

They are automatically downloaded each server restart.

If you can't find translations for your own language, that means this specific language is not included in our repository yet.

In that case, you can contribute new translations here.


## **Contribute translations**

### **Instructions**
- check for untranslated phrases in [these files][translations]
  - you can also update existing permissions that still have untranslated phrases
  - if you can't find your language, you need to copy a template from [this folder][templates] and rename it to your language
- translate the phrases
  - for easier editing use the tool shown below
  - it's important that you keep the same format or it won't work
  - don't use color codes
  - place the `** **` symbols around the same words
- uncomment all phrases you translated by removing the `#` in each line
- create a [pull request]

### **Editing Tool**
If you are using [Visual Studio Code][vscode] as your editor, you can now use an extension that
provides syntax highlighting for the [translation files][translations].

You can get it [here][extension].

---

<!-- Links -->
[discord]: https://discord.gg/3JuHDm8
[spigot]: https://www.spigotmc.org/resources/authors/techscode.29620/
[contributors]: CONTRIBUTORS.md
[pull request]: https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests
[translations]: https://github.com/TechsCode-Team/PluginTranslations/blob/master/Translations/
[templates]: https://github.com/TechsCode-Team/PluginTranslations/blob/master/Templates/
[vscode]: https://code.visualstudio.com/
[extension]: https://marketplace.visualstudio.com/items?itemName=RLNT.plugin-translations-syntax
