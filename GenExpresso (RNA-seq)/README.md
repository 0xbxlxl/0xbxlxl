# GenExpresso

----
## Description

**GenExpresso** is an interactive Python-based platform designed to analyze RNA-Seq data for gene expression and mutation studies. Our project aims to bridge bioinformatics insights with user-friendly functionality, providing researchers with tools to explore gene expression patterns, identify biomarkers, and personalize medicine recommendations.

**Why GenExpresso?**

With the increasing availability of RNA-Seq data, the need for accessible, integrative tools is greater than ever. We chose this project to simplify data processing and visualization for researchers, particularly in personalized medicine, by offering a centralized platform for data analysis and biomarker discovery.

**Goals**

- Provide tools to upload RNA sequences in FASTA format.
- Enable gene expression and mutation analysis.
- Offer interactive visualizations (e.g., PCA plots, heatmaps, pathway graphs) with user control.
- Offer a user-friendly interface for interaction.
- Facilitate the discovery of potential biomarkers.

----
## Functionalities

**1. Data Sources and Retrieval**

- GenExpresson will support RNA-Seq datasets from public repositories (e.g., [GEO](https://www.ncbi.nlm.nih.gov/geo/)) and user uploads.
- Support for sequence data in FASTA format and pre-processed RNA-Seq count files.
- Data cleaning and quality control will be adressed to tackle incomplete or inconsistent datasets

**2. Data Storage and Handling**

- Data will be stored using SQLite for local analysis, with optional cloud integration for scalability.
- Libraries like pandas and numpy for data handling, and sqlalchemy for database interaction.
  
**3. User Management**

- Secure storage of user credentials with hashed passwords.
- A pre-defined database for managing multiple user roles, including admin (admin as in team leader) for creating and deleting accounts, and grant user permission.
- Users and other team members can register new accounts via an email verfication system.
- Logout will include a thank you-message and an auto-logout timeout.

**4. Interface**

- Desktop-based GUI using Tkinter, allowing users to:
    - Upload RNA-Seq data easily.
    - Select analysis types (e.g., normalization or clustering) via menus.
    - View and interact with real-time visualizations.
    - Download basic dataset statistics
    
**5. Statistical Analysis**

- Perform normalization (TPM, RPKM, FPKM) and differential expression analysis
- Tools: statsmodels, scipy, and numpy.
- Advanced clustering (K-means, hierarchical) and pathway enrichment analysis.
  
**6. Visualization**
- Interactive plot and graphs:
    - PCA plots for dimensionality reduction.
    - Heatmaps of gene expression.
    - Network graphs of gene ontology and pathways.
- Libraries: matplotlib, seaborn, plotly, and networkx.
- Visualization features will include user interaction (e.g., zoom, hover-over data points) for greater clarity and usability.



----
## Installation and Usage

To be decided.

----
## Timeline

**Week 1-2:** Finalize project goals and collect datasets, and data cleaning and quality control

**Week 3-4:** Develop backend for data processing (storage, retrieval, statistical analysis) and user management system (login/logout and admin functions)

**Week 5-6:** Build the GUI (data upload analysis selection, and visualization display features)

**Week 7:** Perform testing and debugging

**Week 8:** Finalize and present the project


----
## Group Details

- **Group name:** Hello World
- **Group code:** G07
- **Group repository:** 
- **Tutor responsible:** Corina Elena Wegner
- **Group team leader:** Natasha Machate
- **Group members:** Natasha Machate, Aysu Barut, Bilal Kachir, Sankalpa Acharya

Coming soon:
Include also the (detailed) contribution of each group member to the development of the project.

Example:
**Member A**: Developed the data structure of the project. Helped _Member B_ on the web interface and user management. Refactoring on components X, Y, and Z. Responsible for the unit tests in P ant T.

----
## Acknowlegdments

- Data from [GEO](https://www.ncbi.nlm.nih.gov/geo/).
- Libraries: pandas, numpy, matplotlib, scipy, Flask.
- Group name inspired by Sabrina Carpenter
