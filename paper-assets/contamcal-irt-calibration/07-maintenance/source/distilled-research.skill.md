---
name: distilled-research
description: "LLM benchmark contamination检测与校准领域的实验设计共识、baseline频率、方法论趋势与研究空白"
scope: project
version: 1
tags: [distilled, auto-generated]
distilled_from:
  paper_count: 25
  paper_keys: [dong_2024_cdd, deng_2024_tsguessing, xu_2025_dcr, sun_2025_emperors_new_clothes, li_2025_dcr, zhang_2024_minkpp, choi_2025_kds, lalor_2024_irt_nlp, polo_2024_tinybenchmarks, zhou_2025_psnirt, chiang_2024_chatbot_arena, golchin_2024_time_travel, shi_2023_minkprob, schaeffer_2026_generative_contamination, luettgau_2025_hibayes, zheng_2023_chatbot_arena, brown_2024_ppp, sinharay_2025_irt_fit, guo_2017_calibration, dekoninck_2024_constat, zhang_2024_gsm1k, habba_2025_growing_pains, li_2024_atlas, angelopoulos_2023_conformal, white_2024_livebench]
  last_distilled: "2026-05-23T12:00:00Z"
---

## Baseline 共识

- **Min-K% / Min-K%++** 是 token-level MIA 的标准 baseline（6/25 篇）。Min-K%++ 通过 (log p - μ)/σ 归一化超越 Min-K%，AUROC 提升 6-10pp（来源：Zhang et al. ICLR'25）。置信度：高。
- **Perplexity / Zlib / Ref model** 构成 reference-free/reference-based detection 的 baseline 三件套（5/25 篇）。置信度：高。
- **N-gram overlap + embedding similarity** 仍是最基础的 contamination 检测 baseline（4/25 篇），但多数新方法显著超越。置信度：高。

## Metric 共识

- **检测类**用 AUROC + TPR@FPR（5/25 篇，来源：Min-K%++, KDS）。置信度：高。
- **校准/调整类**用 adjusted accuracy ± correlation（3/25 篇，来源：DCR, CDD/TED）。置信度：中——目前无统一 metric 标准。
- **缓解策略评估**用 fidelity + resistance 对偶指标（1/25 篇，来源：Emperor's ICML'25）。置信度：低但值得注意——可能成为新标准。

## Dataset 共识

- **MMLU**（7/25 篇）和 **GSM8K**（6/25 篇）是 contamination 研究的事实标准 benchmark。置信度：高。
- **WikiMIA**（4/25 篇）是 MIA 方向的标准 benchmark（temporal split 提供 ground truth）。置信度：高。
- **MC 格式 benchmark（ARC, MMLU）比 generative（GSM8K, MATH）更易受 contamination 影响**（3/25 篇：deng TS-Guessing 52% EM on MMLU; schaeffer 发现 generative effect 更弱）。置信度：中。

## 方法论趋势

- **上升趋势**：IRT 进入 LLM 评估（6/25 篇：lalor, polo, zhou, habba, li_atlas + 本项目）；Bayesian UQ（2/25 篇：luettgau, 本项目）；kernel/embedding 方法（choi_kds）。置信度：高。
- **稳定**：token probability 方法（Min-K 系列）；prompt-based 检测（TS-Guessing, Time Travel）。
- **消退**：纯 n-gram overlap 检测正被取代。
- **关键转向**：从「检测是否 contaminated」转向「量化 contamination 的影响并校准」（3/25 篇：xu_dcr, li_dcr, dong_TED）。置信度：高——这正是本项目的定位。

## 竞品 claim 汇总

- **DCR (xu_2025)**：fuzzy inference 调整 accuracy，avg error ~3.5%，但无 UQ，无 per-domain 分析。
- **CDD/TED (dong_2024)**：output distribution peakedness 检测 + 分布过滤校正，up to 66.9% 缓解，但 point estimate only。
- **Li_2025_dcr**：decontamination + calibration + ranking，最接近竞品，但无 IRT grounding、无 Bayesian CI。
- **Emperor's (sun_2025)**：20 种缓解策略全部失败 → 强烈动机支持 post-hoc calibration 路线。

## 共同局限（频率排序）

1. **模型规模受限**（5/25 篇）：多数只测到 13B-72B，frontier 模型未覆盖。
2. **领域/任务覆盖不足**（5/25 篇）：常局限于 2-3 个 benchmark。
3. **缺乏 UQ**（4/25 篇）：point estimate without credible intervals。
4. **计算开销**（3/25 篇）：多次采样、fine-tuning 要求。

## 研究空白

- **检测 → 校准桥接**：多数论文只检测不校准（支持度：5/8 深度精读 detect-only）。置信度：高。
- **IRT + contamination 融合**：IRT 论文不考虑 contamination；contamination 论文不用 IRT（支持度：0/25 篇做过融合）。置信度：高。
- **Per-item / per-domain contamination effect**：所有调整方法是 aggregate-level（支持度：3/25 篇做 domain-level 但无 item-level）。置信度：高。
- **Fisher info identifiability**：无论文分析 N_models 多少时 contamination 参数可识别（支持度：0/25 篇）。置信度：高。
