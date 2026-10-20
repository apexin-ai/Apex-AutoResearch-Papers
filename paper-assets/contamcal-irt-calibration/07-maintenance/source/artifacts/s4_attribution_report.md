# S4 Self-Critique Signal: Attribution Report

## 1. Implementation Description (from code)

File: `/root/contamcal-irt-calibration/exp002/signals/s4_selfcritique.py`

The S4 signal operates in two steps:
1. **Generate answer**: Model produces a greedy-decoded answer to each benchmark item
2. **Self-evaluate**: A critique prompt asks "Is the following answer correct? Answer: {answer}. Question: {question}. Explain briefly then conclude with YES or NO."
3. **Compute entropy**: Extract logits at the last position for YES/NO token variants, normalize to binary probabilities, compute Shannon entropy
4. **Score**: Return **negative entropy** (lower entropy = more confident self-evaluation = higher contamination suspicion)

The intuition: a model that has memorized an item will be more confident in evaluating its own (correct) answer, producing lower entropy in the YES/NO distribution.

## 2. Current Citation (HALLUCINATED)

The paper cites `wust2025selfcritique`:
- **Claimed title**: "Self-Critique as a Contamination Signal: Detecting Memorization via Entropy Collapse in Model Self-Evaluations"
- **Claimed authors**: Wüst, Hoffmann, & Pang
- **Claimed URL**: arXiv 2510.09259

**Verdict: This citation is fabricated.** No paper with these authors/title exists.

## 3. What arXiv 2510.09259 Actually Is

- **Real title**: "Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models"
- **Real authors**: Yongding Tao, Tian Wang, Yihong Dong, Huanyu Liu, Kechi Zhang, Hu XiaoLong, Ge Li
- **Venue**: ICLR 2026
- **Method name**: Also called "Self-Critique"
- **Mechanism**: Probes for RL-induced policy collapse by measuring whether entropy sequences remain similar when the model is asked to produce alternative reasoning paths. High similarity = stuck on memorized path = contamination signal.

**Relationship to our implementation**: Same high-level concept (self-critique + entropy + contamination detection) but fundamentally different mechanism. Tao et al. measure entropy across reasoning path sequences; we measure binary YES/NO entropy of a single self-evaluation.

## 4. Other Related Work

| Paper | Relationship to S4 |
|-------|-------------------|
| Tao et al. (ICLR 2026, 2510.09259) | Same concept name "Self-Critique", same domain (entropy-based contamination detection). Different mechanism. |
| Shi et al. "SPV-MIA" (NeurIPS 2024, 2311.06062) | Self-prompt calibration for membership inference; uses model's own outputs as reference. Closest methodological parallel. |
| Kadavath et al. "Self-Evaluation" (2022, 2207.05221) | Foundational work showing LLMs can evaluate their own outputs with calibrated P(True). |
| Duan et al. "Min-K%++" (2024, 2404.02936) | Token-level membership inference; our S2 signal. S4 is a behavioral complement to this statistical approach. |

## 5. Conclusion

**S4 is best described as an original method** that synthesizes two well-known ideas:
1. LLM self-evaluation capability (Kadavath et al. 2022)
2. Entropy/confidence as a memorization signal (standard in membership inference literature)

The specific combination (generate answer → binary self-critique → entropy as contamination proxy) does not appear in any prior publication in this exact form. Tao et al. (ICLR 2026) independently proposed a method also named "Self-Critique" for contamination detection via entropy, but with a completely different mechanism targeting RL post-training.

## 6. Recommended Citation Strategy

**Option A (preferred)**: Cite as our own contribution, framing the related work:
```latex
\textbf{S4}~(Self-Critique): negative entropy of model self-evaluation
distributions. Inspired by the observation that LLMs exhibit calibrated
self-evaluation \citep{kadavath2022language}, we probe whether contaminated
models show anomalous confidence when judging their own answers. Concurrently,
\citet{tao2026selfcritique} propose a similarly-named technique for
RL post-training contamination, though targeting policy collapse rather than
binary self-assessment entropy.
```

**Option B**: Cite Tao et al. as the primary inspiration if we want to attribute the "self-critique for contamination" idea:
```latex
\textbf{S4}~(Self-Critique): negative entropy of model self-evaluation
distributions, adapted from the entropy-collapse intuition of
\citet{tao2026selfcritique} to the SFT setting via binary self-assessment.
```

**Bib entry to replace the hallucinated one**:
```bibtex
@inproceedings{tao2026selfcritique,
  author    = {Tao, Yongding and Wang, Tian and Dong, Yihong and Liu, Huanyu and Zhang, Kechi and Hu, XiaoLong and Li, Ge},
  title     = {Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models},
  booktitle = {International Conference on Learning Representations (ICLR)},
  year      = {2026},
  eprint    = {2510.09259},
  archiveprefix = {arXiv},
  url       = {https://arxiv.org/abs/2510.09259}
}

@article{kadavath2022language,
  author    = {Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain, Dawn and Perez, Ethan and Schiefer, Nicholas and Hatfield-Dodds, Zac and DasSarma, Nova and Tran-Johnson, Eli and others},
  title     = {Language Models (Mostly) Know What They Know},
  journal   = {arXiv preprint arXiv:2207.05221},
  year      = {2022}
}
```

## 7. Action Items

1. **Remove** both `wust_2025_selfcritique` and `wust2025selfcritique` entries from `references.bib`
2. **Add** `tao2026selfcritique` and `kadavath2022language` entries
3. **Update** `method.tex` line 22: replace `\citep{wust2025selfcritique}` with appropriate framing (Option A or B above)
4. **Update** `literature_map.yaml`: fix the entry for S4's source
