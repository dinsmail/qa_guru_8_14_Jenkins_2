from demoga_tests.pages.registration_page import RegistrationPage


def test_forms_demoga_praktika():
    registration_page = RegistrationPage()

    registration_page.open()
    registration_page.fill_first_name("Dinara")
    registration_page.fill_last_name("Kokhanovskaya")
    registration_page.fill_email("dinkokh@example.com")
    registration_page.fill_gender()
    registration_page.fill_number('9090909090')
    registration_page.fill_date_of_birth(1984, "July", 27)
    registration_page.choose_subject('Computer Science')
    registration_page.choose_hobbies()
    registration_page.upload_picture('image.png')
    registration_page.fill_current_address('460000,Russia, Orenburg, Solynoy')
    registration_page.choose_state('Uttar Pradesh')
    registration_page.choose_city('Agra')
    registration_page.submit_form()

    registration_page.should_registered_user_with(
        'Dinara Kokhanovskaya',
        'dinkokh@example.com',
        'Female',
        '9090909090',
        '27 July,1984',
        'Computer Science',
        'Music',
        'image.png',
        '460000,Russia, Orenburg, Solynoy',
        'Uttar Pradesh Agra'
    )
