# Public PyMol scripts
Welcome to the repository of PyMOl scripts created by the Bio2Byte group!

<p align="center">
  <img src="https://pbs.twimg.com/profile_images/1247824923546079232/B9b_Yg7n_400x400.jpg" width="48px"/>
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Vrije_Universiteit_Brussel_logo.svg/1200px-Vrije_Universiteit_Brussel_logo.svg.png" alt="vub" width="120px"/>
</p>

## AlphaFold pLDDT Colorize script

This function will colorize each atom using the default DeepMind AlphaFold pLDDT scale taking the values from the b-factor column stored inside the PDB file.

> AlphaFold produces a per-residue confidence score (pLDDT) between 0 and 100. Some regions below 50 pLDDT may be unstructured in isolation.

Once you have run the script, the PyMol command interpreter will print out relevant information from the sequence metadata. For instance:

```console
AlphaFold produces a per-residue confidence score (pLDDT) between 0 and 100. Some regions below 50 pLDDT may be unstructured in isolation.

Very high (pLDDT > 90) = 3844 atoms (57.22%)
Confident (90 > pLDDT > 70) = 1500 atoms (22.33%)
Low (70 > pLDDT > 50) = 387 atoms (5.76%)
Very low (pLDDT < 50) = 987 atoms (14.69%)
Avg. pLDDT = 81.244434
```

![example](https://github.com/Bio2Byte/public_notebooks/blob/main/pymol/example_alphafold_pymol.png)

### How to use it?

1. Download the script "alphafold_plddt_colorize.py" to your computer:
    1. From the repository on Github, open the file "alphafold_plddt_colorize.py"
    2. Click on "Raw" button to open the file content on your browser
    3. Save the page as "alphafold_plddt_colorize.py". In Windows or Linux using "Ctrl + S" or in OSX (Apple laptops) using "Command + S"
1. From PyMol, open the script:
    1. From "File" menu, select the option "Run script ..."
    1. Find the script "alphafold_plddt_colorize.py" on your local computer and select it
1. The script will run automatically the first time
1. To run it again, from the PyMol command interpreter type: `alphafold_plddt_colorize()`
