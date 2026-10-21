# infra verify inference deploy

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_verify-inference-deploy_20260514T084054_result.json`
- **Structured JSON:** [`849ff48ee3858491da6c.json`](../../sessions/84/849ff48ee3858491da6c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证完成。

### 结果

| 检查项 | 状态 |
|--------|------|
| inference.py 部署 | **yes** (15632 bytes, 2026-05-14 16:07) |
| dry-run `--help` | **pass** (无 ImportError) |
| SFT checkpoint | **存在** `/root/autodl-tmp/sft_output/adapter_config.json` |
| DocRED 数据 | **存在** `/root/autodl-tmp/data/docred/dev.json` |
| Base model | **存在** `/root/autodl-tmp/models/Qwen3-4B/config.json` |

### 参数匹配分析

任务给的命令用 `--model_path /root/autodl-tmp/sft_output`，但根据 argparse 定义，`--model_path` 的说明是"Base model 路径，或 LoRA adapter 路径（需配合 `--base_model`）"。SFT output 是 LoRA adapter，所以需要同时指定 `--base_model`。

`--base_model` 默认值已经是 `/root/autodl-tmp/models/Qwen3-4B`，所以不显式传也行，但显式传更安全。

### 验证后的 SFT eval 完整命令

```bash
cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=0 python -m freige.eval.inference \
  --model_path /root/autodl-tmp/sft_output \
  --base_model /root/autodl-tmp/models/Qwen3-4B \
  --data_path /root/autodl-tmp/data/docred \
  --output_dir /root/runs/faith-evidence-ie/eval_sft \
  --batch_size 4 \
  --max_new_tokens 1024
```

`--base_model` 的默认值恰好匹配，可省略，但建议保留以明确意图。其余参数名 (`--model_path`, `--data_path`, `--output_dir`, `--batch_size`, `--max_new_tokens`) 全部与 argparse 定义一致。

---
