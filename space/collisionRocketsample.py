import os,sys,math
import pygame as pg #lazy but responsible (avoid namespace flooding)
ticker = 0

class Rocket(pg.sprite.Sprite):
    def __init__(self,surface):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('images/t.png').convert_alpha()
        self.image = pg.transform.scale(self.image, (54, 50))
        self.rect = self.image.get_rect()
        self.mry = 0;
        self.mrx = 0
        self.id = 1
        self.speedx = 32
        self.speedy = 32
        self.xtr = 120
        self.ytr = 120
        self.acce  = 0
        self.ticker = 0;
        self.rticker = 0
        self.backimage = 0;

    def update(self,surface):
        #back = pg.image.load("images/space.png")
        self.mrx += 1
        self.mry += 1
        self.mrx  = 320 + math.sin(self.ticker / self.speedx) * self.xtr
        self.mry  = 400 + math.cos(self.ticker / self.speedy) * self.ytr
        self.ticker += 1
        self.rect.center = (self.mry,self.mrx)
        #self.image = rot_center(self.image,6)
        self.image.set_alpha(240);
        #surface.blit(self.backimage, [0, 0])
        #surface.blit(self.image,self.rect)
        surface.blit(self.image,self.rect)
        
def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pg.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image

def main(Surface,rockets):
    
    game_event_loop()
    #Surface.fill(0)
    rocket = rockets[0]
    Surface.blit(rocket.backimage, [0, 0])
    for rocket in rockets:
        rocket.update(Surface)
        

            
    for rocket in rockets:
        roctic = 0
        for brocket in rockets:
            if rocket != brocket:
                if pg.Rect.colliderect(rocket.rect,brocket.rect):
                    if brocket.speedx > 200:
                        rocket.speedx += 0
                        
                    #rocket.speedx += roctic
                   # rocket.xtr *= -1
                    #rocket.xtr = abs(rocket.xtr)
                    #rocket.ytr *= -1
                    #rocket.ytr = abs(rocket.ytr)
                    if rocket.speedx == 0:
                        rocket.speedx = 1
                    if roctic % 2 == 0:
                        #rocket.ticker += 1
                        #rocket.speedy *= -1
                        rocket.acce = 10
                        #rocket.speedy = math.sin(rocket.speedy / 64) * 100
                        
                        if rocket.speedy == 0:
                            rocket.speedy = 1
                    if roctic % 2 == 1:
                        #rocket.ticker += 1
                        #rocket.speedy *= -1
                        rocket.acce = -10
                        #rocket.speedy = math.sin(rocket.speedy / 64) * 100
                        
                        if rocket.speedy == 0:
                            rocket.speedy = 1
                    roctic += 1
                #roctic %= 12
                
                    
        


def game_event_loop():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit(); sys.exit()

if __name__ == "__main__":
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pg.init()
    Screen = pg.display.set_mode((1000,600))
    MyClock = pg.time.Clock()
    backimage = pg.image.load("images/avaruus.png")
    Screen.blit(backimage, [0, 0])
    rockets = []
    for r in range(10,80,2):
        rocket = Rocket(Screen)
        rocket.id = r
        rocket.backimage = backimage
        rocket.xtr += r * 3
        rocket.ytr += r * 3
        rocket.speedx = 12 * r
        rocket.speedy = 24 * r
        rockets.append(rocket)
    
    while 1:       
        main(Screen,rockets)
        pg.display.update()
        MyClock.tick(120)
