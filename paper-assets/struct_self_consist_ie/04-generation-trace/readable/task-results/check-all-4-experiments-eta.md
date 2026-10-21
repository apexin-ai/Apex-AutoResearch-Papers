# check all 4 experiments eta

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_all-4-experiments-eta_20260519T203940_result.json`
- **Structured JSON:** [`c14491112774312d8505.json`](../../sessions/c1/c14491112774312d8505.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

当前时间约 05-19 20:45 UTC。汇总如下：

| 实验 | 状态 | 进度 | 更新 ETA (UTC) |
|---|---|---|---|
| **exp_qwen25_7b_fewnerd** | RUNNING | Phase 1 训练 63% (13016/20590), ~2.35s/step | 训练完 ~05-20 01:45, 全 pipeline ~**05-20 04:00** |
| **exp_qwen25_72b_fewshot** | RUNNING | Dataset 2/3 (conll2003) 56% (169784/301184), ~15 it/s | conll 完 ~+2.5h, fewnerd 待跑 → **05-20 06:00+** |
| **exp_qwen25_14b_fewnerd** | RUNNING | 训练 42.5% (17500/41180), log 显示剩余 17h | **~05-20 13:45** |
| **exp_qwen25_32b_fewnerd** | RUNNING | 训练 29.1% (12000/41180), log 显示剩余 1d2h27m | **~05-20 23:15** |

关键变化：
- **7B** 远未完成——仍在 Phase 1 训练（还有 7574 步 ≈ 5h），之后还需 export → inference (3 seeds) → analysis → entity construction，比原 ETA (05-19 20:00) 延迟约 **8h**
- **72B fewshot** scierc 已完成，conll2003 进行到 56%，fewnerd 尚未开始，比原 ETA (05-20 00:00) 延迟约 **6h+**
- **14B** 和 **32B** 均大幅慢于预期，分别延迟 ~11h 和 ~13h

---
