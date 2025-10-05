import deskapp
import random
import sys

class_id_hworld = random.random()
class Hworld(deskapp.Module):
    name = "Hworld"
    def __init__(self, app):
        # deskapp.Module expects (app, class_id)
        super().__init__(app, class_id_hworld)
        self.class_id = class_id_hworld
    def page(self, panel):
        panel.win.addstr(1,1,"Hworld.")
        return False

def main():
    app = deskapp.App([Hworld])
    app.start()

if __name__ == "__main__":
    sys.exit(main())
