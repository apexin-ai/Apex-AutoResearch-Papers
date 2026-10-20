# code prepare eval batch predictions

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prepare_eval_batch_predictions_20260516T012041_result.json`
- **Structured JSON:** [`b86eb863310d76c917b4.json`](../../sessions/b8/b86eb863310d76c917b4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本就绪。

---

## 汇总

**脚本路径**: `/root/trace-verdict-study/run_missing_predictions.sh`（chmod 755，未执行）

**用法**: `bash run_missing_predictions.sh [GPU_ID]`，默认 GPU 0

### 两个 eval 命令

| # | 条件 | Checkpoint | Base Model | max_length | 测试样本数 |
|---|------|-----------|------------|------------|-----------|
| 1 | `deepseek_full_trace_seed42_v3` | `.../deepseek_full_trace_seed42_v3/final/` | DeepSeek-Coder-6.7B-Instruct | 16384 | 1190 |
| 2 | `debugbench_vota` | `.../debugbench_vota/final/` | Qwen2.5-Coder-7B-Instruct | 2048 | 426 |

### 注意

- `debugbench_vota` 的 base model 是 **Qwen**（不是 DeepSeek），从 adapter_config.json 确认
- checkpoint 实际目录名是 `deepseek_full_trace_seed42_v3`（不是 `deepseek_full_trace_v3`）

### GPU 时间估算

evaluate.py 是逐样本 greedy decoding（max_new_tokens=1），主要时间在 prefill：

- **deepseek_full_trace_seed42_v3**: 1190 样本 × max_length 16384 → 长序列 prefill 较慢，6.7B 模型在 RTX PRO 6000 上约 **2-3 秒/样本** → 预估 **40-60 分钟**
- **debugbench_vota**: 426 样本 × max_length 2048 → 短序列，7B 模型约 **0.5-1 秒/样本** → 预估 **5-8 分钟**

总计约 **45-70 分钟**。

---
