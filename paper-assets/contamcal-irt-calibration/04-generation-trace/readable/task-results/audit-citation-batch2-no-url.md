# audit citation batch2 no url

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_citation_batch2_no_url_20260517T044825_result.json`
- **Structured JSON:** [`98eb2f0f063f6905a87a.json`](../../sessions/98/98eb2f0f063f6905a87a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成。以下是全部结果：

---

```
[sinharay_2025_irt_fit] STATUS: MATCH
  bib title: "Assessment of Fit of Item Response Theory Models: A Critical Review of the Status Quo and Some Future..."
  real title: "Assessment of fit of item response theory models: A critical review of the status quo and some future directions"
  title match: YES
  bib authors: Sinharay, Sandip
  real authors: Sinharay, Sandip (单作者)
  author match: YES
  notes: British Journal of Mathematical and Statistical Psychology, 2025, vol.78, pp.711–733. 真实存在，信息正确。
```

```
[duan2025minkpp] STATUS: MISMATCH
  bib title: "Min-K%++: Improved Membership Inference for Detecting Pre-Training Data of Large Language Models"
  real title: "Min-K%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models"
  title match: NO ("Membership Inference" → 实为 "Baseline"; "of" → 实为 "from")
  bib authors: Duan, Jiawen and Xie, Cheng and Zhang, J...
  real authors: Jingyang Zhang, Jingwei Sun, Eric Yeats, Yang Ouyang, Martin Kuo, Jianyi Zhang, Hao Frank Yang, Hai Li
  author match: NO (完全虚构——"Duan Jiawen" 和 "Xie Cheng" 不在作者列表中)
  notes: arXiv 2404.02936, ICLR 2025 Spotlight. 第一作者是 Zhang Jingyang，不是 Duan。可能与已有 zhang_2024_minkpp 重复且信息错误。
```

```
[wust2025selfcritique] STATUS: MISMATCH
  bib title: "Self-Critique as a Contamination Signal..."
  real title: "Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models"
  title match: NO (Self-Critique 是方法名，非论文标题)
  bib authors: Wüst, ...
  real authors: Yongding Tao, Tian Wang, Yihong Dong, Huanyu Liu, Kechi Zhang, Xiaolong Hu, Ge Li
  author match: NO ("Wüst" 不在作者中——全部为中国作者)
  notes: arXiv 2510.09259. 论文提出 Self-Critique 方法但标题完全不同。bib 作者完全虚构。可能是 wust_2025_selfcritique 的重复条目——两者均为幻觉。
```

```
[xu2025kds] STATUS: NOT_FOUND
  bib title: "Knowledge Distillation Signatures for Efficient Contamination Detection"
  real title: (不存在)
  title match: N/A
  bib authors: (未详)
  real authors: N/A
  author match: N/A
  notes: 无法在任何数据库中找到此标题。与已验证的 choi_2025_kds（"How Contaminated Is Your Benchmark? Measuring Dataset Leakage with Kernel Divergence"）完全不同。此条目为幻觉。
```

```
[wang2025fragility] STATUS: MISMATCH
  bib title: "On the Fragility of Benchmark Evaluations for Large Language Models"
  real title: "On The Fragility of Benchmark Contamination Detection in Reasoning Models"
  title match: NO ("Benchmark Evaluations" vs "Benchmark Contamination Detection in Reasoning Models")
  bib authors: Wang, Yuxin and Zhao, Yucheng and Li, Ch...
  real authors: Han Wang, Haoyu Li, Brian Ko, Huan Zhang
  author match: NO (Wang Yuxin ≠ Han Wang; 其余作者完全不同)
  notes: arXiv 2510.02386. 标题和作者都被篡改——bib 将 "Wang Yuxin" 与不同论文的作者拼凑。
```

```
[zhang2025forget] STATUS: MISMATCH
  bib title: "How Much Can We Forget? Examining Decontamination Effectiveness in Large Language Models"
  real title: "How Much Can We Forget about Data Contamination?"
  title match: NO (副标题完全不同——实际无副标题 "Examining Decontamination Effectiveness")
  bib authors: Zhang, Yiming and Wang, Yuxin and Dong, ...
  real authors: Sebastian Bordt, Suraj Srinivas, Valentyn Boreiko, Ulrike von Luxburg
  author match: NO (完全虚构——bib 为中国作者，实际是德国图宾根大学团队)
  notes: arXiv 2410.03249, ICML 2025. Venue 正确但标题篡改、作者完全编造。
