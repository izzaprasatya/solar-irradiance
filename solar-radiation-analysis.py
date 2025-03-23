"""
Automation for calculating r.sun parameters for each day in a month (ex. January)
Created by Izza P.A.
"""

import grass.script as gs

# parameters for each days in january
days = {day: {"day": day, "linke_value": 4.5} for day in range(1, 32)}

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
    bufferzone='100',
    output='horangle',
    maxdistance='100')

# r.sun loop operation r.sun
for day, params in days.items():
    gs.run_command('r.sun',
        elevation='dem',
        aspect='aspect@PROJECT',
        slope='slope@PROJECT',
        linke_value=params["linke_value"],
        albedo_value='0.18',
        horizon_basename='horangle',
        horizon_step='30',
        beam_rad=f'rad_beam{day}',
        diff_rad=f'rad_diff{day}',
        refl_rad=f'rad_refl{day}',
        glob_rad=f'rad_glob{day}',
        insol_time=f'rad_insol{day}',
        day=str(params["day"]),
        overwrite=True)
