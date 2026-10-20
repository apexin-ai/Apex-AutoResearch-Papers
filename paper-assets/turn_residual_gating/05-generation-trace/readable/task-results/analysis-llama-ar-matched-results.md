# analysis llama ar matched results

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_llama_ar_matched_results_20260521T042630_result.json`
- **Structured JSON:** [`1388014f2a13beb33953.json`](../../sessions/13/1388014f2a13beb33953.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### Part 1: Llama AR Matched Eval 结果

4 条件全部完成，matched 设置 (N=50, T=4)：

| Condition | mid GAR | nGAR | PPL |
|-----------|---------|------|-----|
| AR Base ours | 0.0082 | 0.100 | 1.267 |
| **AR TG ours** | **0.0388** | **0.493** | 1.413 |
| AR Base dongre | 0.0051 | 0.120 | 1.267 |
| **AR TG dongre** | **0.0180** | **0.431** | 1.413 |

**关键发现——TF-AR gap 是归一化伪影，非真实效果衰减：**

- **GAR-dongre**: AR TG = 0.0180 ≈ TF TG = 0.0180 — **raw GAR 完全一致**，gap = 0
- **GAR-ours**: AR TG raw = 0.0388 vs TF TG raw = 0.4836（12.5× gap），但 **nGAR 对齐**：AR = 0.493 ≈ TF ~0.48
- 之前的 "16× unmatched gap" 主要是设置差异 + 归一化方式造成的

TG 在 AR 模式下的效果完全保持：TG/Base ratio = 4.71× (ours) / 3.54× (dongre)。Gate 动态范围也正常（L28 diff = -0.38, L30 = -0.33）。

### Part 2: v8b SS s123 已提交

- PID 221735, westd-20861
- Step 0 正常：loss=1.6255, gate mean=0.8118, 53GB VRAM
- 3 epochs × 1000 steps, seed=123, SS max_ratio=0.5
- Registry: `v8b_ss_s123` → RUNNING

---
