# code mrsc write and prepare

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mrsc_write_and_prepare_20260520T162510_result.json`
- **Structured JSON:** [`fac9aaf1558f2baa59a9.json`](../../sessions/fa/fac9aaf1558f2baa59a9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 产出汇总

### Part 1: run_mrsc.py

已写入 `artifacts/experiments/mrsc/run_mrsc.py`，语法验证通过。

用法示例：
```bash
CUDA_VISIBLE_DEVICES=3 python run_mrsc.py \
  --base_model_path <模型路径> \
  --adapter_path <可选adapter> \
  --data_path &lt;samples.jsonl> \
  --output_dir ./output_mrsc \
  --dispute_threshold 0.6 \
  --round2_weight 2.0 \
  --batch_size 16
```

### Part 2: autodl-5090-c 环境探查

**FewNERD samples JSONL（可用作 Round 1 数据源）：**

| 路径 | 大小 | 行数 |
|------|------|------|
| `/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_7b/qwen25_7b_n8_seed42/samples.jsonl` | 675M | 37,648 |
| `/root/autodl-tmp/struct_self_consist_ie/output/exp_fewnerd_seed789/samples.jsonl` | 643M | 37,648 |
| `/root/autodl-tmp/struct_self_consist_ie/output/14b_final_inference/conll2003_n8/samples.jsonl` | 38M | 3,453 |
| `/root/autodl-tmp/struct_self_consist_ie/output/14b_final_inference/scierc_n8/samples.jsonl` | 3.8M | 551 |

（fewnerd_7b/qwen25_7b_n8_seed123 目录存在但为空）

**可用模型：**

| 类型 | 路径 |
|------|------|
| 基座 | `/root/autodl-tmp/.hf_cache/Qwen2.5-7B-Instruct` |
| 基座 | `/root/autodl-tmp/.hf_cache/modelscope_hub/Qwen/Qwen2___5-14B-Instruct` |
| 基座 | `/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B` |
| merged | `checkpoints/qwen25-7b-fewnerd-merged` |
| merged | `checkpoints/qwen25-14b-fewnerd-merged-final` |
| merged | `checkpoints/qwen25-14b-fewnerd-merged-ckpt36000` |
| merged | `checkpoints/qwen3-8b-fewnerd-exp021-merged` |
| merged | `checkpoints/qwen3-8b-conll2003-merged` |
| merged | `checkpoints/qwen3-8b-scierc-merged-v2` |
| merged | `checkpoints/qwen25-7b-wnut17-merged` |
| LoRA | `checkpoints/qwen25-7b-fewnerd-qlora-s42` |
| LoRA | `checkpoints/qwen25-14b-fewnerd-qlora-s42` |
| LoRA | `checkpoints/qwen3-8b-fewnerd-exp021-lora` |
| LoRA | `checkpoints/llama3.1-8b-scierc-lora` |

（所有 checkpoints 路径前缀为 `/root/autodl-tmp/struct_self_consist_ie/checkpoints/`）

**Python / 依赖环境：**
- Python 3.12.3（conda base，`/root/miniconda3/bin/python`）
- PyTorch 2.10.0+cu128
- transformers 4.57.1, peft 0.17.1, scipy ✓, sklearn ✓

**GPU 状态：**

| GPU | 型号 | 显存占用 | 利用率 |
|-----|------|----------|--------|
| 0 | RTX 5090 | 31101/32607 MiB | 97% |
| 1 | RTX 5090 | 0/32607 MiB | 0% |
| 2 | RTX 5090 | 0/32607 MiB | 0% |
| **3** | **RTX 5090** | **0/32607 MiB** | **0%** |

**cuda:3 空闲，可用。**

**磁盘：** `/root/autodl-tmp` 350G 总量，127G 可用（64% 使用）。

---
