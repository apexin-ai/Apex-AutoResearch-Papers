# ssh bulk check running experiments

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_bulk-check-running-experiments_20260517T095258_result.json`
- **Structured JSON:** [`eed73efe80f1e64e78a8.json`](../../sessions/ee/eed73efe80f1e64e78a8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All processes checked. Here's the summary:

## 全部 13 个实验仍在运行，无一完成

### bjb1-18228 — 3 experiments, all RUNNING

| PID | Exp ID | Elapsed | Status |
|-----|--------|---------|--------|
| 474319 | eval-obs-only-object-norm01-seed45 | **1d 00:50** | Rl |
| 587763 | eval-obs-only-object-norm01-seed46-r2 | 3:02 | Rl |
| 588037 | eval-obs-only-object-norm01-seed47-r2 | 3:02 | Rl |

No JSON output files yet.

### bjb1-32546 — 4 experiments, all RUNNING

| PID | Exp ID | Elapsed | Status |
|-----|--------|---------|--------|
| 319128 | eval-obs-only-object-norm02-seed47 | **12:20** | Rl |
| 319463 | eval-perdof-object-norm03-seed45-r2 | **12:19** | Rl |
| 322337 | eval-argmin-object-seed47 | **12:14** | Rl |
| 393646 | eval-perdof-object-norm01-seed46-r2 | 3:02 | Rl |

No JSON output files yet. Note: PID 322337 is actually running `--mode reconvla` (output: `eval_object_reconvla_seed47.json`), not argmin as labeled in registry.

### bjb2-28827 — 6 processes (5 experiments + 1 extra), all RUNNING

| PID | Exp ID | Elapsed | Status |
|-----|--------|---------|--------|
| 242264 | eval-obs-only-object-default-seed45 | **23:09** | Rl |
| 224623 | eval-scalar-object-seed45 | **1d 01:16** | S (bash wrapper) |
| 222824 | eval-perdof-object-norm02-seed45 | **1d 01:20** | S (bash wrapper) |
| 326081 | eval-perdof-object-norm02-seed44 | **9:16** | Rl+ |
| 363223 | eval-obs-only-object-norm01-seed47-bjb2 | 2:59 | Rl |
| 365893 | eval-obs-only-object-norm01-seed46-bjb2 | 2:44 | Rl+ |

No JSON output files for any current runs. (Pre-existing JSONs on this server are from earlier completed experiments.)

Note: PID 365893 outputs to `results/` not `logs/`.

### bjb2-40593 — idle
GPU 0: 0 MiB, 0% utilization. Fully available.

## 总结

| 状态 | 数量 |
|------|------|
| 仍在运行 | 13 |
| 已完成 | 0 |
| 已失败 | 0 |
| 空闲 GPU | bjb2-40593 (1x GPU) |

两个需注意的问题：
1. **Registry 不一致**: `eval-argmin-object-seed47` (PID 322337) 实际跑的是 `reconvla` 模式
2. **输出路径不一致**: PID 365893 输出到 `results/` 而非 `logs/`，可能导致后续检查遗漏

---
