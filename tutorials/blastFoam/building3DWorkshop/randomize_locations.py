import os
import subprocess
import random


def randomize_variables():
    """Randomize the variables in wall_loc and charge_loc files."""
    wall_loc_path = os.path.join("variables", "wall_loc")
    charge_loc_path = os.path.join("variables", "charge_loc")

    # Randomize wall_loc variables
    with open(wall_loc_path, 'w') as f:
        f.write("""/*--------------------------------*- C++ -*----------------------------------*\\
  =========                 |
  \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox
   \\    /   O peration     | Website:  https://openfoam.org
    \\  /    A nd           | Version:  dev
     \\/     M anipulation  |
\\*---------------------------------------------------------------------------*/
FoamFile
{
    version     2.0;
    format      ascii;
    class       IOobject;
    location    "include";
    object      wall_loc;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //
""")
        x_start = -1.9
        x_increment = 2.0
        for i in range(1, 4):
            if i == 1:
                xMin_1 = -4.9
                xMin_2 = -3.9
                xMax_1 = -2.0
                xMax_2 = -1.0
            elif i == 2:
                xMin_1 = -0.9
                xMin_2 = 0.1
                xMax_1 = 1.0
                xMax_2 = 2.0
            elif i == 3:
                xMin_1 = 2.9
                xMin_2 = 3.9
                xMax_1 = 4.0
                xMax_2 = 4.9
            xMin = random.uniform(xMin_1, xMin_2)
            xMax = random.uniform(xMax_1, xMax_2)
            yMin = random.uniform(2.0, 3.0)
            yMax = yMin + random.uniform(0.5, 1.0)
            zMin = 0.0
            zMax = random.uniform(0.5, 2.0)
            f.write(f"xMin{i}      {xMin};\n")
            f.write(f"yMin{i}      {yMin};\n")
            f.write(f"zMin{i}      {zMin};\n")
            f.write(f"xMax{i}      {xMax};\n")
            f.write(f"yMax{i}      {yMax};\n")
            f.write(f"zMax{i}      {zMax};\n\n")

    # Randomize charge_loc variables
    with open(charge_loc_path, 'w') as f:
        f.write("""/*--------------------------------*- C++ -*----------------------------------*\\
  =========                 |
  \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox
   \\    /   O peration     | Website:  https://openfoam.org
    \\  /    A nd           | Version:  dev
     \\/     M anipulation  |
\\*---------------------------------------------------------------------------*/
FoamFile
{
    version     2.0;
    format      ascii;
    class       IOobject;
    location    "include";
    object      charge_loc;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //
""")
        for i in range(2):
            if i == 0:
                cent = (random.uniform(-4.9, 4.9), random.uniform(-4.9, 2.0), random.uniform(0.0, 1.0))
                p1 = (random.uniform(0.0, 2.0), random.uniform(0.0, 2.0), random.uniform(0.0, 1.0))
                radius = random.uniform(0.1, 1.0)
                mass = random.uniform(5.0, 20.0)
                f.write(f"mass      {mass};\n\n")
            else:
                pnew = (p1[0], p1[1], 0.0)
                p1 = pnew
                radius = 0.75
            f.write(f"cent{i}     ({cent[0]} {cent[1]} {cent[2]});\n")
            f.write(f"p1{i}       ({p1[0]} {p1[1]} {p1[2]});\n")
            f.write(f"radius{i}    {radius};\n")