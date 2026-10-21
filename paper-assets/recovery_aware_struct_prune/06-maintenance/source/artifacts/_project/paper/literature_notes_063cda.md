# Related Work Literature Notes

> Generated 2026-05-15. Verified via WebSearch + WebFetch.

## Core Comparisons

### 1. Self-Healing (2025)
- **Full Title**: Self-Healing: Recovering Pruned Large Reasoning Models via Reinforcement Learning
- **Authors**: Yixin Ji, Zhimin Lin, Juntao Li, Kaixin Wu, Kai Yao, Xu Jia, Linjian Mo, Min Zhang
- **Venue/Year**: ICLR 2026 (submitted Sep 2025, modified Feb 2026)
- **arXiv**: Not found on arXiv; OpenReview ID: Cy8Qa4gAst
- **Core Method**: First work applying RLVR (reinforcement learning with verifiable reward) to recover pruned large reasoning models. Shows that structured pruning degrades math reasoning but doesn't destroy it — leaving room for RL-based recovery. RLVR treats recovery as active exploration rather than passive imitation (SFT).
- **Key Results**: At 25% compression, RLVR recovery achieves >95% accuracy vs ~80% with SFT across 5 LRMs on 6 math benchmarks, nearly matching unpruned performance.
- **vs RASP**: Self-Healing tests RLVR recovery with standard importance-based pruning at a single sparsity ratio. RASP optimizes the pruning decision itself FOR recovery by predicting recoverability via CKA, yielding better accuracy at the same sparsity+recovery budget.

### 2. GRASPrune (ACL 2026)
- **Full Title**: GRASPrune: Global Gating for Budgeted Structured Pruning of Large Language Models
- **Authors**: Ziyang Wang, Jiangfeng Xiao, Chuan Xiao, Ruoxiang Li, Rui Mao, Jianbin Qin
- **Venue/Year**: ACL 2026 Main
- **arXiv**: 2604.19398 (Apr 2026)
- **Core Method**: Jointly prunes FFN channels and KV head groups under a single global budget. Learns lightweight gate scores with a projected straight-through estimator enforcing a hard mask at every step, backbone weights frozen. Post-mask calibration of scaling factors mitigates scale mismatch.
- **Key Results**: LLaMA-2-7B at 50% params → 12.18 PPL on WikiText-2 with competitive zero-shot accuracy. At 0.4 retention ratio, achieves best average accuracy among structured pruning methods.
- **vs RASP**: SOTA budgeted pruning without studying post-pruning recovery. GRASPrune is our primary pruning baseline — RASP adds recovery-awareness (CKA functional overlap) on top of importance-based scoring.

### 3. RESP (Dec 2025)
- **Full Title**: Think Before You Prune: Self-Reflective Structured Pruning for Reasoning Language Models
- **Authors**: Ziyan Wang, Enmao Diao, Qi Le, Pu Wang, Guanchu Wang, Minwoo Lee, Shu-ping Yeh, Li Yang
- **Venue/Year**: arXiv preprint, Dec 2025
- **arXiv**: 2512.02185
- **Core Method**: Self-reflective structured pruning (RESP) aligns pruning with the model's reasoning dynamics via three components: (1) self-generated reasoning traces as calibration (not human labels), (2) decode-only gradient-based importance estimation, (3) progressive calibration regeneration that refreshes traces as sparsity increases.
- **Key Results**: On Qwen3-8B at 40% sparsity: GSM8K 81.3%, MathQA 59.6% — surpassing strongest baselines by 66.87% and 47% respectively. Near-dense accuracy at 20-30% sparsity.
- **vs RASP**: RESP uses reasoning-trace calibration to improve pruning importance estimation but has no post-pruning recovery mechanism. RASP includes recovery-awareness in the pruning score itself via CKA overlap, enabling RLVR recovery to restore more reasoning capability.

### 4. MPruner (2024)
- **Full Title**: MPruner: Optimizing Neural Network Size with CKA-Based Mutual Information Pruning
- **Authors**: Seungbeom Hu, ChanJun Park, Andrew Ferraiuolo, Sang-Ki Ko, Jinwoo Kim, Haein Song, Jieung Kim
- **Venue/Year**: arXiv preprint, Aug 2024
- **arXiv**: 2408.13482
- **Core Method**: Leverages CKA similarity between consecutive layers to identify redundant layers via clustering. Uses mutual information through vector similarity for global layer-wise pruning decisions. Analysis stage runs in linear time.
- **Key Results**: Up to 50% reduction in parameters and memory for CNN and transformer models with minimal accuracy loss. Up to 70% compression in some configurations.
- **vs RASP**: MPruner uses inter-layer CKA for depth pruning (removing entire layers) in CNNs/transformers. RASP uses intra-layer CKA between individual attention heads for width pruning in reasoning LLMs, and crucially uses CKA as a recoverability predictor rather than a redundancy detector.

