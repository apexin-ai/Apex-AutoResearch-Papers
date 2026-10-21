# diagnose test eval 4b rsft v2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_test_eval_4b_rsft_v2_20260522T011535_result.json`
- **Structured JSON:** [`c90b892e2b80c9096599.json`](../../sessions/c9/c90b892e2b80c9096599.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

## 1. 失败根因

两个问题：
- **`--rsft_adapter` 不是有效参数**。`test_inference.py` 没有这个参数。按照脚本用法，RSFT adapter 应传给 `--model_path`，基座模型传给 `--base_model`。
- **基座模型路径错误**：命令用了 `/root/autodl-tmp/models/Qwen/Qwen3-4B`（不存在），正确路径是 `/root/autodl-tmp/models/Qwen3-4B`。

## 2. 修正后的完整命令

```
bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && CUDA_VISIBLE_DEVICES=2 python -m freige.eval.test_inference --model_path /root/autodl-tmp/rsft_output_ced_s42_v2 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/re-docred-repo/data --output_dir /root/autodl-tmp/eval_results/test_eval_4b_rsft_s42_v2 --batch_size 1 --max_new_tokens 2048 --no-quantize --seed 42 --split test_revised'
```

改动点：
- `--model_path` → 指向 RSFT adapter (`rsft_output_ced_s42_v2`)
- `--base_model` → 指向基座模型 (`/root/autodl-tmp/models/Qwen3-4B`)
- 删除不存在的 `--rsft_adapter` 参数
- 添加 `cd /root/autodl-tmp/freige`

## 3. Checkpoint 状态

`/root/autodl-tmp/rsft_output_ced_s42_v2/` 正常，包含 `adapter_model.safetensors` (504MB) 和 `adapter_config.json`，以及 5 个 checkpoint。

---
