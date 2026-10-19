# ssh check running experiments progress

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-running-experiments-progress_20260520T041518_result.json`
- **Structured JSON:** [`8f9c57509cf779e94f17.json`](../../sessions/8f/8f9c57509cf779e94f17.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已收集。以下是汇总：

---

## bjb2-28827 (6 GPUs)

| GPU | 实验 | 进度 | 预计剩余 |
|-----|------|------|----------|
| 0 | crm-spatial-49 | 8/10 tasks (~85%) | ~20 min |
| 1 | vla-long-49 | 7/10 tasks (~75%) | ~30 min |
| - | vla-long-50 | 7/10 tasks (~75%) | ~30 min |
| 2 | vla-long-51 | 4/10 tasks (~45%) | ~1h |
| 3 | crm-goal-48 | 9/10 tasks (~95%) | ~10 min |
| 4 | **crm-goal-47** | **DONE** ✓ | SR=69.0% |
| 5 | calibration | ep 95/100 (~95%) | ~10 min |
| 1 | **p75-seed42** | **DONE** ✓ | fast_path=86.6%, avg_k=3.1 |

## bjb1-18228 (4 GPUs)

| GPU | 实验 | 进度 | 预计剩余 |
|-----|------|------|----------|
| 0 | adaptive-k-p25-44-r2 | 4/10 tasks (~45%) | ~1.3h |
| 1 | vla-goal-49 | 3/10 tasks (~35%) | ~1.5h |
| 2 | crm-spatial-51 | 7/10 tasks (~75%) | ~30 min |
| 3 | vla-long-52 | 6/10 tasks (~65%) | ~45 min |
| 3 | **p50-seed43** | **DONE** ✓ | fast_path=77.4%, avg_k=3.8 |

## bjb1-32546 (6 GPUs)

| GPU | 实验 | 进度 | 预计剩余 |
|-----|------|------|----------|
| 0 | **crm-spatial-50** | **DONE** ✓ | SR=35.0% |
| 0 | **p75-seed44** | **DONE** ✓ | fast_path=87.2%, avg_k=3.0 |
| 1 | vla-spatial-51 | 7/10 tasks (~75%) | ~30 min |
| 2 | vla-object-51 | 9/10 tasks (~95%) | ~10 min |
| 3 | crm-long-50 | 5/10 tasks (~55%) | ~45 min |
| 4 | crm-long-48 | 8/10 tasks (~85%) | ~20 min |
| 4 | crm-long-49 | 8/10 tasks (~85%) | ~20 min |

## bjb2-40593 (1 GPU)

| GPU | 实验 | 进度 | 预计剩余 |
|-----|------|------|----------|
| 0 | adaptive-k-p25-44 | 8/10 tasks (~85%) | ~20 min |
| 0 | calibration | T3 R9, ~30/100 eps (~30%) | ~2.5h |

---

### 重点回答

1. **Calibration 进度**：
   - **bjb2-28827**: 95% 完成，正在跑最后一个 task (tomato_sauce) ep 5/10，**~10 min 内结束**，JSON 尚未生成（完成后才写入）
   - **bjb2-40593**: 30% 完成，task 3 episode 9/10，还需 ~2.5h，且与 p25-seed44 共享同一块 GPU

2. **P25-seed44 哪个先完成**：
   - **bjb2-40593 先完成** — 已跑 8/10 tasks（~85%），~20 min 内结束
   - bjb1-18228 (r2) 才跑到 4/10 tasks（~45%），还需 ~1.3h

3. **即将完成（>80%）可释放 GPU 的实验**：
   - **crm-goal-48** (bjb2-28827 GPU3) — 95%, ~10 min
   - **calibration** (bjb2-28827 GPU5) — 95%, ~10 min
   - **crm-spatial-49** (bjb2-28827 GPU0) — 85%, ~20 min
   - **vla-object-51** (bjb1-32546 GPU2) — 95%, ~10 min
   - **crm-long-48/49** (bjb1-32546 GPU4) — 85%, ~20 min
   - **p25-seed44** (bjb2-40593 GPU0) — 85%, ~20 min

   短期内可释放：bjb2-28827 约 3 个 GPU，bjb1-32546 约 3 个 GPU，bjb2-40593 1 个 GPU（但 calibration 还在跑）

---
