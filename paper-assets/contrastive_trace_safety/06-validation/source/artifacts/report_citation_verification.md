# Citation Verification Report

Date: 2026-05-17

## Summary

| # | Key | Status | Paper |
|---|-----|--------|-------|
| 1 | trajguard | **真实** | TrajGuard (Liu et al., 2026) |
| 2 | safeswitch | **真实** | SafeSwitch (Han et al., 2025) |
| 3 | siren | **真实** | SIREN (Jiao et al., 2026) |
| 4 | saferemind | **真实** | SafeRemind (Kim et al., 2026) |
| 5 | safethink | **真实** | SafeThink (Ghosal et al., 2026) |
| 6 | selfjailbreak | **真实** | Self-Jailbreaking (Yong & Bach, 2025) |
| 7 | harmthoughts | **真实** | HarmThoughts (Kakkar et al., 2026) |
| 8 | arditi2024refusal | **真实** | Refusal Directions (Arditi et al., 2024) |

**结论: 全部 8 个引用均为真实论文，无幻觉。**

---

## 1. trajguard

- **状态**: 真实
- **真实论文**: TrajGuard: Streaming Hidden-state Trajectory Detection for Decoding-time Jailbreak Defense (Cheng Liu, Xiaolei Liu, Xingyu Li, Bangzhou Xin, Kangyi Ding, 2026, arXiv preprint)
- **验证依据**: arXiv:2604.07727, 95% detection rate confirmed
- **BibTeX**:

```bibtex
@article{trajguard,
  title={TrajGuard: Streaming Hidden-state Trajectory Detection for Decoding-time Jailbreak Defense},
  author={Liu, Cheng and Liu, Xiaolei and Li, Xingyu and Xin, Bangzhou and Ding, Kangyi},
  journal={arXiv preprint arXiv:2604.07727},
  year={2026},
  url={https://arxiv.org/abs/2604.07727}
}
```

---

## 2. safeswitch

- **状态**: 真实
- **真实论文**: SafeSwitch: Steering Unsafe LLM Behavior via Internal Activation Signals (Peixuan Han, Cheng Qian, Xiusi Chen, Yuji Zhang, Heng Ji, Denghui Zhang, 2025, EMNLP 2025 Findings)
- **验证依据**: arXiv:2502.01042, ACL Anthology confirmed
- **BibTeX**:

```bibtex
@inproceedings{safeswitch,
  title={SafeSwitch: Steering Unsafe LLM Behavior via Internal Activation Signals},
  author={Han, Peixuan and Qian, Cheng and Chen, Xiusi and Zhang, Yuji and Ji, Heng and Zhang, Denghui},
  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2025},
  year={2025},
  url={https://arxiv.org/abs/2502.01042}
}
```

---

## 3. siren

- **状态**: 真实
- **真实论文**: LLM Safety From Within: Detecting Harmful Content with Internal Representations (Difan Jiao, Yilun Liu, Ye Yuan, Zhenwei Tang, Linfeng Du, Haolun Wu, Ashton Anderson, 2026, ACL 2026)
- **验证依据**: arXiv:2604.18519, GitHub repo CSSLab/SIREN
- **BibTeX**:

```bibtex
@inproceedings{siren,
  title={LLM Safety From Within: Detecting Harmful Content with Internal Representations},
  author={Jiao, Difan and Liu, Yilun and Yuan, Ye and Tang, Zhenwei and Du, Linfeng and Wu, Haolun and Anderson, Ashton},
  booktitle={Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (ACL)},
  year={2026},
  url={https://arxiv.org/abs/2604.18519}
}
```

---

## 4. saferemind

- **状态**: 真实
- **真实论文**: How Does the Thinking Step Influence Model Safety? An Entropy-based Safety Reminder for LRMs (Su-Hyeon Kim, Hyundong Jin, Yejin Lee, Yo-Sub Han, 2026, arXiv preprint)
- **验证依据**: arXiv:2601.03662
- **BibTeX**:

