# ops check codellama13b status

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_codellama13b_status_20260517T130350_result.json`
- **Structured JSON:** [`5eea368d4f70bd1d8cdb.json`](../../sessions/5e/5eea368d4f70bd1d8cdb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 实验状态

| 实验 | 状态 | 完成时间 | GPU |
|------|------|----------|-----|
| codellama13b_exception_only_seed42 | **已完成** | May 16 22:43 (cuda:0) | 空闲 0% |
| codellama13b_vota_seed42 | **已完成** | May 17 02:19 (cuda:1) | 空闲 0% |

两个实验都跑了 444 steps（3 个 checkpoint + final），无 tmux session、无训练进程在运行。

### Eval 结果

| 指标 | exception_only | vota |
|------|---------------|------|
| **Accuracy** | **99.83%** | **98.57%** |
| Accuracy 95% CI | [99.58%, 100%] | [97.90%, 99.16%] |
| Pass F1 | 99.88% | 99.00% |
| Fail F1 | 99.71% | 97.48% |
| Majority baseline | 71.51% | 71.51% |
| N | 1190 | 1190 |

exception_only 接近完美（仅 2 例错误），vota 稍低但仍然很强。

### Checkpoint 位置

- `/root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_exception_only_seed42/final/`
- `/root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_vota_seed42/final/`

每个 final 目录含 adapter (~239MB safetensors) + tokenizer + eval_results.json + predictions.jsonl。

### 模型权重

| 模型 | 路径 | 状态 |
|------|------|------|
| Qwen2.5-Coder-7B-Instruct | `/root/trace-verdict-study/models/Qwen2.5-Coder-7B-Instruct` | **存在** |
| DeepSeek-Coder-6.7B-Instruct | `/root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct` | **存在** |

### 磁盘空间

| 挂载点 | 总量 | 已用 | 可用 | 使用率 |
|--------|------|------|------|--------|
| / (root) | 30G | 24G | 6.2G | 80% |
| /root/autodl-tmp | 250G | 209G | 42G | 84% |

### 注意事项

- GPU 0 显示 49GB 显存占用但无 compute app，可能是驱动缓存残留，不影响后续使用
- outputs/codellama13b_nomarker_seed42 是空目录（之前的失败尝试残留）

---
