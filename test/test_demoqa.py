import allure
from selene import have, browser
from allure_commons.types import Severity

from qa_quru_python_8_11_jenkins.pages.registration_page import RegistrationPage

@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Kostromin")
@allure.story("Регистрация пользователя")
def test_Positive_Student_Registration_Form():

    registration_page = RegistrationPage()

    # WHEN
    with allure.step("Открываем форму"):
        registration_page.open()
        browser.execute_script('document.querySelector("#fixedban").remove()')
        browser.element('footer').execute_script('element.remove()')

    with allure.step("Заполняем Имя"):
        registration_page.type_first_name("Aleksei")

    with allure.step("Заполняем фамилию"):
        registration_page.type_last_name("Kostromin")

    with allure.step("Вводим Email"):
        registration_page.type_email("test@mail.ru")

    with allure.step("Выбираем мужской пол"):
        registration_page.set_gender("Male")

    with allure.step("Заполняем моб.телефон"):
        registration_page.type_mobile("8927761453")

    with allure.step("Заполняем дату рождения"):
        registration_page.fill_birthday("1994", "May", "20")

    with allure.step("Заполняем интересы"):
        registration_page.type_subjects("Computer Science")

    with allure.step("Заполняем хобби "):
        registration_page.set_hobbies("Music")

    with allure.step("Загружаем файл"):
        registration_page.file_upload("test.txt")

    with allure.step("Заполняем адресс"):
        registration_page.type_current_address("some text")

    with allure.step("Скролим страницу до нужного элемента"):
        registration_page.scroll_down()

    with allure.step("Заполяем город и штат"):
        registration_page.set_state_and_city("Haryana", "Panipat")

    with allure.step("Отправляем форму"):
        registration_page.submit()

    # THEN
    with allure.step("Сравниваем заголовок попапа"):
        registration_page.title_should_have_text("Thanks for submitting the form")

    with allure.step("Сравниваем введенные данные с полученным результатом"):
        registration_page.registered_user_data.should(have.texts(
            'Aleksei Kostromin',
            'test@mail.ru',
            'Male',
            '8927761453',
            '20 May,1994',
            'Computer Science',
            'Music',
            'test.txt',
            'some text',
            'Haryana Panipat'
        ))
