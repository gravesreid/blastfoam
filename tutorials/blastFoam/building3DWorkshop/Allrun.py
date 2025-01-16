import os
import subprocess

from randomize_locations import randomize_variables

def run_command(command):
    """Run a shell command after sourcing the environment."""
    source_command = ". $WM_PROJECT_DIR/bin/tools/RunFunctions"
    full_command = f"bash -c '{source_command} && {command}'"
    print("Running command: " + command)
    result = subprocess.run(full_command, shell=True, text=True)
    if result.returncode != 0:
        print("Error running command: " + command)
        exit(1)

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    randomize_variables()

    # Create paraview file
    run_command("paraFoam -builtin -touch")

    # Create mesh for the fluid
    run_command("runApplication blockMesh")

    # Decompose the mesh
    #run_command("runApplication decomposePar -copyZero")

    # Cut out the shapes
    #run_command("runParallel snappyHexMesh -overwrite")
    run_command("runApplication snappyHexMesh -overwrite")

    # Add internal patch
    #run_command("runParallel addEmptyPatch internalPatch internal -overwrite")
    run_command("runApplication addEmptyPatch internalPatch internal -overwrite")

    # Set initial conditions
    #run_command("runParallel setRefinedFields")
    run_command("runApplication setRefinedFields")

    # Run the calculation
    application = subprocess.getoutput("bash -c '. $WM_PROJECT_DIR/bin/tools/RunFunctions && getApplication'").strip()
    #run_command(f"runParallel {application}")
    run_command(f"runApplication {application}")

    # Pressure probes
    run_command("runApplication calculateImpulse pressureProbes")

if __name__ == "__main__":
    main()

