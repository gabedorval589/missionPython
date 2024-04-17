import sys

import pygame


def run_game():
  pygame.init()
  screen = pygame.display.set_mode((1200, 800))
  pygame.display.set_caption("testing 123")
  bg_color = (79, 210, 95)
  screen.fill(bg_color)

  room_map = [[1,1,1,1,1],
            [1,0,0,0,1],
            [1,0,1,0,1],
            [1,0,0,0,1],
            [1,0,0,0,1],
            [1,0,0,0,1],
            [1,1,1,1,1]
           ]

  top_left_x = 100
  top_left_y = 150

  DEMO_OBJECTS = ['images/floor.png', 'images/pillar.png'] 

  room_height = 7
  room_width  = 5

  def draw():
    for y in range (room_height):
      for x in range (room_width):
        image_to_draw = DEMO_OBJECTS[room_map[y][x]]
        my_surf = pygame.image.load(image_to_draw).convert()
        screen.blit(my_surf,
                    (top_left_x + (x * 30), 
                     top_left_y + (y * 30) - 
                     my_surf.get_height()))

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
    draw()
    pygame.display.flip()

run_game()
