# Literature Gap Search Results

Search date: 2026-05-14
Context: exp-004 found high-AUC gamma underestimation (-0.016) due to exposure-ability collinearity causing posterior variance inflation. Need theoretical anchors for Discussion.

---

## Gap 1 (P0): Exposure-ability collinearity / confounding in IRT

### San Martin, Gonzalez & Tuerlinckx (2015)
- **Citation:** San Martin, E., Gonzalez, J., & Tuerlinckx, F. (2015). On the unidentifiability of the fixed-effects 3PL model. *Psychometrika*, 80(2), 450-467.
- **Relevance to ContamCal:** Establishes formal unidentifiability results for fixed-effects IRT models with guessing parameters. Our 4PL-based contamination model inherits these identifiability challenges; when exposure acts as a quasi-covariate correlated with ability, parameter confounding is amplified. Provides theoretical grounding for why gamma is underestimated under high collinearity.

```bibtex
@article{sanmartin2015,
  author  = {San Mart\'{i}n, Ernesto and Gonz\'{a}lez, Jorge and Tuerlinckx, Francis},
  title   = {On the Unidentifiability of the Fixed-Effects {3PL} Model},
  journal = {Psychometrika},
  volume  = {80},
  number  = {2},
  pages   = {450--467},
  year    = {2015},
  doi     = {10.1007/s11336-014-9404-2}
}
```

### Mislevy (1987)
- **Citation:** Mislevy, R. J. (1987). Exploiting auxiliary information about examinees in the estimation of item parameters. *Applied Psychological Measurement*, 11(1), 81-91.
- **Relevance to ContamCal:** Shows that person-level covariate information can improve IRT estimation precision equivalent to adding 2-6 items, but only when covariates are not collinear with ability. In our setting, contamination exposure is correlated with ability by design (high-AUC items discriminate), creating the exact condition where auxiliary information becomes confounded rather than helpful.

```bibtex
@article{mislevy1987,
  author  = {Mislevy, Robert J.},
  title   = {Exploiting Auxiliary Information About Examinees in the Estimation of Item Parameters},
  journal = {Applied Psychological Measurement},
  volume  = {11},
  number  = {1},
  pages   = {81--91},
  year    = {1987},
  doi     = {10.1177/014662168701100106}
}
```

### Wainer, Bradlow & Wang (2007)
- **Citation:** Wainer, H., Bradlow, E. T., & Wang, X. (2007). *Testlet response theory and its applications*. Cambridge University Press.
- **Relevance to ContamCal:** Documents how ignoring local item dependence (analogous to item-group contamination effects) inflates parameter correlations and biases difficulty/discrimination estimates. The testlet-induced dependency structure parallels how contamination exposure creates local dependence among affected items.

```bibtex
@book{wainer2007testlet,
  author    = {Wainer, Howard and Bradlow, Eric T. and Wang, Xiaohui},
  title     = {Testlet Response Theory and Its Applications},
  publisher = {Cambridge University Press},
  year      = {2007}
}
```

---

## Gap 2 (P0): Measurement error attenuation bias

### Carroll, Ruppert, Stefanski & Crainiceanu (2006)
- **Citation:** Carroll, R. J., Ruppert, D., Stefanski, L. A., & Crainiceanu, C. M. (2006). *Measurement error in nonlinear models: A modern perspective* (2nd ed.). Chapman & Hall/CRC.
- **Relevance to ContamCal:** Definitive reference on measurement error in nonlinear models. Our gamma parameter is estimated in a model where ability (theta) enters nonlinearly; measurement error in theta attenuates gamma toward zero. Chapter 2 provides the theoretical framework for understanding why naive regression on estimated abilities produces attenuated contamination effect estimates.

```bibtex
@book{carroll2006,
  author    = {Carroll, Raymond J. and Ruppert, David and Stefanski, Leonard A. and Crainiceanu, Ciprian M.},
  title     = {Measurement Error in Nonlinear Models: A Modern Perspective},
  edition   = {2nd},
  publisher = {Chapman \& Hall/CRC},
  year      = {2006},
  isbn      = {9781584886334}
}
```

### Fuller (1987)
- **Citation:** Fuller, W. A. (1987). *Measurement error models*. Wiley.
- **Relevance to ContamCal:** Classic treatment of errors-in-variables regression. Establishes that when a regressor is measured with error, the OLS slope is attenuated by the reliability ratio lambda = var(true)/var(observed). Provides the foundational result that our gamma underestimation mechanism generalizes from.

```bibtex
@book{fuller1987,
  author    = {Fuller, Wayne A.},
  title     = {Measurement Error Models},
  publisher = {Wiley},
  year      = {1987},
  series    = {Wiley Series in Probability and Statistics},
  isbn      = {9780471861874}
}
```

