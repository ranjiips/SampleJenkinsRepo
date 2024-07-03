

from pythonProject.python_exercises.seleniumBaseActions import SeleniumBaseActions

class SeleniumPracticeElements(SeleniumBaseActions):

    def __int__(self):
        SeleniumBaseActions.__int__(self)

    def launch_browser_load_url(self, url, pageTitle):
        #self.launch_browser_and_maximize()
        self.load_webPage(url)
        title = self.get_page_title()
        print("Title of the web page is: " + title)
        title.__eq__(pageTitle)



pageURL = "https://www.letskodeit.com/practice"
autoSuggestInput = "input#autosuggest"
bmwRadioBtn = "input#bmwradio"
benzRadioBtn = "input#benzradio"
hondaRadioBtn = "input#hondaradio"
bmwCheckBox = "input#bmwcheck"
benzCheckBox = "input#benzcheck"
hondaCheckBox = "input#hondacheck"

practicePage = SeleniumPracticeElements()
practicePage.launch_browser_load_url(pageURL,"Practice Page")
practicePage.enter_text(autoSuggestInput,"Sample Text")
practicePage.click_element(bmwRadioBtn)
practicePage.click_element(benzRadioBtn)
practicePage.click_element(bmwCheckBox)
practicePage.click_element(hondaCheckBox)


