from browser import document, console, window, html
from scripts.auth import Auth
from scripts.editor import Editor
from scripts.menu import Sidebar 
#import cookielib


def render_app():
    """Renders the app components dynamically."""
    app_div = document["app"]
    app_div.clear()
    nav = html.DIV(Class="flex justify-between mt-4 ml-4 mr-4 p-4 pl-8 pr-8 navbar navbar-expand-lg navbar-transparent navbar-light shadow-soft navbar-theme-primary")
    ham = html.DIV(html.SPAN(Class="mdi-light--hamburger"), Class="ham")
    
    title = html.SPAN([html.B("Letter", Style="color: #EE7429; font-size: 20px;"), html.B("Box", Style="color: #221F21; font-size: 20px;"), html.IMG(Src="./assets/logo2.png", Id="logomain", Style="")], Class="flex p-2 ml-4")
    nav <= ham
    nav <= title
    
    if Auth.check_login():
        #print(Auth.user_info) 
        logout_btn = html.BUTTON(["Logout ", html.IMG(Src="./assets/logout.png", Id="logo", Style="margin-top: -5px")], Id="logout-btn", Class="flex login")
        logout_btn.bind("click", Auth.logout_click)
        
        nav <= logout_btn
        app_div <= nav
        name = Auth.user_info["name"]
        app_div <= Editor.render(name)
        quill = window.Quill.new("#editor", {"theme": "snow"})
    else:
        #print("Hello")
        nav <= Auth.render()
        app_div <= nav
    
    app_div <= Sidebar.render()
    ham.bind("click", Sidebar.open_sidebar)
    document["close"].bind("click",Sidebar.close_sidebar)
# Run the app
render_app()
