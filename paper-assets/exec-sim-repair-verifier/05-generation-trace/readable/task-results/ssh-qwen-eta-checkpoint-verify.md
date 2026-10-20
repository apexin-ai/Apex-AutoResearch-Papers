# ssh qwen eta checkpoint verify

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_qwen-eta-checkpoint-verify_20260520T093039_result.json`
- **Structured JSON:** [`e88bf10cc8d2a4051d13.json`](../../sessions/e8/e88bf10cc8d2a4051d13.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已收集。以下是原始结果和计算所需的关键数据。

---

## s123 Checkpoint 时间戳 (CST +0800)

| Checkpoint | Modify Time | 备注 |
|-----------|-------------|------|
| 300 | 2026-05-20 **05:51:00** | 训练09:30才启动，此为旧 run 残留 |
| 900 | 2026-05-20 **15:31:21** | |
| 1000 | 2026-05-20 **16:10:46** | |
| 1100 | 2026-05-20 **16:50:16** | |
| 1200 | 2026-05-20 **17:29:48** | |

**100-step 间隔:**
- 900→1000: **39m25s** (2365s) → 23.65s/step
- 1000→1100: **39m30s** (2370s) → 23.70s/step
- 1100→1200: **39m32s** (2372s) → 23.72s/step

## s456 Checkpoint 时间戳 (CST +0800)

| Checkpoint | Modify Time |
|-----------|-------------|
| 300 | 2026-05-20 **11:32:52** |
| 900 | 2026-05-20 **15:26:19** |
| 1000 | 2026-05-20 **16:05:03** |
| 1100 | 2026-05-20 **16:43:53** |
| 1200 | 2026-05-20 **17:22:43** |

**100-step 间隔:**
- 900→1000: **38m44s** (2324s) → 23.24s/step
- 1000→1100: **38m50s** (2330s) → 23.30s/step
- 1100→1200: **38m50s** (2330s) → 23.30s/step

## 训练启动时间

- s123: `2026-05-20 09:30:05` — Loaded train=70748, val=9335
- s456: `2026-05-20 09:30:08` — Loaded train=70748, val=9335

## tqdm 当前进度

**s123** (tail): step **1207**/6633, elapsed 7:55:00, ~12s/it (纯训练), tqdm ETA ~17:55:30
**s456** (tail): step **1243**/6633, elapsed 7:54:51, ~12s/it (纯训练), tqdm ETA ~17:48:36

每 100 步触发一次 val eval（9335 samples @ ~8 it/s ≈ 19min）+ checkpoint save，这就是 tqdm 报 12s/it 但 wall-clock 实际 ~23.5s/step 的原因。

## Total steps: **6633**（tqdm 分母）

## 真实 ETA 计算

以 wall-clock rate（含 eval+save 开销）：

| | s123 | s456 |
|--|------|------|
| 当前 step | ~1207 | ~1243 |
| 剩余 steps | 5426 | 5390 |
| Wall-clock rate | 23.7s/step | 23.3s/step |
| **剩余时间** | **35.7h** | **34.9h** |
| **预计完成** | **~5/21 凌晨 5:10** | **~5/21 凌晨 4:20** |

（完成时间基于当前时刻 ~17:30 CST 推算）

---
