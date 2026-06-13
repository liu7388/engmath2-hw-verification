# engmath2-hw-verification

## 📌 Project Overview
This repository is dedicated to storing the code verification components of the **Engineering Mathematics (II) — AI-Assisted Homework Assignment**. 

The core objective of this project is to utilize Python scripts (leveraging libraries such as `NumPy`, `Matplotlib`, and `SymPy`) to perform **numerical simulation, symbolic computation, and convergence verification** for two randomly assigned engineering mathematics problems. This process rigorously ensures 100% correctness of the analytical solutions derived during the AI-collaborative workflow.

* 📑 **Detailed Homework Report (HackMD)**: [Click here to view my full Engineering Mathematics report](https://hackmd.io/@QENvl1H2S7C_KP9TKmSJIA/SJvyBc5bfl)

---

## 📂 Project Structure and Problem Mapping

The directory structure of this repository is organized as follows. Files are clearly categorized by `problem1` and `problem2` to facilitate seamless cross-referencing and review:

```text
engmath2-hw-verification/
├── README.md                  # This documentation file
├── problem1_fourier.py               # Problem 1: Fourier series convergence verification script
├── problem2_wave.py                # Problem 2: 1-D wave equation symbolic differentiation verification script
└── output_plots/              # Data visualization output directory
    └── problem1_convergence.png  # Problem 1: Fourier series partial sums (first N terms) approximation plot
```

## 📊 Verification Methodology & Key Results

### 1. Problem 1: Fourier Series Convergence Verification (`problem1_fourier.py`)
* **Objective:** Verify the half-wave rectified piecewise function's Fourier expansion coefficients (a₀, aₙ, bₙ) over period p = 1 (L = 1/2).
* **Methodology:** Implemented numerical summation of the partial sums from N = 5 up to N = 50 using NumPy and Matplotlib.
* **Key Observations:** The visualization clearly presents the Gibbs phenomenon near the discontinuities (x = ±1/2), perfectly corroborating Dirichlet's Theorem where the series converges to the midpoint value of 1/4.

### 2. Problem 2: 1-D Wave Equation Special Solution (`problem2_wave.py`)
* **Objective:** Formally verify whether the specific solution u(x, t) = cos(4t)sin(2x) satisfies the homogeneous wave equation uₜₜ = c² uₓₓ.
* **Methodology:** Utilized SymPy for exact symbolic differentiation to compute the analytical partial derivatives (∂²u/∂t² and ∂²u/∂x²) and verify boundary conditions.
**Verification Output:**
```text
[SymPy Engine Output]
Calculated u_tt = -16*sin(2*x)*cos(4*t)
Calculated u_xx = -4*sin(2*x)*cos(4*t)
Solving algebraic relation u_tt = c^2 * u_xx...
Successfully derived Wave Speed Constant c = [-2, 2] (Matches Hand Derivation perfectly!)
```

## 🛠️ Quick Start & Environment Setup

To clone this project and replicate the verification analysis locally, follow these steps:

### 1. Clone the Repository
* **Objective:** Obtain a local copy of the verification source code.
* **Methodology:** Use Git to clone the repository and navigate into the project directory.

**Execution Command:**
```bash
git clone [https://github.com/liu7388/engmath2-hw-verification.git](https://github.com/liu7388/engmath2-hw-verification.git)
cd engmath2-hw-verification
```

### 2. Install Dependencies
Ensure you have Python 3.8+ installed, then install the required core computing libraries:

**Execution Command:**
```bash
pip install numpy matplotlib sympy
```

### 3. Run Verification Scripts
Execute the scripts to run the symbolic computations and regenerate the convergence plot:


**Execution Command:**
```bash
# Run Fourier Series approximation and plot generator
python problem1_fourier.py

# Run Wave Equation partial differentiation verification
python problem2_wave.py
```