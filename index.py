import pandas as pd
import csv


def conversion():
    df = pd.read_csv("final_output.csv")

    # Drop NAN Values
    df = df.dropna(axis=0)

    # Convert Values to Floats
    df["Radius"] = df['Radius'].astype(float)
    df['Mass'] = df['Mass'].astype(float)

    # Convert Data to SI units
    df['Radius'] = df['Radius'] * 6.957e+8
    df['Mass'] = df['Mass'] * 1.989e+30

    df.to_csv("final_list_converted.csv", index=False)

    calculate_gravity(df)


def calculate_gravity(df):
    gravities = []
    radiuses = []
    masses = []
    data = []

    with open("./final_list_converted.csv", 'r') as file:
        csv_data = csv.reader(file)

        for row in csv_data:
            data.append(row)

    content = data[1:]
    for row in content:
        radius = float(row[1])
        mass = float(row[2])

        G = 6.67E-11
        r = radius
        M = mass

        gravity = (G * M) / (r * r)
        gravities.append(gravity)
        radiuses.append(radius)
        masses.append(masses)

    new_dataframe(gravities)


def new_dataframe(gravities):
    df = pd.read_csv("./final_list_converted.csv")
    df = df.assign(Gravity=gravities)

    df.to_csv("final_list.csv", index=False)


conversion()
