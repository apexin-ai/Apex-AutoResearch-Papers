# code trace then judge prep

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_trace-then-judge-prep_20260512T032031_result.json`
- **Structured JSON:** [`6e90ff9a216ebeaafb8a.json`](../../sessions/6e/6e90ff9a216ebeaafb8a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报结果：

---

## Trace-then-Judge 数据 + 脚本准备结果

### 1. 数据转换

| 数据集 | 样本数 | trace 长度 (words) |
|--------|--------|-------------------|
| trace_train.jsonl | 15,290 | mean=30.1, median=30, min=22, max=42 |
| trace_val.jsonl | 1,896 | mean=30.2, median=30, min=22, max=42 |
| trace_test.jsonl | 1,890 | mean=30.3, median=30, min=22, max=42 |

PASS 样本示例 target:
> `Checking 'separate_paren_groups': the code follows the correct algorithm. The test assertions align with the function's output. Execution completes without errors. Verdict: PASS`

FAIL 样本示例 target:
> `Analyzing: the test calls 'separate_paren_groups' and checks the output. The code contains an off-by-one error in an integer value. This modification causes the function to produce incorrect output, leading to an assertion failure. Verdict: FAIL`

### 2. Dry-run 结果：通过

- 5 steps 正常完成，无报错
- Loss 快速下降：6.19 → 3.38（5 steps 内）
- 截断率极低：train 10/15290 (0.1%), val 0/1896 (0.0%)
- 每步耗时 ~2.8s（单卡 5090）

### 3. 创建的文件

- `build_trace_data.py` — 数据转换脚本
- `train_trace_judge.py` — 训练脚本（CWM generation 风格，loss 仅在 target tokens 上计算）
- `eval_trace_judge.py` — 评估脚本（提取 Verdict: PASS/FAIL，报告 classification metrics + trace quality metrics）

### 4. 完整训练命令

```bash
cd /home/sonny/exec-sim-repair-verifier && python3 train_trace_judge.py \
  --data_dir data/ \
  --model_name Qwen/Qwen3-4B \
  --output_dir checkpoints_trace/ \
  --batch_size 2 \
  --grad_accumulation 16 \
  --lr 2e-4 \
  --epochs 3 \
  --seed 42 \
  --run_name trace-judge-qwen3-4b-lora \
  --wandb_project exec-sim-repair-verifier
```

### 5. 评估命令

```bash
cd /home/sonny/exec-sim-repair-verifier && python3 eval_trace_judge.py \
  --data_dir data/ \
  --checkpoint_dir checkpoints_trace/best/ \
  --model_name Qwen/Qwen3-4B \
  --output eval_trace_results.json \
  --max_new_tokens 150
```

---
