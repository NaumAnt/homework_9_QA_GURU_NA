import allure
from selene.support.shared.jquery_style import s
from selene.support.conditions import be
from selene.support import by


class IssueName:
    @allure.step("Поиск репозитория {value}")
    def search_repository(self, value):
        s('[data-target="qbsearch-input.inputButtonText"]').click()
        s('#query-builder-test').send_keys(value).press_enter()

    @allure.step("Открытие репозитория {value}")
    def open_repository(self, value):
        s(by.partial_link_text(value)).click()

    @allure.step("Переход в Issues")
    def open_issue(self):
        s('[data-content="Issues"').click()

    @allure.step("Проверка присутствия Issue с названием {value}")
    def should_issue_name(self, value):
        s(by.text(value)).should(be.visible)