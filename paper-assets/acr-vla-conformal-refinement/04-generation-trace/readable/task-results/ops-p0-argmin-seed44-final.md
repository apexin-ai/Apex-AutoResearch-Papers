# ops p0 argmin seed44 final

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_p0-argmin-seed44-final_20260516T144501_result.json`
- **Structured JSON:** [`2fe320934f695d08a3f2.json`](../../sessions/2f/2fe320934f695d08a3f2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### 1. argmin seed44 — 未完成，9/10 tasks done

PID 428117 仍在运行（13h13m），GPU3 活跃（1906 MiB, 22%）。最后一个 task 进行中，预计 **~1h 内完成**。

当前 9 tasks 累计：**11/90 成功**，最终 arg_44 将在 **11-16%** 范围。

### 2. Fisher test 预分析

| 最后 task SR | arg_44 | arg pooled | delta | p-value (one-sided) | sig@.05 | sig@.10 | Narrative |
|-------------|--------|------------|-------|---------------------|---------|---------|-----------|
| 0/10 | 11% | 40/300=13.3% | +4.7pp | **0.0720** | No | **Yes** | B (robustness) |
| 1/10 | 12% | 41/300=13.7% | +4.3pp | **0.0897** | No | **Yes** | B (robustness) |
| 2/10 | 13% | 42/300=14.0% | 0.1102 | No | No | C (non-sig) |
| 3/10 | 14% | 43/300=14.3% | 0.1337 | No | No | C (non-sig) |
| 4/10 | 15% | 44/300=14.7% | 0.1601 | No | No | C (non-sig) |
| 5/10 | 16% | 45/300=15.0% | 0.1895 | No | No | C (non-sig) |

**关键判断**：在任何场景下都 **不显著 at p<0.05**。只有最后 task ≤1/10 时才 marginal significant at p<0.10。大概率 **Narrative B or C**。

### 3. 服务器 GPU 状态 (bjb1-18228, 4×RTX 4090)

| GPU | Memory | Util |
|-----|--------|------|
| 0 | 4735/24564 MiB | 21% |
| 1 | 2410/24564 MiB | 22% |
| 2 | 1/24564 MiB | **0% (空闲)** |
| 3 | 1906/24564 MiB | 22% (argmin seed44) |

### 4. bjb1-18228 最近完成的 eval JSON

- `eval_object_obs_only_norm02_seed44.json` (22:38 today)
- `eval_object_perdof_default_norm_r2.json` (16:57)
- `eval_object_perdof_seed43.json` (11:10)
- `eval_object_obs_only_seed43.json` (08:40)
- `eval_object_reconvla_seed43.json` (08:34)

**需要等 ~1h 后重新检查拿最终 arg_44 数字再跑 Fisher exact test。**

---
