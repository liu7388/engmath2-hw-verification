import sympy as sp

# Define symbolic variables
x, t, c = sp.symbols('x t c', real=True)

# Define the given solution u(x, t)
u = sp.cos(4 * t) * sp.sin(2 * x)

# Differentiate u twice with respect to t (u_tt)
u_tt = sp.diff(u, t, 2)

# Differentiate u twice with respect to x (u_xx)
u_xx = sp.diff(u, x, 2)

# Print the results of partial differentiation
print(f"Calculated u_tt = {u_tt}")
print(f"Calculated u_xx = {u_xx}")

# Set up the wave equation u_tt = (c^2) * u_xx and solve for c
wave_equation = sp.Eq(u_tt, (c**2) * u_xx)
c_solutions = sp.solve(wave_equation, c)

print(f"\nSubstituting into the wave equation, solved constant c = {c_solutions}")