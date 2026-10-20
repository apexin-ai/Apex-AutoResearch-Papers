# ops tau 2chain extraction

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_tau_2chain_extraction_20260517T154744_result.json`
- **Structured JSON:** [`59ca3b5e32ab9b3c8c5e.json`](../../sessions/59/59ca3b5e32ab9b3c8c5e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Full MMLU τ (14042 items, 2 chains) — 结果

| 指标 | τ | p-value |
|------|---|---------|
| Vanilla 2PL theta vs dosage | **0.0237** | 0.893 |
| Calibrated score vs dosage | 0.0237 | 0.893 |
| Raw accuracy vs dosage | 0.1185 | 0.501 |

### θ per model

| Model | Dosage | θ | cal_score | raw_acc |
|-------|--------|-----|-----------|---------|
| 1.5B_d000_s123 | 0 | 0.3688 | 0.5995 | 0.5855 |
| 1.5B_d000_s42 | 0 | 0.3752 | 0.6005 | 0.5853 |
| 1.5B_d005_s123 | 5 | 0.3963 | 0.6037 | 0.5869 |
| 1.5B_d005_s42 | 5 | 0.3706 | 0.5998 | 0.5852 |
| 1.5B_d025_s123 | 25 | 0.3821 | 0.6015 | 0.5881 |
| 1.5B_d025_s42 | 25 | 0.3818 | 0.6015 | 0.5902 |
| 1.5B_d100_s123 | 100 | 0.4157 | 0.6066 | 0.5956 |
| 1.5B_d100_s42 | 100 | 0.3692 | 0.5996 | 0.5933 |
| Llama-3B_d000 | 0 | -0.6056 | 0.4184 | 0.4545 |
| Llama-3B_d005 | 5 | -0.7606 | 0.3862 | 0.4256 |
| Llama-3B_d025 | 25 | -0.8513 | 0.3676 | 0.4150 |
| Llama-3B_d100 | 100 | -1.1898 | 0.3008 | 0.3408 |
| Qwen-3B_d000_s123 | 0 | 0.7854 | 0.6595 | 0.6332 |
| Qwen-3B_d000_s42 | 0 | 0.7637 | 0.6565 | 0.6307 |
| Qwen-3B_d005_s123 | 5 | 0.7888 | 0.6600 | 0.6324 |
| Qwen-3B_d005_s42 | 5 | 0.7667 | 0.6569 | 0.6308 |
| Qwen-3B_d025_s123 | 25 | 0.7909 | 0.6602 | 0.6367 |
| Qwen-3B_d025_s42 | 25 | 0.6761 | 0.6444 | 0.6242 |
| Qwen-3B_d100_s123 | 100 | 0.7790 | 0.6586 | 0.6330 |
| Qwen-3B_d100_s42 | 100 | 0.7803 | 0.6588 | 0.6364 |

### Rhat (2 chains)
- Range: [0.9995, 1.0026]
- All < 1.01 — 2 chains 收敛良好

### Per-group τ (theta vs dosage)
- **1.5B**: τ=0.31 (p=0.31) — 弱正向，不显著
- **Llama-3B**: τ=**-1.00** (p=0.08) — 完全负相关，contamination 训练摧毁了 MMLU 能力
- **Qwen-3B**: τ=0.08 (p=0.80) — 基本为零

### 对比与解读

| 设置 | τ | p |
|------|---|---|
| 300-item subsampled | 0.6377 | 0.0061 |
| **14k-item full (2 chains)** | **0.0237** | **0.893** |

**核心发现**: 在 full MMLU 上 vanilla 2PL 完全检测不到 contamination signal。原因：
1. 14k items 中仅 ~300 (2%) 被 contaminate，信号被稀释
2. Llama-3B 出现灾难性遗忘——contamination 训练反而大幅降低整体 MMLU 表现（raw acc 从 0.45 降到 0.34）
3. Qwen-3B 的 θ 在各 dosage 间几乎无差异

这验证了 ContamCal item-level exposure-weighted 模型的必要性：需要 item-level 污染信息才能分离信号。Vanilla IRT 将所有 items 等权处理，clean items 主导了 ability estimate。

---
