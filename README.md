# B2btools: Predict the biophysical behavior of your protein(s) - Public Notebooks
Welcome to the repository of Jupyter Notebooks created by the Bio2Byte group!

<p align="center">
  <img src="https://pbs.twimg.com/profile_images/1247824923546079232/B9b_Yg7n_400x400.jpg" width="48px"/>
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Vrije_Universiteit_Brussel_logo.svg/1200px-Vrije_Universiteit_Brussel_logo.svg.png" alt="vub" width="120px"/>
</p>

## :wrench: About the b2btools
The b2btools are a set of in-house developed biophysical predictors that enable the exploration of the 'biophysical variation' of proteins along its sequence. The predictions reflect 'emerging' properties, so what the sequence is capable of, not necessarily what it will do in a particular context, for example when it adopts a specific fold. Studying the biophysical properties of a protein is relevant as these properties, like the dynamics of a protein, are conserved by evolution in order to preserve the protein's function.

The biophysical features that can be studied by the b2btools are the following:
- Backbone and sidechain dynamics (DynaMine)
- Conformational propensities (sheet, helix, coil, polyproline II) (DynaMine)
- Early folding propensities (EFoldMine)
- Disorder propensities (DisoMine)
- Beta aggregation propensity (AgMata)
- Phase seperation propensity (PPser)

*For a detailed description of the predictors, please refer to the citations stated at the end of this page. An implementation of the b2btools into an analysis is also available in that section.*

Both a single sequence and a Multiple Sequence Alignment (MSA) can be used as input of the b2btools. Jupyter Notebooks to illustrate the functionalities of the b2btools are available below.

## 📚 List of available notebooks

### Single Sequence analysis

- 📓 Prediction of the biophysical features of a single sequence and visualization of the predicted values on 2D plots and on the 3D structures/models of the corresponding sequence: `Bio2ByteTools_v3_singleseq_pypi.ipynb`
[⏯️ Open Jupyter Notebook on Google Colab](https://colab.research.google.com/github/Bio2Byte/public_notebooks/blob/main/Bio2ByteTools_v3.0.5_SingleSequence_demo.ipynb)

- 📓 Comparison between the predicted biophysical features of a single sequence and the pLDDT values of the AlphaFold model of that sequence:  `AlphaFold_+_B2B_Tools.ipynb`
[⏯️ Open Jupyter Notebook on Google Colab](https://colab.research.google.com/github/Bio2Byte/public_notebooks/blob/main/Bio2Byte_AlphaFold_Analysis.ipynb)


### Multiple Sequence Alignment (MSA) analysis
Prediction of the biophysical features of a MSA, computation of the MSA biophysical and sequence conservation and 2D visualization of these values. This analysis can be done:

- 📓In function of a protein's behavior [⏯️ Open Jupyter Notebook on Google Colab](https://colab.research.google.com/github/Bio2Byte/public_notebooks/blob/main/B2B_Tools_Single_sequence_Example.ipynb)
- 📓For the overall behavior of the MSA [⏯️ Open Jupyter Notebook on Google Colab](https://colab.research.google.com/github/Bio2Byte/public_notebooks/blob/main/Bio2ByteTools_v3_multipleseq_pypi.ipynb)

## 📃 How to use them?
1. Open the Jupyter notebook file of interest
2. There will be a "Open In Colab" button, if you click on it, a new session on Google Colab will be started
3. From the Google Colab session you will be able to run the code of the notebook.

## :package: PyPi Repository

Want to try out the b2btools? Download the Bio2Byte's tools package from our PyPi repository: [Bio2Byte tools package](https://pypi.org/project/b2bTools/).

## About Bio2Byte

Proteins are the molecular machines that make cells work. They perform a wide variety of functions through interactions with each other and many additional molecules. Traditionally, proteins are described in a single static state (a picture). It is now increasingly recognised that many proteins can adopt multiple states and move between these conformational states dynamically (a movie).

We investigate how the dynamics, conformational states and available experimental data of proteins relates to their amino acid sequence. Underlying physical and chemical principles are computationally unravelled through data integration, analysis and machine learning, so connecting them to biological events and improving our understanding of the way proteins work.

The Bio2Byte group is primarily situated at the Interuniversity Institute of Bioinformatics in Brussels, a collaborative interfaculty institute between the Vrije Universiteit Brussel and the Université Libre de Bruxelles. It is located at the the ULB side of the Pleinlaan/La Plaine campus on the 6th floor of the C building.

At the VUB, the group is linked to Structural Biology Brussels at the Bioengineering sciences department, as well as the departments of Computer Science and Chemistry at the Faculty of Sciences, plus to the Biomedical sciences at the Faculty of Medicine and Pharmacy.

## 🔗 Links

- [Bio2Byte](https://bio2byte.be)
- [Bio2Byte online predictors](https://bio2byte.be/b2btools)
- [Feedback or Questions](https://www.bio2byte.be/b2btools/feedback)
- [Bio2Byte tools package](https://pypi.org/project/b2bTools/)

## :book: Citations

- Implementation of the b2btools to study the protein biophysical features and their conservation:
> Kagami, L. P., Orlando, G., Raimondi, D., Ancien, F., Dixit, B., Gavaldá-García, J., Ramasamy, P., Roca-Martínez, J., Tzavella, K., & Vranken, W. (2021). b2bTools: Online predictions for protein biophysical features and their conservation. Nucleic Acids Research, 49(W1), W52–W59. https://doi.org/10.1093/nar/gkab425

- DynaMine:
> Cilia, E., Pancsa, R., Tompa, P., Lenaerts, T., & Vranken, W. F. (2013). From protein sequence to dynamics and disorder with DynaMine. Nature Communications, 4(1), 2741–2741. https://doi.org/10.1038/ncomms3741

- EFoldMine:
> Raimondi, D., Orlando, G., Pancsa, R., Khan, T., & Vranken, W. F. (2017). Exploring the Sequence-based Prediction of Folding Initiation Sites in Proteins. Scientific Reports, 7(1), 8826–8826. https://doi.org/10.1038/s41598-017-08366-3

- Disomine:
> Orlando, G., Raimondi, D., Codicè, F., Tabaro, F., & Vranken, W. (2022). Prediction of Disordered Regions in Proteins with Recurrent Neural Networks and Protein Dynamics. Journal of Molecular Biology, 434(12), 167579. https://doi.org/10.1016/j.jmb.2022.167579

- AgMata:
> Orlando, G., Silva, A., Macedo-Ribeiro, S., Raimondi, D., & Vranken, W. (2020). Accurate prediction of protein beta-aggregation with generalized statistical potentials. Bioinformatics, 36(7), 2076–2081. https://doi.org/10.1093/bioinformatics/btz912

- PSPer:
> Orlando, G., Raimondi, D., Tabaro, F., Codicè, F., Moreau, Y., & Vranken, W. F. (2019). Computational identification of prion-like RNA-binding proteins that form liquid phase-separated condensates. Bioinformatics, 35(22), 4617–4623. https://doi.org/10.1093/bioinformatics/btz274

## Copyright

© Wim Vranken, Bio2Byte group, VUB
