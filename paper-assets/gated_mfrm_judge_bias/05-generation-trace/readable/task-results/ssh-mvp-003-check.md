# ssh mvp 003 check

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_mvp_003_check_20260521T204409_result.json`
- **Structured JSON:** [`74a59e3fa6e51f1b52b3.json`](../../sessions/74/74a59e3fa6e51f1b52b3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇报如下：

---

## mvp_003 结果

### 1. 结果表

| method | RMSE mean±std | τ mean±std | p-value |
|--------|--------------|------------|---------|
| raw_average | 0.8063±0.0841 | 0.8401±0.0347 | — |
| mfrm_only_v3 | 0.2539±0.0448 | 0.8388±0.0345 | — |
| sequential_v3 | 0.2211±0.0376 | 0.8593±0.0293 | ref |
| **joint_gmfrm_v3** | **0.1243±0.0164** | **0.9223±0.0098** | **0.000001** |

### 2. 收敛诊断

| 指标 | mvp_002 | mvp_003 | 变化 |
|------|---------|---------|------|
| max R̂ | 1.05 | **1.03** | 改善 |
| min ESS | 47 | **224** | **4.8x 提升** |

ESS 从 47 提升到 224，远超 100 阈值。NCP + target_accept=0.95 + 2000 warmup + 4000 samples 的调优完全解决了收敛问题。

### 3. VERDICT: **PASS**

两项子检验均通过：
- 收敛检验：PASS（R̂=1.03 < 1.05, ESS=224 > 100）
- Wilcoxon 检验：PASS（p=0.000001）

### 4. 与 mvp_002 对比

| 指标 | mvp_002 | mvp_003 | 变化 |
|------|---------|---------|------|
| Verdict | **FAIL** | **PASS** | 翻转 |
| joint RMSE | 0.1486±0.0199 | 0.1243±0.0164 | **-16.4%** |
| joint τ | 0.9028±0.0181 | 0.9223±0.0098 | +0.0195 |
| RMSE reduction vs seq | 32.8% | **43.8%** | +11pp |
| joint τ std | 0.0181 | **0.0098** | 方差减半 |
| 运行时间 | 1935s | 4385s | 2.3x（符合预期，4x samples） |

MCMC 调优不仅修复了收敛，还带来了实质性的估计精度提升——joint RMSE 降低 16.4%，τ 方差减半，说明 mvp_002 的收敛不足确实导致了估计偏差。

### 5. Registry 更新

- `status`: RUNNING → **DONE**
- `conclusion`: **success**
- `metrics`: 完整记录（含 verdict, convergence, 各 method RMSE/τ, p-value, runtime）
- `checkpoint_path`: `/root/gated_mfrm_judge_bias/mvp/results_mvp003.csv`
- `log_path`: `/tmp/mvp_003.log`

---
