from web.po_test.web_page.home_page import HomePage


class TestWeixin:
    def setup(self):
        self.home = HomePage()

    # def teardown(self):
    #     pass

    def test_home_add(self):
        username = "a10"
        account = "13600000010"
        phone = "13600000010"

        member = self.home.goto_memberedit()
        member.member_edit(username, account, phone)

        assert phone in member.get_member()
