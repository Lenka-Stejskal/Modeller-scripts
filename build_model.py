from modeller import *
from modeller.automodel import *

log.verbose()

class MyModel(automodel):
    def special_patches(self, aln):
        self.patch(residue_type='DISU', residues=(self.residues['76'], self.residues['103']))


env = environ()

env.io.atom_files_directory = ['.', '../atom_files']

# Build models, and assess with DOPE
a = MyModel(env, alnfile = 'alignment_full.ali',
             knowns = (‘4mwf_chain_D.pdb','4dgv_A.pdb','4dgy_A.pdb','4g6a_A.pdb','4gag_p.pdb','4gaj_P.pdb','4hs6_Z.pdb','4wht_i.pdb','5eoc_q.pdb','4hs8_A.pdb'),
             sequence = '4mwf_d.full',
             assess_methods=(assess.DOPE))

a.md_level = refine.slow
a.starting_model= 1
a.ending_model  = 1000
a.make()
