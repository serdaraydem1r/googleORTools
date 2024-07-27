"""
Max 3x+4y
x + 2y <= 14
3x - y >= 0
x - y <= 2
x,y >= 0
"""

from ortools.linear_solver import pywraplp

def main():
    # çözücüyü oluştur
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return

    # değişkenleri oluştur.
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print(f"Değişkenler Oluşturuldu : x = ", x.solution_value(), ", y=",
          y.solution_value())

    # kısıtları ekle
    solver.Add(x + 2*y <= 14)
    solver.Add(3*x - y >= 0)
    solver.Add(x - y <= 2)

    print(f"Kısıtlar Eklendi.")

    # hedef fonksiyonu tanımla
    solver.Maximize(3*x + 4*y)

    # Çöz
    durum = solver.Solve()

    if durum == pywraplp.Solver.OPTIMAL:
        print("Optimal solution is found !")
        print(f"x: {x.solution_value()}")
        print(f"y: {y.solution_value()}")
        print(f"Maxsimum value =", solver.Objective().Value())
    else :
        print("Optimal solution is NOT found !")

main()
