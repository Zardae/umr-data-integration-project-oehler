# Data Integration Project 

This repository serves as template for the students project accompanying the
"Data Integration" lecture at University of Marburg.

Students can
[fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) or copy
this repository to kick-start their project.

## Structure

This data integration project has four components: preparation, data
integration, data cleaning, and showcase.

- `0_datasets`: We recommend to read and write source, intermediate, and final datasets from `0_datasets` directory. Its content is gitignored (i.e., it will not be tracked by Git), use [Hessenbox](https://hessenbox.uni-marburg.de) to sync-and-share your datasets.
- `1_preparation`: Code to extract and load your datasets into a common space
  (e.g., sqlite or Jupyter notebook). You might also want to write code to explore the
datasets.
- `2_integration`: Experiments to integrate your datasets and a program that
  implements your final integration pipeline.
- `3_cleaning`: Experiments to clean your integrated dataset and a program that
  implements your final data cleaning pipeline.
- `3_showcase`: Code to implement your showcase. You can already run it against
  the results of your data integration pipeline, and, finally, against your
integrated and cleaned data.

## Documentation

- Preparation
  - `scrape-walkthrough`: Used to scrape all relevant (and some less relevant) location information off Serebii.net (49 html sites)
- Integration
  - `prepare_integrated_db`: Used to prepare the integrated database
  - `html_processing`: Used to extract useful data from the scraped html files and transfer it into the integrated database
  - `pbs_processing`: Used to transfer the data from the pbs (txt) files extracted from the Pokémon Essentials into the integrated database
  - `main_integration`: Integration brought together in one file
	
