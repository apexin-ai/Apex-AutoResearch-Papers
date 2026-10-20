# Round 8 引用验证报告

## Paper 1: ThinK

- **Title:** ThinK: Thinner Key Cache by Query-Driven Pruning
- **Authors:** Yuhui Xu, Zhanming Jie, Hanze Dong, Lei Wang, Xudong Lu, Aojun Zhou, Amrita Saha, Caiming Xiong, Doyen Sahoo
- **arXiv:** 2407.21018
- **Venue:** ICLR 2025 (Spotlight)
- **与本文关系:** KV cache 的 channel 维度 query-driven pruning 方法，识别 key cache 中 channel 维度的冗余并选择性裁剪，属于 structured pruning 方向。与我们的 compound sparsity 方法互补——ThinK 关注 channel 维度裁剪，我们关注 token-level 和 head-level 的复合稀疏。
- **BibTeX entry:**
```bibtex
@inproceedings{xu2025think,
  title     = {{ThinK}: Thinner Key Cache by Query-Driven Pruning},
  author    = {Xu, Yuhui and Jie, Zhanming and Dong, Hanze and Wang, Lei and Lu, Xudong and Zhou, Aojun and Saha, Amrita and Xiong, Caiming and Sahoo, Doyen},
  booktitle = {International Conference on Learning Representations (ICLR)},
  year      = {2025}
}
```

## Paper 2: ForesightKV

- **Title:** ForesightKV: Optimizing KV Cache Eviction for Reasoning Models by Learning Long-Term Contribution
- **Authors:** Zican Dong, Peiyu Liu, Junyi Li, Zhipeng Chen, Han Peng, Shuo Wang, Wayne Xin Zhao
- **arXiv:** 2602.03203
- **Venue:** arXiv preprint, February 2026
- **与本文关系:** 通过学习预测 KV pair 的长期贡献来指导 eviction，是 reasoning-aware 的 learned importance 方法。与我们的 attention-based importance scoring 互补——ForesightKV 用 supervised + RL 训练 importance predictor，我们用 attention weight 作为 importance signal 进行 phase-gated 压缩。
- **BibTeX entry:**
```bibtex
@article{dong2026foresightkv,
  title   = {{ForesightKV}: Optimizing {KV} Cache Eviction for Reasoning Models by Learning Long-Term Contribution},
  author  = {Dong, Zican and Liu, Peiyu and Li, Junyi and Chen, Zhipeng and Peng, Han and Wang, Shuo and Zhao, Wayne Xin},
  journal = {arXiv preprint arXiv:2602.03203},
  year    = {2026}
}
```

## Paper 3: Prune-then-Quantize

- **Title:** Prune-then-Quantize or Quantize-then-Prune? Understanding the Impact of Compression Order in Joint Model Compression
- **Authors:** Minjun Kim, Jaehyeon Choi, Hyunwoo Yang, Jongjin Kim, Jinho Song, U Kang
- **arXiv:** 2603.18426
- **Venue:** ICLR 2026
- **与本文关系:** 研究 pruning 和 quantization 的施加顺序对联合压缩效果的影响，提出 Progressive Intensity Hypothesis（弱扰动应先于强扰动）。与我们的 compound sparsity 直接相关——我们的 phase-gated 策略本质上也是在设计不同压缩方式的施加顺序和强度组合。
- **BibTeX entry:**
```bibtex
@inproceedings{kim2026pqqp,
  title     = {Prune-then-Quantize or Quantize-then-Prune? Understanding the Impact of Compression Order in Joint Model Compression},
  author    = {Kim, Minjun and Choi, Jaehyeon and Yang, Hyunwoo and Kim, Jongjin and Song, Jinho and Kang, U},
  booktitle = {International Conference on Learning Representations (ICLR)},
  year      = {2026}
}
```

## LKV Fix

- **论文:** LKV: End-to-End Learning of Head-wise Budgets and Token Selection for LLM KV Cache Eviction
- **arXiv:** 2605.06676
- **实际作者:** Enshuai Zhou, Yifan Hao, Chao Wang, Rui Zhang, Di Huang, Jiaming Guo, Xing Hu, Zidong Du, Qi Guo, Yunji Chen

- **原 entry:** `author = "Anonymous"`
- **更正后完整 BibTeX:**
```bibtex
@article{zhou2026lkv,
  title   = {{LKV}: End-to-End Learning of Head-wise Budgets and Token Selection for {LLM} {KV} Cache Eviction},
  author  = {Zhou, Enshuai and Hao, Yifan and Wang, Chao and Zhang, Rui and Huang, Di and Guo, Jiaming and Hu, Xing and Du, Zidong and Guo, Qi and Chen, Yunji},
  journal = {arXiv preprint arXiv:2605.06676},
  year    = {2026}
}
```
