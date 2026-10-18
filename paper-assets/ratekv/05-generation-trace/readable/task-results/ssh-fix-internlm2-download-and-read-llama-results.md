# ssh fix internlm2 download and read llama results

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix_internlm2_download_and_read_llama_results_20260515T225451_result.json`
- **Structured JSON:** [`f0b4d76d80b497ac4d18.json`](../../sessions/f0/f0b4d76d80b497ac4d18.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有结果汇总如下：

---

## 任务 1：Llama-3.1-8B 3-seed downstream CI 结果

```json
{
  "model": "Llama-3.1-8B",
  "tasks": ["arc_challenge", "hellaswag", "winogrande", "piqa"],
  "num_fewshot": 0,
  "budget": 0.25,
  "max_2bit": 2,
  "seeds": [0, 1, 2],
  "note": "Single profile, same MCKP allocation for all seeds. Variance from lm_eval only.",
  "baseline": {
    "arc_challenge": 0.5188,
    "hellaswag": 0.6073,
    "piqa": 0.7922,
    "winogrande": 0.7388
  },
  "uniform_4bit": {
    "arc_challenge": 0.5256,
    "hellaswag": 0.6024,
    "piqa": 0.7873,
    "winogrande": 0.7261
  },
  "seed_mckp": {
    "0": {"arc_challenge": 0.5179, "hellaswag": 0.6021, "piqa": 0.7867, "winogrande": 0.7309},
    "1": {"arc_challenge": 0.5179, "hellaswag": 0.6021, "piqa": 0.7867, "winogrande": 0.7309},
    "2": {"arc_challenge": 0.5179, "hellaswag": 0.6021, "piqa": 0.7867, "winogrande": 0.7309}
  },
  "summary": {
    "arc_challenge": {"values": [0.5179, 0.5179, 0.5179], "mean": 0.5179, "std": 0.0},
    "hellaswag": {"values": [0.6021, 0.6021, 0.6021], "mean": 0.6021, "std": 0.0},
    "winogrande": {"values": [0.7309, 0.7309, 0.7309], "mean": 0.7309, "std": 0.0},
    "piqa": {"values": [0.7867, 0.7867, 0.7867], "mean": 0.7867, "std": 0.0}
  },
  "elapsed_seconds": 1935.1
}
```

注意：3 个 seed 结果完全相同（std=0.0），因为 MCKP allocation 是 deterministic 的，方差仅来自 lm_eval 采样，但此处也为零。

---

## 任务 2：InternLM2-7B 下载

- 已杀掉卡住的进程 379330
- 已清理不完整的 HF cache
- **ModelScope 下载已启动，PID: 380895**
- 初始进度：`pytorch_model-00001-of-00002.bin` — 0% (6MB/9.28GB)，速度 1.70 MB/s，预计 ~1.5h

---

## 任务 3：Phi-3-medium 下载进度

- 进程 379202 仍在运行（通过 ModelScope 下载 `LLM-Research/Phi-3-medium-128k-instruct`）
- 当前进度：**model-00005-of-00006.safetensors — 60% (2.67G/4.44G)**，速度 1.54 MB/s
- 这是第 5/6 个 shard，前 4 个已完成。剩余：当前 shard ~20min + 最后 1 个 shard ~48min
- **预计还需 ~1-1.5 小时完成**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "model": "Llama-3.1-8B",
    "tasks": [
      "arc_challenge",
      "hellaswag",
      "winogrande",
      "piqa"
    ],
    "num_fewshot": 0,
    "budget": 0.25,
    "max_2bit": 2,
    "seeds": [
      0,
      1,
      2
    ],
    "note": "Single profile, same MCKP allocation for all seeds. Variance from lm_eval only.",
    "baseline": {
      "arc_challenge": 0.5188,
      "hellaswag": 0.6073,
      "piqa": 0.7922,
      "winogrande": 0.7388
    },
    "uniform_4bit": {
      "arc_challenge": 0.5256,
      "hellaswag": 0.6024,
      "piqa": 0.7873,
      "winogrande": 0.7261
    },
    "seed_mckp": {
      "0": {
        "arc_challenge": 0.5179,
        "hellaswag": 0.6021,
        "piqa": 0.7867,
        "winogrande": 0.7309
      },
      "1": {
        "arc_challenge": 0.5179,
        "hellaswag": 0.6021,
        "piqa": 0.7867,
        "winogrande": 0.7309
      },
      "2": {
        "arc_challenge": 0.5179,
        "hellaswag": 0.6021,
        "piqa": 0.7867,
        "winogrande": 0.7309
      }
    },
    "summary": {
      "arc_challenge": {
        "values": [
          0.5179,
          0.5179,
          0.5179
        ],
        "mean": 0.5179,
        "std": 0.0
      },
      "hellaswag": {
        "values": [
          0.6021,
          0.6021,
          0.6021
        ],
        "mean": 0.6021,
        "std": 0.0
      },
      "winogrande": {
        "values": [
          0.7309,
          0.7309,
          0.7309
        ],
        "mean": 0.7309,
        "std": 0.0
      },
      "piqa": {
        "values": [
          0.7867,
          0.7867,
          0.7867
        ],
        "mean": 0.7867,
        "std": 0.0
      }
    },
    "elapsed_seconds": 1935.1
  }
}
```

</details>

---
