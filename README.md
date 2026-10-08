# Integrative Machine Learning and Network Biology Analysis Reveals Molecular Links Between Post-Traumatic Stress Disorder and Depression

This repository contains the analysis scripts, processed data, and supplementary resources used in the study:

**"Integrative Machine Learning and Network Biology Analysis Reveals Molecular Links Between Post-Traumatic Stress Disorder and Depression"**

The study combines transcriptomic analysis, machine learning–based feature selection, network biology, and exploratory molecular docking to identify genes shared between post-traumatic stress disorder (PTSD) and major depressive disorder (MDD), and to assess how well these genes transfer to independent cohorts.

---

## Data Sources

Gene expression datasets were obtained from the NCBI Gene Expression Omnibus (GEO).

**Discovery cohorts**

- GSE98793 (GPL570) – MDD cases and healthy controls (128 / 64)
- GSE63878 (GPL6244) – PTSD cases and controls in trauma-exposed U.S. Marines (48 / 48)

**Independent validation cohorts**

- GSE32280 (GPL570) – MDD (peripheral blood lymphocytes); subsyndromal depression samples excluded
- GSE39653 (GPL10558) – MDD (PBMCs); bipolar disorder samples excluded
- GSE54566 (GPL570) – MDD (postmortem brain; exploratory cross-tissue analysis)
- GSE67663 (GPL6884) – comorbid PTSD and depression (brain tissue)

Protein structures were obtained from the RCSB Protein Data Bank, and compound structures from PubChem. 
---

## Analysis Workflow

1. **Data preprocessing**
   - Downloading GEO datasets
   - Each dataset processed on its own platform; ComBat used only for exploratory visualization of platform effects

2. **Differential Gene Expression Analysis**
   - DEGs identified separately in each dataset with limma (Benjamini–Hochberg adjusted p-value)

3. **Feature Selection**
   - Fisher Score ranking within each dataset
   - Selection of the top 800 genes per dataset
   - Cut-off stability and bootstrap analyses 

4. **Common DEG Identification**
   - Intersection of the two top-ranked lists (19 shared genes)
   - Log2 fold change, p-value, Fisher-score rank and direction of change reported for every shared gene

5. **Protein–Protein Interaction (PPI) Network**
   - Construction in NetworkAnalyst using STRING; the network is expanded by one interaction degree from the seed genes
   - Visualization and analysis in Cytoscape

6. **Hub Gene Identification**
   - Degree-based ranking with the CytoHubba plugin
   - Seed genes (IGF1R, STAT2, HGF, PML) distinguished from STRING-derived interactors

7. **Functional Enrichment Analysis**
   - Over-representation analysis (hypergeometric test, Benjamini–Hochberg FDR) for the shared DEGs and the hub genes
   - Gene universe: 16,911 genes measured on both platforms
   - Libraries: GO (Biological Process, Molecular Function, Cellular Component), KEGG, WikiPathways; Reactome, BioCarta and BioPlanet as supplementary libraries

8. **Weighted Gene Co-expression Network Analysis (WGCNA)**
   - Reference network: GSE98793; test network: GSE63878
   - Module detection from the full gene-level matrices (5,017 genes)
   - Module preservation (200 permutations), module–disease association, and robustness analyses

9. **External Validation of the Hub-Gene Signature**
   - Logistic-regression models trained only in the discovery cohorts and frozen before validation
   - Applied unchanged to the independent cohorts
   - Within-cohort nested cross-validation reported separately as internal performance

10. **Regulatory Network Analysis**
    - Transcription factor (TF)–gene interactions (JASPAR)
    - miRNA–gene interactions (miRTarBase)
    - TF–miRNA co-regulatory networks (RegNetwork)

11. **Molecular Docking Analysis (exploratory)**
    - Candidate compound prioritization (DSigDB drug–gene enrichment and published evidence)
    - Docking with AutoDock Vina and visualization in PyMOL
    - Docking results are exploratory; the grid placement was not validated by redocking

---

## Key Findings

- **19 shared genes** were identified between the MDD and PTSD top-ranked lists. Eight changed in the same direction in both disorders and eleven in opposite directions. The overlap was sensitive to the significance threshold and did not exceed chance expectation.

- **10 hub genes** were identified by degree centrality:

  IGF1R, STAT2, PML, HGF, HDAC1, JAK2, JAK1, MDM2, ERBB2, STAT3

  Four of them (IGF1R, STAT2, HGF, PML) were seed genes with direct expression-level support; the other six were introduced through STRING network expansion.

- **Functional enrichment** of the shared DEGs was limited, with a few significant growth-factor, cancer-related and type I interferon pathways (FDR < 0.05). The hub genes were enriched in cytokine and JAK–STAT-related pathways, which partly reflects how the network was built.

- **WGCNA** showed partly preserved co-expression structure between the two cohorts, but no module was associated with MDD or PTSD.

- **Frozen-model validation** showed limited transferability of the hub-gene signature to independent cohorts (pooled AUC ≈ 0.55), so the genes are presented as mechanistic candidates rather than validated diagnostic markers.

- **Molecular docking** was used as an exploratory screen of natural compounds, including 3-acetylursolic acid, against the hub proteins. None of the compounds is an approved drug, and the results are not evidence of therapeutic viability.

---

## Software and Tools

**Programming environments**

- R (v[ ])
- Python (v[ ])

**R packages**

- limma (v[ ])
- GEOquery (v[ ])
- sva (v[ ]) – ComBat visualization
- WGCNA (v[ ])

**Python packages**

- scikit-learn (v[ ]), pandas (v[ ]), NumPy (v[ ]), SciPy (v[ ]), Matplotlib (v[ ])

**Network analysis and visualization**

- NetworkAnalyst 3.0
- STRING database
- Cytoscape (v3.10.3) with the CytoHubba and NetworkAnalyzer plugins

**Functional enrichment**

- Enrichr libraries: GO Biological Process 2025, GO Molecular Function 2025, GO Cellular Component 2025, KEGG 2021 Human, WikiPathways 2024 Human, Reactome Pathways 2024, BioCarta 2016, BioPlanet 2019, DSigDB
- Tool used for the hypergeometric test: [ ]

**Regulatory networks**

- JASPAR database
- RegNetwork
- miRTarBase (v9.0)

**Molecular docking**

- AutoDockTools (v1.5.7)
- AutoDock Vina (v[ ])
- PyMOL (v[ ])

---

## Repository Structure
Analysis scripts/ R and Python scripts for the analysis
Molecular-docking/ docking inputs (receptor, ligand, config) and results
Processed data/ processed datasets and DEG tables
Result_Analysis/Result_Figures/ analysis outputs and figures
supplementary/ supplementary tables used in the manuscript
README.md
Requirements.txt
---

## Reproducibility

All scripts and processed datasets required to reproduce the analyses presented in the manuscript are provided in this repository. Run the scripts in `Analysis scripts/` sequentially, followed by the code in `Validation/` and `WGCNA/`. A fixed random seed (42) was used for cross-validation and bootstrap analyses. Python dependencies are listed in `Requirements.txt`, and the R session information is provided in `WGCNA/sessionInfo.txt`.

---
