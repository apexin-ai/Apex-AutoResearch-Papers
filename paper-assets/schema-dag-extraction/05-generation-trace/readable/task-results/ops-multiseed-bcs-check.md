# ops multiseed bcs check

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_multiseed_bcs_check_20260518T080629_result.json`
- **Structured JSON:** [`ba2648f98de6bb31e741.json`](../../sessions/ba/ba2648f98de6bb31e741.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

没有活跃的 cron job，跳过。

---

## 实验结果汇报：exp_multiseed_bcs_re

**状态：DONE (success)**

两个 seed 均完整完成，各 150 批次 × 96 samples = 14400 results。

### Seed 123

| Condition | Low Acc | High Acc | Delta (pp) | 95% CI |
|-----------|---------|----------|------------|--------|
| 0-shot | 0.6696 | 0.4508 | **+21.88** | [18.79, 24.83] |
| 1-shot | 0.7342 | 0.4817 | **+25.25** | [21.08, 29.29] |
| 5-shot | 0.6650 | 0.4225 | **+24.25** | [19.96, 28.29] |

### Seed 456

| Condition | Low Acc | High Acc | Delta (pp) | 95% CI |
|-----------|---------|----------|------------|--------|
| 0-shot | 0.6808 | 0.4571 | **+22.38** | [19.58, 24.96] |
| 1-shot | 0.7279 | 0.4842 | **+24.38** | [20.58, 28.04] |
| 5-shot | 0.6796 | 0.4288 | **+25.08** | [21.62, 28.58] |

### 关键发现

1. **BCS 效应跨 seed 稳定复现**：两个 seed 的 0-shot delta 分别为 +21.88pp 和 +22.38pp，高度一致，所有 CI 不含零。回应了 R15-W2 的 single-seed concern。
2. **Few-shot 不缓解 BCS 效应**：delta 从 0-shot 的 ~22pp 反而增加到 5-shot 的 ~25pp。两个 seed 均观察到相同趋势。

### 结果文件路径
- `seed_123/`: `/root/schema-dag-extraction/artifacts/multiseed_bcs_re/seed_123/` (analysis.json, results_incremental.jsonl, run.log)
- `seed_456/`: `/root/schema-dag-extraction/artifacts/multiseed_bcs_re/seed_456/` (同上)
- 总日志: `/root/schema-dag-extraction/artifacts/multiseed_bcs_re/run_all.log`

---
