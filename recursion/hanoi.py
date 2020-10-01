def moveTower(height, fromPole, withPole, toPole):
    if height >= 1:
        moveTower(height-1, fromPole, toPole, withPole)
        moveDisk(height, fromPole, toPole)
        moveTower(height-1, withPole, fromPole, toPole)

def moveDisk(height, fromPole, toPole):
    print(f"Moving disk[{height}] from {fromPole} to {toPole}")

moveTower(3, '#1', "#2", '#3')