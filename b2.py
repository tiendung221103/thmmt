import numpy as np
import matplotlib.pyplot as plt
from sympy import *
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class CalcHelper:
  def __init__(self):
    self.window = tk.Tk()
    self.window.title("Phần mềm hỗ trợ học Giải tích")
    self.window.geometry("800x600")

    # Tạo notebook để chứa các tab
    self.notebook = ttk.Notebook(self.window)

    # Tab tính đạo hàm
    self.derivative_tab = ttk.Frame(self.notebook)
    self.create_derivative_tab()

    # Tab tính tích phân
    self.integral_tab = ttk.Frame(self.notebook)
    self.create_integral_tab()

    # Tab tính nguyên hàm
    self.antiderivative_tab = ttk.Frame(self.notebook)
    self.create_antiderivative_tab()

    # Tab vẽ đồ thị hàm số
    self.graph_tab = ttk.Frame(self.notebook)
    self.create_graph_tab()

    self.notebook.add(self.derivative_tab, text="Đạo hàm")
    self.notebook.add(self.integral_tab, text="Tích phân")
    self.notebook.add(self.antiderivative_tab, text="Nguyên hàm")
    self.notebook.add(self.graph_tab, text="Đồ thị")
    self.notebook.pack(expand=True, fill='both')

  def create_derivative_tab(self):
    # Frame nhập liệu
    input_frame = ttk.Frame(self.derivative_tab)
    input_frame.pack(pady=10)

    ttk.Label(input_frame, text="Nhập hàm số:").pack(side=tk.LEFT)
    self.derivative_entry = ttk.Entry(input_frame, width=40)
    self.derivative_entry.pack(side=tk.LEFT, padx=5)

    ttk.Button(input_frame, text="Tính đạo hàm", command=self.calculate_derivative).pack(side=tk.LEFT)

    # Kết quả
    self.derivative_result = tk.Text(self.derivative_tab, height=5, width=60)
    self.derivative_result.pack(pady=10)

  def create_integral_tab(self):
    # Frame nhập liệu
    input_frame = ttk.Frame(self.integral_tab)
    input_frame.pack(pady=10)

    ttk.Label(input_frame, text="Nhập hàm số:").pack(side=tk.LEFT)
    self.integral_entry = ttk.Entry(input_frame, width=40)
    self.integral_entry.pack(side=tk.LEFT, padx=5)

    limit_frame = ttk.Frame(self.integral_tab)
    limit_frame.pack(pady=5)

    ttk.Label(limit_frame, text="Cận dưới:").pack(side=tk.LEFT)
    self.lower_limit = ttk.Entry(limit_frame, width=10)
    self.lower_limit.pack(side=tk.LEFT, padx=5)

    ttk.Label(limit_frame, text="Cận trên:").pack(side=tk.LEFT)
    self.upper_limit = ttk.Entry(limit_frame, width=10)
    self.upper_limit.pack(side=tk.LEFT, padx=5)

    ttk.Button(input_frame, text="Tính tích phân", command=self.calculate_integral).pack(side=tk.LEFT)

    # Kết quả
    self.integral_result = tk.Text(self.integral_tab, height=5, width=60)
    self.integral_result.pack(pady=10)

  def create_antiderivative_tab(self):
    # Frame nhập liệu
    input_frame = ttk.Frame(self.antiderivative_tab)
    input_frame.pack(pady=10)

    ttk.Label(input_frame, text="Nhập hàm số:").pack(side=tk.LEFT)
    self.antiderivative_entry = ttk.Entry(input_frame, width=40)
    self.antiderivative_entry.pack(side=tk.LEFT, padx=5)

    ttk.Button(input_frame, text="Tính nguyên hàm", command=self.calculate_antiderivative).pack(side=tk.LEFT)

    # Kết quả
    self.antiderivative_result = tk.Text(self.antiderivative_tab, height=5, width=60)
    self.antiderivative_result.pack(pady=10)

  def create_graph_tab(self):
    # Frame nhập liệu
    input_frame = ttk.Frame(self.graph_tab)
    input_frame.pack(pady=10)

    ttk.Label(input_frame, text="Nhập hàm số:").pack(side=tk.LEFT)
    self.graph_entry = ttk.Entry(input_frame, width=40)
    self.graph_entry.pack(side=tk.LEFT, padx=5)

    ttk.Button(input_frame, text="Vẽ đồ thị", command=self.plot_graph).pack(side=tk.LEFT)

    # Frame đồ thị
    self.graph_frame = ttk.Frame(self.graph_tab)
    self.graph_frame.pack(fill=tk.BOTH, expand=True)

  def calculate_derivative(self):
    try:
      x = Symbol('x')
      expr = self.derivative_entry.get()
      derivative = diff(expr, x)
      self.derivative_result.delete(1.0, tk.END)
      self.derivative_result.insert(tk.END, f"Đạo hàm của {expr} là:\n{derivative}")
    except Exception as e:
      self.derivative_result.delete(1.0, tk.END)
      self.derivative_result.insert(tk.END, f"Lỗi: {str(e)}")

  def calculate_integral(self):
    try:
      x = Symbol('x')
      expr = self.integral_entry.get()

      # Kiểm tra nếu có nhập cận
      if self.lower_limit.get() and self.upper_limit.get():
        a = float(self.lower_limit.get())
        b = float(self.upper_limit.get())
        result = integrate(expr, (x, a, b))
        self.integral_result.delete(1.0, tk.END)
        self.integral_result.insert(tk.END, f"Tích phân xác định của {expr} từ {a} đến {b} là:\n{result}")
      else:
        result = integrate(expr, x)
        self.integral_result.delete(1.0, tk.END)
        self.integral_result.insert(tk.END, f"Tích phân của {expr} là:\n{result} + C")
    except Exception as e:
      self.integral_result.delete(1.0, tk.END)
      self.integral_result.insert(tk.END, f"Lỗi: {str(e)}")

  def calculate_antiderivative(self):
    try:
      x = Symbol('x')
      expr = self.antiderivative_entry.get()
      antiderivative = integrate(expr, x)
      self.antiderivative_result.delete(1.0, tk.END)
      self.antiderivative_result.insert(tk.END, f"Nguyên hàm của {expr} là:\n{antiderivative} + C")
    except Exception as e:
      self.antiderivative_result.delete(1.0, tk.END)
      self.antiderivative_result.insert(tk.END, f"Lỗi: {str(e)}")

  def plot_graph(self):
    try:
      # Xóa đồ thị cũ nếu có
      for widget in self.graph_frame.winfo_children():
        widget.destroy()

      # Tạo đồ thị mới
      fig, ax = plt.subplots(figsize=(6, 4))
      x = np.linspace(-10, 10, 1000)

      # Chuyển đổi biểu thức sang hàm numpy
      expr = self.graph_entry.get()
      y = eval(expr.replace('x', 'x'))

      ax.plot(x, y)
      ax.grid(True)
      ax.axhline(y=0, color='k', linestyle='-', alpha=0.3)
      ax.axvline(x=0, color='k', linestyle='-', alpha=0.3)

      # Hiển thị đồ thị trong frame
      canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
      canvas.draw()
      canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    except Exception as e:
      # Hiển thị lỗi trong một label
      error_label = ttk.Label(self.graph_frame, text=f"Lỗi: {str(e)}")
      error_label.pack()

  def run(self):
    self.window.mainloop()


if __name__ == "__main__":
  app = CalcHelper()
  app.run()