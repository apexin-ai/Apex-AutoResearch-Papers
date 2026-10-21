# code exp 003 followup

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_003_followup_20260516T050317_result.json`
- **Structured JSON:** [`2e84e229b212b7918222.json`](../../sessions/2e/2e84e229b212b7918222.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三项任务全部完成：

**1. 文件持久化** — 6 个文件/目录从 `/tmp/` 复制到 `/root/autodl-tmp/exp003/`：`exp003_results.json`, `exp003_flagged_items.json`, `exp003_item_alignment.py`, `item_aligned_gap.py`, `exp003_mock/`, `exp003_real_test/`, `test_exp003/`。

**2. Within-size 对比表** — 写入 `/root/autodl-tmp/exp003/within_size_gap_table.md`。关键发现：

| Size | d000 gap | d100 gap | Delta (d100−d000) |
|------|----------|----------|--------------------|
| 1.5B | −2.14 pp | −2.85 pp | **−0.71 pp** |
| 3B   | −1.73 pp | −2.52 pp | **−0.80 pp** |

控制 model-size 后，d100 确实比 d000 的 para-aligned gap 更大约 0.7-0.8pp，说明污染使 aligned 版本相对更容易（或 para 版本更容易），但效应量较小。

**3. Registry 更新** — `exp_003_mmlu_item_aligned_gap` 的 notes 已更新，包含三点结论（systematic artifact / model-size confound / baseline correction 需求）。

---
