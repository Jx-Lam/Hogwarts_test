from web.po_test.web_page.home_page import HomePage


class TestWeixin:
    def setup(self):
        self.home = HomePage()

    # def teardown(self):
    #     pass

    def test_home_add(self):
        username = "a8"
        account = "13600000008"
        phone = "13600000008"

        member = self.home.goto_memberedit()
        member.member_edit(username, account, phone)

        assert username in member.get_member()
