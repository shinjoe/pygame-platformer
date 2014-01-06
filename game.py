import pygame
import Tile_Map

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

FPS = 30
size = [400, 400]
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("platformer")

tile_map = Tile_Map.TileMap()

done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(BLACK)
    for row in range(tile_map.num_rows):
        for col in range(tile_map.num_cols):
            cur_tile = tile_map.tiles[row][col]
            if cur_tile == 0:
                cur_color = BLACK
            elif cur_tile == 1:
                cur_color = WHITE
            pygame.draw.rect(screen, cur_color, [tile_map.tile_width * col,
                                                 tile_map.tile_height * row,
                                                 tile_map.tile_width,
                                                 tile_map.tile_height])

    pygame.display.flip()
    clock.tick(FPS)


pygame.quit()
