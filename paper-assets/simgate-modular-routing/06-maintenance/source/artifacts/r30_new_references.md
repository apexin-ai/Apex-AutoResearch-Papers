# R30 New References

## 1. SelfCheckGPT (Manakul et al., 2023)

```bibtex
@inproceedings{manakul2023selfcheckgpt,
  author    = {Potsawee Manakul and Adian Liusie and Mark J. F. Gales},
  title     = {{SelfCheckGPT}: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models},
  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
  year      = {2023},
  url       = {https://aclanthology.org/2023.emnlp-main.557},
}
```

**Summary**: Proposes a zero-resource hallucination detection method that samples multiple responses from a black-box LLM and measures cross-sample consistency to identify hallucinated claims, without requiring external knowledge bases.

---

## 2. Kadavath et al. (2022)

```bibtex
@article{kadavath2022language,
  author  = {Saurav Kadavath and Tom Conerly and Amanda Askell and Tom Henighan and Dawn Drain and Ethan Perez and Nicholas Schiefer and Zac Hatfield-Dodds and Nova DasSarma and Eli Tran-Geesaman and Scott Johnston and Sheer El-Showk and Andy Jones and Nelson Elhage and Tristan Hume and Anna Chen and Yuntao Bai and Sam Bowman and Stanislav Fort and Deep Ganguli and Danny Hernandez and Josh Jacobson and Jackson Kernion and Shauna Kravec and Liane Lovitt and Kamal Ndousse and Catherine Olsson and Sam Ringer and Dario Amodei and Tom Brown and Jack Clark and Nicholas Joseph and Ben Mann and Sam McCandlish and Chris Olah and Jared Kaplan},
  title   = {Language Models (Mostly) Know What They Know},
  journal = {arXiv preprint arXiv:2207.05221},
  year    = {2022},
}
```

**Summary**: Demonstrates that large language models can self-evaluate the validity of their own claims and calibrate confidence, showing that model P(True) scores correlate with actual correctness -- establishing the basis for self-knowledge in LLMs.

---

## 3. DeeBERT (Xin et al., 2020)

```bibtex
@inproceedings{xin2020deebert,
  author    = {Ji Xin and Raphael Tang and Jaejun Lee and Yaoliang Yu and Jimmy Lin},
  title     = {{DeeBERT}: Dynamic Early Exiting for Accelerating {BERT} Inference},
  booktitle = {Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics (ACL)},
  year      = {2020},
  pages     = {2246--2251},
  url       = {https://aclanthology.org/2020.acl-main.204},
}
```

**Summary**: Attaches classification heads to intermediate BERT layers and uses entropy-based confidence to decide when to exit early, achieving up to 40% inference speedup with minimal accuracy loss on classification tasks.

---

## 4. PABEE (Zhou et al., 2020)

```bibtex
@inproceedings{zhou2020bert,
  author    = {Wangchunshu Zhou and Canwen Xu and Tao Ge and Julian McAuley and Ke Xu and Furu Wei},
  title     = {{BERT} Loses Patience: Fast and Robust Inference with Early Exit},
  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
  volume    = {33},
  pages     = {18330--18341},
  year      = {2020},
}
```

**Summary**: Proposes patience-based early exit (PABEE) that stops inference when internal classifiers' predictions remain unchanged for t consecutive layers, providing a more robust early-exit criterion than single-layer confidence thresholds.
