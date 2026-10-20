# eval gold dryrun v4

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_gold-dryrun-v4_20260515T010911_result.json`
- **Structured JSON:** [`8637c2d6d1ad3041e6c6.json`](../../sessions/86/8637c2d6d1ad3041e6c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Gold-set evaluation pipeline dry-run v4 完成。** Registry 已更新为 DONE/success。

### 结果摘要

| Model | N | Macro-F1 |
|---|---|---|
| MV Labels | 650 | 1.0000 |
| GRU Probe | 650 | 0.9639 |
|   └ gold_in_test | 203 | 0.9502 |
| Structural RF | 650 | 0.9967 |
| Structural GB | 650 | 0.9967 |
| TWV Labels | 650 | 0.9485 |
| TWV Probe | 650 | 0.9517 |

### 验证点全部通过
- Probe checkpoint 正确加载，无 shape mismatch
- Structural features 正确提取（5000 trajectories indexed, 30 features）
- TWV labels 正确加载和评估
- MV-Gold agreement = 1.0（符合预期，pseudo gold 来自 MV labels）
- 所有模型 n_evaluated = 650
- 所有 macro_f1 > 0.9（circular eval 预期内）
- Leakage-fix 正常工作：RF/GB 排除了 447/10634 gold windows from training
- 输出 results.json 和 report.md 格式正确

---
