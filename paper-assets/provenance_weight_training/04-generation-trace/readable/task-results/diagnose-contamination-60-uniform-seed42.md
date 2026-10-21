# diagnose contamination 60 uniform seed42

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_contamination_60_uniform_seed42_20260516T010513_result.json`
- **Structured JSON:** [`0dd33240b0dc0006b4c3.json`](../../sessions/0d/0dd33240b0dc0006b4c3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

| 项目 | 结果 |
|------|------|
| 训练完成 | ✓ 6103/6103 steps, 3:35:04 |
| SIGHUP 原因 | 训练完成后发生（与 bs8_nmin2_seed42_r2 相同模式） |
| Checkpoint 有效 | ✓ final/ 目录，model.safetensors = 1.19GB |
| **Eval PPL** | **17.77** (loss=2.8773, 4.08M tokens) |
| Registry | conclusion 已更新为 success，metrics 已写入 |

与 bs8_nmin2_seed42_r2 (PPL=17.73) 几乎一致，符合 uniform baseline 预期。无需重新提交。

---
