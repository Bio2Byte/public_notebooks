#####################################################################
#
# AlphaFold predicted structure:
# Colorized by pLDDT
#
#####################################################################

from pymol import cmd, stored

def alphafold_plddt_colorize():
	"""
AUTHOR

	Adrián Diaz
	Wim Wranken - Bio2Byte group - Vrije Universiteit Brussel
	Belgium
	https://bio2byte.be

USAGE

	alphafold_plddt_colorize()

	This function will colorize each atom using the default DeepMind AlphaFold pLDDT scale
	taking the values from the b-factor column stored inside the PDB file.
	AlphaFold produces a per-residue confidence score (pLDDT) between 0 and 100.
	Some regions below 50 pLDDT may be unstructured in isolation.
	"""

	# Declare pLDDT ranges
	very_high_condition = 'b > 90 or b = 90'
	confident_condition = 'b < 90 & (b > 70 | b = 70)'
	low_condition       = 'b < 70 & (b > 50 | b = 50)'
	very_low_condition  = 'b < 50'

	# Declare range colors
	cmd.set_color('veryhigh', [0, 83, 214])
	cmd.set_color('confident', [101, 203, 243])
	cmd.set_color('low', [255, 219, 19])
	cmd.set_color('verylow', [255, 125, 69])

	# Count the number of atoms of each range
	total_atoms_count = cmd.count_atoms('all')
	very_high_condition_atoms_count = cmd.count_atoms(very_high_condition)
	confident_condition_atoms_count = cmd.count_atoms(confident_condition)
	low_condition_atoms_count = cmd.count_atoms(low_condition)
	very_low_condition_atoms_count = cmd.count_atoms(very_low_condition)

	# Percentages
	very_high_condition_percentage = (very_high_condition_atoms_count / total_atoms_count) * 100
	confident_condition_percentage = (confident_condition_atoms_count / total_atoms_count) * 100
	low_condition_percentage = (low_condition_atoms_count / total_atoms_count) * 100
	very_low_condition_percentage = (very_low_condition_atoms_count / total_atoms_count) * 100

	# Average pLDDT
	avg_plddt = average_plddt_from_b_factor()

	# Print out
	print("AlphaFold produces a per-residue confidence score (pLDDT) between 0 and 100. Some regions below 50 pLDDT may be unstructured in isolation.\n")
	print("Very high (pLDDT > 90) = %d atoms (%.2f%%)" % (very_high_condition_atoms_count, very_high_condition_percentage))
	print("Confident (90 > pLDDT > 70) = %d atoms (%.2f%%)" % (confident_condition_atoms_count, confident_condition_percentage))
	print("Low (70 > pLDDT > 50) = %d atoms (%.2f%%)" % (low_condition_atoms_count, low_condition_percentage))
	print("Very low (pLDDT < 50) = %d atoms (%.2f%%)" % (very_low_condition_atoms_count, very_low_condition_percentage))
	print("Avg. pLDDT = %f" % avg_plddt)

	# Apply the color to each range
	cmd.color('verylow', very_low_condition)
	cmd.color('low', low_condition)
	cmd.color('confident', confident_condition)
	cmd.color('veryhigh', very_high_condition)


def average_plddt_from_b_factor(selection = 'all'):

	"""
	Adapted from average_b.py
	Written by Gregor Hagelueken

	https://pymolwiki.org/index.php/Average_b
	"""

	stored.tempfactor = 0
	stored.atomnumber = 0
	cmd.iterate(selection, "stored.tempfactor = stored.tempfactor + b")
	cmd.iterate(selection, "stored.atomnumber = stored.atomnumber + 1")
	averagetempfactor = stored.tempfactor / stored.atomnumber

	return averagetempfactor


# Add alphafold_plddt_colorize to the PyMOL command list
cmd.extend("alphafold_plddt_colorize", alphafold_plddt_colorize)

alphafold_plddt_colorize()