### Stefanski & Carroll (1985)
- **Citation:** Stefanski, L. A., & Carroll, R. J. (1985). Covariate measurement error in logistic regression. *Annals of Statistics*, 13(4), 1335-1351.
- **Relevance to ContamCal:** Proves that covariate measurement error in logistic regression (our ICC is logistic) produces asymptotic bias in parameter estimates. The naive estimator from regressing on observed (error-prone) covariates is inconsistent. Directly applicable: our contamination model uses logistic ICC where ability enters as a noisy estimate.

```bibtex
@article{stefanski1985,
  author  = {Stefanski, Leonard A. and Carroll, Raymond J.},
  title   = {Covariate Measurement Error in Logistic Regression},
  journal = {Annals of Statistics},
  volume  = {13},
  number  = {4},
  pages   = {1335--1351},
  year    = {1985},
  doi     = {10.1214/aos/1176349741}
}
```

### Battauz & Bellio (2011)
- **Citation:** Battauz, M., & Bellio, R. (2011). Structural modeling of measurement error in generalized linear models with Rasch measures as covariates. *Psychometrika*, 76(1), 40-56.
- **Relevance to ContamCal:** Directly addresses the problem of using IRT ability estimates as covariates in secondary models. Shows that ignoring heteroskedastic measurement error (which varies with true ability) biases regression coefficients. This is exactly our setting: estimated theta_hat is used to model contamination effect gamma, and its measurement error is ability-dependent.

```bibtex
@article{battauz2011,
  author  = {Battauz, Michela and Bellio, Ruggero},
  title   = {Structural Modeling of Measurement Error in Generalized Linear Models with {Rasch} Measures as Covariates},
  journal = {Psychometrika},
  volume  = {76},
  number  = {1},
  pages   = {40--56},
  year    = {2011},
  doi     = {10.1007/s11336-010-9195-z}
}
```

### Westfall & Yarkoni (2016)
- **Citation:** Westfall, J., & Yarkoni, T. (2016). Statistically controlling for confounding constructs is harder than you think. *PLoS ONE*, 11(3), e0152719.
- **Relevance to ContamCal:** Demonstrates that measurement error in confounds causes residual confounding even after statistical control, with Type I error rates approaching 100% at moderate reliability and large N. Directly relevant to our scenario: controlling for estimated ability when assessing contamination effect does not fully remove the ability confound due to measurement error in theta_hat.

```bibtex
@article{westfall2016,
  author  = {Westfall, Jacob and Yarkoni, Tal},
  title   = {Statistically Controlling for Confounding Constructs Is Harder than You Think},
  journal = {PLoS ONE},
  volume  = {11},
  number  = {3},
  pages   = {e0152719},
  year    = {2016},
  doi     = {10.1371/journal.pone.0152719}
}
```

### Jerzak & Jessee (2026)
- **Citation:** Jerzak, C. T., & Jessee, S. A. (2026). Attenuation bias with latent predictors. *arXiv preprint*, arXiv:2507.22218.
- **Relevance to ContamCal:** Shows that standard attenuation-correction methods (IV, method of composition) are themselves biased when applied to latent regressors, sometimes worse than naive regression. Estimated shifts up to 50% in coefficient magnitude. Highly relevant as our contamination effect gamma is regressed on a latent predictor (ability).

```bibtex
@article{jerzak2026,
  author  = {Jerzak, Connor T. and Jessee, Stephen A.},
  title   = {Attenuation Bias with Latent Predictors},
  journal = {arXiv preprint arXiv:2507.22218},
  year    = {2026}
}
```

---

## Gap 3 (P1): IRT power analysis / information function

### Embretson & Reise (2000)
- **Citation:** Embretson, S. E., & Reise, S. P. (2000). *Item response theory for psychologists*. Erlbaum.
- **Relevance to ContamCal:** Chapters on information functions and parameter estimation precision provide the framework for understanding when sample size and test length are sufficient to separate contamination effects from ability. Our exp-004 results on gamma estimation precision can be contextualized using IRT information theory.

```bibtex
@book{embretson2000,
  author    = {Embretson, Susan E. and Reise, Steven P.},
  title     = {Item Response Theory for Psychologists},
  publisher = {Lawrence Erlbaum Associates},
  year      = {2000},
  address   = {Mahwah, NJ}
}
```

### Thissen & Wainer (2001)
- **Citation:** Thissen, D., & Wainer, H. (Eds.). (2001). *Test scoring*. Erlbaum.
- **Relevance to ContamCal:** Comprehensive treatment of IRT-based scoring and the information function. Relevant for discussing how contaminated items contribute (or fail to contribute) information about ability and contamination effects simultaneously.

