# Citation Verification Report

Date: 2026-05-16

---

## 1. dodge2020finetuning

```
Citation: dodge2020finetuning
Exists: YES
Title: Fine-Tuning Pretrained Language Models: Weight Initializations, Data Orders, and Early Stopping
Authors: Jesse Dodge, Gabriel Ilharco, Roy Schwartz, Ali Farhadi, Hannaneh Hajishirzi, Noah A. Smith
Venue: arXiv preprint (arXiv:2002.06305), 2020
Context Match: PARTIAL
Reason: The paper demonstrates that fine-tuning is brittle (high variance from random seeds) and that
  many runs "diverge" during training on small datasets, recommending early stopping. However, it does
  NOT explicitly discuss the misalignment between validation loss and downstream task performance (i.e.,
  "val loss continues improving after task performance degrades"). The paper focuses on variance of
  validation performance across seeds and training divergence, not loss-metric disconnect.
Better Alternative: For the specific claim about loss-metric misalignment, consider:
  - Mosbach et al. (2021) "On the Stability of Fine-tuning BERT: Misconceptions, Explanations,
    and Strong Baselines" (ICLR 2021) — explicitly analyzes optimization failures vs. overfitting
    and shows that instability stems from optimization, not from loss-metric divergence.
  - The Dodge paper is still citable for "fine-tuning instability and checkpoint sensitivity" but
    the specific framing "val loss improving while task performance degrades" should be rephrased
    to match what the paper actually shows: "fine-tuning performance varies dramatically across
    random seeds, and early stopping on validation performance is essential."
BibTeX:
  @article{dodge2020finetuning,
    title={Fine-Tuning Pretrained Language Models: Weight Initializations, Data Orders, and Early Stopping},
    author={Dodge, Jesse and Ilharco, Gabriel and Schwartz, Roy and Farhadi, Ali and Hajishirzi, Hannaneh and Smith, Noah A.},
    journal={arXiv preprint arXiv:2002.06305},
    year={2020}
  }
```

---

## 2. thakur2021beir

```
Citation: thakur2021beir
Exists: YES
Title: BEIR: A Heterogeneous Benchmark for Zero-shot Evaluation of Information Retrieval Models
Authors: Nandan Thakur, Nils Reimers, Andreas Rücklé, Abhishek Srivastava, Iryna Gurevych
Venue: NeurIPS 2021 (Datasets and Benchmarks Track)
Context Match: NO
Reason: The BEIR paper introduces a benchmark and evaluates 10 retrieval systems in zero-shot settings.
  It does NOT discuss checkpoint selection sensitivity or ranking instability. The paper uses fixed
  pre-trained checkpoints and reports single-run results. The claim "BEIR benchmark rankings are
  sensitive to checkpoint selection" is not made in this paper.
Better Alternative: For "checkpoint selection sensitivity on BEIR":
  - Clavié et al. (2024) "MultiContrievers: Analysis of Dense Retrieval Representations"
    (BlackboxNLP 2024) — trains 25 dense retrievers with different random seeds and explicitly
    shows that BEIR rankings are highly sensitive to initialization/checkpoint, with ranking of
    models changing drastically across datasets despite identical loss curves.
  If the intent is simply to cite BEIR as a benchmark (alongside MTEB), the citation is fine —
  but the associated claim about checkpoint sensitivity must be attributed to MultiContrievers
  or similar work, not to the BEIR paper itself.
BibTeX:
  @inproceedings{thakur2021beir,
    title={{BEIR}: A Heterogeneous Benchmark for Zero-shot Evaluation of Information Retrieval Models},
    author={Thakur, Nandan and Reimers, Nils and R{\"u}ckl{\'e}, Andreas and Srivastava, Abhishek and Gurevych, Iryna},
    booktitle={Proceedings of the Neural Information Processing Systems Track on Datasets and Benchmarks},
    year={2021}
  }

  % RECOMMENDED ADDITION for checkpoint sensitivity claim:
  @inproceedings{clavie2024multicontrievers,
    title={MultiContrievers: Analysis of Dense Retrieval Representations},
    author={Clavi{\'e}, Benjamin and others},
    booktitle={Proceedings of the 7th BlackboxNLP Workshop},
    year={2024}
  }
```

---

## 3. muennighoff2023mteb

