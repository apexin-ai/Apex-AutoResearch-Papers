# prepare exp e qwen3 3shot baseline

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prepare_exp-e-qwen3-3shot-baseline_20260519T043217_result.json`
- **Structured JSON:** [`16c194b42b19ea05f7b9.json`](../../sessions/16/16c194b42b19ea05f7b9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry run 通过。以下是完整结果。

---

## 准备好的命令

**submit_training_job 参数：**
- `server`: `seetacloud-westd-4x5090`
- `exp_id`: `exp-e-qwen3-3shot-baseline`
- `gpu_ids`: `["cuda:3"]`（待释放）
- `command`:

```bash
cd /home/sonny/exec-sim-repair-verifier && HF_HUB_OFFLINE=1 /root/miniconda3/bin/python eval_3shot_baseline.py --model_name_or_path /root/autodl-tmp/models/Qwen/Qwen3-8B --data_dir data/swebench_full --split test --max_seq_length 4096 --device cuda:0 --output_dir artifacts/eval_3shot_qwen3_8b
```

## Dry run 结果

```
Train: 5869 instances
Test:  9784 instances (labels={1: 7138, 0: 2646})
Demos: 3 (labels: ['PASS', 'FAIL', 'PASS'])
Sample prompt: 8 messages, ~6951 chars
```

## 之前 DeepSeek 3-shot baseline 失败分析

Registry 记录的 failure_reason（"100% unparseable, context length overflow"）是过期元数据。**实际最终运行成功完成**，日志显示：

| 指标 | 值 |
|---|---|
| per-test accuracy | 46.28% |
| variant accuracy | 45.83% (22/48) |
| majority baseline | 73.0% |
| truncated | 0/9784 |
| unparseable | 0 |
| 运行时间 | 33.8 min |

DeepSeek 3-shot 大幅偏向预测 FAIL（4886 FN），accuracy 低于 majority baseline 26.7pp。

## 本次规避措施

1. **无 context overflow 风险**：DeepSeek 在 seq_length=4096 下 truncated=0，Qwen3 tokenizer 效率相当
2. **Qwen3 thinking mode 自动禁用**：脚本检测路径中的 "qwen3" 自动设置 `enable_thinking=False`
3. **`parse_prediction` 已有 `&lt;/think>` fallback**：即使 thinking 泄漏也能正确解析
4. **不含 `--no_wandb`**：脚本不用 wandb，无此参数
5. **不硬编码 `CUDA_VISIBLE_DEVICES`**：由 submit_training_job 框架注入
6. **预估运行时间**：DeepSeek 6.7B 用了 34min，Qwen3-8B 更大，预计 60-90min

---
