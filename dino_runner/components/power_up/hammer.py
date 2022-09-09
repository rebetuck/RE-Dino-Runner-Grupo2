from  dino_runner.components.power_up.power_up import PowerUp

from dino_runner.utils.constants import HAMMER, HAMMER_TYPE

class Hammer(PowerUp):
    def __init__(self):
        self.image = HAMMER
        self.type = HAMMER_TYPE
        super(Hammer,self).__init__(self.image, self.type)