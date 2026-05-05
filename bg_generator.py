import matplotlib.pyplot as plt
import numpy as np
import os

output_dir = os.path.join('media', 'bg_spirograph')
os.makedirs(output_dir, exist_ok=True)

print(f"Generating frames in: {output_dir}...")

# Loop to create 10 frames
for i in range(30,40,1):
    # 100 * pi gives us 50 full rotations to build a dense, complex mesh
    t = np.linspace(0, 100 * np.pi, 10000) 
    
    # 'k' controls the number of "rays" or "petals". 
    # Using a fraction (33.33) forces the lines to overlap and fill a circle.
    # Adding (i * 0.03) slightly shifts the math each frame for the animation.
    k = 33.33 + (i * 0.03) 
    
    # Polar math (Rose Curve): Guarantees a perfectly circular boundary
    r = np.sin(k * t)
    
    # Convert back to X and Y for plotting
    x = r * np.cos(t)
    y = r * np.sin(t)
    
    plt.figure(figsize=(8,8))
    
    # Plot the sun/globe. 
    # Alpha is low (0.2) because so many lines cross in the center, making a naturally dark core
    plt.plot(x, y, color="#0E4277", alpha=0.2, linewidth=0.7)
    
    plt.axis('off') # Hide axes
    
    # CRITICAL: Force the limits of the graph so the globe doesn't "jump" or change size between frames
    plt.xlim(-1.1, 1.1)
    plt.ylim(-1.1, 1.1)
    
    filepath = os.path.join(output_dir, f'random_{i}.png')
    
    plt.savefig(filepath, transparent=True, dpi=150, bbox_inches='tight', pad_inches=0)
    plt.close()
    
    print(f"Saved frame {i+1}/10: {filepath}")

print("Done! Check the media/bg_spirograph folder.")