```bibtex
@book{thissen2001,
  author    = {Thissen, David and Wainer, Howard},
  title     = {Test Scoring},
  publisher = {Lawrence Erlbaum Associates},
  year      = {2001},
  address   = {Mahwah, NJ}
}
```

---

## Gap 4 (P2): 4PL identifiability

### Barton & Lord (1981)
- **Citation:** Barton, M. A., & Lord, F. M. (1981). An upper asymptote for the three-parameter logistic item-response model. *ETS Research Report Series*, 1981(1), i-8.
- **Relevance to ContamCal:** Original 4PL model paper. Showed that the upper asymptote parameter had limited impact on ability estimates in their data. ContamCal's contamination model can be seen as a constrained 4PL where the upper asymptote is structurally linked to contamination exposure, which may aid identifiability compared to the unconstrained 4PL.

```bibtex
@article{barton1981,
  author  = {Barton, Mark A. and Lord, Frederic M.},
  title   = {An Upper Asymptote for the Three-Parameter Logistic Item-Response Model},
  journal = {ETS Research Report Series},
  volume  = {1981},
  number  = {1},
  pages   = {i--8},
  year    = {1981},
  doi     = {10.1002/j.2333-8504.1981.tb01255.x}
}
```

### Culpepper (2016)
- **Citation:** Culpepper, S. A. (2016). Revisiting the 4-parameter item response model: Bayesian estimation and application. *Psychometrika*, 81(4), 1142-1163.
- **Relevance to ContamCal:** Demonstrates that Bayesian estimation with informative priors on asymptote parameters resolves 4PL identifiability issues. Our model's structural constraint (linking upper asymptote to contamination exposure) serves a similar regularizing role, which we can frame as a theory-driven alternative to Culpepper's prior-based approach.

```bibtex
@article{culpepper2016,
  author  = {Culpepper, Steven Andrew},
  title   = {Revisiting the 4-Parameter Item Response Model: {B}ayesian Estimation and Application},
  journal = {Psychometrika},
  volume  = {81},
  number  = {4},
  pages   = {1142--1163},
  year    = {2016},
  doi     = {10.1007/s11336-015-9477-6}
}
```

### Liao, Ho, Yen & Cheng (2012)
- **Citation:** Liao, W.-W., Ho, R.-G., Yen, Y.-C., & Cheng, H.-C. (2012). The four-parameter logistic item response theory model as a robust method of estimating ability despite aberrant responses. *Social Behavior and Personality*, 40(10), 1679-1694.
- **Relevance to ContamCal:** Shows 4PL improves ability estimation under aberrant response patterns (analogous to contamination-induced response distortions). Supports ContamCal's rationale of explicitly modeling upper asymptote deviations caused by contamination rather than treating them as nuisance.

```bibtex
@article{liao2012,
  author  = {Liao, Wen-Wei and Ho, Rong-Guey and Yen, Yung-Chin and Cheng, Hao-Chang},
  title   = {The Four-Parameter Logistic Item Response Theory Model As a Robust Method of Estimating Ability Despite Aberrant Responses},
  journal = {Social Behavior and Personality},
  volume  = {40},
  number  = {10},
  pages   = {1679--1694},
  year    = {2012},
  doi     = {10.2224/sbp.2012.40.10.1679}
}
```

---

## Already in references.bib (no action needed)
- De Boeck & Wilson (2004) - `deboeck2004`
- Mislevy (1986) - `mislevy1986` (different paper from the 1987 above)
- San Martin, Del Pino & De Boeck (2009) - `sanmartin2009` (different paper from the 2015 above)

## Summary: New entries to add to references.bib

| Priority | Key | Gap |
|----------|-----|-----|
| P0 | `sanmartin2015` | Collinearity/identifiability |
| P0 | `mislevy1987` | Covariate-ability confounding |
| P0 | `wainer2007testlet` | Local dependence / parameter correlation |
| P0 | `carroll2006` | Measurement error in nonlinear models |
| P0 | `fuller1987` | Errors-in-variables classic |
| P0 | `stefanski1985` | Logistic regression measurement error |
| P0 | `battauz2011` | IRT measures as covariates |
| P0 | `westfall2016` | Residual confounding under measurement error |
| P0 | `jerzak2026` | Attenuation with latent predictors |
| P1 | `embretson2000` | IRT information / power |
| P1 | `thissen2001` | Test scoring / information |
| P2 | `barton1981` | Original 4PL model |
| P2 | `culpepper2016` | Bayesian 4PL estimation |
| P2 | `liao2012` | 4PL for aberrant responses |