```

```
[lyu2025atlas] STATUS: MISMATCH
  bib title: "ATLAS: Adaptive Testing via Latent Ability Scoring for Large Language Models"
  real title: "Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks"
  title match: NO (框架名 ATLAS 正确但正式标题完全不同)
  bib authors: Lyu, Haoran and Ding, Yufei and Wang, Ha...
  real authors: Peiyu Li, Xiuxiu Tang, Si Chen, Ying Cheng, Ronald Metoyer, Ting Hua, Nitesh V. Chawla
  author match: NO (全部虚构——Lyu Haoran 不在作者中)
  notes: arXiv 2511.04689. ATLAS 是论文内部的框架缩写，但 bib 把缩写展开错了（"via Latent Ability Scoring" 是编造的），作者全部错误。
```

```
[zhuang2025hibayes] STATUS: MISMATCH
  bib title: "HiBayES: Hierarchical Bayesian Evaluation System for Language Models"
  real title: "HiBayES: A Hierarchical Bayesian Modeling Framework for AI Evaluation Statistics"
  title match: NO ("Evaluation System for Language Models" vs "Modeling Framework for AI Evaluation Statistics")
  bib authors: Zhuang, Yuekai and Polo, Felipe Maia and...
  real authors: Lennart Luettgau, Harry Coppock, Magda Dubois, Christopher Summerfield, Cozmin Ududec
  author match: NO (完全虚构——Zhuang 和 Polo 均不在作者中)
  notes: arXiv 2505.05602, UK AISI 出品. 与可能存在的 luettgau_2025_hibayes 是同一篇论文但 bib 作者全错。确认为重复条目 + 作者幻觉。
```

```
[li2025dcr] STATUS: MISMATCH (幻觉拼凑)
  bib title: "DCR: ..."
  real title: 真实 DCR 论文为 "DCR: Quantifying Data Contamination in LLMs Evaluation" (Xu, Cheng et al., EMNLP 2025)
  title match: 无法判断（bib title 不完整）
  bib authors: Li, Yucheng and Flanigan, Frank and Sher...
  real authors (DCR): Cheng Xu, Nan Yan, Shuhao Guan, Changhong Jin, Yuke Mei, Yibing Guo, Tahar Kechadi
  author match: NO
  notes: Li Yucheng 的真实论文是 "Estimating Contamination via Perplexity"（单作者，ICLR 2025）。"Flanigan, Frank" 不存在——可能混淆了 Li 的合作者 Frank Guerin。"Sherborne" 也无据可查。此条目为幻觉拼凑，与已有 xu_2025_dcr 重复。
```

```
[chang2025benchmarking] STATUS: MISMATCH (年份/venue 错误)
  bib title: "A Survey on Evaluation of Large Language Models"
  real title: "A Survey on Evaluation of Large Language Models"
  title match: YES
  bib authors: Chang, Yupeng and Wang, Xu and Wang, Jin...
  real authors: Yupeng Chang, Xu Wang, Jindong Wang, Yuan Wu, Linyi Yang, Kaijie Zhu, Hao Chen, Xiaoyuan Yi, Cunxiang Wang, Yidong Wang, Wei Ye, Yue Zhang, Yi Chang, Philip S. Yu, Qiang Yang, Xing Xie
  author match: YES
  notes: 标题和作者正确，但 bib 标记 EMNLP 2025 是错误的。真实发表：arXiv 2023-07 (2307.03109)，正式发表于 ACM TIST vol.15(3), 2024-03。年份应为 2023/2024，venue 应为 ACM TIST。
```

---

**汇总**：
- MATCH: 1/10（sinharay）
- MISMATCH: 8/10（duan, wust, wang, zhang, lyu, zhuang, li, chang）
- NOT_FOUND: 1/10（xu2025kds — 完全幻觉）

严重程度排序：xu2025kds（完全不存在）> wust/lyu/zhuang/zhang/wang/li（作者全部编造）> duan（作者错误+标题篡改）> chang（仅年份/venue错误）。

---
