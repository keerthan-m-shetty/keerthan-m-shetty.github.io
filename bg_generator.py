import matplotlib.pyplot as plt
import numpy as np
import os

output_dir = os.path.join('media', 'bg_spirograph')
os.makedirs(output_dir, exist_ok=True)

print(f"Generating frames in: {output_dir}...")

def make_circular_globe(seed: int, line_count=2000):
    rng = np.random.default_rng(seed)
    
    x_lines, y_lines, alphas = [], [], []

    for i in range(line_count):
        # FIX 1: Remove the hard minimum gap. Let lines generate naturally down to the center.
        base_radius = 0.85 * (rng.random() ** 0.8)
        
        ratio = base_radius / 0.85
        alpha_val = 0.04 + (0.1 * ratio)

        angles = np.linspace(0, 2 * np.pi, 500)
        waves = rng.integers(3, 15)
        phase = rng.random() * 2 * np.pi
        
        # By hardcoding a minimum wobble of `0.03`, lines near the center will sweep 
        # *across* the origin rather than shrinking into a tiny dense dot. 
        # This completely fills the hole with a soft, uniform texture.
        wobble = (0.03 + base_radius * 0.04) * np.sin(waves * angles + phase)
        jitter = rng.normal(scale=0.003, size=500)
        
        r_path = base_radius + wobble + jitter
        
        # Close the loop
        r_path[-1] = r_path[0] 
        
        x_lines.append(r_path * np.cos(angles))
        y_lines.append(r_path * np.sin(angles))
        alphas.append(alpha_val)
        
    return x_lines, y_lines, alphas

for i in range(30, 40):
    x_lines, y_lines, alphas = make_circular_globe(i, line_count=2000)

    plt.figure(figsize=(8, 8))
    
    for x_line, y_line, alpha_val in zip(x_lines, y_lines, alphas):
        plt.plot(x_line, y_line, color="#6CE6E8", alpha=alpha_val, linewidth=0.5)
        
    plt.axis('off')
    plt.xlim(-1.1, 1.1)
    plt.ylim(-1.1, 1.1)

    filepath = os.path.join(output_dir, f'random_{i}.png')
    plt.savefig(filepath, transparent=True, dpi=150, bbox_inches='tight', pad_inches=0)
    plt.close()

    print(f"Saved frame {i-29}/10: {filepath}")

print("Done! Check the media/bg_spirograph folder.")