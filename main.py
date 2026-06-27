from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import requests

class OMPApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.label = Label(text='آماده برای ارسال درخواست...')
        self.btn = Button(text='ارسال درخواست API')
        self.btn.bind(on_press=self.send_request)
        
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.btn)
        return self.layout

    def send_request(self, instance):
        try:
            # اینجا همان منطقی که قبلاً تست کردی را قرار بده
            url = "https://my.ompfinex.com/api/v1/some-endpoint"
            headers = {"X-Sid": "2051"} # بقیه هدرها
            response = requests.get(url, headers=headers, timeout=5)
            self.label.text = f"Status: {response.status_code}"
        except Exception as e:
            self.label.text = f"Error: {str(e)}"

if __name__ == '__main__':
    OMPApp().run()