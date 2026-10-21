# analysis exp 002 signals 3B d100 a32 s42

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_002_signals_3B_d100_a32_s42_20260516T104922_result.json`
- **Structured JSON:** [`51f7afccfe1a493dbdca.json`](../../sessions/51/51f7afccfe1a493dbdca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

W&B API 工具有 bug，跳过。数据已足够分析。

---

## exp_002_signals_3B_d100_a32_s42 分析报告

### 1. 完成状态：✅ SUCCESS

日志末尾 `=== Sat May 16 18:45:54 CST 2026 | d100_a32_s42 ALL_DONE ===`，所有 9 个 signal 文件正常生成。

### 2. 产出文件确认（9/9 齐全）

| Benchmark | s1_embedding | s2_minkpp | s4_selfcritique |
|-----------|:---:|:---:|:---:|
| mmlu | ✅ (7.8MB) | ✅ (2.9MB) | ✅ (3.3MB) |
| gsm8k | ✅ (733KB) | ✅ (272KB) | ✅ (317KB) |
| arc_challenge | ✅ (663KB) | ✅ (250KB) | ✅ (290KB) |

### 3. Signal 数值汇总 & d100 vs d000 对比

| Benchmark | Signal | d000 mean | d100 mean | Δ | 方向符合预期? |
|-----------|--------|-----------|-----------|---|:---:|
| **mmlu** | s1_embedding | +0.4788 | **+0.7725** | +0.2937 | ✅ 升高=更像训练数据 |
| | s2_minkpp | -1.7111 | **-1.4034** | +0.3077 | ✅ 升高(less negative)=更可能被记忆 |
| | s4_selfcritique | -0.8500 | **-0.8786** | -0.0286 | ⚠️ 微降，变化小 |
| **gsm8k** | s1_embedding | +0.6069 | **+0.8062** | +0.1993 | ✅ |
| | s2_minkpp | -1.6277 | **-1.4585** | +0.1692 | ✅ |
| | s4_selfcritique | -0.7114 | **-0.7404** | -0.0290 | ⚠️ 微降 |
| **arc_challenge** | s1_embedding | +0.5455 | **+0.7596** | +0.2141 | ✅ |
| | s2_minkpp | -1.7214 | **-1.3550** | +0.3665 | ✅ |
| | s4_selfcritique | -0.8193 | **-0.8361** | -0.0168 | ⚠️ 微降 |

### 4. 分析

**s1_embedding（cosine similarity）**：d100 在所有 benchmark 上均大幅升高（+0.19 ~ +0.29），说明 100% 污染模型的训练数据与 benchmark items 的 embedding 相似度显著更高。信号方向强且一致。

**s2_minkpp（Min-K++）**：d100 在所有 benchmark 上显著升高（+0.17 ~ +0.37），即 perplexity 更低，模型对 benchmark items 更"熟悉"。ARC 变化最大（+0.37），符合直觉（小数据集+100%污染 → 记忆效应更强）。信号方向强且一致。

**s4_selfcritique**：三个 benchmark 变化幅度均很小（-0.017 ~ -0.029），且方向为微降。s4 对 d100 vs d000 的区分度较弱，可能需要后续在 RRF 聚合时降权。

### 5. 结论

**SUCCESS** — d100 相对 d000 的 s1/s2 信号变化方向完全符合预期，区分度大。s4 区分度较弱但未出现反向异常。

**3B s42 全齐（d000 + d100），可以跑 RRF 聚合。**

（注：W&B list_wandb_runs 工具报 `wandb_project` 参数错误，未能拉取 W&B 指标，但服务器端数据已充分验证实验完成。）

---
