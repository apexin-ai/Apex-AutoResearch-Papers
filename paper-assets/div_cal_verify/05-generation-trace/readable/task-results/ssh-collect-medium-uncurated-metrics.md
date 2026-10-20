# ssh collect medium uncurated metrics

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_collect_medium_uncurated_metrics_20260513T213705_result.json`
- **Structured JSON:** [`04345994de6ddaf3d7b1.json`](../../sessions/04/04345994de6ddaf3d7b1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## medium_uncurated_seed42 Results

**Status: COMPLETE** (03:01 → 05:24 CST, ~2h23m)

```json
{
  "gen_0": {"ppl": 26.55, "rankme": 371.57, "knn": 0.9880, "rare": 0.0346, "corr": 0.0219},
  "gen_1": {"ppl": 35.12, "rankme": 403.80, "knn": 0.9880, "rare": 0.0281, "corr": 0.0228},
  "gen_2": {"ppl": 46.90, "rankme": 420.83, "knn": 0.9880, "rare": 0.0216, "corr": 0.0181},
  "gen_3": {"ppl": 57.40, "rankme": 425.35, "knn": 0.9880, "rare": 0.0185, "corr": 0.0011},
  "gen_4": {"ppl": 67.45, "rankme": 430.68, "knn": 0.9880, "rare": 0.0172, "corr": -0.0046},
  "gen_5": {"ppl": 78.55, "rankme": 438.62, "knn": 0.9870, "rare": 0.0159, "corr": -0.0175},
  "gen_6": {"ppl": 84.59, "rankme": 442.85, "knn": 0.9870, "rare": 0.0144, "corr": -0.0462},
  "gen_7": {"ppl": 91.66, "rankme": 443.98, "knn": 0.9880, "rare": 0.0139, "corr": -0.0379}
}
```

- Checkpoint path: `/root/autodl-tmp/div_cal_verify/results_medium_uncurated/uncurated/` (gen_0 ~ gen_7 + all_results.json)
- Log path: `/root/autodl-tmp/div_cal_verify/medium_uncurated.log`
- RankMe baseline (gen-0): 296.93
- Selection ratio: N/A (uncurated, no selection)
- 趋势：PPL 持续恶化 (26→92)，RankMe 单调上升 (372→444)，Rare 单调下降 (0.035→0.014)，Corr 从正变负

## ext_seed456 Status

**Status: RUNNING — Gen 6/7, step [3/5] Training**

已完成 Gen 0-5 metrics:
```json
{
  "gen_0": {"ppl": 36.51, "rankme": 273.85, "knn": 0.9880, "rare": 0.0284, "corr": -0.0103, "ratio": 1.1621},
  "gen_1": {"ppl": 44.77, "rankme": 291.93, "knn": 0.9880, "rare": 0.0203, "corr": -0.0404, "ratio": 1.0686},
  "gen_2": {"ppl": 50.84, "rankme": 298.52, "knn": 0.9870, "rare": 0.0152, "corr": -0.0292, "ratio": 1.1119},
  "gen_3": {"ppl": 54.43, "rankme": 298.35, "knn": 0.9870, "rare": 0.0130, "corr": -0.0223, "ratio": 1.1551},
  "gen_4": {"ppl": 49.91, "rankme": 295.86, "knn": 0.9880, "rare": 0.0118, "corr": -0.0321, "ratio": 1.1841},
  "gen_5": {"ppl": 50.45, "rankme": 297.37, "knn": 0.9880, "rare": 0.0111, "corr": -0.0300, "ratio": 1.2186}
}
```

- Gen 6 selection done (ratio=1.0818), currently training
- Checkpoint path: `/root/autodl-tmp/div_cal_verify/results_seed456/`
- Log last modified: 05:21 CST
- **注意：GPU 1 utilization=0%, memory=21GB — 可能训练已挂起或卡住，需关注**

## rgds_seed456 Status

- **Auto-started: NO** — ext_seed456 尚未完成，rgds_seed456 未启动
- 无 rgds_seed456 日志文件

## medium_rgds_seed42 Status

- **Running: YES** (GPU 0, 41% util, 68GB mem)
- Started: 05:25:25 CST (medium_uncurated 完成后自动链式启动)
- Current progress: 仍在加载模型/计算 baseline (log 只有 6 行，last modified 05:26)
- Log path: `/root/autodl-tmp/div_cal_verify/medium_rgds.log`
- Results dir: `/root/autodl-tmp/div_cal_verify/results_medium_rgds/rgds/` (已创建，暂无文件)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "gen_0": {
      "ppl": 36.51,
      "rankme": 273.85,
      "knn": 0.988,
      "rare": 0.0284,
      "corr": -0.0103,
      "ratio": 1.1621
    },
    "gen_1": {
      "ppl": 44.77,
      "rankme": 291.93,
      "knn": 0.988,
      "rare": 0.0203,
      "corr": -0.0404,
      "ratio": 1.0686
    },
    "gen_2": {
      "ppl": 50.84,
      "rankme": 298.52,
      "knn": 0.987,
      "rare": 0.0152,
      "corr": -0.0292,
      "ratio": 1.1119
    },
    "gen_3": {
      "ppl": 54.43,
      "rankme": 298.35,
      "knn": 0.987,
      "rare": 0.013,
      "corr": -0.0223,
      "ratio": 1.1551
    },
    "gen_4": {
      "ppl": 49.91,
      "rankme": 295.86,
      "knn": 0.988,
      "rare": 0.0118,
      "corr": -0.0321,
      "ratio": 1.1841
    },
    "gen_5": {
      "ppl": 50.45,
      "rankme": 297.37,
      "knn": 0.988,
      "rare": 0.0111,
      "corr": -0.03,
      "ratio": 1.2186
    }
  }
}
```

</details>

---
