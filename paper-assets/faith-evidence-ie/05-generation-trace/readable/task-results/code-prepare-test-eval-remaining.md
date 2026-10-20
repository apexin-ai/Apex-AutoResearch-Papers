# code prepare test eval remaining

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prepare_test_eval_remaining_20260521T104033_result.json`
- **Structured JSON:** [`ee51e5ac8e90347bfde1.json`](../../sessions/ee/ee51e5ac8e90347bfde1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成。以下是汇总和命令。

---

## 验证结果

### 路径状态

| Scale | RSFT adapter (CED k1 s42) | Base model | SFT adapter | 状态 |
|-------|---------------------------|------------|-------------|------|
| 1.7B | `/root/autodl-tmp/rsft_output_qwen3_1_7b_k1` | `/root/autodl-tmp/models/Qwen/Qwen3-1.7B` | `/root/autodl-tmp/sft_output_qwen3_1_7b_bf16` | ✅ |
| 4B | `/root/autodl-tmp/rsft_output/` (已删除) | `/root/autodl-tmp/models/Qwen3-4B` | `/root/autodl-tmp/sft_output` | ❌ **adapter 不存在** |
| 8B | `/root/autodl-tmp/rsft_output_qwen3_8b_k1` | `/root/autodl-tmp/models/Qwen/Qwen3-8B` | `/root/autodl-tmp/sft_output_qwen3_8b_bf16` | ✅ |

**4B RSFT s42 问题**：原始 adapter `/root/autodl-tmp/rsft_output/` 已被删除。服务器上仅存的 4B RSFT 是：
- `rsft_output_ced_s43` (seed 43)
- `rsft_output_4b_sft_s44` / `rsft_output_4b_sft_s44_bf16` (seed 44)
- `rsft_output_random_k1` (random baseline, 非 CED 方法)

需要重新训练 4B RSFT s42，或确认是否用其他 seed 替代。

---

## 准备好的命令（2/3）

### 命令 1: Qwen3-1.7B RSFT test eval

```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && CUDA_VISIBLE_DEVICES=X python -m freige.eval.test_inference \
  --model_path /root/autodl-tmp/rsft_output_qwen3_1_7b_k1 \
  --base_model /root/autodl-tmp/models/Qwen/Qwen3-1.7B \
  --sft_adapter /root/autodl-tmp/sft_output_qwen3_1_7b_bf16 \
  --data_path /root/autodl-tmp/data/re-docred-repo/data \
  --output_dir /root/autodl-tmp/eval_results/test_eval_1_7b_rsft_s42 \
  --batch_size 1 --max_new_tokens 2048 --no-quantize --seed 42 \
  --split test_revised"
```

### 命令 2: Qwen3-4B RSFT test eval

**❌ 无法生成** — adapter 已删除。

### 命令 3: Qwen3-8B RSFT test eval

```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && CUDA_VISIBLE_DEVICES=X python -m freige.eval.test_inference \
  --model_path /root/autodl-tmp/rsft_output_qwen3_8b_k1 \
  --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B \
  --sft_adapter /root/autodl-tmp/sft_output_qwen3_8b_bf16 \
  --data_path /root/autodl-tmp/data/re-docred-repo/data \
  --output_dir /root/autodl-tmp/eval_results/test_eval_8b_rsft_s42 \
  --batch_size 1 --max_new_tokens 2048 --no-quantize --seed 42 \
  --split test_revised"
```

---

**说明**：
- `CUDA_VISIBLE_DEVICES=X` 需替换为实际空闲 GPU 编号（提交前按 C001 用 nvidia-smi 确认显存 < 2GB）
- RSFT adapter 使用根目录（含 `adapter_model.safetensors`，即最终 checkpoint）
- 1.7B 模型较小，约需 1 张 RTX 5090；8B 也需 1 张

---
