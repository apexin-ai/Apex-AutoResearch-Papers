# provenance exp 018 registry

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_provenance_exp_018_registry_20260515T055957_result.json`
- **Structured JSON:** [`c3ece0186ad3af0d7063.json`](../../sessions/c3/c3ece0186ad3af0d7063.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有溯源数据收集完毕，输出最终结果。

---

## exp_018 系列溯源报告

### 完整 Spec

```json
{
  "exp_018_qwen_scierc_seed123": {
    "command": "python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --seed 123 --n_samples 8 --temperature 1.0 --max_tokens 1024 --output_dir output/exp_018_qwen_scierc_seed123",
    "server": "autodl-5090",
    "seed": 123,
    "N": 8,
    "T": 1.0,
    "max_tokens": 1024,
    "model_name": "Qwen3-8B-SciERC-merged-v2",
    "model_path": "checkpoints/qwen3-8b-scierc-merged-v2",
    "dataset": "scierc",
    "subtask": "joint",
    "data_path": "data/scierc/processed_data",
    "data_count": 551,
    "use_train_format": true,
    "is_new_inference": true,
    "parent": null,
    "run_timestamp": "2026-05-15 13:09",
    "output_path": "output/exp_018_qwen_scierc_seed123/",
    "log_path": "output/exp_018_qwen_scierc_seed123.log",
    "samples_md5": "866a59581dea56f4633149f0b18a31ae"
  },
  "exp_018_qwen_scierc_seed456": {
    "command": "python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --seed 456 --n_samples 8 --temperature 1.0 --max_tokens 1024 --output_dir output/exp_018_qwen_scierc_seed456",
    "server": "autodl-5090",
    "seed": 456,
    "N": 8,
    "T": 1.0,
    "max_tokens": 1024,
    "model_name": "Qwen3-8B-SciERC-merged-v2",
    "model_path": "checkpoints/qwen3-8b-scierc-merged-v2",
    "dataset": "scierc",
    "subtask": "joint",
    "data_path": "data/scierc/processed_data",
    "data_count": 551,
    "use_train_format": true,
    "is_new_inference": true,
    "parent": null,
    "run_timestamp": "2026-05-15 13:08~13:13",
    "output_path": "output/exp_018_qwen_scierc_seed456/",
    "log_path": "output/exp_018_qwen_scierc_seed456/run.log",
    "samples_md5": "46d0de47ad7693c07e7df3a77c90c3be"
  },
  "exp_018_llama_scierc_seed123": {
    "command": "python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask joint --seed 123 --n_samples 8 --temperature 1.0 --max_tokens 1024 --output_dir output/exp_018_llama_scierc_seed123",
    "server": "autodl-5090",
    "seed": 123,
    "N": 8,
    "T": 1.0,
    "max_tokens": 1024,
    "model_name": "LLaMA-3.1-8B-SciERC-merged",
    "model_path": "checkpoints/llama3.1-8b-scierc-merged",
    "dataset": "scierc",
    "subtask": "joint",
    "data_path": "data/scierc/processed_data",
    "data_count": 551,
    "use_train_format": true,
    "is_new_inference": true,
    "parent": null,
    "run_timestamp": "2026-05-15 13:09",
    "output_path": "output/exp_018_llama_scierc_seed123/",
    "log_path": "output/exp_018_llama_scierc_seed123.log",
    "samples_md5": "072eeca68236d46b4c5c84b945209abc"
  },
  "exp_018_llama_scierc_seed456": {
    "command": "原始命令为 exp_007: python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask joint --seed 456 --n_samples 8 --temperature 1.0 --max_tokens 1024 --output_dir output/exp_007_llama_seed456",
    "server": "autodl-5090",
    "seed": 456,
    "N": 8,
    "T": 1.0,
    "max_tokens": 1024,
    "model_name": "LLaMA-3.1-8B-SciERC-merged",
    "model_path": "checkpoints/llama3.1-8b-scierc-merged",
    "dataset": "scierc",
    "subtask": "joint",
    "data_path": "data/scierc/processed_data",
    "data_count": 551,
    "use_train_format": true,
    "is_new_inference": false,
    "parent": "exp_007_llama_seed456",
    "original_run_timestamp": "2026-05-14 23:08~23:12",
    "copy_timestamp": "2026-05-15 13:08",
    "output_path": "output/exp_018_llama_scierc_seed456/",
    "log_path": "output/exp_018_llama_scierc_seed456/run.log (inherited from exp_007)",
    "samples_md5": "2034b5e4989c387b84e2b7225c7e5367"
  }
}
```

### 溯源结论

1. **exp_018_llama_scierc_seed456 是 exp_007 的复制** — MD5 完全一致（`2034b5e4989c387b84e2b7225c7e5367`）。其 run.log 明确写着 `Saved to output/exp_007_llama_seed456/samples.jsonl`。exp_007 原始运行时间 05-14 23:08，复制到 exp_018 目录的时间 05-15 13:08。

2. **新推理 vs 复用**：
   - **新推理（3个）**：qwen_seed123, qwen_seed456, llama_seed123 — 均为 05-15 13:08~13:13 新跑
   - **复用（1个）**：llama_seed456 — 从 exp_007 复制
   - 注意：exp_007_llama_seed123 也存在（MD5 `765712e5b842f12fd4f19494598ab341`），但 exp_018_llama_scierc_seed123 的 MD5 不同（`072eeca68236d46b4c5c84b945209abc`），说明 llama_seed123 是**重新跑的**而非复制

3. **max_tokens 均为 1024** — `run_mvp_pilot.py` 默认值 1024，`sampling.py` 默认值 1024，bash history 无覆盖记录，run.log 中无 max_tokens 覆盖迹象。不存在 exp_012 的 512 截断问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "exp_018_qwen_scierc_seed123": {
      "command": "python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --seed 123 --n_samples 8 --temperature 1.0 --max_tokens 1024 --output_dir output/exp_018_qwen_scierc_seed123",
      "server": "autodl-5090",
      "seed": 123,
      "N": 8,
      "T": 1.0,
      "max_tokens": 1024,
      "model_name": "Qwen3-8B-SciERC-merged-v2",
      "model_path": "checkpoints/qwen3-8b-scierc-merged-v2",
      "dataset": "scierc",
      "subtask": "joint",
      "data_path": "data/scierc/processed_data",
      "data_count": 551,
      "use_train_format": true,
      "is_new_inference": true,
      "parent": null,
      "run_timestamp": "2026-05-15 13:09",
      "output_path": "output/exp_018_qwen_scierc_seed123/",
      "log_path": "output/exp_018_qwen_scierc_seed123.log",
      "samples_md5": "866a59581dea56f4633149f0b18a31ae"
    },
    "exp_018_qwen_scierc_seed456": {
      "command": "python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --seed 456 --n_samples 8 --temperature 1.0 --max_tokens 1024 --output_dir output/exp_018_qwen_scierc_seed456",
      "server": "autodl-5090",
      "seed": 456,
      "N": 8,
      "T": 1.0,
      "max_tokens": 1024,
      "model_name": "Qwen3-8B-SciERC-merged-v2",
      "model_path": "checkpoints/qwen3-8b-scierc-merged-v2",
      "dataset": "scierc",
      "subtask": "joint",
      "data_path": "data/scierc/processed_data",
      "data_count": 551,
      "use_train_format": true,
      "is_new_inference": true,
      "parent": null,
      "run_timestamp": "2026-05-15 13:08~13:13",
      "output_path": "output/exp_018_qwen_scierc_seed456/",
      "log_path": "output/exp_018_qwen_scierc_seed456/run.log",
      "samples_md5": "46d0de47ad7693c07e7df3a77c90c3be"
    },
    "exp_018_llama_scierc_seed123": {
      "command": "python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask joint --seed 123 --n_samples 8 --temperature 1.0 --max_tokens 1024 --output_dir output/exp_018_llama_scierc_seed123",
      "server": "autodl-5090",
      "seed": 123,
      "N": 8,
      "T": 1.0,
      "max_tokens": 1024,
      "model_name": "LLaMA-3.1-8B-SciERC-merged",
      "model_path": "checkpoints/llama3.1-8b-scierc-merged",
      "dataset": "scierc",
      "subtask": "joint",
      "data_path": "data/scierc/processed_data",
      "data_count": 551,
      "use_train_format": true,
      "is_new_inference": true,
      "parent": null,
      "run_timestamp": "2026-05-15 13:09",
      "output_path": "output/exp_018_llama_scierc_seed123/",
      "log_path": "output/exp_018_llama_scierc_seed123.log",
      "samples_md5": "072eeca68236d46b4c5c84b945209abc"
    },
    "exp_018_llama_scierc_seed456": {
      "command": "原始命令为 exp_007: python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask joint --seed 456 --n_samples 8 --temperature 1.0 --max_tokens 1024 --output_dir output/exp_007_llama_seed456",
      "server": "autodl-5090",
      "seed": 456,
      "N": 8,
      "T": 1.0,
      "max_tokens": 1024,
      "model_name": "LLaMA-3.1-8B-SciERC-merged",
      "model_path": "checkpoints/llama3.1-8b-scierc-merged",
      "dataset": "scierc",
      "subtask": "joint",
      "data_path": "data/scierc/processed_data",
      "data_count": 551,
      "use_train_format": true,
      "is_new_inference": false,
      "parent": "exp_007_llama_seed456",
      "original_run_timestamp": "2026-05-14 23:08~23:12",
      "copy_timestamp": "2026-05-15 13:08",
      "output_path": "output/exp_018_llama_scierc_seed456/",
      "log_path": "output/exp_018_llama_scierc_seed456/run.log (inherited from exp_007)",
      "samples_md5": "2034b5e4989c387b84e2b7225c7e5367"
    }
  }
}
```

</details>

---
