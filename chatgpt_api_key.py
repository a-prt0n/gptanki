import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QInputDialog
from aqt import mw
import requests

class ChatGPTAddon(QWidget):
    def __init__(self):
        super().__init__()

    def prompt_for_api_key(self):
        api_key, ok = QInputDialog.getText(None, "Enter ChatGPT API Key", "API Key:")
        if ok:
            self.api_key = api_key
            return api_key
        else:
            self.api_key = None
            return None

    def submit(self):
        api_key = self.api_key
        if api_key:
            try:
                headers = {"Authorization": f"Bearer {api_key}"}
                data = {'model': 'text-davinci-002', 'prompt': 'Once upon a time'}
                response = requests.post(f'https://api.openai.com/v1/completions', json=data, headers=headers)
                if response.status_code == 200:
                    config = mw.addonManager.getConfig(__name__)
                    if not config:
                        # create default configuration settings
                        config = {"api_key": api_key}
                        mw.addonManager.writeConfig(__name__, config) # api_key saved in meta.json

                    api_key = config["api_key"]
                    QMessageBox.information(self, 'Success', 'API key saved successfully.')
                    self.close()
                else:
                    QMessageBox.critical(self, 'Error', 'Invalid API key.')
            except:
                QMessageBox.critical(self, 'Error', 'Error connecting to the ChatGPT API.')
        else:
            QMessageBox.critical(self, 'Error', 'Please enter your API key.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ChatGPTAddon()
    sys.exit(app.exec_())
