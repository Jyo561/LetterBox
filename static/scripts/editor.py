from browser import document, ajax, html, window
from scripts.auth import Auth
class Editor:
    @staticmethod
    def upload_to_drive(event):
        """Uploads letter content to Google Drive."""
        content = window.Quill("#editor").root.innerText
        print(content)
        data = window.JSON.stringify({"content": content, "filename": "My Letter"})

        req = ajax.ajax()
        req.open("POST", f"/drive/upload", False)
        req.set_header("Content-Type", "application/json")
        req.send(data)

        if req.status == 200:
            window.alert("Uploaded successfully!")
        else:
            window.alert("Upload failed!")

    @staticmethod
    def render(name):
        """Renders the text editor and upload UI."""
        editor_div = html.DIV(Class="flex flex-col justify-center items-center mt-10 w-full",Id="container")
        img = html.IMG(Src=f"{Auth.user_info['picture']}", Id="image")
        user_info = html.P(["Welcome! ", img, f" {name}"], Class="user-wel")
        
        text_area = html.DIV(Id="editor",Class="")
        
        upload_btn = html.BUTTON("Upload to Drive", Id="upload-btn")
        upload_btn.bind("click", Editor.upload_to_drive)


        editor_div <= [user_info, text_area, upload_btn]
        return editor_div