```bibtex
@article{saferemind,
  title={How Does the Thinking Step Influence Model Safety? An Entropy-based Safety Reminder for LRMs},
  author={Kim, Su-Hyeon and Jin, Hyundong and Lee, Yejin and Han, Yo-Sub},
  journal={arXiv preprint arXiv:2601.03662},
  year={2026},
  url={https://arxiv.org/abs/2601.03662}
}
```

---

## 5. safethink

- **状态**: 真实
- **真实论文**: Safety Recovery in Reasoning Models Is Only a Few Early Steering Steps Away (Soumya Suvra Ghosal, Souradip Chakraborty, Vaibhav Singh, Furong Huang, Dinesh Manocha, Amrit Singh Bedi, 2026, arXiv preprint)
- **验证依据**: arXiv:2602.11096, project page itsvaibhav01.github.io/SafeThink-web/
- **BibTeX**:

```bibtex
@article{safethink,
  title={Safety Recovery in Reasoning Models Is Only a Few Early Steering Steps Away},
  author={Ghosal, Soumya Suvra and Chakraborty, Souradip and Singh, Vaibhav and Huang, Furong and Manocha, Dinesh and Bedi, Amrit Singh},
  journal={arXiv preprint arXiv:2602.11096},
  year={2026},
  url={https://arxiv.org/abs/2602.11096}
}
```

---

## 6. selfjailbreak

- **状态**: 真实
- **真实论文**: Self-Jailbreaking: Language Models Can Reason Themselves Out of Safety Alignment After Benign Reasoning Training (Zheng-Xin Yong, Stephen H. Bach, 2025, arXiv preprint)
- **验证依据**: arXiv:2510.20956, OpenReview submission confirmed
- **核心发现**: After benign reasoning training on math/code, reasoning models use multiple strategies to circumvent safety guardrails; longer reasoning chains increase circumvention probability
- **BibTeX**:

```bibtex
@article{selfjailbreak,
  title={Self-Jailbreaking: Language Models Can Reason Themselves Out of Safety Alignment After Benign Reasoning Training},
  author={Yong, Zheng-Xin and Bach, Stephen H.},
  journal={arXiv preprint arXiv:2510.20956},
  year={2025},
  url={https://arxiv.org/abs/2510.20956}
}
```

**补充相关论文** (同一现象, 不同角度):
```bibtex
@article{mao2025selfjailbreak,
  title={When Models Outthink Their Safety: Unveiling and Mitigating Self-Jailbreak in Large Reasoning Models},
  author={Mao, Yingzhi and Zhang, Chunkang and Wang, Junxiang and Guan, Xinyan and Cao, Boxi and Lu, Yaojie and Lin, Hongyu and Han, Xianpei and Sun, Le},
  journal={arXiv preprint arXiv:2510.21285},
  year={2025},
  url={https://arxiv.org/abs/2510.21285}
}
```

---

## 7. harmthoughts

- **状态**: 真实
- **真实论文**: When Safety Fails Before the Answer: Benchmarking Harmful Behavior Detection in Reasoning Chains (Ishita Kakkar et al., 2026, arXiv preprint)
- **验证依据**: arXiv:2604.19001 (HTML version accessible), HuggingFace dataset page ishitakakkar-10/HarmThoughts, Google Scholar profile confirmed
- **数据集**: 56,931 sentence-level annotations, 1,018 reasoning traces, 4 model families, 16-label taxonomy, MIT license
- **BibTeX**:

```bibtex
@article{harmthoughts,
  title={When Safety Fails Before the Answer: Benchmarking Harmful Behavior Detection in Reasoning Chains},
  author={Kakkar, Ishita and others},
  journal={arXiv preprint arXiv:2604.19001},
  year={2026},
  url={https://arxiv.org/abs/2604.19001}
}
```

---

## 8. arditi2024refusal

