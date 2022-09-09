from dino_runner.components.power_up.power_up import PowerUp
from dino_runner.utils.constants import CAKE, SHIELD_TYPE

class Cake(PowerUp):
    def __init__(self):
        self.image = CAKE
        self.type = SHIELD_TYPE
        super(Cake,self).__init__(self.image, self.type)