import allure


class Test003:

    @allure.severity(allure.severity_level.BLOCKER)  # 最严重的
    def test_001(self):
        assert True

    @allure.severity(allure.severity_level.CRITICAL)  # 严重的
    def test_002(self):
        assert False

    @allure.severity(allure.severity_level.NORMAL)  # 一般的
    def test_003(self):
        assert True

    @allure.severity(allure.severity_level.MINOR)  # 普通的 轻微的
    def test_004(self):
        assert True

    @allure.severity(allure.severity_level.TRIVIAL)  # 忽略的
    def test_005(self):
        assert True
