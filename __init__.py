from mycroft import MycroftSkill, intent_file_handler, intent_handler
from adapt.intent import IntentBuilder


class EasyShoppingAssistant(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('assistant.shopping.easy.intent')
    def handle_assistant_shopping_easy(self, message):
        self.speak_dialog('assistant.shopping.easy')
        
    #padatious intent
    @intent_handler('is.there.any.goods.intent')
    def handle_is_there_any_goods(self, message):
        category_label = message.data.get('category')
        str = 'yes, I find ' + category_label + ' in front of tou'
        self.speak(str)    
    	
    	
    	

    @intent_handler(IntentBuilder('AskItemBrand').require('Brand'))
    def handle_brand_intent(self, message):
        """ This is an Adapt intent handler, it is triggered by a keyword."""
        self.speak_dialog("brand")
        
        
    @intent_handler(IntentBuilder('messi').require('MessiKeyword'))
    def handle_messi_intent(self, message):
        """ This is an Adapt intent handler, it is triggered by a keyword."""
        self.speak_dialog("messi")
        
    
    @intent_handler(IntentBuilder('AskItemCategory').require('Category').build())
    def handle_ask_item_category(self, message):
    	self.speak('I am talking about the category of the item')

    @intent_handler(IntentBuilder('AskItemColor').require('Color').build())
    def handle_ask_item_color(self, message):
    	self.speak('I am talking about the color of the item')

    @intent_handler(IntentBuilder('AskItemKw').require('Kw').build())
    def handle_ask_item_keywords(self, message):
        self.speak('I am talking about the keywords of the item')

    @intent_handler(IntentBuilder('AskItemInfo').require('Info').build())
    def handle_ask_item_complete_info(self, message):
        self.speak('I am speaking the complete information of the item')

    @intent_handler(IntentBuilder('FinishOneItem').require('Finish').build())
    def handle_finish_current_item(self, message):
        self.speak('Got you request. Let\'s continue shopping!')
    
        


def create_skill():
    return EasyShoppingAssistant()

