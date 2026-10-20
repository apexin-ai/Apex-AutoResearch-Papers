# ops prepare next submissions

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_prepare_next_submissions_20260516T012708_result.json`
- **Structured JSON:** [`ebc0af25e7babf978cec.json`](../../sessions/eb/ebc0af25e7babf978cec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有信息已收集完毕。以下是检查结果：

---

## 实验就绪状态报告

### 1. full_trace_2048tok_seed42 ✅ 就绪（有一个注意事项）

| 检查项 | 状态 |
|--------|------|
| 训练脚本 `train/train_sft.py` | ✅ 存在 |
| 训练数据 `full_trace_train.jsonl` | ✅ `/root/autodl-tmp/trace-verdict-study-data/full_trace_train.jsonl` |
| 测试数据 `full_trace_test.jsonl` | ✅ `/root/autodl-tmp/trace-verdict-study-data/full_trace_test.jsonl` |
| 基座模型 Qwen2.5-Coder-7B-Instruct | ✅ `/root/trace-verdict-study/models/Qwen2.5-Coder-7B-Instruct` |

**提交命令：**

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
export HF_HOME=/root/autodl-tmp/.hf_cache
cd /root/trace-verdict-study

nohup python train/train_sft.py \
  --condition full_trace \
  --data_dir /root/autodl-tmp/trace-verdict-study-data/ \
  --model_path /root/trace-verdict-study/models/Qwen2.5-Coder-7B-Instruct \
  --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_2048tok \
  --max_trace_tokens 2048 \
  --seed 42 \
  --wandb_run_name full_trace_2048tok_seed42 \
  --gradient_checkpointing \
  --gpu 0 \
> /tmp/full_trace_2048tok.log 2>&1 &
```

**注意：** `--max_trace_tokens 2048` 控制 trace 截断到 2048 token（与 256tok/512tok/1024tok 系列一致）。SFTConfig 的 `max_length` 硬编码为 2048，所以当 trace 截断到 2048 token 时实际上不会截断（overhead 约 50-80 token，训练时 chat template 会把 input 截到 budget 内）。如果 2048tok 的含义是"允许更长序列"，可能需要同时修改 `train_sft.py` 中的 `max_length`。

**⚠️ full_trace_1024tok 尚未训完** — 该目录只有 checkpoint-148、checkpoint-296，没有 `final/`。如果 1024tok 还在跑，2048tok 需要排在它后面。

---

### 2. deepseek_full_trace_seed42_v3 predictions ✅ 就绪

| 检查项 | 状态 |
|--------|------|
| Checkpoint `final/` | ✅ 存在（adapter_model.safetensors 153MB） |
| eval_results.json | ✅ 已有（说明 eval 跑过，但当时没加 `--save_predictions`） |
| predictions.jsonl | ❌ 缺失 |
| 评估脚本 `eval/evaluate.py` | ✅ 存在，支持 `--save_predictions` |
| 测试数据 `full_trace_test.jsonl` | ✅ 存在 |
| 基座模型 DeepSeek-Coder-6.7B | ✅ `/root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6.7b-instruct` |

**提交命令：**

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
export HF_HOME=/root/autodl-tmp/.hf_cache
cd /root/trace-verdict-study

nohup python eval/evaluate.py \
  --condition full_trace \
  --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_full_trace_seed42_v3/final \
  --model_path /root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6.7b-instruct \
  --data_dir /root/autodl-tmp/trace-verdict-study-data/ \
  --gpu 0 \
  --max_length 16384 \
  --output /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_full_trace_seed42_v3/final/eval_results.json \
  --save_predictions \
> /tmp/deepseek_full_trace_v3_pred.log 2>&1 &
```

（命令直接来自已有的 `run_missing_predictions.sh`，已验证参数正确）

---

### 3. debugbench_vota_seed42 predictions ❌ 目录不存在

`/root/autodl-tmp/trace-verdict-study-checkpoints/debugbench_vota_seed42/` 不存在。

存在的是 **`debugbench_vota/`**（无 seed42 后缀），其中：
- `final/` 目录 ✅ 存在（有 adapter_model.safetensors、eval_results.json）
- `predictions.jsonl` ❌ 缺失

**提交命令：**

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
export HF_HOME=/root/autodl-tmp/.hf_cache
cd /root/trace-verdict-study

nohup python eval/evaluate.py \
  --condition debugbench_vota \
  --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/debugbench_vota/final \
  --model_path /root/trace-verdict-study/models/Qwen2.5-Coder-7B-Instruct \
  --data_dir /root/autodl-tmp/trace-verdict-study-data/ \
  --gpu 0 \
  --output /root/autodl-tmp/trace-verdict-study-checkpoints/debugbench_vota/final/eval_results.json \
  --save_predictions \
> /tmp/debugbench_vota_pred.log 2>&1 &
```

（同样来自 `run_missing_predictions.sh`，已验证）

---

### 汇总

| 实验 | 状态 | 阻塞项 |
|------|------|--------|
| full_trace_2048tok_seed42（训练） | ✅ 可提交 | ⚠️ 确认 1024tok 是否跑完释放 GPU；确认 max_length=2048 是否需要调大 |
| deepseek_full_trace_seed42_v3（eval） | ✅ 可提交 | 无 |
| debugbench_vota（eval） | ✅ 可提交 | 注意实际目录名是 `debugbench_vota`，不是 `debugbench_vota_seed42` |

两个 eval 任务可以串行跑（`run_missing_predictions.sh` 已经打包好了，可以直接 `bash run_missing_predictions.sh 0` 一键执行）。

---
