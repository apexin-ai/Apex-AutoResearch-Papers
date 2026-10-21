# diag gsm8k qwen14b s123 exit

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_gsm8k-qwen14b-s123-exit_20260520T085124_result.json`
- **Structured JSON:** [`2f92f9e34defc338a7ec.json`](../../sessions/2f/2f92f9e34defc338a7ec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇报

| | s42 | s123 | 差异 |
|---|---|---|---|
| **d000** | 60.80% | **76.65%** (1011/1319) | **+15.85pp** |
| **d100** | 81.27% | 仍在运行 | — |

### 状态

- **d000_s123**: 已完成。Accuracy = **76.65%**
- **d100_s123**: **仍在运行**（PID 309330, cuda:1, 33GB VRAM, 95% util）。刚完成 5/165 batches（~3%），按 ~14s/batch 估算还需 ~37 分钟
- **cuda:1**: **未释放**，d100 eval 仍在占用

### 关键发现

d000（clean baseline）跨 seed 差异巨大：s123 比 s42 高 **+15.85pp**（76.65% vs 60.80%）。如果 d100_s123 的结果也大幅高于 s42，那 +20.47pp 的 contamination effect 估算需要重新审视——seed 本身引入的方差可能与 contamination effect 量级相当。

等 d100_s123 完成后才能算出 s123 的 Δ(d100-d000) 并与 s42 的 +20.47pp 对比。

---
