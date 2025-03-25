import numpy as np

def radians_to_degrees(rad_values):
    degrees = np.degrees(rad_values)
    for rad, deg in zip(rad_values, degrees):
        print(f"{rad} rad = {deg:.2f}°")
    print()

def degrees_to_radians(deg_values):
    radians = np.radians(deg_values)
    for deg, rad in zip(deg_values, radians):
        print(f"{deg}° = {rad:.4f} rad")
    print()

def conversion_table():
    degrees_table = [30, 45, 60, 90, 120, 135, 150, 180, 270, 360]
    print("Asteet  | Radiaanit")
    print("-" * 20)
    for deg in degrees_table:
        print(f"{deg:<7} | {np.radians(deg):.4f}")
    print()

def calculate_hypo(a, b):
    hypo = np.sqrt(a**2 + b**2)
    print(f"Hypotenuusa: {hypo:.2f} m\n")

def rectangle_sides(diagonal, ratio1, ratio2):
    factor = diagonal / np.sqrt(ratio1**2 + ratio2**2)
    side1 = factor * ratio1
    side2 = factor * ratio2
    print(f"Suorakulmion sivut: {side1:.2f} m ja {side2:.2f} m\n")

def main():
    print("1. Radiaanit asteiksi:")
    radians_to_degrees([2.493, 0.911])

    print("2. Asteet radiaaneiksi:")
    degrees_to_radians([137.7, 62.3])

    print("3. Kulmataulukko:")
    conversion_table()

    print("4. Hypotenuusa:")
    calculate_hypo(1.6, 2.3)

    print("5. Suorakulmion sivujen laskeminen:")
    rectangle_sides(6.4, 3, 2)

if __name__ == "__main__":
    main()