# ops 3B s42 signals status and merge

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_3B_s42_signals_status_and_merge_20260516T102324_result.json`
- **Structured JSON:** [`eefaf74933dc081e7927.json`](../../sessions/ee/eefaf74933dc081e7927.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

d100_a32_s42 目前只有 mmlu 的 s1+s2（2/9），加上正在跑的 s4 mmlu chunks。还需 gsm8k 和 arc_challenge 的全部信号。

## 汇总

### 1. d000_a32_s42 — DONE ✅
- 9/9 信号文件完整（3 benchmark × 3 signals）
- 3 merged 文件已生成：mmlu (14042), gsm8k (1319), arc_challenge (1172)
- Registry 已更新：`exp_002_signals_3B_d000_a32_s42` → DONE/success

### 2. d025_v3_s42 — DONE ✅
- 9/9 信号文件完整
- 3 merged 文件已生成：同上 item 数
- Registry 已更新：`exp_002_signals_3B_d025_v3_s42` → DONE/success

### 3. d005_a32_s42 — 之前已 DONE ✅

### 4. d100_a32_s42 — 仍在运行 🔄
- 当前进度：2/9（mmlu 的 s1_embedding + s2_minkpp 完成，s4_selfcritique mmlu 正在 chunk 中）
- 还缺：gsm8k 全部 3 signals + arc_challenge 全部 3 signals + s4 mmlu 完成
- 在某个 GPU 上运行中

### GPU 4 状态
**空闲，0 MiB / 0% 利用率**，可用于下一任务。

### 3B s42 signals 覆盖率
| Dosage | Signals | Merged | Status |
|--------|---------|--------|--------|
| d000_a32 | 9/9 | 3/3 | ✅ DONE |
| d005_a32 | 9/9 | 3/3 | ✅ DONE |
| d025_v3 | 9/9 | 3/3 | ✅ DONE |
| d100_a32 | 2/9 | 0/3 | 🔄 RUNNING |

**3/4 dosage 完成，d100 预计还需较长时间（7 个信号待完成）。GPU 4 空闲可分配。**

---
