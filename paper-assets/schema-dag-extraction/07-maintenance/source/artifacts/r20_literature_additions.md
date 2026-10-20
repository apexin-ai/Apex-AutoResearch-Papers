# R20 Literature Additions

## MR1: Dubey et al. (2018)

### BibTeX
```bibtex
@inproceedings{dubey-2018-pairwise-confusion,
  author    = {Abhimanyu Dubey and Otkrist Gupta and Pei Guo and Ramesh Raskar and Ryan Farrell and Nikhil Naik},
  title     = {Pairwise Confusion for Fine-Grained Visual Classification},
  booktitle = {Proceedings of the European Conference on Computer Vision (ECCV)},
  pages     = {71--88},
  year      = {2018}
}
```

### Suggested citation text
In visual recognition, pairwise confusion between classes has been explicitly modeled to improve fine-grained classification \citep{dubey-2018-pairwise-confusion}, where a regularization objective encourages the learned features to reduce inter-class confusability. Our Schema Confusability Score (SCS) brings a similar pairwise confusability quantification to NLP information extraction, measuring how likely an LLM is to confuse one relation (or event) type with another under structured decoding.


## MR2: Collier et al. (2021)

> **注意**: 用户指定的标题 "Exploiting Class Similarity for Machine Learning with Confidence Labels" 实际作者是 Gare & Galeotti (arXiv 2021)，不是 Collier。Collier et al. 2021 的论文是 "Correlated Input-Dependent Label Noise in Large-Scale Image Classification" (CVPR 2021)，主题也涉及 class similarity（通过 label noise correlation 建模类间相似性）。两篇均列出，请确认需要哪篇。

### Option A: Gare & Galeotti (2021) — 匹配用户给的标题
```bibtex
@article{gare-2021-class-similarity,
  author    = {Gautam Rajendrakumar Gare and John Michael Galeotti},
  title     = {Exploiting Class Similarity for Machine Learning with Confidence Labels and Projective Loss Functions},
  journal   = {arXiv preprint arXiv:2103.13607},
  year      = {2021}
}
```

#### Suggested citation text (Option A)
\citet{gare-2021-class-similarity} introduce confidence labels that encode pairwise class similarity and propose projective loss functions that relax penalties for confusions between similar classes, showing that explicitly modeling inter-class confusability improves robustness to label noise.

### Option B: Collier et al. (2021) — 匹配用户给的作者名
```bibtex
@inproceedings{collier-2021-correlated-noise,
  author    = {Mark Collier and Basil Mustafa and Efi Kokiopoulou and Rodolphe Jenatton and Jesse Berent},
  title     = {Correlated Input-Dependent Label Noise in Large-Scale Image Classification},
  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
  pages     = {1551--1560},
  year      = {2021}
}
```

#### Suggested citation text (Option B)
\citet{collier-2021-correlated-noise} model label noise as input-dependent and correlated across semantically similar classes, demonstrating that the learned covariance structure captures known inter-class confusability patterns in large-scale classification.


## MR3: LLM calibration × constrained decoding

### BibTeX
```bibtex
@inproceedings{park-2024-grammar-aligned,
  author    = {Kanghee Park and Jiayu Wang and Taylor Berg-Kirkpatrick and Nadia Polikarpova and Loris D'Antoni},
  title     = {Grammar-Aligned Decoding},
  booktitle = {Advances in Neural Information Processing Systems 37 (NeurIPS)},
  year      = {2024}
}
```

### Suggested citation text
Constrained decoding techniques that restrict LLM outputs to valid grammars (e.g., JSON schemas) can distort the model's original probability distribution, producing outputs whose likelihoods are no longer proportional to the unconstrained distribution \citep{park-2024-grammar-aligned}. This distribution distortion is directly relevant to our setting, where structured extraction under schema constraints may alter the model's calibration and confusability patterns across relation types.
