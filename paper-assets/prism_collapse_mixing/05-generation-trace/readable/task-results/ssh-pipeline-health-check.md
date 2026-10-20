# ssh pipeline health check

**prism collapse mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_pipeline-health-check_20260515T224536_result.json`
- **Structured JSON:** [`a255b94ac2c97657e779.json`](../../sessions/a2/a255b94ac2c97657e779.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总报告：

## Pipeline 状态

| 项目 | 状态 |
|------|------|
| 父进程 PID 197985 | **运行中**，已运行 2h08m，`run_pipeline.py --seeds 42,137 --start_gen 1` |
| 子进程 200889/200890 | 已结束（任务完成后退出） |
| Gen 1 信号 | **已完成** (06:41-06:42) |
| Gen 2 合成 | **已完成** (06:46, ~10MB/seed) |
| Gen 2 混合 | **进行中**（文件尚未写出） |
| Gen 2 训练/信号 | 未开始 |
| GPU 0 | 92% 利用率, 10623/97887 MiB |
| GPU 1 | 94% 利用率, 10623/97887 MiB |

## Gen 1 信号指标

```json
{
  "gen1_signals": {
    "seed_42": {
      "rho_loss_entropy": 0.9118,
      "rho_loss_spectral_rank": -0.2050,
      "loss_mean": 3.1118,
      "loss_std": 0.5208,
      "entropy_mean": 3.0437,
      "entropy_std": 0.4513,
      "spectral_rank_mean": 165.0,
      "spectral_rank_std": 8.93,
      "corpus_spectral_rank": 4.68,
      "distinct_1": 0.0382,
      "distinct_2": 0.3385,
      "distinct_3": 0.6793,
      "num_probe_samples": 5000
    },
    "seed_137": {
      "rho_loss_entropy": 0.9119,
      "rho_loss_spectral_rank": -0.2036,
      "loss_mean": 3.1115,
      "loss_std": 0.5209,
      "entropy_mean": 3.0472,
      "entropy_std": 0.4521,
      "spectral_rank_mean": 164.8,
      "spectral_rank_std": 8.93,
      "corpus_spectral_rank": 4.68,
      "distinct_1": 0.0384,
      "distinct_2": 0.3399,
      "distinct_3": 0.6817,
      "num_probe_samples": 5000
    }
  },
  "pipeline_stage": "gen2_mixing",
  "gpu_utilization": {"gpu0": "92%", "gpu1": "94%"}
}
```

两个 seed 的 Gen 1 信号高度一致：loss-entropy 相关性强 (ρ≈0.91)，loss-spectral 弱负相关 (ρ≈-0.20)，corpus spectral rank=4.68。Pipeline 当前正在 Gen 2 混合阶段，双 GPU 均在活跃工作。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "gen1_signals": {
      "seed_42": {
        "rho_loss_entropy": 0.9118,
        "rho_loss_spectral_rank": -0.205,
        "loss_mean": 3.1118,
        "loss_std": 0.5208,
        "entropy_mean": 3.0437,
        "entropy_std": 0.4513,
        "spectral_rank_mean": 165.0,
        "spectral_rank_std": 8.93,
        "corpus_spectral_rank": 4.68,
        "distinct_1": 0.0382,
        "distinct_2": 0.3385,
        "distinct_3": 0.6793,
        "num_probe_samples": 5000
      },
      "seed_137": {
        "rho_loss_entropy": 0.9119,
        "rho_loss_spectral_rank": -0.2036,
        "loss_mean": 3.1115,
        "loss_std": 0.5209,
        "entropy_mean": 3.0472,
        "entropy_std": 0.4521,
        "spectral_rank_mean": 164.8,
        "spectral_rank_std": 8.93,
        "corpus_spectral_rank": 4.68,
        "distinct_1": 0.0384,
        "distinct_2": 0.3399,
        "distinct_3": 0.6817,
        "num_probe_samples": 5000
      }
    },
    "pipeline_stage": "gen2_mixing",
    "gpu_utilization": {
      "gpu0": "92%",
      "gpu1": "94%"
    }
  }
}
```

</details>

---
