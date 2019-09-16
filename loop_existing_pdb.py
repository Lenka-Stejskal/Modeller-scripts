# Loop refinement of an existing model
from modeller import *
from modeller.automodel import *

log.verbose()
env = environ()

# directories for input atom files
env.io.atom_files_directory = ['.', '../atom_files']

# Create a new class based on 'loopmodel' so that we can redefine
# select_loop_atoms (necessary)
class MyLoop(loopmodel):
    # This routine picks the residues to be refined by loop modeling
    def select_loop_atoms(self):
        return selection(self.residue_range('203:', '213:'),
                        self.residue_range('191:', '194:'))

a = MyLoop(env,
           inimodel=‘input_model.pdb’,   # initial model of the target
           sequence='4mwf_d.full',                 # code of the target
           loop_assess_methods=assess.DOPE) # assess loops with DOPE


a.loop.starting_model= 1           # index of the first loop model
a.loop.ending_model  = 1000        # index of the last loop model
a.loop.md_level = refine.slow  # loop refinement method

a.make()
