# exp docred int4 quant check and run

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_docred-int4-quant-check-and-run_20260523T054733_result.json`
- **Structured JSON:** [`94e337189606d9b947fa.json`](../../sessions/94/94e337189606d9b947fa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个任务已并行启动：

| GPU | 实验 | PID | 状态 |
|-----|------|-----|------|
| cuda:0 | `sf2_qwen_int4_docred_s1` | 21101 | 量化中 (4/36 layers) |
| cuda:1 | `sf2_llama_int4_docred_s1` | 21381 | 量化中 (0/32 layers) |

**流水线**：量化 (~30min) → 推理 full_s1 200 docs (~1-2h) → eval_d064.py

**FP16 baseline 用于对比**：
- Qwen FP16: `d065_qwen_greedy_4096_r2` → R-F1=40.79, E-F1=81.87, DR=0% (998 docs)
- Llama FP16: `d066_sweep_llama_docred_beam1_s1` → R-F1=47.35, E-F1=85.43, DR=0% (200 docs)

注意：Qwen 没有 200-doc FP16 baseline（beam sweep 结果未记录），INT4 用 200 docs 跑，对比时需注明 sample count 不同。

等量化完成后再来检查推理进度。

---
