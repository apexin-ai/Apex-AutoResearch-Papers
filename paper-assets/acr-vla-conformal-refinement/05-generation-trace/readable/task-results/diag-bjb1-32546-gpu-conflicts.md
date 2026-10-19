# diag bjb1 32546 gpu conflicts

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_bjb1-32546-gpu-conflicts_20260521T025701_result.json`
- **Structured JSON:** [`d24b14376b85b7d6781c.json`](../../sessions/d2/d24b14376b85b7d6781c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### Part 1: bjb1-32546 调查结果

| 实验 | PID | 状态 | success_rate |
|------|-----|------|-------------|
| norm003_seed64 | 723784 | DONE | 0.17 |
| norm003_seed65 | 725722 | DONE | 0.17 |
| norm005_seed64 | 729873 | DONE | 0.15 |
| norm01_seed64 | 726800 | DONE | 0.15 |
| norm01_seed65 | 728057 | DONE | 0.15 |
| norm01_seed52_r3 | 733203 | DONE | 0.15 |
| norm003_seed63_r2 | 735998 | DONE(failed) | 无 JSON |
| norm01_seed51_r3 | 731912 | **仍在运行** (GPU 0) | — |
| vla_only_object_seed49 | 542620 | 已是 DONE | 0.10 |
| norm003_seed62_r2 | — | 已是 DONE | — |

GPU 2 被 PID 805840 (norm005_seed67) 占用；GPU 1/3/4/5 空闲。

### Part 2: 部署

- **eval-adaptive-k-spatial-p90-seed44-bjb2** → 已部署在 **bjb2-28827:cuda:0**（cuda:5 被 norm003-seed67 占用），PID 975409，registry 已更新为 RUNNING
- **eval-vla-only-spatial-seed50** → **无法部署**，bjb1-18228 四块 GPU 全满（PID 642428/666593/642506/642775）

---
