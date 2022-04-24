# Adding a new language

* Checkout repository
* Make sure application builds correctly - open an issue if something does not work
* Create a new translation file by running
  ```shell
  make create-new-translation lang=<locale>
  ```
  while `<locale>` is the locale for the language to add
* Update all possible translations by running
  ```shell
  make update-translations
  ```
* New `<locale>.ts` file should appear in the `i18n` directory
* Translate the `ts` file using Qt Linguist 6
* To test the translation:
  * Run
    ```shell
    make develop-build
    ```
  * Edit the `settings.ini` and change `language` to the new `<locale>`
  * If the language option is not present in the `settings.ini`, add a new line `language=<locale>`
* Open a new pull request
* Add a new entry in the `MpvqcLanguageModel.qml` file

**Thank you very much!** 💚