from mycroft import MycroftSkill, intent_file_handler


class FortniteDrops(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('drops.fortnite.intent')
    def handle_drops_fortnite(self, message):
        self.speak_dialog('drops.fortnite')


def create_skill():
    return FortniteDrops()

