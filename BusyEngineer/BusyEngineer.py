import pygame,sys
pygame.init()
myfont,screen,score,clock = pygame.font.SysFont("monospace", 15),pygame.display.set_mode([640,480]), 0,pygame.time.Clock()
e,h,t,cc,tt = pygame.image.load("eng.jpg"), pygame.image.load("h.jpg"),pygame.image.load("t.jpg"),pygame.image.load("cc.jpg"),pygame.image.load("tt.jpg")
t_p,h_p,e_p,cc_p,tt_p =  t.get_rect(center = (380,0)),h.get_rect(center = (220,0)),e.get_rect(center = (250,430)),cc.get_rect(center=(80,0)),tt.get_rect(center=(550,50))
while 1:
        label = myfont.render('SCORE : '+format(score), 1, (255,0,0))
        screen.fill(0)
        screen.blit(e,e_p)#engineer
        screen.blit(h,h_p)#hack night 
        screen.blit(t,t_p)#trivia
        screen.blit(tt,tt_p)#tech talk
        screen.blit(cc,cc_p)#coding competition
        screen.blit(label, (525, 30))
        for event in pygame.event.get():
                if event.type==pygame.QUIT: pygame.quit()
                if pygame.key.get_pressed()[pygame.K_LEFT]: e_p = e_p.move(-50,0)
                if pygame.key.get_pressed()[pygame.K_RIGHT]: e_p = e_p.move(50,0)        
        h_p = h_p.move(0,3)
        t_p = t_p.move(0,2)
        tt_p = tt_p.move(0,5)
        cc_p = cc_p.move(0,1)
        if(h_p.bottom > 480): h_p = h_p.move(0,-480)
        if(t_p.bottom > 480): t_p = t_p.move(0,-480)
        if(tt_p.bottom > 480): tt_p = tt_p.move(0,-400)
        if(cc_p.bottom > 480): cc_p = cc_p.move(0,-480)
        if(h_p.colliderect(e_p)): h_p,score = h_p.move(0,-430),score + 40
        if(t_p.colliderect(e_p)): t_p,score = t_p.move(0,-430),score + 50
        if(tt_p.colliderect(e_p)): tt_p,score = tt_p.move(0,-350),score + 30
        if(cc_p.colliderect(e_p)): cc_p,score = cc_p.move(0,-430),score + 70
        pygame.display.flip()
        clock.tick(20)
        
                        
	
                
