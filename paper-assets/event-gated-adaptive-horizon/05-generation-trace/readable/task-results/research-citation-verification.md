# research citation verification

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_citation-verification_20260521T123315_result.json`
- **Structured JSON:** [`a4a84ad16ebf48073867.json`](../../sessions/a4/a4a84ad16ebf48073867.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 引用验证报告

---

### 1. Turcato et al. 2024 — ✅ 已验证

| 字段 | 声称 | 实际 |
|------|------|------|
| arXiv ID | 2402.09078 | **2402.09078** ✅ |
| 标题 | (未明确) | *Exploiting Estimation Bias in Clipped Double Q-Learning for Continuous Control Reinforcement Learning Tasks* |
| 作者 | Turcato | **Niccolò Turcato**, Alberto Sinigaglia, Alberto Dalla Libera, Ruggero Carli, Gian Antonio Susto ✅ |
| Venue | (未明确) | arXiv preprint（2024-02 提交，2024-10 修订，未见会议发表记录） |
| 核心 claim | environment-dependent bias preference: Walker/Ant 偏好 underestimation，Swimmer/Reacher 偏好 overestimation | **匹配** — 论文研究不同环境中 estimation bias 的影响，设计 Bias Exploiting (BE) 机制动态选择最优 bias ✅ |

---

### 2. CrossQ (Bhatt et al.) — ✅ 已验证

| 字段 | 声称 | 实际 |
|------|------|------|
| arXiv ID | (未提供) | **1902.05605**（2019 年首次提交，多次修订） |
| 标题 | CrossQ | *CrossQ: Batch Normalization in Deep Reinforcement Learning for Greater Sample Efficiency and Simplicity* ✅ |
| 作者 | Bhatt et al. | **Aditya Bhatt**, Daniel Palenicek, Boris Belousov, Max Argus, Artemij Amiranashvili, Thomas Brox, Jan Peters ✅ |
| Venue | ICLR 2024 | **ICLR 2024 (Top 5% Spotlight)** ✅ |
| 核心 claim | implicit regularization (BN) > explicit pessimism (min-of-two)；2 个 critic 降到 1 个效果更好 | **匹配** — 通过 BatchNorm 提供隐式正则化，移除 target network，使用单个 double-Q 网络做 joint forward pass，不依赖传统的 bias-reduction schemes ✅ |

---

### 3. DARC — ✅ 已验证

| 字段 | 声称 | 实际 |
|------|------|------|
| arXiv ID | (未提供) | **2106.03050** |
| 标题 | DARC (double actors + regularized critics) | *Efficient Continuous Control with Double Actors and Regularized Critics* ✅ |
| 作者 | (未提供) | **Jiafei Lyu**, Xiaoteng Ma, Jiangpeng Yan, Xiu Li |
| Venue | AAAI 2022 | **AAAI 2022** ✅ |
| 核心 claim | double actors + regularized critics | **完全匹配** — 双 actor 改善探索并缓解 overestimation，regularized critics 缓解双 critic 的 pessimistic estimate ✅ |

---

## 总结

3 篇论文全部真实存在，核心 claim 均与原文一致，**无幻觉**。补充缺失信息：

- Turcato et al.: 目前仍为 arXiv preprint，引用时注意标注
- CrossQ: arXiv ID 为 `1902.05605`（非 2024 年 ID，首次提交于 2019 年）
- DARC: arXiv ID 为 `2106.03050`，作者为 Lyu, Ma, Yan, Li

Sources:
- [Turcato et al. 2402.09078](https://arxiv.org/abs/2402.09078)
- [CrossQ - arXiv](https://arxiv.org/abs/1902.05605)
- [CrossQ - OpenReview ICLR 2024](https://openreview.net/forum?id=PczQtTsTIX)
- [DARC - AAAI Proceedings](https://ojs.aaai.org/index.php/AAAI/article/view/20732)
- [DARC - arXiv](https://arxiv.org/abs/2106.03050)
- [DARC - GitHub](https://github.com/dmksjfl/DARC)

---
