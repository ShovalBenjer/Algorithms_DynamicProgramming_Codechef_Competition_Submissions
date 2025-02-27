#Your task is to determine the minimum number of times you need to switch between the two guns to shoot all N targets in the given order.

T = int(input())  # Number of test cases

for _ in range(T):
    N, D = map(int, input().split())  # Number of targets and close-range gun range
    targets = list(map(int, input().split()))  # Target distances

    switches = 0  # Initialize gun switch count
    current_gun = "close"  # Initially holding the close-range gun

    for distance in targets:
        if current_gun == "close" and distance <= D:
            # Can shoot with current gun
            continue
        elif current_gun == "long" and distance > D:
            # Can shoot with current gun
            continue
        else:
            # Need to switch guns
            switches += 1
            current_gun = "long" if current_gun == "close" else "close"

    print(switches)  # Output the minimum number of gun switches
