import grass.script as gscript

# Define the output raster name for the monthly average
output_raster = "rad_insol_2_avg"

# Generate the list of input rasters (rad_glob1 to rad_glob31)
input_rasters = [f"rad_insol{i}" for i in range(32, 60)]

# Run r.series to compute the average of the 31 rasters
gscript.run_command("r.series",
                     input=",".join(input_rasters),
                     output=output_raster,
                     method="average")