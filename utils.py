def lerp(current, target, speed):
    difference = target - current
    step = difference * speed
    current = current + step
    return current
