# diag qwen14b s123 d100 final

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_qwen14b-s123-d100-final_20260520T092918_result.json`
- **Structured JSON:** [`79f22f43a99b35fd516d.json`](../../sessions/79/79f22f43a99b35fd516d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**d100 已完成。** 刚刚跑完（17:29:10，约 1 分钟前）。

| seed | d000 | d100 | Δ(d100−d000) |
|------|------|------|-------------|
| s42 | 60.80% | 81.27% | +20.47pp |
| s123 | 76.65% | **82.34%** | **+5.69pp** |

d100 s123 accuracy = **82.34%** (1086/1319)

cuda:1 已释放（0MiB）。cuda:0 和 cuda:2 仍有进程在跑。

注意：s123 的 Δ 只有 +5.69pp，远小于 s42 的 +20.47pp。d000 基线差异很大（s42=60.80% vs s123=76.65%），但 d100 几乎持平（81.27% vs 82.34%），说明 contamination 的边际效应在高基线下大幅缩小——这对 IRT calibration 的 dosage-response 建模很重要。

---
