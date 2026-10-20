# Data

## ScienceWorld v1.2.3

Interactive text-based science simulation environment.

- **License**: Apache 2.0
- **Install**: `pip install scienceworld==1.2.3`
- **Reference**: https://github.com/allenai/ScienceWorld
- **Requirement**: Java JDK 11+

The environment is accessed programmatically via the `scienceworld` Python package. No separate data download is needed; the package includes all task definitions and variations.

## ALFWorld

Interactive household task environment built on TextWorld.

- **License**: MIT
- **Install**: `pip install alfworld`
- **Reference**: https://github.com/alfworld/alfworld
- **Data**: Game files are included in the alfworld package (`json_2.1.1` split).

## MATH Dataset

Competition mathematics problems (Levels 4-5 used in this work).

- **License**: MIT
- **Reference**: https://github.com/hendrycks/math
- **Download**: Available via HuggingFace Datasets (`hendrycks/competition_math`) or the original repository.

Only Level 4-5 problems are used for the counterfactual analysis to ensure sufficient difficulty for meaningful internal vs. code-interpreter divergence.
