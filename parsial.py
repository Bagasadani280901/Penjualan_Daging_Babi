import streamlit as st 
import sympy as sp 
import numpy as np 
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D 

# Header
st.title("Aplikasi Interaktif: Turunan Parsial dan Bidang Singgung")
st.write("Masukkan fungsi f(x, y) dan titik evaluasi untuk menghitung turunan parsial serta menampilkan grafik.")

# Input pengguna
x, y = sp.symbols('x y')
fungsi_input = st.text_input("Masukkan fungsi f(x, y):", value="x**2 + y**2 + 2*x*y")
p = st.number_input("Masukkan nilai p (untuk x):", value=1.0)
h = st.number_input("Masukkan nilai h (untuk y):", value=2.0)

# Proses simbolik
try:
    f = sp.sympify(fungsi_input)
    fx = sp.diff(f, x)
    fy = sp.diff(f, y)

    # Evaluasi turunan di titik (2p, h)
    x_val, y_val = 2*p, h
    fx_val = fx.subs({x: x_val, y: y_val})
    fy_val = fy.subs({x: x_val, y: y_val})
    f_val = f.subs({x: x_val, y: y_val})

    st.markdown(f"**Turunan parsial terhadap x:** {fx} → Nilai di titik ({x_val}, {y_val}) = {fx_val}")
    st.markdown(f"**Turunan parsial terhadap y:** {fy} → Nilai di titik ({x_val}, {y_val}) = {fy_val}")
    st.markdown(f"**Nilai f(x, y) di titik ({x_val}, {y_val}) = {f_val}**")

    # Grafik permukaan dan bidang singgung
    st.markdown("### Visualisasi 3D")

    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')

    X = np.linspace(x_val - 2, x_val + 2, 50)
    Y = np.linspace(y_val - 2, y_val + 2, 50)
    X, Y = np.meshgrid(X, Y)
    f_np = sp.lambdify((x, y), f, modules='numpy')
    Z = f_np(X, Y)

    ax.plot_surface(X, Y, Z, alpha=0.6, cmap='viridis', edgecolor='none')

    # Bidang singgung
    Z_tangent = float(f_val) + float(fx_val)*(X - x_val) + float(fy_val)*(Y - y_val)
    ax.plot_surface(X, Y, Z_tangent, color='red', alpha=0.5)

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('f(x, y)')
    st.pyplot(fig)

except Exception as e:
    st.error(f"Terjadi kesalahan: {e}")
