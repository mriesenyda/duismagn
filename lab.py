angle = 90
direction = None

switch (angle):
    case 0:
        direction = "Right"
        break
    case 90:
        direction = "Up"
        # fall through
    case 180:
        direction = "Left"
        break
    case 270:
        direction = "Down"
        break
    default:
        direction = "Unknown"

print(direction)  # Output: Up