```
Citation: muennighoff2023mteb
Exists: YES
Title: MTEB: Massive Text Embedding Benchmark
Authors: Niklas Muennighoff, Nouamane Tazi, Loïc Magne, Nils Reimers
Venue: EACL 2023 (Proceedings of the 17th Conference of the European Chapter of the ACL)
Context Match: YES
Reason: MTEB spans 8 embedding tasks (including retrieval) across 58 datasets and 112 languages.
  Citing it as a "corpus-scale evaluation benchmark" alongside BEIR is appropriate — MTEB subsumes
  and extends BEIR-style retrieval evaluation. The paper evaluates 33 models and finds no single
  method dominates all tasks, which is relevant to checkpoint/model selection discussions.
Better Alternative: N/A — citation is appropriate.
BibTeX:
  @inproceedings{muennighoff2023mteb,
    title={{MTEB}: Massive Text Embedding Benchmark},
    author={Muennighoff, Niklas and Tazi, Nouamane and Magne, Lo{\"i}c and Reimers, Nils},
    booktitle={Proceedings of the 17th Conference of the European Chapter of the Association for Computational Linguistics (EACL)},
    pages={2014--2037},
    year={2023}
  }
```

---

## 4. craswell2020overview

```
Citation: craswell2020overview
Exists: YES
Title: Overview of the TREC 2020 Deep Learning Track
Authors: Nick Craswell, Bhaskar Mitra, Emine Yilmaz, Daniel Campos
Venue: TREC 2020 (Text REtrieval Conference, NIST)
Context Match: PARTIAL
Reason: The paper documents the TREC 2020 DL track methodology including depth-10 pooling, the
  reranking subtask (top-100 candidates), and reports performance gaps between full-ranking and
  reranking runs (5% NDCG@10 gap in 2020). This implicitly demonstrates that evaluation depth
  matters. However, the paper does not explicitly frame the "gap between small-pool and corpus-scale
  evaluation" as a general finding — it reports track results. For the explicit discussion of
  pooling depth effects on evaluation validity, the companion SIGIR paper is stronger.
Better Alternative: For the explicit claim about pool-size vs. corpus-scale evaluation gap:
  - Craswell et al. (2021) "TREC Deep Learning Track: Reusable Test Collections in the Large
    Data Regime" (SIGIR 2021) — explicitly analyzes pooling depth effects, LOU tests, and
    collection reusability. This paper directly addresses whether shallow pools produce biased
    evaluation relative to deeper annotation.
  The TREC 2020 overview paper is still citable for the track description and the reranking vs.
  full-ranking gap, but the methodological claim about pool size should cite the SIGIR 2021 paper.
BibTeX:
  @inproceedings{craswell2020overview,
    title={Overview of the {TREC} 2020 Deep Learning Track},
    author={Craswell, Nick and Mitra, Bhaskar and Yilmaz, Emine and Campos, Daniel},
    booktitle={Proceedings of the Twenty-Ninth Text REtrieval Conference (TREC 2020)},
    year={2021},
    publisher={NIST}
  }

  % RECOMMENDED ALTERNATIVE for pool-size evaluation gap:
  @inproceedings{craswell2021reusable,
    title={{TREC} Deep Learning Track: Reusable Test Collections in the Large Data Regime},
    author={Craswell, Nick and Mitra, Bhaskar and Yilmaz, Emine and Campos, Daniel and Voorhees, Ellen M. and Soboroff, Ian},
    booktitle={Proceedings of the 44th International ACM SIGIR Conference on Research and Development in Information Retrieval},
    year={2021}
  }
```

---

## Summary

| Citation | Exists | Context Match | Action Required |
|----------|--------|---------------|-----------------|
| dodge2020finetuning | YES | PARTIAL | Rephrase citation context from "val loss vs task performance misalignment" to "fine-tuning instability and checkpoint sensitivity across random seeds" |
| thakur2021beir | YES | NO | Split: cite BEIR as benchmark only; attribute checkpoint sensitivity claim to MultiContrievers (Clavié et al., 2024) |
| muennighoff2023mteb | YES | YES | No change needed |
| craswell2020overview | YES | PARTIAL | Consider citing Craswell et al. SIGIR 2021 for explicit pool-depth analysis; keep TREC overview for track description |
