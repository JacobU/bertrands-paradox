import sys
import pygame
import bertrand

def update_chord(point1, point2, center, circleRadius):
    x1 = point1[0] * circleRadius + center[0] 
    y1 = point1[1] * circleRadius + center[1] 

    x2 = point2[0] * circleRadius + center[0]
    y2 = point2[1] * circleRadius + center[1]
    
    newPoint1 = (x1,y1)
    newPoint2 = (x2,y2)
    return (newPoint1, newPoint2)

def main():
    pygame.init()

    size = width, height = 500, 500
    center = (width/2, height/2)
    circleRadius = 200
    # Colours 
    white = 255, 255, 255
    black = 0, 0, 0
    red = 117, 32, 32
    
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Bertrand Method #1")

    clock = pygame.time.Clock()
    count = 0
    chordList = []
    while count < 1000:

        # This means it should update every 1/2 second
        clock.tick(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        screen.fill(white)

        pygame.draw.circle(screen, black, center, circleRadius, 1)

        # Create the next chord here
        chord = bertrand.get_chord_method_three()
        chord = update_chord(chord[0], chord[1], center, circleRadius)
        # Add it to the list of chords
        chordList.append(chord)
        # Draw all the chords
        for chords in chordList:
            pygame.draw.line(screen, red, chords[0], chords[1], 1)
        pygame.display.flip()

        count += 1

if __name__ == "__main__":
    main()

