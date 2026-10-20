# analyze exp 001 eval 3B raw gen

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_exp_001_eval_3B_raw_gen_20260514T093608_result.json`
- **Structured JSON:** [`f0b8b0c5688be9e54d65.json`](../../sessions/f0/f0b8b0c5688be9e54d65.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp_001_eval_3B_raw_gen 结果

| Benchmark | Score | Detail |
|-----------|-------|--------|
| **GSM8K** | **0.6050** | 798/1319 correct |
| **HumanEval** | **0.0000** | 0/164 correct |

### 对比

| Model | GSM8K | HumanEval |
|-------|-------|-----------|
| 0.5B raw | 0.0628 | 0.0305 |
| **3B raw** | **0.6050** | **0.0000** |
| 1.5B SFT | 0.6368 | 0.1280 |

### 异常：HumanEval pass@1 = 0

HumanEval 全部失败。从 item_responses 看，模型生成的是解释性文本 + markdown 代码块格式（`"Here's the completed Python function:\n\n```python"`），而非直接输出可执行代码。评估器无法从这种格式中提取有效代码。这是裸基座模型的典型行为——它在续写时倾向于生成"教程式"回答而非纯代码补全。

0.5B raw 反而有 0.0305，可能是因为小模型更倾向于直接续写代码而非生成解释性文本。

GSM8K 0.6050 正常，接近 1.5B SFT 的 0.6368，说明 3B base model 的数学推理能力本身不错。

### 结果文件

- `/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_raw/eval_results.json`
- `/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_raw/correctness_matrix.json`
- `/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_raw/item_responses.json`

无 W&B run。

---
