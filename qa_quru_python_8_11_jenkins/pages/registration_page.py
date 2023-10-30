from selene import browser, command, have

from qa_quru_python_8_11_jenkins import resource


class RegistrationPage:
    def __init__(self):
        self.registered_user_data = browser.element('.table').all('tr td:nth-child(2)')

    def open(self):
        browser.open("/automation-practice-form")

    def type_first_name(self, param):
        browser.element("#firstName").type(param)

    def type_last_name(self, param):
        browser.element("#lastName").type(param)

    def type_email(self, param):
        browser.element("#userEmail").type(param)

    def set_gender(self, param):
        if param == "Male":
            browser.element('[for="gender-radio-1"]').click()
        elif param == "Female":
            browser.element('[for="gender-radio-2"]').click()
        else:
            browser.element('[for="gender-radio-3"]').click()

    def type_mobile(self, param):
        browser.element("#userNumber").type(param)

    def fill_birthday(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()

    def type_subjects(self, param):
        browser.element("#subjectsInput").type(param)
        browser.all(".subjects-auto-complete__menu-list").first.click()

    def set_hobbies(self, param):
        if param == "Sports":
            browser.element("[for='hobbies-checkbox-3']").click()
        elif param == "Reading":
            browser.element("[for='hobbies-checkbox-2']").click()
        elif param == "Music":
            browser.element("[for='hobbies-checkbox-3']").click()

    def file_upload(self, param):
        browser.element("#uploadPicture").send_keys(resource.path(param))

    def type_current_address(self, param):
        browser.element("#currentAddress").type(param)

    def scroll_down(self):
        browser.element('[id="stateCity-label"]').perform(command.js.scroll_into_view)

    def set_state_and_city(self, state, city):
        browser.element("#state").click()
        browser.all(".css-11unzgr").element_by(have.text(state)).click()
        browser.element("#city").click()
        browser.all(".css-11unzgr").element_by(have.text(city)).click()

    def submit(self):
        browser.element("#submit").click()

    def title_should_have_text(self, param):
        browser.element("#example-modal-sizes-title-lg").should(have.text(param))
