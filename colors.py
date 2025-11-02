import arcade, logging, random
from collections import namedtuple as nt

LOG_LEVEL = "INFO"

def start_logging():
    log = logging.getLogger(__name__)
    log.setLevel(LOG_LEVEL)

    handler = logging.StreamHandler()
    formatter = logging.Formatter("%(name)s:%(levelname)s: %(message)s")
    handler.setFormatter(formatter)
    log.addHandler(handler)

    return log


Game_Info = nt("Game_Info",["screen_width","screen_height","window_name"])
game_info = Game_Info(screen_width=1280, screen_height=720, window_name= "TITLE")

class GameView(arcade.Window):
    def __init__(self):
        super().__init__(*game_info)

        self.background_color = arcade.csscolor.BLACK
        self.hello_world = arcade.Text("Hello World!",game_info.screen_width/2,game_info.screen_height/2)

        #gets the names of all the Colors:
        self.csscolors_list = [
            key for key, value in arcade.csscolor.__dict__.items()
            if not key.startswith("__")
            ]
        
        self.colors_list = [
            key for key, value in arcade.color.__dict__.items()
            if not key.startswith("__")
            ]

    def setup(self):
        background = random.choice(self.csscolors_list)
        self.background_color = getattr(arcade.csscolor, background)

    def on_update(self,delta_time):
        pass

    def on_draw(self):
        self.clear()
        self.hello_world.draw()









if __name__ == "__main__":
    window = GameView()
    window.setup()
    arcade.run()

