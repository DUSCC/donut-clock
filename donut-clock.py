import math
import time
import argparse
import shutil
from colorama import Fore, init

init(autoreset=True)

A = 0
B = 0

# Parse command line arguments
parser = argparse.ArgumentParser(description='Rotating 3D donut animation.')
parser.add_argument('--duration', type=int, default=30, help='Duration of the animation in seconds.')
args = parser.parse_args()

duration = args.duration  # Duration in seconds for the effect
half_duration = duration / 2
start_time = time.time()

while True:
    columns, rows = shutil.get_terminal_size()
    rows -= 2  # Adjust for the newline character

    z = [0] * columns * rows
    b = [' '] * columns * rows
    elapsed_time = time.time() - start_time

    if elapsed_time > duration:
        print()
        print("Competition Over!")
        print()
        break

    # Calculate remaining time and format it as HH:MM:SS
    remaining_time = duration - elapsed_time
    hours, rem = divmod(remaining_time, 3600)
    minutes, seconds = divmod(rem, 60)
    time_str = "{:0>2}:{:0>2}:{:05.2f}".format(int(hours), int(minutes), seconds)

    for j in range(0, 628, 7):
        for i in range(0, 628, 2):
            c = math.sin(i)
            d = math.cos(j)
            e = math.sin(A)
            f = math.sin(j)
            g = math.cos(A)
            h = d + 2
            D = 1 / (c * h * e + f * g + 5)
            l = math.cos(i)
            m = math.cos(B)
            n = math.sin(B)
            t = c * h * g - f * e
            x = int((columns / 2) + (columns / 2 - 2) * D * (l * h * m - t * n))  # adjust x
            y = int((rows / 2) + (rows / 2 - 4) * D * (l * h * n + t * m))  # adjust y
            o = int(x + columns * y)
            N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))
            
            color_ratio = (y - rows / 4) / (rows / 2)  # Calculate color ratio based on y-coordinate
            if elapsed_time < half_duration:
                color = Fore.YELLOW if color_ratio < elapsed_time / half_duration else Fore.GREEN
            else:
                color = Fore.RED if color_ratio < (elapsed_time - half_duration) / half_duration else Fore.YELLOW

            if 0 <= y < rows and 0 <= x < columns and D > z[o]:
                z[o] = D
                b[o] = color + '.,-~:;=!*#$@'[N if N > 0 else 0]

    print('\033[0;0H' + ''.join(b) + f'\nTime Remaining: {time_str}')
    time.sleep(0.01)
    A += 0.04
    B += 0.02
