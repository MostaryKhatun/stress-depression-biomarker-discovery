# Network Biology and Gene Expression Profiling Identify Key Biomarkers Underlying the Molecular link Between Stress and Depression: Bioinformatics and Machine Learning Approach

This repository contains the analysis scripts, processed data, and supplementary resources used in the study:

**“Network Biology and Gene Expression Profiling Identify Key Biomarkers Underlying the Molecular link Between Stress and Depression: Bioinformatics and Machine Learning Approach”**

The study integrates transcriptomic analysis, machine learning–based feature selection, network biology, and molecular docking to identify shared biomarkers and potential therapeutic targets associated with stress and depression.

---

## Data Sources

Gene expression datasets were obtained from the NCBI Gene Expression Omnibus (GEO):

- GSE98793 – Major depressive disorder transcriptomic dataset  
- GSE63878 – Stress-related gene expression dataset  

These datasets were used for differential gene expression analysis and downstream integrative analysis.

---

## Analysis Workflow

The computational workflow of this study consists of the following steps:

1. **Data preprocessing**
   - Downloading GEO datasets
   - Normalization and batch effect correction

2. **Differential Gene Expression Analysis**
   - Identification of DEGs using the limma package

3. **Feature Selection**
   - Fisher Score ranking
   - Selection of top-ranked genes

4. **Common DEG Identification**
   - Intersection analysis between stress and depression datasets

5. **Protein–Protein Interaction (PPI) Network**
   - Construction using STRING database
   - Visualization and analysis in Cytoscape

6. **Hub Gene Identification**
   - Topological analysis using the CytoHubba plugin

7. **Functional Enrichment Analysis**
   - Gene Ontology (GO)
   - KEGG pathway analysis
   - WikiPathways analysis

8. **Weighted Gene Co-expression Network Analysis (WGCNA)**
   - Construction of gene co-expression modules
   - Identification of modules associated with hub genes

9. **Regulatory Network Analysis**
   - Transcription factor (TF)–gene interactions (JASPAR)
   - miRNA–gene interactions (miRTarBase)
   - TF–miRNA co-regulatory networks

10. **Molecular Docking Analysis**
   - Screening of candidate compounds
   - Docking simulation using AutoDock Vina
   - Structural visualization using PyMOL

---

## Key Findings

- Identification of **19 shared differentially expressed genes (DEGs)** between stress and depression datasets.
- Detection of **10 hub genes**:
  
  IGF1R, STAT2, PML, HGF, HDAC1, JAK2, JAK1, MDM2, ERBB2, STAT3

- Functional enrichment analysis revealed significant involvement in:
  - JAK–STAT signaling pathway
  - Cytokine–cytokine receptor interaction
  - Immune and inflammatory signaling
  - Neuroactive ligand–receptor interaction

- Molecular docking analysis identified **3-acetylursolic acid** as a potential candidate compound interacting with multiple hub proteins.

---

## Software and Tools

The following computational tools were used in this study:

- R (v4.2.2)
- limma
- WGCNA (v1.72-1)
- NetworkAnalyst 3.0
- STRING database
- Cytoscape (v3.10.3)
- CytoHubba plugin
- Gene Ontology (GO)
- KEGG database
- WikiPathways
- JASPAR database
- miRTarBase
- PyMOL (v3.1.3.1)
- AutoDock Vina

---

## Repository Structure

Analysis scripts/
R scripts for analysis

Figures/
analysis outputs results and figures

Molecular-docking/
molecular docking results

Processed data/
processed datasets and DEG tables

supplementary/
supplementary tables used in the manuscript

README.md

Requirements.txt

## Reproducibility

All scripts and processed datasets required to reproduce the analyses presented in the manuscript are provided in this repository. The workflow can be reproduced by running the scripts sequentially in the `Analysis scripts/` directory.

---
