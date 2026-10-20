# code plan 005 train config

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_005_train_config_20260515T232914_result.json`
- **Structured JSON:** [`75ec6f9d862e52ea9de6.json`](../../sessions/75/75ec6f9d862e52ea9de6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 产出汇总

### 1. 代码修改（已完成并提交）

`train/train_sft.py:104` 和 `eval/evaluate.py:121` 的 `--condition choices` 列表添加了 5 个 DebugBench 条件：`debugbench_no_trace`, `debugbench_vota`, `debugbench_full_trace`, `debugbench_ae_only`, `debugbench_exception_only`。

无需其他改动——`load_data()` 用 `f"{condition}_train.jsonl"` 构造路径，`debugbench_no_trace` 正好匹配 `debugbench_no_trace_train.jsonl`。

### 2. 数据兼容性确认

| 项目 | 状态 |
|------|------|
| 文件路径 | ✅ `debugbench_{condition}_{train,test}.jsonl` 全部存在 |
| 数据量 | ✅ 每条件 1622 train / 426 test |
| Label 格式 | ✅ `"output": "pass"/"fail"`，与 DCSH 一致 |
| Prompt 格式 | ✅ 尾部 `"Does this code pass all tests? Answer: "`，evaluate.py 的 `classify_prediction()` 兼容 |
| Trace marker | ✅ vota/full_trace/exception_only/ae_only 含 `"Execution trace:\n"` marker，`truncate_traces()` 可正常工作 |

### 3. 训练参数（与 DCSH 完全一致）

| 参数 | 值 |
|------|-----|
| LoRA r/alpha/dropout | 16 / 32 / 0.05 |
| target_modules | q/k/v/o/gate/up/down_proj |
| epochs | 3 |
| batch / grad_accum | 4 / 8 (effective=32) |
| lr / warmup | 2e-4 / 0.1 |
| max_length | 2048 |
| bf16 | True |

DebugBench 步数：1622/32 ≈ 51 steps/epoch × 3 = **153 steps**（DCSH 是 444 steps），预计每条件 ~18 min 训练 + ~2 min eval。

### 4. 5 条完整训练命令

每个 CONDITION 替换为 `exception_only` / `no_trace` / `ae_only` / `vota` / `full_trace`：

```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
export HF_HOME=/root/autodl-tmp/.hf_cache && \
cd /root/trace-verdict-study && \
python train/train_sft.py \
  --condition debugbench_CONDITION \
  --gradient_checkpointing \
  --gpu 0 \
  --seed 42 \
  --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/debugbench_CONDITION \
  --wandb_project trace-verdict-study \
  --wandb_run_name debugbench_CONDITION_seed42 && \
python eval/evaluate.py \
  --condition debugbench_CONDITION \
  --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/debugbench_CONDITION/final \
  --gpu 0 \
  --output /root/autodl-tmp/trace-verdict-study-checkpoints/debugbench_CONDITION/final/eval_results.json"
```

### 5. RUNNING 实验进度

| 实验 | GPU | 进度 | 预估剩余 |
|------|-----|------|----------|
| `full_trace_512tok_seed42` | cuda:0 | 130/444 (29%), epoch 1 | ~36 min 训练 + ~3 min eval（含 2 次 epoch eval） |
| `full_trace_256tok_seed42` | cuda:1 | 151/444 (34%), epoch 2 刚开始 | ~34 min 训练 + ~3 min eval（还剩 2 次 epoch eval） |

**两个 GPU 都被占用**，DebugBench 训练需等当前实验完成后才能启动。预计 ~40 min 后两个 GPU 都空出。

---
