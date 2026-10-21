# prep no evi test eval commands

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_no-evi-test-eval-commands_20260521T225630_result.json`
- **Structured JSON:** [`9322c10ef3c8b9bb2ca5.json`](../../sessions/93/9322c10ef3c8b9bb2ca5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个命令均成功启动，模型加载正常，开始推理后被 timeout 终止。

---

## 验证结果

**所有路径存在** ✓  
**`--no_evidence` 参数支持** ✓  
**两个命令 dry-run 通过** ✓

### 14B no-evidence test eval 命令

```bash
CUDA_VISIBLE_DEVICES=X python -m freige.eval.test_inference \
  --model_path /root/autodl-tmp/models/Qwen/Qwen3-14B \
  --sft_adapter /root/autodl-tmp/sft_output_14b/checkpoint-144 \
  --data_path /root/autodl-tmp/data/re-docred-repo/data \
  --output_dir /root/autodl-tmp/eval_results/test_eval_14b_sft_s42_no_evi \
  --batch_size 1 --max_new_tokens 2048 --no-quantize --seed 42 \
  --split test_revised --no_evidence
```

### 1.7B no-evidence test eval 命令

```bash
CUDA_VISIBLE_DEVICES=X python -m freige.eval.test_inference \
  --model_path /root/autodl-tmp/models/Qwen/Qwen3-1.7B \
  --sft_adapter /root/autodl-tmp/sft_output_qwen3_1_7b_bf16 \
  --data_path /root/autodl-tmp/data/re-docred-repo/data \
  --output_dir /root/autodl-tmp/eval_results/test_eval_1_7b_sft_s42_no_evi \
  --batch_size 1 --max_new_tokens 2048 --no-quantize --seed 42 \
  --split test_revised --no_evidence
```

（`X` = 提交时替换为空闲 GPU 编号，按 C001 要求先 `nvidia-smi` 确认显存 < 2GB）

### 磁盘空间

| 路径 | 总量 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| `/root/autodl-tmp` | 350G | 244G | 107G | 70% |

空间充足，eval 输出文件很小，无磁盘风险。

### 问题
无。命令前需加 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige &&` 环境前缀。

---
