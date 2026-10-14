<div align="center">

  <!-- Header Banner -->
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=10,15,20&height=220&section=header&text=Bilal%20Kachir&fontSize=52&fontColor=ffffff&animation=fadeIn&subtext=Computational%20Biologist%20%7C%20Biomedical%20ML%20Researcher&subfontSize=20&subfontColor=d1d5db" width="100%" />

  <p align="center">
    <strong>MSc Bioinformatics & Computational Biology</strong> @ <a href="https://www.uni-goettingen.de/">Georg-August-Universität Göttingen</a> 🇩🇪<br/>
    BSc Biology (Minor in Bioinformatics) @ University of Detroit Mercy 🇺🇸
  </p>

  <p align="center">
    <a href="https://linkedin.com/in/bilal-kachir-b7729b269"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
    <a href="mailto:Bilalkachir00@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=flat-square&logo=gmail&logoColor=white" alt="Email"/></a>
    <a href="https://github.com/0xbxlxl"><img src="https://img.shields.io/badge/GitHub-0xbxlxl-181717?style=flat-square&logo=github&logoColor=white" alt="GitHub"/></a>
  </p>

  <p align="center">
    🎯 <em>MSc Thesis Submission: February 2027 • Available for PhD & Industry Roles: March 2027</em>
  </p>

</div>

---

### 🧬 About Me

I am a computational biologist and biomedical machine learning researcher based in Göttingen, Germany. My work bridges **wet-lab biological training** with **single-cell transcriptomics, graph machine learning, and reproducible scientific computing**.

Currently, I am completing my Master’s thesis (**MetaBridge-GCN**) at the Department of Medical Bioinformatics, University of Göttingen, focusing on:
- **Large-Scale Metacell Aggregation**: Transforming 754,140 single cells into 25,161 cell-line-stratified metacells across 49 cancer cell lines using `SEACells`, `Scanpy`, and parallel Linux workflows.
- **Graph-Based Domain Adaptation**: Building custom sparse `GCN` and `GraphSAGE` encoders in `PyTorch` over a shared 9,317-gene `STRING v12.0` interaction network to evaluate bulk-to-metacell drug-response transfer across anticancer compounds.
- **Evaluation Rigor**: Designing leak-free validation splits, >3,000 controlled hyperparameter trials, validation-frozen decision thresholds, and matched frozen-source controls to diagnose representation compression and weak supervision limits.

---

### 🔬 Core Research & Expertise

<table>
  <tr>
    <td width="50%" valign="top">
      <h4>🧬 Single-Cell & Spatial Omics</h4>
      <ul>
        <li><strong>scRNA-seq Processing</strong>: Quality control, normalization, HVG selection, and sparse count aggregation (<code>Scanpy</code>, <code>AnnData</code>).</li>
        <li><strong>Metacell Workflows</strong>: Stratified micro-state aggregation with <code>SEACells</code> across 750k+ cells.</li>
        <li><strong>Spatial Transcriptomics</strong>: 10x Visium integration with scRNA-seq references and Digital Tissue Deconvolution.</li>
      </ul>
    </td>
    <td width="50%" valign="top">
      <h4>🧠 Biomedical ML & Optimization</h4>
      <ul>
        <li><strong>Graph Neural Networks</strong>: Custom sparse <code>GCN</code> and <code>GraphSAGE</code> architectures on biological networks in <code>PyTorch</code>.</li>
        <li><strong>Domain Adaptation</strong>: Gaussian-RBF MMD alignment, latent spread/covariance diagnostics, and matched control evaluation.</li>
        <li><strong>Simulation Optimization & RL</strong>: Bayesian Optimization (<code>BoTorch</code>), <code>CMA-ES</code>, and Soft Actor-Critic (<code>SAC</code>) in <code>PyTorch</code>.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h4>🧪 Transcriptomics & Wet-Lab Literacy</h4>
      <ul>
        <li><strong>Bulk RNA-seq</strong>: Differential expression workflows and cross-drug comparisons (<code>DESeq2</code>, <code>limma</code>, <code>edgeR</code>).</li>
        <li><strong>Upstream & Functional Analysis</strong>: Read QC (<code>FastQC</code>), adapter trimming, <code>Galaxy</code> pipelines, and pathway enrichment (<code>GO</code>, <code>KEGG</code>, <code>biomaRt</code>).</li>
        <li><strong>Bench Foundation</strong>: Hands-on experience in RNA isolation, cDNA/qPCR, cell culture, and confocal microscopy.</li>
      </ul>
    </td>
    <td width="50%" valign="top">
      <h4>⚡ Scientific Computing & Engineering</h4>
      <ul>
        <li><strong>Parallel Linux Workflows</strong>: Multi-GPU experiment automation and parallel job orchestration (<code>Bash</code>, <code>xargs</code>, rootless <code>Docker</code>).</li>
        <li><strong>Sparse Data Engineering</strong>: High-efficiency CSR matrix manipulation, gene-order harmonization, and cross-domain preprocessing audits.</li>
        <li><strong>Reproducibility</strong>: Deterministic checkpointing, input/code hash provenance, and multi-seed validation sweeps.</li>
      </ul>
    </td>
  </tr>
