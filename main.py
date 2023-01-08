# Copyright (c) 2023 Yağız Işkırık
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from templates import Templates

class GithubMaker:
    def __init__(self):
        self.isCont = False

        self.isCodeOfConduct = True
        self.isContributing = True
        self.isLicense = True
        self.isReadme = True
        self.isSecurity = True
        self.isGithubTemplates = True
        self.isOSIgnore = False
        self.isPLIgnore = False

        self.userName = ""
        self.name = ""
        self.contactMail = ""
        self.version = ""
        self.repoName = ""

        self.programmingLanguagesList = ['Python', 'Lua']
        self.OSList = ['macOS', 'Linux', 'Windows']
        self.LicenseList = ['MIT', 'ISC']

        self.selectedPL = []
        self.selectedOSL = []
        self.selectedLicense = "MIT"

        self.start()

    def editVar(self, inputTxt, defaultVal):
        while True:
            tempVar = input(inputTxt)
            if tempVar == "":
                return defaultVal
            elif tempVar == "y" or tempVar == "Y":
                return True
            elif tempVar == "n" or tempVar == "N":
                return False
            else:
                print("Wrong input.\n")

    def selectSingle(self, listToChoose):
        while True:
            for i, key in enumerate(listToChoose):
                print(f"{i+1}: {key}")
            print("")
            selection = input("Selection: ")
            try:
                if int(selection) < 1:
                    raise TypeError()
                return listToChoose[int(selection)-1]
            except ValueError:
                print("Please enter a number.")
            except TypeError:
                print("Please enter a valid number.")
            except IndexError:
                print("Please enter a valid number.")

    def selectMultiple(self, listToChoose):
        tempSelection = []
        while True:
            for i, key in enumerate(listToChoose):
                print(f"{i+1}: {key}")
            print("")
            selection = input("Selection (enter to finish): ")
            try:
                if selection == "":
                    return tempSelection
                if int(selection) < 1:
                    raise TypeError()
                tempSelection.append(listToChoose[int(selection)-1])
                listToChoose.pop(int(selection)-1)
            except ValueError:
                print("Please enter a number.")
            except TypeError:
                print("Please enter a valid number.")
            except IndexError:
                print("Please enter a valid number.")

    def printSettings(self):
        print(f"Code of Conduct: {self.isCodeOfConduct}")
        print(f"Contributing: {self.isContributing}")
        print(f"License: {self.isLicense}")
        if self.isLicense:
            print(f"License Type: {self.selectedLicense}")
        print(f"Readme: {self.isReadme}")
        print(f"Security: {self.isSecurity}")
        print(f"Github Templates: {self.isGithubTemplates}")
        print(f"OS Files Ignore: {self.isOSIgnore}")
        if self.isOSIgnore:
            for i, key in enumerate(self.selectedOSL):
                print(f"{i+1}: {key}")
        print(f"Programing Languages Ignore: {self.isPLIgnore}")
        if self.isPLIgnore:
            for i, key in enumerate(self.selectedPL):
                print(f"{i+1}: {key}")
        print("")

    def start(self):
        self.printSettings()
        self.isCont = self.editVar('Is it ok? (Y/n): ', True)
        while not self.isCont:
            self.isCodeOfConduct = self.editVar('Code of Conduct (Y/n): ', True)
            self.isContributing = self.editVar('Contributing (Y/n): ', True)
            self.isLicense = self.editVar('License (Y/n): ', True)
            if self.isLicense:
                self.selectedLicense = self.selectSingle(self.LicenseList)
            self.isReadme = self.editVar('Readme (Y/n): ', True)
            self.isSecurity = self.editVar('Security (Y/n): ', True)
            self.isGithubTemplates = self.editVar('Github Templates (Y/n): ', True)
            self.isOSIgnore = self.editVar('OS Files Ignore (y/N): ', False)
            if self.isOSIgnore:
                self.selectedOSL = self.selectMultiple(self.OSList.copy())
            self.isPLIgnore = self.editVar('Programming Language Ignore (y/N): ', False)
            if self.isPLIgnore:
                self.selectedPL = self.selectMultiple(self.programmingLanguagesList.copy())

            print("")
            self.printSettings()
            self.isCont = self.editVar('Is it ok? (Y/n): ', True)

if __name__ == '__main__':
    GithubMaker()
