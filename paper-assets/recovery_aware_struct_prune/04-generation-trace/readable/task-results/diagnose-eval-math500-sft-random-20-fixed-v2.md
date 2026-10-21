# diagnose eval math500 sft random 20 fixed v2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_math500_sft_random_20_fixed_v2_20260523T212155_result.json`
- **Structured JSON:** [`5dcb39e7d3773e0388c3.json`](../../sessions/5d/5dcb39e7d3773e0388c3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据齐全，编写诊断报告。

```json
{
  "sigterm_source": "kill_job 终止。首次 _v2 尝试(05:05)时，_fixed 版本仍在 cuda:1 上运行(到 sample 78)，两个 sft_random_20 模型同时加载在同一物理 GPU 上导致严重竞争。两者均被 kill，_v2 于 05:16 重新启动",
  "slow_reason": "213s/it 是异常值，非实际速度。原因：(1) GPU 竞争——两个模型同时占用 cuda:1，推理时间翻倍；(2) sft_random_20 模型本身比 sft_cka_only_20 慢约 2.6x，因为它生成更长的响应（大量 sample 打满 max_new_tokens=2048），而 sft_cka_only_20 平均 673 tokens 即自然停止",
  "speed_data": {
    "sft_random_20_fixed_78samples": {
      "avg_sec_per_sample": 70.8,
      "samples_completed": 78,
      "elapsed": "1:32:01",
      "estimated_500_total_hours": 9.83,
      "note": "无 GPU 竞争时的真实速度，sample 间波动大(3s~110s)"
    },
    "sft_random_20_v2_current": {
      "avg_sec_per_sample": 61.6,
      "samples_completed": 7,
      "elapsed": "7:11",
      "tqdm_smoothed_rate": "53.79s/it",
      "tqdm_eta": "7:22",
      "note": "正在运行中，早期 sample 偏简单，预计后续趋近 70s/it"
    },
    "first_v2_attempt_anomaly": {
      "avg_sec_per_sample": 216,
      "note": "GPU 竞争导致，非正常速度"
    }
  },
  "comparison_model_speed": {
    "sft_cka_only_20": {
      "avg_sec_per_sample": 26.95,
      "total_time": "3:44:36",
      "avg_response_length": 673,
      "truncated_rate": "23.2% (116/500)",
      "accuracy": "0.2740 ± 0.0199"
    },
    "grpo_cka_only_20_fixed_ongoing": {
      "avg_sec_per_sample": 28.7,
      "progress": "228/500",
      "elapsed": "1:48:54",
      "eta_completion": "~2h remaining"
    }
  },
  "gpu_status": {
    "cuda_0": "eval_math500_grpo_cka_only_20_fixed, 17053 MiB / 97887 MiB, 99% util, 228/500",
    "cuda_1": "eval_math500_sft_random_20_fixed_v2, 15135 MiB / 97887 MiB, 99% util, 7/500"
  },
  "timeline": {
    "v2_started": "05:18 CST (May 24)",
    "estimated_completion": "~15:00-15:30 CST (May 24)",
    "ddl": "~08:30 CST (May 25)",
    "margin": "~17h buffer"
  },
  "recommendation": "不需要干预。当前 _v2 正常运行在 cuda:1 上（无 GPU 竞争），预计 ~10h 完成，距 DDL 有 ~17h 余量。213s/it 是 GPU 竞争导致的异常，实际速度 ~70s/it。timeout=72000s (20h) 也足够。降低 max_new_tokens 可加速但会截断推理链影响准确率，无必要冒险。"
}
```

**核心结论**：

1. **SIGTERM 来源**：`kill_job` 杀掉了与 _fixed 版本冲突的进程。不是 OOM。

2. **213s/it 是假象**：两个 sft_random_20 实例同时加载在 cuda:1 上导致推理竞争。正常速度是 ~70s/it。

3. **当前 _v2 运行正常**：7/500 已完成，速度符合预期。预计 ~10h 完成（~15:00 CST），距 DDL 有 ~17h 余量。

4. **无需加速**：当前速度足够赶上 DDL。降 max_new_tokens 虽可加速但有截断推理链的风险。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "sigterm_source": "kill_job 终止。首次 _v2 尝试(05:05)时，_fixed 版本仍在 cuda:1 上运行(到 sample 78)，两个 sft_random_20 模型同时加载在同一物理 GPU 上导致严重竞争。两者均被 kill，_v2 于 05:16 重新启动",
    "slow_reason": "213s/it 是异常值，非实际速度。原因：(1) GPU 竞争——两个模型同时占用 cuda:1，推理时间翻倍；(2) sft_random_20 模型本身比 sft_cka_only_20 慢约 2.6x，因为它生成更长的响应（大量 sample 打满 max_new_tokens=2048），而 sft_cka_only_20 平均 673 tokens 即自然停止",
    "speed_data": {
      "sft_random_20_fixed_78samples": {
        "avg_sec_per_sample": 70.8,
        "samples_completed": 78,
        "elapsed": "1:32:01",
        "estimated_500_total_hours": 9.83,
        "note": "无 GPU 竞争时的真实速度，sample 间波动大(3s~110s)"
      },
      "sft_random_20_v2_current": {
        "avg_sec_per_sample": 61.6,
        "samples_completed": 7,
        "elapsed": "7:11",
        "tqdm_smoothed_rate": "53.79s/it",
        "tqdm_eta": "7:22",
        "note": "正在运行中，早期 sample 偏简单，预计后续趋近 70s/it"
      },
      "first_v2_attempt_anomaly": {
        "avg_sec_per_sample": 216,
        "note": "GPU 竞争导致，非正常速度"
      }
    },
    "comparison_model_speed": {
      "sft_cka_only_20": {
        "avg_sec_per_sample": 26.95,
        "total_time": "3:44:36",
        "avg_response_length": 673,
        "truncated_rate": "23.2% (116/500)",
        "accuracy": "0.2740 ± 0.0199"
      },
      "grpo_cka_only_20_fixed_ongoing": {
        "avg_sec_per_sample": 28.7,
        "progress": "228/500",
        "elapsed": "1:48:54",
        "eta_completion": "~2h remaining"
      }
    },
    "gpu_status": {
      "cuda_0": "eval_math500_grpo_cka_only_20_fixed, 17053 MiB / 97887 MiB, 99% util, 228/500",
      "cuda_1": "eval_math500_sft_random_20_fixed_v2, 15135 MiB / 97887 MiB, 99% util, 7/500"
    },
    "timeline": {
      "v2_started": "05:18 CST (May 24)",
      "estimated_completion": "~15:00-15:30 CST (May 24)",
      "ddl": "~08:30 CST (May 25)",
      "margin": "~17h buffer"
    },
    "recommendation": "不需要干预。当前 _v2 正常运行在 cuda:1 上（无 GPU 竞争），预计 ~10h 完成，距 DDL 有 ~17h 余量。213s/it 是 GPU 竞争导致的异常，实际速度 ~70s/it。timeout=72000s (20h) 也足够。降低 max_new_tokens 可加速但会截断推理链影响准确率，无必要冒险。"
  }
}
```

</details>

---
