# B2btools: Predict the biophysical behavior of your protein(s) - Public Notebooks
Welcome to the repository of Jupyter Notebooks created by the Bio2Byte group!

<p align="center">
  <img src="https://pbs.twimg.com/profile_images/1247824923546079232/B9b_Yg7n_400x400.jpg" width="48px"/>
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Vrije_Universiteit_Brussel_logo.svg/1200px-Vrije_Universiteit_Brussel_logo.svg.png" alt="vub" width="120px"/>
</p>

## About Bio2Byte

Proteins are the molecular machines that make cells work. They perform a wide variety of functions through interactions with each other and many additional molecules. Traditionally, proteins are described in a single static state (a picture). It is now increasingly recognised that many proteins can adopt multiple states and move between these conformational states dynamically (a movie).

We investigate how the dynamics, conformational states and available experimental data of proteins relates to their amino acid sequence. Underlying physical and chemical principles are computationally unravelled through data integration, analysis and machine learning, so connecting them to biological events and improving our understanding of the way proteins work.

The Bio2Byte group is primarily situated at the Interuniversity Institute of Bioinformatics in Brussels, a collaborative interfaculty institute between the Vrije Universiteit Brussel and the Université Libre de Bruxelles. It is located at the the ULB side of the Pleinlaan/La Plaine campus on the 6th floor of the C building.

At the VUB, the group is linked to Structural Biology Brussels at the Bioengineering sciences department, as well as the departments of Computer Science and Chemistry at the Faculty of Sciences, plus to the Biomedical sciences at the Faculty of Medicine and Pharmacy.

### 🔗 Links
- [Bio2Byte](https://bio2byte.be)
- [Bio2Byte online predictors](https://bio2byte.be/b2btools)
- [Feedaback](https://www.bio2byte.be/b2btools/feedback)
- [Bio2Byte tools package](https://pypi.org/project/b2bTools/)

## About the b2btools
Explore the prediction-based 'biophysical variation' of proteins along its sequence. The predictions reflect 'emerging' properties, so what the sequence is capable of, not necessarily what it will do in a particular context, for example when it adopts a specific fold. 
The predicted biophysical features are the following:
- Backbone and sidechain dynamics (DynaMine)
- Conformational propensities (sheet, helix, coil, polyproline II) (DynaMine)
- Early folding propensities (EFoldMine)
- Disorder propensities (DisoMine)
- Beta aggregation propensity (AgMata)
- Phase seperation propensity (PPser) 


## 📚 List of available notebooks

### Single Sequence analysis

##### 📓 Title: `Bio2ByteTools_v3_singleseq_pypi.ipynb` (latest version)

Example of usage of our Bio2Byte tools package for single sequence(s) using v3.0.5.
- [⏯️ Open Jupyter Notebook on Google Colab](https://colab.research.google.com/github/Bio2Byte/public_notebooks/blob/main/Bio2ByteTools_v3.0.5_SingleSequence_demo.ipynb)

##### 📓 Title: `AlphaFold_+_B2B_Tools.ipynb`

Run the biophysical feature predictions on top of an Alphafold thee-dimensional predicted structure.
- [⏯️ Open Jupyter Notebook on Google Colab](https://colab.research.google.com/github/Bio2Byte/public_notebooks/blob/main/AlphaFold_%2B_B2B_Tools.ipynb)

##### 📓 Title: `Bio2Byte_AlphaFold_Analysis.ipynb`

Compare the predicted biophysical features obtained with the b2btools and the pLDTT computed by Alphafold.
- [⏯️ Open Jupyter Notebook on Google Colab](https://colab.research.google.com/github/Bio2Byte/public_notebooks/blob/main/Bio2Byte_AlphaFold_Analysis.ipynb)


### Multiple Sequence Alignment analysis

Explore prediction-based 'biophysical variation' of proteins from a multiple sequence alignment.

#### 📦 Using PyPI (Python Package Index)

##### 📓 Title: `Bio2ByteTools_v3_multipleseq_pypi.ipynb`

Example of usage of our Bio2Byte tools package for Multiple Sequence Alignment file inputs
- [⏯️ Open Jupyter Notebook on Google Colab](https://colab.research.google.com/github/Bio2Byte/public_notebooks/blob/main/Bio2ByteTools_v3_multipleseq_pypi.ipynb)

### PyMol on Google Colab

##### 📓 Title: `Bio2Byte_Pymol_scripting.ipynb`

Example of PyMol scripting in Python. This notebook fetchs a PDB and renders both a static image and a 360-degree rotated animation
- [⏯️ Open Jupyter Notebook on Google Colab](https://colab.research.google.com/github/Bio2Byte/public_notebooks/blob/main/Bio2Byte_Pymol_scripting.ipynb)


## 📃 How to use them?
1. Open the Jupyter notebook file of interest
1. There will be a "Open In Colab" button, if you click on it, a new session on Google Colab will be started
1. From the Google Colab session you will be able to run the code of the notebook.

## Copyright

© Wim Vranken, Bio2Byte group, VUB
