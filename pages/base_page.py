from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    # função de inicialização da classe
    def __init__(self, driver):
        self.driver = driver

    # Função para abrir uma pagina

    def _visitar(self, url):
        self.driver.get(url)

    # Função generica de localização dde elemento

    def _procurar(self, locator):
        return self.driver.find_element(locator, ['by'], locator['value'])

    # Função para clicar em um elemento
    def _clicar(self, locator):
        self._procurar().click()

    # Função para digitar em um elemento

    def _digitar(self, locator, input_text):
        self._procurar(locator).send_Keys(input_text)

    def _ler(self, locator):
        self._procurar().text

        # função para verificar se o elemento está visivel
        def _esta_visivel(self, locator, timeout=0):
            # se precisa ter paciência
            if timeout > 0:
                try:
                    wait = WebDriverWait(self.driver, timeout)
                    wait.until(
                        expected_conditions.visibility_of_element_located(
                            (locator['by'], locator['value'])
                        )
                    )
                # Esgotou o tempo de espera
                except TimeoutException:
                    return False  # não encontrou o elemento
                return True  # encontrou o elemento
            # se não precisa esperar
            else:
                try:
                    return self._procurar(locator).is_displayed()
                # Não encontrou o elementot
                except NoSuchElementException:
                    return False  # não encontrou o elemento
                # return True    # encontrou o elemento
