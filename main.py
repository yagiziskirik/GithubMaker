# Copyright (c) 2023 Yağız Işkırık
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from templates import Templates
from gitignorecreator import GitIgnore
import os
import pathlib

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
        self.versionNumber = ""
        self.repoName = pathlib.Path(__file__).resolve().parent.name

        self.programmingLanguagesList = ['Python', 'Lua', 'Node', 'C++', 'Jupyter Notebooks', 'Beef', 'Android', 'Arch Linux Packages', 'Autotools', 'Cmake', 'Go', 'Godot', 'Java', 'Kotlin', 'Objective-C', 'Packer', 'Perl', 'Qt', 'R', 'Rails', 'Ruby', 'Rust', 'Sass', 'Swift', 'Unity', 'UnrealEngine', 'VisualStudio', 'VisualStudioCode', 'Vim', 'Xcode', 'Eclipse', 'Emacs', 'JetBrains']
        self.OSList = ['macOS', 'Linux', 'Windows']
        self.LicenseList = ['MIT', 'ISC', 'Apache License 2.0', 'GNU General Public License v3.0']

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

    def changeIfNotEmpty(self, txt, currentVal):
        tempVal = input(f"{txt} ({currentVal}): ")
        if tempVal != "":
            return tempVal
        else:
            return currentVal

    def printSettings(self):
        print("")
        print(f"Github User Name: {self.userName}")
        print(f"Repository Name: {self.repoName}")
        print(f"Full Name: {self.name}")
        print(f"Contact Mail: {self.contactMail}")
        print(f"Program Version: {self.versionNumber}")
        print("--------------------")
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
        while not self.isCont:
            self.repoName = self.changeIfNotEmpty("Repository Name", self.repoName)
            self.userName = self.changeIfNotEmpty("Github User Name", self.userName)
            self.name = self.changeIfNotEmpty("Full Name", self.name)
            self.contactMail = self.changeIfNotEmpty("Contact Mail", self.contactMail)
            self.versionNumber = self.changeIfNotEmpty("Program Version", self.versionNumber)

            self.isCodeOfConduct = self.editVar('Code of Conduct (Y/n): ', True)
            self.isContributing = self.editVar('Contributing (Y/n): ', True)
            self.isLicense = self.editVar('License (Y/n): ', True)
            if self.isLicense:
                self.selectedLicense = self.selectSingle(self.LicenseList)
            self.isReadme = self.editVar('Readme (Y/n): ', True)
            self.isSecurity = self.editVar('Security (Y/n): ', True)
            self.isGithubTemplates = self.editVar('Github Templates (Y/n): ', True)
            self.isOSIgnore = self.editVar('OS Files Ignore (Y/n): ', True)
            if self.isOSIgnore:
                self.selectedOSL = self.selectMultiple(self.OSList.copy())
            self.isPLIgnore = self.editVar('Programming Language Ignore (Y/n): ', True)
            if self.isPLIgnore:
                self.selectedPL = self.selectMultiple(self.programmingLanguagesList.copy())

            self.printSettings()
            self.isCont = self.editVar('Is it ok? (Y/n): ', True)

        if self.isOSIgnore or self.isPLIgnore:
            gitIgnoreGenerator = GitIgnore(self.selectedPL, self.selectedOSL)
            gitIgnoreFile = gitIgnoreGenerator.createIgnore()
            with open(".gitignore", "w") as f:
                f.write(gitIgnoreFile)

        allTemplates = Templates(self.userName, self.contactMail, self.versionNumber, self.name, self.repoName, self.selectedLicense)

        if self.isLicense:
            if not os.path.exists("LICENSE.md"):
                licenseFile = allTemplates.getLicense()
                with open("LICENSE.md", "w") as f:
                    f.write(licenseFile)

        if self.isCodeOfConduct:
            if not os.path.exists("CODE_OF_CONDUCT.md"):
                codeOfConductFile = allTemplates.codeOfConduct()
                with open("CODE_OF_CONDUCT.md", "w") as f:
                    f.write(codeOfConductFile)

        if self.isContributing:
            if not os.path.exists("CONTRIBUTING.md"):
                contributingFile = allTemplates.contributing()
                with open("CONTRIBUTING.md", "w") as f:
                    f.write(contributingFile)

        if self.isSecurity:
            if not os.path.exists("SECURITY.md"):
                securityFile = allTemplates.security()
                with open("SECURITY.md", "w") as f:
                    f.write(securityFile)

        if self.isReadme:
            if not os.path.exists("README.md"):
                readmeFile = allTemplates.readme()
                with open("README.md", "w") as f:
                    f.write(readmeFile)

        if self.isGithubTemplates:
            if not os.path.exists(".github"):
                os.mkdir(".github")
            if not os.path.exists(".github/ISSUE_TEMPLATE"):
                os.mkdir(".github/ISSUE_TEMPLATE")
            if not os.path.exists(".github/PULL_REQUEST_TEMPLATE.md"):
                pullRequestFile = allTemplates.pullRequestTemplate()
                with open(".github/PULL_REQUEST_TEMPLATE.md", "w") as f:
                    f.write(pullRequestFile)
            if not os.path.exists(".github/ISSUE_TEMPLATE/bug_report.md"):
                bugReportFile = allTemplates.bugReport()
                with open(".github/ISSUE_TEMPLATE/bug_report.md", "w") as f:
                    f.write(bugReportFile)
            if not os.path.exists(".github/ISSUE_TEMPLATE/feature_request.md"):
                featureRequestFile = allTemplates.featureRequest()
                with open(".github/ISSUE_TEMPLATE/feature_request.md", "w") as f:
                    f.write(featureRequestFile)
            if not os.path.exists(".github/ISSUE_TEMPLATE/question.md"):
                questionFile = allTemplates.question()
                with open(".github/ISSUE_TEMPLATE/question.md", "w") as f:
                    f.write(questionFile)

if __name__ == '__main__':
    GithubMaker()
