# analysis mvp p1 gpu1 v3

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mvp-p1-gpu1-v3_20260513T151635_result.json`
- **Structured JSON:** [`95efe489e4218f856e6a.json`](../../sessions/95/95efe489e4218f856e6a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验 mvp-p1-gpu1-v3 数据收集完毕。这个 run 只跑了 2 个 task type（chemistry-mix-paint-secondary-color + grow-plant），各 20 episodes。

```
METRICS:
- task: chemistry-mix-paint-secondary-color (20 episodes)
  internal_mean: -41.0 ± 53.8
  det_mean:       -5.5 ± 32.8
  oracle_mean:     4.5 ±  8.0
  det_minus_internal: +35.5 (方向: positive ✓)
  oracle_minus_internal: +45.5
  oracle_minus_det: +10.0

- task: grow-plant (20 episodes)
  internal_mean: 0.5 ± 1.4
  det_mean:      0.5 ± 1.4
  oracle_mean:   0.5 ± 1.4
  det_minus_internal: 0.0 (方向: neutral ✗)
  oracle_minus_internal: 0.0
  oracle_minus_det: 0.0

WANDB_RUN_ID: N/A
EXIT_STATUS: normal (EXIT_CODE=0)
EPISODES_COMPLETED: 40/40 (20 chemistry-mix-paint + 20 grow-plant)
LOG_TAIL:
  score=2.0 (int=0/det=30) (311s)
  --- grow-plant Summary ---
    always-internal:      0.5 ± 1.4
    always-deterministic: 0.5 ± 1.4
    oracle-routing:       0.5 ± 1.4
  Global summary saved to results/mvp/global_summary.json
  EXIT_CODE=0
```

**关键发现：**

1. **chemistry-mix-paint**: det 大幅优于 internal（+35.5），信号很强。internal 因频繁 death penalty（-100）而均值极低（-41.0），det 避开了大部分 death 仅有 2 次（-5.5）。oracle 进一步提升到 +4.5。

2. **grow-plant**: 三种策略**完全相同**——逐 episode scores 一模一样。说明这个任务的 deterministic module 没有被触发，或者对该任务无适用的确定性操作。routing 在这里无差别。

3. **附加数据**：results/mvp/ 下还有 GPU0 跑的 3 个 task（boil/melt/change-the-state-of-matter-of），det_minus_internal 分别为 +30.1/+40.2/+40.2，全部 positive。

**MVP 初步判定**（仅 GPU1 的 2 任务）：1/2 positive。结合 GPU0 的 3 任务，全局 4/5 positive（grow-plant 是唯一 neutral）。bootstrap CI 需要单独计算才能确认是否 CI 下界 > 0。

---
