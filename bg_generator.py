import matplotlib.pyplot as plt
import numpy as np
import os

output_dir = os.path.join('media', 'bg_spirograph')
os.makedirs(output_dir, exist_ok=True)

print(f"Generating frames in: {output_dir}...")


def make_scribble_circle(seed: int, line_count=120, points_per_line=360):
    rng = np.random.default_rng(seed)
    angles = np.linspace(0, 2 * np.pi, points_per_line)

    x_lines = []
    y_lines = []

    for _ in range(line_count):
        base_radius = np.sqrt(rng.random()) * 0.80
        base_angle = rng.random() * 2 * np.pi
        center_x = base_radius * np.cos(base_angle)
        center_y = base_radius * np.sin(base_angle)

        jitter = rng.normal(scale=0.04, size=points_per_line)
        wobble = 0.12 + 0.08 * np.sin(12 * angles + rng.random() * 3.0)
        radius = np.clip(0.08 + wobble + jitter, 0, 0.22)

        offset = rng.random() * 2 * np.pi
        x_line = center_x + radius * np.cos(angles + offset)
        y_line = center_y + radius * np.sin(angles + offset)

        x_lines.append(x_line)
        y_lines.append(y_line)

    return x_lines, y_lines


for i in range(30, 40):
    x_lines, y_lines = make_scribble_circle(i, line_count=2000, points_per_line=320)

    plt.figure(figsize=(8, 8))
    for x_line, y_line in zip(x_lines, y_lines):
        plt.plot(x_line, y_line, color="#144473", alpha=0.06, linewidth=0.35)
    plt.axis('off')
    plt.xlim(-1.1, 1.1)
    plt.ylim(-1.1, 1.1)

    filepath = os.path.join(output_dir, f'random_{i}.png')
    plt.savefig(filepath, transparent=True, dpi=150, bbox_inches='tight', pad_inches=0)
    plt.close()

    print(f"Saved frame {i-29}/10: {filepath}")

print("Done! Check the media/bg_spirograph folder.")