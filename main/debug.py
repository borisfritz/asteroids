import pygame
import os

class GameDebugger:
    def __init__(self, game):

        self.enabled = True  # Toggle debug system on/off

        self.game = game
        self.previous_keys = pygame.key.get_pressed()
    
    def debug_menu(self):
        print("============DEBUG MENU============")
        print("=== F1: Print Asteroids        ===")
        print("=== F2: Print Player Info      ===")
        print("=== F3: Print Performance Info ===")
        print("=== F4: Print Movement Keys    ===")
        print("=== F5: Clear Console          ===")
        print("==================================")

    def debug_asteroids(self):
        print(f"\n=== ASTEROID DEBUG ({len(self.game.asteroids)} total) ===")
        for i, asteroid in enumerate(self.game.asteroids):
            print(f"Asteroid {i+1}: pos=({asteroid.position.x:.1f}, {asteroid.position.y:.1f}) "
                  f"vel=({asteroid.velocity.x:.1f}, {asteroid.velocity.y:.1f}) radius={asteroid.radius}")
    
    def debug_player(self):
        print(f"\n=== PLAYER DEBUG ===")
        print(f"Position: ({self.game.player.position.x:.1f}, {self.game.player.position.y:.1f})")
        print(f"Rotation: {self.game.player.rotation:.1f} degrees")
    
    def debug_performance(self):
        print(f"\n=== PERFORMANCE DEBUG ===")
        print(f"FPS: {self.game.clock.get_fps():.1f}")
        print(f"Delta time: {self.game.delta_time:.4f}s")
        print(f"Active sprites: {len(self.game.updatable)}")

    def debug_movement_keys(self):
        print(f"\n=== MOVEMENT KEYS ===")
        current_keys = pygame.key.get_pressed()
        if current_keys[pygame.K_w] and not self.previous_keys[pygame.K_w]:
            print("W pressed!")
        if current_keys[pygame.K_s] and not self.previous_keys[pygame.K_s]:
            print("S pressed!")
        if current_keys[pygame.K_a] and not self.previous_keys[pygame.K_a]:
            print("A pressed!")
        if current_keys[pygame.K_d] and not self.previous_keys[pygame.K_d]:
            print("D pressed!")
        self.previous_keys = current_keys
    
    def clear_console(self):
        os.system('clear' if os.name == 'posix' else 'cls')
    
    def handle_debug_keys(self):
        if not self.enabled:
            return
            
        current_keys = pygame.key.get_pressed()
        
        # F1 - Print asteroids
        if current_keys[pygame.K_F1] and not self.previous_keys[pygame.K_F1]:
            self.debug_asteroids()
        
        # F2 - Print player info  
        if current_keys[pygame.K_F2] and not self.previous_keys[pygame.K_F2]:
            self.debug_player()
        
        # F3 - Print performance info
        if current_keys[pygame.K_F3] and not self.previous_keys[pygame.K_F3]:
            self.debug_performance()

        # F4 - Print Movement Keys while F4 is held
        if current_keys[pygame.K_F4] and not self.previous_keys[pygame.K_F5]:
            self.debug_movement_keys()
        
        # F5 - Clear console
        if current_keys[pygame.K_F5] and not self.previous_keys[pygame.K_F4]:
            self.clear_console()

        # F12 - Toggle debug system on/off
        if current_keys[pygame.K_F12] and not self.previous_keys[pygame.K_F12]:
            self.enabled = not self.enabled
            print(f"Debug system: {'ON' if self.enabled else 'OFF'}")
        
        self.previous_keys = current_keys
