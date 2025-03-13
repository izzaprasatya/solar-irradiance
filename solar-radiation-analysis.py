"""
Automation for calculating r.sun parameters monthly in a year
Created by Izza P.A. using pyGRASS
"""

import grass.script as gs

# parameters for each month
months = {
    1: {"day": 23, "linke_value": 4.5},
    2: {"day": 54, "linke_value": 4.5},
    3: {"day": 82, "linke_value": 5.2},
    4: {"day": 113, "linke_value": 5.5},
    5: {"day": 143, "linke_value": 6.0},
    6: {"day": 174, "linke_value": 6.5},
    7: {"day": 204, "linke_value": 7.0},
    8: {"day": 235, "linke_value": 6.5},
    9: {"day": 266, "linke_value": 6.0},
    10: {"day": 296, "linke_value": 5.5},
    11: {"day": 327, "linke_value": 5.0},
    12: {"day": 357, "linke_value": 4.8},
}

# slope & aspect calculation
gs.run_command('r.slope.aspect',
    elevation='dem',
    slope='slope',
    aspect='aspect',
    overwrite=True)

# horizon calculation
gs.run_command('r.horizon',
    elevation='dem',
    step='30',
    bufferzone='200',
    output='horangle',
    maxdistance='500')

# r.sun loop operation r.sun
for month, params in months.items():
    gs.run_command('r.sun',
        elevation='elevation@PERMANENT',
        aspect='aspect@PROJECT',
        slope='slope@PROJECT',
        linke_value=params["linke_value"],
        albedo_value='0.18',
        horizon_basename='horangle',
        horizon_step='30',
        beam_rad=f'beam{month}',
        diff_rad=f'diff{month}',
        refl_rad=f'refl{month}',
        glob_rad=f'glob{month}',
        insol_time=f'insol{month}',
        day=str(params["day"]),
        overwrite=True)

# coloring the global irradiance
for i in range(1, 13):
    gs.run_command('r.colors', map=f'glob{i}', color='bcyr')

# univariate statistics of global irradiance for each months
stats = [gs.read_command('r.univar', map=f'glob{i}') for i in range(1, 13)]
print("\n".join(stats))
