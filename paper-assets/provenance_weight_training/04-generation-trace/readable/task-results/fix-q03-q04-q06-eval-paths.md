# fix q03 q04 q06 eval paths

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_q03-q04-q06-eval-paths_20260518T215010_result.json`
- **Structured JSON:** [`9f2ceea853059719915f.json`](../../sessions/9f/9f2ceea853059719915f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个 eval 全部完成。结果汇总：

| 实验 | Perplexity | Loss |
|------|-----------|------|
| q03 (detect_remove_q03_seed42_r2) | **17.25** | 2.8480 |
| q04 (detect_remove_q04_seed42) | **17.26** | 2.8485 |
| q06 (detect_remove_q06_seed42) | **17.30** | 2.8507 |

三个结果非常接近（17.25–17.30），差异在噪声范围内。

根因：checkpoint 路径应为 `/root/autodl-tmp/output/models/...`，原始路径多了一层 `provenance_weight_training/`。

---