</table>

---

### 📂 Selected Research & Projects

- **MetaBridge-GCN (MSc Thesis, Univ. of Göttingen)** — Two-stage graph domain-adaptation pipeline in `PyTorch` transferring bulk drug-sensitivity models (`GDSC2`) to 25,161 `SEACells` metacells (`Tahoe`) over a 9,317-gene `STRING v12.0` network.
- **[Exploratory Spatial Transcriptomics](https://github.com/0xbxlxl/spatiotrans_internship) (Systems Biology Internship, Univ. of Göttingen)** — Python deconvolution workflow integrating human intestine 10x Visium data with a single-cell gut atlas (`E-MTAB-9543`) via Digital Tissue Deconvolution and preranked `KEGG` GSEA.
- **Photoacoustic Simulation Optimization (QMILab, European Neuroscience Institute Göttingen)** — Optimization and reinforcement-learning framework (`BoTorch`, `CMA-ES`, `Nelder-Mead`, and `SAC`) wrapping the `SIMPA` simulator for 6D two-laser parameter recovery.
- **Systemic Sclerosis Fibroblast Transcriptomics (Varga Lab, Univ. of Michigan)** — Differential expression (`DESeq2`, `limma`), PCA/UMAP, and pathway analysis of human fibroblast RNA-seq datasets combined with wet-lab qPCR and microscopy workflows.

---

### 🛠 Tech Stack & Tools

<p align="center">
  <!-- Core Languages -->
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/R-276DC3?style=for-the-badge&logo=r&logoColor=white" alt="R"/>
  <img src="https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnu-bash&logoColor=white" alt="Bash"/>
  <br/>
  <!-- ML & Scientific Computing -->
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white" alt="PyTorch"/>
  <img src="https://img.shields.io/badge/BoTorch-EC4E20?style=for-the-badge&logo=pytorch&logoColor=white" alt="BoTorch"/>
  <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Scikit-Learn"/>
  <img src="https://img.shields.io/badge/SciPy-8CAAE6?style=for-the-badge&logo=scipy&logoColor=white" alt="SciPy"/>
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy"/>
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas"/>
  <br/>
  <!-- Bioinformatics & Genomics -->
  <img src="https://img.shields.io/badge/Scanpy-AnnData-009688?style=for-the-badge&logo=dna&logoColor=white" alt="Scanpy"/>
  <img src="https://img.shields.io/badge/Single--Cell-SEACells-3F51B5?style=for-the-badge" alt="SEACells"/>
  <img src="https://img.shields.io/badge/Bioconductor-DESeq2_%7C_limma-108040?style=for-the-badge" alt="Bioconductor"/>
  <img src="https://img.shields.io/badge/STRING_v12.0-Network_Biology-8E24AA?style=for-the-badge" alt="STRING"/>
  <br/>
  <!-- Environments & Visualization -->
  <img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black" alt="Linux"/>
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker"/>
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git"/>
  <img src="https://img.shields.io/badge/ggplot2-Matplotlib-276DC3?style=for-the-badge" alt="Visualization"/>
</p>

---

<div align="center">
  <sub>🌍 Academic & research background across Lebanon, the United States, and Germany • Languages: English (Fluent), Arabic (Native), French (Reading/Listening), German (A2)</sub><br/><br/>
  <sub>Open to PhD and industry opportunities in Computational Biology, Single-Cell Omics, and Biomedical ML — reach out via <a href="mailto:Bilalkachir00@gmail.com">Email</a> or <a href="https://linkedin.com/in/bilal-kachir-b7729b269">LinkedIn</a>.</sub>
</div>
