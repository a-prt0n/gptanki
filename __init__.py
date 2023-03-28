from aqt import QAction, QMenu
from aqt import mw
from aqt.utils import qconnect
from .chatgpt_api_key import ChatGPTAddon

def generate_apikey_prompt():
    addon = ChatGPTAddon()
    addon.prompt_for_api_key()
    addon.submit()

# create menu item
action = QAction("ChatGPT API Key", mw)
qconnect(action.triggered, generate_apikey_prompt)

# add menu item to Tools menu
menu = QMenu(mw)
menu.setTitle("Tools")
menu.addAction(action)
mw.form.menuTools.addAction(menu.menuAction())