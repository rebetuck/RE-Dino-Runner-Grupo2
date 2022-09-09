from asyncio import shield
from dino_runner.components.power_up.power_up import PowerUp
from dino_runner.utils.constants import SHIELD, DEFAULT_TYPE

class Shield(PowerUp):
    def __init__(self):
        self.image = SHIELD
        self.type = DEFAULT_TYPE
        super(shield,self).__init__(self.image, self.type)