- **状态**: 真实
- **真实论文**: Refusal in Language Models Is Mediated by a Single Direction (Andy Arditi, Oscar Obeso, Aaquib Syed, Daniel Paleka, Nina Panickssery, Wes Gurnee, Neel Nanda, 2024, NeurIPS 2024)
- **验证依据**: arXiv:2406.11717, NeurIPS 2024 proceedings confirmed, GitHub repo andyrdt/refusal_direction
- **BibTeX**:

```bibtex
@inproceedings{arditi2024refusal,
  title={Refusal in Language Models Is Mediated by a Single Direction},
  author={Arditi, Andy and Obeso, Oscar and Syed, Aaquib and Paleka, Daniel and Panickssery, Nina and Gurnee, Wes and Nanda, Neel},
  booktitle={Advances in Neural Information Processing Systems 37 (NeurIPS)},
  year={2024},
  url={https://arxiv.org/abs/2406.11717}
}
```

---

## Combined references.bib

```bibtex
@article{trajguard,
  title={TrajGuard: Streaming Hidden-state Trajectory Detection for Decoding-time Jailbreak Defense},
  author={Liu, Cheng and Liu, Xiaolei and Li, Xingyu and Xin, Bangzhou and Ding, Kangyi},
  journal={arXiv preprint arXiv:2604.07727},
  year={2026},
  url={https://arxiv.org/abs/2604.07727}
}

@inproceedings{safeswitch,
  title={SafeSwitch: Steering Unsafe LLM Behavior via Internal Activation Signals},
  author={Han, Peixuan and Qian, Cheng and Chen, Xiusi and Zhang, Yuji and Ji, Heng and Zhang, Denghui},
  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2025},
  year={2025},
  url={https://arxiv.org/abs/2502.01042}
}

@inproceedings{siren,
  title={LLM Safety From Within: Detecting Harmful Content with Internal Representations},
  author={Jiao, Difan and Liu, Yilun and Yuan, Ye and Tang, Zhenwei and Du, Linfeng and Wu, Haolun and Anderson, Ashton},
  booktitle={Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (ACL)},
  year={2026},
  url={https://arxiv.org/abs/2604.18519}
}

@article{saferemind,
  title={How Does the Thinking Step Influence Model Safety? An Entropy-based Safety Reminder for LRMs},
  author={Kim, Su-Hyeon and Jin, Hyundong and Lee, Yejin and Han, Yo-Sub},
  journal={arXiv preprint arXiv:2601.03662},
  year={2026},
  url={https://arxiv.org/abs/2601.03662}
}

@article{safethink,
  title={Safety Recovery in Reasoning Models Is Only a Few Early Steering Steps Away},
  author={Ghosal, Soumya Suvra and Chakraborty, Souradip and Singh, Vaibhav and Huang, Furong and Manocha, Dinesh and Bedi, Amrit Singh},
  journal={arXiv preprint arXiv:2602.11096},
  year={2026},
  url={https://arxiv.org/abs/2602.11096}
}

@article{selfjailbreak,
  title={Self-Jailbreaking: Language Models Can Reason Themselves Out of Safety Alignment After Benign Reasoning Training},
  author={Yong, Zheng-Xin and Bach, Stephen H.},
  journal={arXiv preprint arXiv:2510.20956},
  year={2025},
  url={https://arxiv.org/abs/2510.20956}
}

@article{harmthoughts,
  title={When Safety Fails Before the Answer: Benchmarking Harmful Behavior Detection in Reasoning Chains},
  author={Kakkar, Ishita and others},
  journal={arXiv preprint arXiv:2604.19001},
  year={2026},
  url={https://arxiv.org/abs/2604.19001}
}

@inproceedings{arditi2024refusal,
  title={Refusal in Language Models Is Mediated by a Single Direction},
  author={Arditi, Andy and Obeso, Oscar and Syed, Aaquib and Paleka, Daniel and Panickssery, Nina and Gurnee, Wes and Nanda, Neel},
  booktitle={Advances in Neural Information Processing Systems 37 (NeurIPS)},
  year={2024},
  url={https://arxiv.org/abs/2406.11717}
}
```
