import pygame
import random

# Inisialisasi game
pygame.init()

# Warna 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Ukuran Layar
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Catch the Falling Object")

# Clock untuk mengatur frame rate
clock = pygame.time.Clock()

# Pengaturan pemain
player_width = 70
player_height = 10
player_x = SCREEN_WIDTH // 2 - player_width // 2
player_y = SCREEN_HEIGHT - player_height - 10
player_speed = 10

# Objek yang jatuh
falling_object_width = 20
falling_object_height = 20
falling_object_x = random.randint(0, SCREEN_WIDTH - falling_object_width)
falling_object_y = -falling_object_height
falling_object_speed = 5

# Fungsi untuk menggambar pemain
def draw_player(x, y):
    pygame.draw.rect(screen, RED, [x, y, player_width, player_height])

# Fungsi untuk menggambar objek yang jatuh
def draw_falling_object(x, y):
    pygame.draw.rect(screen, BLACK, [x, y, falling_object_width, falling_object_height])

# Fungsi utama untuk game
def game_loop():
    global player_x, falling_object_x, falling_object_y

    # Flag game berakhir
    game_over = False
    score = 0

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        # Kontrol pemain
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_width:
            player_x += player_speed

        # Update posisi objek yang jatuh
        falling_object_y += falling_object_speed

        # Jika objek jatuh melewati batas bawah, atur ulang posisinya
        if falling_object_y > SCREEN_HEIGHT:
            falling_object_y = -falling_object_height
            falling_object_x = random.randint(0, SCREEN_WIDTH - falling_object_width)
            score += 1

        # Cek apakah pemain menangkap objek yang jatuh
        if (falling_object_x + falling_object_width > player_x and
            falling_object_x < player_x + player_width and
            falling_object_y + falling_object_height > player_y):
            score += 5
            falling_object_y = -falling_object_height
            falling_object_x = random.randint(0, SCREEN_WIDTH - falling_object_width)

        # Gambar latar belakang, pemain, dan objek yang jatuh
        screen.fill(WHITE)
        draw_player(player_x, player_y)
        draw_falling_object(falling_object_x, falling_object_y)

        # Tampilan skor
        font = pygame.font.SysFont(None, 35)
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))  # Fix: Use parentheses instead of curly braces

        pygame.display.update()

        # Atur frame rate
        clock.tick(60)

    # Quit pygame properly when the game loop ends
    pygame.quit()

# Jalankan permainan
game_loop()
