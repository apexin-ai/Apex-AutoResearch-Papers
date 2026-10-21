# diagnose d000 mmlu signals rrf

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_d000-mmlu-signals-rrf_20260516T204533_result.json`
- **Structured JSON:** [`ee73811b78dc9119806e.json`](../../sessions/ee/ee73811b78dc9119806e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

1. **d000 MMLU signals — 完成** ✓  
   `signals_merged_mmlu.json` 2.5MB, May 17 04:44

2. **RRF 运行 — 成功** ✓  
   - `exposure_scores.json`: 15.9MB, 540k 行（含所有 respondent × benchmark 组合）
   - `exposure_aggregated.json`: 418KB, 按 benchmark 聚合（arc_challenge, gsm8k, mmlu）
   - 涵盖所有模型包括 Llama-3.2-3B_d000_s42 MMLU、各 Qwen 0.5B/1.5B/3B 配置
   - 比旧 RRF（02:58, 509k行）多了 ~31k 条记录（即 MMLU 新增信号）

3. **GPU 1 — 空闲**，无运行中进程

---
