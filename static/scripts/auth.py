from browser import document, ajax, window, html


class Auth:
    user_info = None

    @staticmethod
    def check_login():
        """Check if the user is logged in."""
        req = ajax.ajax()
        req.open("GET", f"/auth/user", False)  # Sync request
        req.send()
        if req.status == 200:
            Auth.user_info = dict(window.JSON.parse(req.text))
            return True
        return False

    @staticmethod
    def login_click(event):
        """Redirects to Google OAuth login."""
        window.location.href = f"/auth/login"

    @staticmethod
    def logout_click(event):
        """Logs out user and refreshes UI."""
        req = ajax.ajax()
        req.open("GET", f"/auth/logout", False)
        req.send()
        window.location.reload()

    @staticmethod
    def render():
        """Renders login UI."""
        google_logo = html.IMG(Src="../assets/google.png", Id="logo", Style="border-radius: 30px")
        login_btn = html.BUTTON(["Login ", google_logo], Id="login-btn", Class="flex login")
        login_btn.bind("click", Auth.login_click)
        
        return login_btn

