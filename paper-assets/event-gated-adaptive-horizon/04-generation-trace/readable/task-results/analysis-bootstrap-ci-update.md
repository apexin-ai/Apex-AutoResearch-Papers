# analysis bootstrap ci update

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bootstrap-ci-update_20260516T174322_result.json`
- **Structured JSON:** [`2523eebb102951426ae6.json`](../../sessions/25/2523eebb102951426ae6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。更新内容：

1. **脚本** (`compute_bootstrap_cis.py`): SGS_full 数据替换为 018v2（NVE peak=4.01, eval=448.34, collapse=0），注释标注 018 无效原因
2. **汇总** (`bootstrap_ci_summary.md`):
   - SGS_full 行已更新为 018v2 point estimates
   - NVE >1.5× exceedance: SGS_full 从 0.000 → 1.000（4.01 > 1.5）
   - 新增 "SGS_full − trained_dt_emb" effect size 表（eval +216, collapse −0.667）
   - Independence Notes 中标注 018 排除原因和 seed 2 需求

关键发现：SGS_full (018v2) 比 trained_dt_emb 的 eval return 高 +216（448 vs 232），且无 collapse，但 n=1 无法计算 CI。

---
