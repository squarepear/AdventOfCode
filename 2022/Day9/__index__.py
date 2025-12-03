# Initialize grid with starting position of head and tail
grid = [['.' for  in range(5)] for  in range(5)]
head_pos = (2, 2)
tail_pos = (2, 2)
grid[head_pos[0]][head_pos[1]] = 'H'
grid[tail_pos[0]][tail_pos[1]] = 'T'

# Read in list of motions
motions = []
while True:
    try:
        line = input()
        motions.append(line)
    except EOFError:
        break

# Iterate over list of motions
for motion in motions:
    # Parse the direction and number of steps from the input
    direction = motion[0]
    num_steps = int(motion[1:])

    # Update the position of the head based on the direction
    if direction == 'U':
        head_pos = (head_pos[0] - num_steps, head_pos[1])
    elif direction == 'D':
        head_pos = (head_pos[0] + num_steps, head_pos[1])
    elif direction == 'L':
        head_pos = (head_pos[0], head_pos[1] - num_steps)
    elif direction == 'R':
        head_pos = (head_pos[0], head_pos[1] + num_steps)

    # Update the position of the tail based on the new position of the head
    if head_pos[0] == tail_pos[0] + 2 and head_pos[1] == tail_pos[1]:
        # Head is two steps directly above the tail
        tail_pos = (tail_pos[0] + 1, tail_pos[1])
    elif head_pos[0] == tail_pos[0] - 2 and head_pos[1] == tail_pos[1]:
        # Head is two steps directly below the tail
        tail_pos = (tail_pos[0] - 1, tail_pos[1])
    elif head_pos[0] == tail_pos[0] and head_pos[1] == tail_pos[1] + 2:
        # Head is two steps directly to the right of the tail
        tail_pos = (tail_pos[0], tail_pos[1] + 1)
    elif head_pos[0] == tail_pos[0] and head_pos[1] == tail_pos[1] - 2:
        # Head is two steps directly to the left of the tail
        tail_pos = (tail_pos[0], tail_pos[1] - 1)
    elif abs(head_pos[0] - tail_pos[0]) == 1 and abs(head_pos[1] - tail_pos[1]) == 1:
        # Head and tail are touching, but not in the same row or column
        if head_pos[0] < tail_pos[0] and head_pos[1] < tail_pos[1]:
            # Head is to the top left of the tail
            tail_pos = (tail_pos[0] - 1, tail_pos[1] - 1)
        elif head_pos[0] < tail_pos[0] and head_pos[
