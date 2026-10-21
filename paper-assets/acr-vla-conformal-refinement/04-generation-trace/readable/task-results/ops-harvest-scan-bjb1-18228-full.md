# ops harvest scan bjb1 18228 full

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_harvest-scan-bjb1-18228-full_20260519T013030_result.json`
- **Structured JSON:** [`39c3991964ef55dce4c8.json`](../../sessions/39/39c3991964ef55dce4c8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## bjb1-18228 扫描报告

### GPU 状态

| GPU | Util% | VRAM Used | 实验 1 | 实验 2 | 空闲 slot |
|-----|-------|-----------|--------|--------|-----------|
| 0 | 98% | 8533/24564 MiB | obs_only norm003 seed47 | perdof norm03 seed48 | 无 |
| 1 | 99% | 8533/24564 MiB | obs_only_object norm003 seed43 | obs_only norm003 seed46 | 无 |
| 2 | 99% | 6206/24564 MiB | **ORPHAN** perdof_object norm003 seed44 (1923M) | obs_only norm005 seed46 | ~14G 可用 |
| 3 | 99% | 9000/24564 MiB | obs_only norm003 seed49 | obs_only norm003 seed45 | 无 |

**4 GPU 全部满载，共 9 个 evaluate.py 进程（8 tmux + 1 orphan）。**

### Tmux Sessions (7个，全部存活)

所有 session 均在活跃跑 object benchmark 任务，当前进度在 `pick_up_the_bbq_sauce` / `pick_up_the_salad_dressing` 附近：

| Session | GPU | 当前进度 |
|---------|-----|----------|
| eval-obs-only-norm003-seed45-t16 | 3 | rollout 1/10 |
| eval-obs-only-norm003-seed46 | 1 | rollout 4/10 |
| eval-obs-only-norm003-seed47 | 0 | rollout 5/10 |
| eval-obs-only-norm003-seed49-t16 | 3 | rollout 8/10 |
| eval-obs-only-norm005-seed46 | 2 | rollout 6/10 |
| eval-obs-only-object-norm003-seed43 | 1 | rollout 4/10 |
| eval-perdof-norm03-seed48 | 0 | rollout 3/10 |

### Orphan 进程

| PID | 实验 | GPU | 启动时间 | 说明 |
|-----|------|-----|----------|------|
| 853864 | perdof_object norm003 seed44 | 2 | May 18 | agent-ml job 管理，无 tmux session，已跑 988 min CPU time，仍在运行，占 1923 MiB |

### 最近 12h 完成实验（未收割）

| 文件 | 完成时间 | SR |
|------|----------|----|
| eval_object_obs_only_norm02_seed48.json | May 19 00:49 | **0.18** |
| eval_object_perdof_default_seed43.json | May 19 08:49 | **0.0** |

### 建议动作
- GPU 2 上 orphan PID 853864 占 1923 MiB 但已跑超过 12h，确认是否需要 kill 回收资源（可在 GPU 2 再塞一个实验）
- 两个已完成实验结果偏低（0.18 / 0.0），需确认是否收录到汇总

---
