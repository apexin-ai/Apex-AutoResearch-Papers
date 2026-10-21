# diagnose grpo unstructured 20 disk

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_grpo_unstructured_20_disk_20260519T044411_result.json`
- **Structured JSON:** [`774b533e50e8bc0a5204.json`](../../sessions/77/774b533e50e8bc0a5204.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

## 诊断结果

**根因**：`/root/autodl-tmp` 分区（250G）在 checkpoint step 100 保存时 100% 满。model.safetensors (15G) 写入成功后，写 optimizer state (~9.5G) 时磁盘空间不足，触发 `iostream error`。optimizer.pt 写入失败后被清理，目前分区恢复到 9.5G 可用（97%）。

**空间占用**：
| 路径 | 大小 |
|---|---|
| `recovery_aware_struct_prune/` | ~226G（清理后）|
| `DeepSeek-R1-Distill-Qwen-7B/` | 15G |
| `data/` | 1.5G |
| **总计** | ~241G / 250G |

**checkpoint-100 状态**：model.safetensors + tokenizer 完好，optimizer.pt 和 training_args.bin 缺失。可用于推理/eval，不能恢复训练。

**可清理项**（不执行，仅列出）：
- `/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B/` — 15G（如不再需要）
- `grpo_unstructured_20/checkpoint-100/` — 15G（重跑时可删）
- 已完成实验的 checkpoint 子目录（如 `grpo_cka_only_20/checkpoint-100` 12G、`grpo_rasp_25` 11G 等）
- 预计可释放 30-50G+

**修复方案**：在 `train_grpo_v5.py` 的 GRPOConfig 中加 `save_only_model=True`，跳过 optimizer/scheduler 保存（每个 checkpoint 省 ~9.5G）。当前代码未设置该参数。

```json
{"root_cause":"autodl-tmp 250G 分区在 checkpoint step 100 写 optimizer.pt (~9.5GB) 时磁盘空间耗尽（model shard 15G 写入后剩余不足 1G）","error_type":"resource","disk_free_gb":9.5,"checkpoint_dir":"/root/autodl-tmp/recovery_aware_struct_prune/grpo_unstructured_20","partial_files":"checkpoint-100 缺 optimizer.pt 和 training_args.bin（写入失败后被清理），model.safetensors 15G 完好","fix_steps":["在 train_grpo_v5.py GRPOConfig 中添加 save_only_model=True（每 checkpoint 省 9.5G）","删除 grpo_unstructured_20/checkpoint-100（15G，无法恢复训练，重跑即可）","考虑删除 /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B（15G，如不再需要）","考虑清理已完成实验的旧 checkpoint 目录释放 30G+"],"can_auto_fix":true}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "autodl-tmp 250G 分区在 checkpoint step 100 写 optimizer.pt (~9.5GB) 时磁盘空间耗尽（model shard 15G 写入后剩余不足 1G）",
    "error_type": "resource",
    "disk_free_gb": 9.5,
    "checkpoint_dir": "/root/autodl-tmp/recovery_aware_struct_prune/grpo_unstructured_20",
    "partial_files": "checkpoint-100 缺 optimizer.pt 和 training_args.bin（写入失败后被清理），model.safetensors 15G 完好",
    "fix_steps": [
      "在 train_grpo_v5.py GRPOConfig 中添加 save_only_model=True（每 checkpoint 省 9.5G）",
      "删除 grpo_unstructured_20/checkpoint-100（15G，无法恢复训练，重跑即可）",
      "考虑删除 /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B（15G，如不再需要）",
      "考虑清理已完成实验的旧 checkpoint 目录释放 30G+"
    ],
    "can_auto_fix": true
  }
}
```

</details>

---
