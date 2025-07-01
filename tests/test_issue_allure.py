import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared.jquery_style import s
from pages.search_issue import IssueName


def test_selen_issue(open_browser):
    s('[data-target="qbsearch-input.inputButtonText"]').click()
    s('#query-builder-test').send_keys("homework_9_QA_GURU_NA").press_enter()
    s(by.partial_link_text('homework_9_QA_GURU_NA')).click()
    s('[data-content="Issues"').click()
    s(by.text("issue for hw9")).should(be.visible)


def test_dynamic_steps_issue(open_browser):
    with allure.step("Поиск репозитория"):
        s('[data-target="qbsearch-input.inputButtonText"]').click()
        s('#query-builder-test').send_keys("homework_9_QA_GURU_NA").press_enter()
    with allure.step("Открытие репозитория"):
        s(by.partial_link_text('homework_9_QA_GURU_NA')).click()
    with allure.step("Переход в Issues"):
        s('[data-content="Issues"').click()
    with allure.step("Проверка присутствия Issue с названием {value}"):
        s(by.text("issue for hw9")).should(be.visible)


def test_decorator_steps_issue(open_browser):
    issue_name = IssueName()

    issue_name.search_repository('homework_9_QA_GURU_NA')
    issue_name.open_repository("homework_9_QA_GURU_NA")
    issue_name.open_issue()
    issue_name.should_issue_name("issue for hw9")


@allure.tag("test")
@allure.severity(Severity.MINOR)
@allure.label('owner', 'anaumenko')
@allure.feature('Issues_name')
@allure.story('Проверка присутствия Issue')
@allure.link('https://github.com', name='Testing')
def test_allure_labels():
    pass