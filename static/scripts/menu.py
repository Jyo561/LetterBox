from browser import document, ajax, html, window

class Sidebar:
    data = None
    
    @staticmethod
    def on_complete(req):
        if req.status == 200:
            data = window.JSON.parse(req.text)
            #document["doc_list"].clear()
            #for doc in data["docs"]:
            #    li = html.LI(doc["name"], Class="doc-item")
            #    li.bind("click", lambda e, doc_id=doc["id"]: fetch_content(doc_id))
            #    document["doc_list"] <= li
    
    @staticmethod
    def on_complete_content(req):
        if req.status == 200:
            data2 = window.JSON.parse(req.text)
            document["doc_content"].text = data["content"]

    @staticmethod
    def fetch_docs():
        """Fetches list of Google Docs and updates the UI."""
        req = ajax.ajax()
        req.open("GET", f"/drive/docs", True)
        req.bind("complete", on_complete)
        req.send()

    @staticmethod
    def fetch_content(file_id):
        """Fetches document content and displays it."""
        req = ajax.ajax()
        req.open("GET", f"/drive/docs/{file_id}", True)
        req.bind("complete", on_complete_content)
        req.send()
    
    @staticmethod
    def open_sidebar(event):
        document["sidebar"].style["left"] = "0px"
    
    @staticmethod
    def close_sidebar(event):
        document["sidebar"].style["left"] = "-250px"

    @staticmethod
    def render():
        """Renders login UI."""
        google_logo = html.IMG(Src="../assets/google.png", Id="logo", Style="border-radius: 30px")
        sidebar = html.DIV(["Sidebar Content", html.DIV(html.SPAN(Class="mdi-light--arrow-right-circle", Style="margin-top: -5px; margin-left: -5px", Id="close"), Class="ham", Style="height: 40px !important; width: 40px !important;")], Id="sidebar", Class="flex justify-between") 
        return sidebar

