# diagnose exp A final check

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_A_final_check_20260515T111450_result.json`
- **Structured JSON:** [`cb0d7ef87d62c9c37c45.json`](../../sessions/cb/cb0d7ef87d62c9c37c45.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## EXP-A 最终状态：4/4 组全部完成

日志末尾明确输出 `========== ALL 4 RUNS COMPLETE ==========`。进程正常退出（不是 OOM），cron 报 "Process gone" 是因为实验跑完了。

### 汇总

| # | Scorer | Generator Data | K* | AUC(0v1) | AUC(1v2) | Ordinal MAE | Ordinal Acc | Spearman ρ vs baseline |
|---|--------|---------------|-----|----------|----------|-------------|-------------|----------------------|
| 1 | Pythia-1.4B | Qwen-RW | **2** | 0.9923 | 0.7012 | 1.006 | 0.417 | 0.906 |
| 2 | Pythia-1.4B | Qwen-cont | **1** | 0.9900 | 0.5923 | 1.216 | 0.371 | 0.942 |
| 3 | OLMo-1B | Qwen-RW | **2** | 0.9918 | 0.6947 | 1.016 | 0.413 | 0.920 |
| 4 | OLMo-1B | Qwen-cont | **1** | 0.9890 | 0.5858 | 1.229 | 0.368 | 0.902 |

### 关键发现

**K\* 不全是 2**，按 generator data 分裂：
- **Qwen-RW 数据 → K\*=2**（两个 scorer 一致）
- **Qwen-cont 数据 → K\*=1**（两个 scorer 一致）

原因清晰：Qwen-cont 数据上 AUC(1v2) 只有 ~0.59，未过 θ=0.60 阈值；Qwen-RW 数据上 AUC(1v2) ~0.70，轻松过线。这说明 K\* 差异来自 **generator data 的性质**，而非 scorer 选择。

**Feature importance**：4 组 Top-3 都是 `freq_entropy`、`surp_mean`、`hapax_ratio`/`surp_d1_skew`，高度一致。

**Spearman ρ 全部 ≥ 0.90**（p=0.0），替代 scorer 的 feature importance ranking 与 Qwen baseline 高度相关，验证了 scorer 无关性。

---