### 5. PASER (2025)
- **Full Title**: PASER: Post-Training Data Selection for Efficient Pruned Large Language Model Recovery
- **Authors**: Bowei He, Lihao Yin, Hui-Ling Zhen, Xiaokun Zhang, Mingxuan Yuan, Chen Ma
- **Venue/Year**: ICLR 2026 (submitted Feb 2025, revised Feb 2026)
- **arXiv**: 2502.12594
- **Core Method**: Post-training data selection for pruned LLM recovery. Uses manifold learning and spectral clustering to group recovery instructions in semantic space, then allocates data budget across clusters by degree of capability degradation. Detects and filters conflicting/irrelevant recovery data.
- **Key Results**: Recovers general capabilities of pruned LLMs using only 4-20% of original post-training data, significantly outperforming conventional baselines.
- **vs RASP**: PASER optimizes recovery DATA selection; RASP optimizes pruning STRUCTURE. The two are complementary — PASER could be applied to RASP's recovery phase to further improve data efficiency.

---

## Additional Related Work

### Pruning for Reasoning Models

#### 6. SSGR (Nov 2025)
- **Full Title**: Think Before You Prune: Selective Self-Generated Calibration for Pruning Large Reasoning Models
- **Authors**: Yang Xiang, Yixin Ji, Juntao Li, Min Zhang
- **arXiv**: 2511.18864
- **Core Method**: First empirical study of pruning LRMs. Proposes Selective Self-Generated Reasoning (SSGR) calibration data strategy — challenging, moderately-lengthy reasoning examples work best.
- **Key Results**: 10-13% reasoning improvement over general pruning methods on DeepSeek-R1-Distill models.
- **Relation**: Complements RESP's self-generated calibration approach; from same group as Self-Healing (Ji, Juntao Li, Min Zhang).

#### 7. RAC — Reasoning-Aware Compression (Sep 2025)
- **Full Title**: Reasoning Models Can be Accurately Pruned Via Chain-of-Thought Reconstruction
- **Authors**: Ryan Lucas, Kayhan Behdin, Zhipeng Wang, Qingquan Song, Shao Tang, Rahul Mazumder
- **Venue/Year**: NeurIPS 2025
- **arXiv**: 2509.12464
- **Core Method**: During pruning, jointly reconstructs activations from input AND model's on-policy CoT traces. Integrates into SparseGPT-style pipelines without retraining.
- **Key Results**: Significant improvement over standard calibration for reasoning model compression.
- **Relation**: Focuses on unstructured/2:4 sparsity with CoT-aware calibration. RASP targets structured width pruning with recovery prediction.

#### 8. From LLMs to LRMs (Jan 2026)
- **Full Title**: From LLMs to LRMs: Rethinking Pruning for Reasoning-Centric Models
- **Authors**: Longwei Ding, Anhao Zhao, Fanghua Ye, Ziyang Chen, Xiaoyu Shen
- **arXiv**: 2601.18091
- **Core Method**: Systematic comparison of depth/width/dynamic pruning across instruction-following vs reasoning-augmented models on 17 tasks.
- **Key Results**: Width pruning outperforms depth pruning for generation and reasoning tasks. Static pruning better preserves reasoning; dynamic methods struggle with extended reasoning chains.
- **Relation**: Provides evidence motivating RASP's width-pruning focus.

#### 9. Doing More With Less (Apr 2026)
- **Full Title**: Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling
- **Authors**: Ocean Monjur, Shahriar Kabir Nahin, Anshuman Chhabra
- **arXiv**: 2604.25098
- **Core Method**: Studies pruning's impact on test-time scaling (TTS) in reasoning LLMs (s1.1-7B, Qwen3-8B).
- **Key Results**: Structured pruning significantly degrades TTS performance. Unstructured pruning can augment TTS and even outperform unpruned models. Layer-wise sparsity allocation improves TTS further.
- **Relation**: Directly motivates why structured pruning needs a recovery mechanism — the degradation is especially severe for reasoning tasks requiring longer chains.

### Reasoning Trace Compression

#### 10. ThinkPrune (Apr 2025)
- **Full Title**: ThinkPrune: Pruning Long Chain-of-Thought of LLMs via Reinforcement Learning
- **arXiv**: 2504.01296
- **Core Method**: Uses RL to prune (shorten) reasoning traces at inference time, addressing "overthinking" in long-CoT models.
- **Key Results**: On AIME24, DeepSeek-R1-Distill-Qwen-1.5B reasoning length reduced by 50% with only 2% performance drop.
- **Relation**: Orthogonal — prunes reasoning tokens, not model parameters. Could be combined with RASP for joint model+inference compression.

#### 11. Think, Prune, Train, Improve (Apr 2025)
- **Full Title**: Think, Prune, Train, Improve: Scaling Reasoning without Scaling Models
- **Authors**: Caia Costello, Simon Guo, Anna Goldie, Azalia Mirhoseini (Stanford)
- **arXiv**: 2504.18116
- **Core Method**: Iteratively fine-tunes models on their own correct CoT solutions. Ground-truth pruning filters incorrect traces.
- **Key Results**: GSM8K: Gemma2-2B 41.9%→57.6%, Gemma2-9B reaches 82% (matching LLaMA-3.1-70B), LLaMA-3.1-70B reaches 91% (surpassing GPT-4o).
- **Relation**: "Prune" refers to trace filtering, not parameter pruning. Different problem setting but relevant to reasoning capability scaling.

