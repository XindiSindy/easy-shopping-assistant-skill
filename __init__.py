from mycroft import MycroftSkill, intent_file_handler


class EasyShoppingAssistant(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('assistant.shopping.easy.intent')
    def handle_assistant_shopping_easy(self, message):
        self.speak_dialog('assistant.shopping.easy')


def create_skill():
    return EasyShoppingAssistant()

