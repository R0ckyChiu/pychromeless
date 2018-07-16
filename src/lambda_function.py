import time

from webdriver_wrapper import WebDriverWrapper


def lambda_handler(*args, **kwargs):
    driver = WebDriverWrapper()

    driver.get_url('https://www.backerkit.com/admins/sign_in')

    driver.set_input_value_byName('admin[email]', 'YOUR_EMAIL')
    driver.set_input_value_byName('admin[password]', 'YOUR_PASSWORD')

    driver.click_byName('commit')
    
    driver.get_url('URL_OF_EXPORT_PAGE_OF_DESIRED_SEGMENT')
    
    driver.set_input_value('XPATH_OF_FILE', '\n')
    
    driver.close()
