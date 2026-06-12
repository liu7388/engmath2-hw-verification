import numpy as np
import matplotlib.pyplot as plt
import os

# Fourier series partial sum expansion
def fourier_approximation(x, N):
    f_sum = 1 / 8
    for n in range(1, N + 1):
        an = ((-1) ** n - 1) / (2 * (n ** 2) * (np.pi ** 2))
        bn = ((-1) ** (n + 1)) / (2 * n * np.pi)
        f_sum += an * np.cos(2 * n * np.pi * x) + bn * np.sin(2 * n * np.pi * x)
    return f_sum

# Figure configuration (300 DPI for high quality)
fig, ax = plt.subplots(figsize=(11, 4.5), dpi=300)

# Center the spines at (0,0) to match the textbook style
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_linewidth(1.0)
ax.spines['bottom'].set_linewidth(1.0)

# Plot original piecewise function f(x) by periods
# Plot segments separately to avoid vertical lines at discontinuities
periods = [-1, 0, 1, 2]
label_added = False

for k in periods:
    # Flat segment (from k-0.5 to k)
    x_flat = np.linspace(k - 0.5, k, 100)
    y_flat = np.zeros_like(x_flat)

    # Ramp segment (from k to k+0.5)
    x_ramp = np.linspace(k, k + 0.5, 100)
    y_ramp = x_ramp - k

    # Avoid duplicate legend labels
    if not label_added:
        ax.plot(x_flat, y_flat, color='blue', lw=2.5, label='Original f(x)')
        label_added = True
    else:
        ax.plot(x_flat, y_flat, color='blue', lw=2.5)

    # Filter out segments beyond plot limits
    if (k + 0.5) <= 2.1:
        ax.plot(x_ramp, y_ramp, color='blue', lw=2.5)

# Add solid and hollow dots at jump discontinuities
jump_pts = [-0.5, 0.5, 1.5]
# Solid dots at the top
ax.plot(jump_pts, [0.5, 0.5, 0.5], 'o', color='blue', markersize=4.5, zorder=5)
# Hollow dots at the bottom
ax.plot(jump_pts, [0, 0, 0], 'o', color='blue', markerfacecolor='white', markeredgecolor='blue', markersize=4.5, zorder=5)

# Plot Fourier approximations for N=5 and N=50
x_fourier = np.linspace(-1.7, 2.2, 2000)
ax.plot(x_fourier, fourier_approximation(x_fourier, N=5),
        label='Fourier Series (N=5)', color='teal', linestyle=':', lw=1.5)
ax.plot(x_fourier, fourier_approximation(x_fourier, N=50),
        label='Fourier Series (N=50)', color='darkorange', linestyle='--', lw=1.5)

# Global reference line at y = 0.5
ax.axhline(y=0.5, color='gray', linestyle='--', linewidth=0.8, alpha=0.5, zorder=1)

# Axis ticks and LaTeX formatting
ax.set_xticks([-1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2])
ax.set_xticklabels(
    [r'$-\frac{3}{2}$', r'$-1$', r'$-\frac{1}{2}$', r'$0$', r'$\frac{1}{2}$', r'$1$', r'$\frac{3}{2}$', r'$2$'],
    fontsize=11)
ax.set_yticks([0.5])
ax.set_yticklabels([r'$\frac{1}{2}$'], fontsize=11)

# Adjust tick positions to avoid overlap with centered axes
ax.xaxis.get_major_ticks()[3].label1.set_va('top')
ax.xaxis.get_major_ticks()[3].label1.set_ha('right')

# Add axis labels x and f(x)
ax.text(2.25, -0.04, r'$x$', fontsize=13)
ax.text(-0.08, 0.56, r'$f(x)$', fontsize=13)

# Set display limits
ax.set_xlim(-1.7, 2.3)
ax.set_ylim(-0.12, 0.62)

# Legend settings
ax.legend(loc='upper left', frameon=True, facecolor='white', framealpha=0.9, fontsize=9)
plt.tight_layout()

# Save the plot to my specified directory
output_dir = "output_plots"
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "problem1_convergence.png")

# Export high-res image
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Verification plot successfully saved to: {output_path}")

plt.show()