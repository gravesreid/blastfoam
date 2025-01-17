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
    for i in range(20, 30, 1):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        os.chdir(script_dir)

        # clean workspace
        run_command("./Allclean")

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

        # copy all results and porstProcessing directory to dataset directory
        dataset_dir = f"/home/reid/projects/blast_waves/dataset_0/{i}"
        if not os.path.exists(dataset_dir):
            os.makedirs(dataset_dir)
        run_command(f"cp -r 0* {dataset_dir}")
        run_command(f"cp -r postProcessing {dataset_dir}")
        run_command(f"cp -r variables {dataset_dir}")
        run_command(f"cp *.foam {dataset_dir}")
    

if __name__ == "__main__":
    main()