---

## Citation BibTeX

```bibtex
@inproceedings{ji2025selfhealing,
  title={Self-Healing: Recovering Pruned Large Reasoning Models via Reinforcement Learning},
  author={Ji, Yixin and Lin, Zhimin and Li, Juntao and Wu, Kaixin and Yao, Kai and Jia, Xu and Mo, Linjian and Zhang, Min},
  booktitle={International Conference on Learning Representations (ICLR)},
  year={2026},
  note={OpenReview ID: Cy8Qa4gAst}
}

@inproceedings{wang2026grasprune,
  title={{GRASPrune}: Global Gating for Budgeted Structured Pruning of Large Language Models},
  author={Wang, Ziyang and Xiao, Jiangfeng and Xiao, Chuan and Li, Ruoxiang and Mao, Rui and Qin, Jianbin},
  booktitle={Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (ACL)},
  year={2026},
  eprint={2604.19398},
  archivePrefix={arXiv}
}

@article{wang2025resp,
  title={Think Before You Prune: Self-Reflective Structured Pruning for Reasoning Language Models},
  author={Wang, Ziyan and Diao, Enmao and Le, Qi and Wang, Pu and Wang, Guanchu and Lee, Minwoo and Yeh, Shu-ping and Yang, Li},
  journal={arXiv preprint arXiv:2512.02185},
  year={2025}
}

@article{hu2024mpruner,
  title={{MPruner}: Optimizing Neural Network Size with {CKA}-Based Mutual Information Pruning},
  author={Hu, Seungbeom and Park, ChanJun and Ferraiuolo, Andrew and Ko, Sang-Ki and Kim, Jinwoo and Song, Haein and Kim, Jieung},
  journal={arXiv preprint arXiv:2408.13482},
  year={2024}
}

@inproceedings{he2025paser,
  title={{PASER}: Post-Training Data Selection for Efficient Pruned Large Language Model Recovery},
  author={He, Bowei and Yin, Lihao and Zhen, Hui-Ling and Zhang, Xiaokun and Yuan, Mingxuan and Ma, Chen},
  booktitle={International Conference on Learning Representations (ICLR)},
  year={2026},
  eprint={2502.12594},
  archivePrefix={arXiv}
}

@article{xiang2025ssgr,
  title={Think Before You Prune: Selective Self-Generated Calibration for Pruning Large Reasoning Models},
  author={Xiang, Yang and Ji, Yixin and Li, Juntao and Zhang, Min},
  journal={arXiv preprint arXiv:2511.18864},
  year={2025}
}

@inproceedings{lucas2025rac,
  title={Reasoning Models Can be Accurately Pruned Via Chain-of-Thought Reconstruction},
  author={Lucas, Ryan and Behdin, Kayhan and Wang, Zhipeng and Song, Qingquan and Tang, Shao and Mazumder, Rahul},
  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
  year={2025},
  eprint={2509.12464},
  archivePrefix={arXiv}
}

@article{ding2026lrmpruning,
  title={From {LLMs} to {LRMs}: Rethinking Pruning for Reasoning-Centric Models},
  author={Ding, Longwei and Zhao, Anhao and Ye, Fanghua and Chen, Ziyang and Shen, Xiaoyu},
  journal={arXiv preprint arXiv:2601.18091},
  year={2026}
}

@article{monjur2026doingmore,
  title={Doing More With Less: Revisiting the Effectiveness of {LLM} Pruning for Test-Time Scaling},
  author={Monjur, Ocean and Nahin, Shahriar Kabir and Chhabra, Anshuman},
  journal={arXiv preprint arXiv:2604.25098},
  year={2026}
}

@article{thinkprune2025,
  title={{ThinkPrune}: Pruning Long Chain-of-Thought of {LLMs} via Reinforcement Learning},
  journal={arXiv preprint arXiv:2504.01296},
  year={2025}
}

@article{costello2025thinkprunetrain,
  title={Think, Prune, Train, Improve: Scaling Reasoning without Scaling Models},
  author={Costello, Caia and Guo, Simon and Goldie, Anna and Mirhoseini, Azalia},
  journal={arXiv preprint arXiv:2504.18116},
  year={2025}
}
```

---

## Search Notes

- **Self-Healing**: No arXiv ID found. Paper only on OpenReview (Cy8Qa4gAst). Submitted Sep 2025, accepted ICLR 2026.
- **RESP**: No confirmed venue acceptance. arXiv-only (2512.02185, Dec 2025).
- **SSGR vs RESP**: Both titled "Think Before You Prune" but different papers/groups. SSGR (2511.18864) from Ji/Li/Zhang group (same as Self-Healing). RESP (2512.02185) from Wang/Diao/Yang group.
- All 5 core papers verified real via WebSearch + WebFetch. No fabricated entries.
