# fix mistral uniform ppl bug and orphan kill

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_mistral_uniform_ppl_bug_and_orphan_kill_20260515T150250_result.json`
- **Structured JSON:** [`8a15953cb787c29c29e7.json`](../../sessions/8a/8a15953cb787c29c29e7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

### Part 1: Orphan Kill
- PID 343246/343582 在任务开始前已自行退出，GPU 0/1 均空闲（0MiB）

### Part 2: Root Cause
- **Bug**：`run_mistral_hires_constrained.py` line 118 调用 `uniform_quantization_baseline(profiles, budget)` 将 `budget=0.25` 传入 `bits` 参数
- **机制**：`bits=0.25` → `str(0.25)="0.25"` 不在 quantization dict 中 → distortion 默认 0，但 allocation 写入 `["quant", 0.25]` → patch_attention 按 0.25-bit 量化 → PPL 50130
- **修复**：改为 `uniform_quantization_baseline(profiles, bits=4)`

### Part 3: Reeval 结果
| Method | PPL |
|--------|-----|
| Baseline (bf16) | 7.0352 |
| MCKP (k=2) | 7.1341 |
| **Uniform 4-bit (fixed)** | **7.1308** |

- MCKP vs uniform delta = **-0.0033**（MCKP 略差于 uniform）
- Verdict: FAIL — 符合 Flat model 预期（Mistral concentration 低，MCKP 没有优势空间）
- 实验 `mistral_uniform_reeval` 已完成并注册 DONE
- 两个 GPU 均已释放

---
