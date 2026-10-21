# ops eval and submit next

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval_and_submit_next_20260522T094543_result.json`
- **Structured JSON:** [`965c77b351791316d053.json`](../../sessions/96/965c77b351791316d053.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正在启动（Train: 4720, Eval: 1190），模型加载中。

---

## 报告

### 1. 代码修改
`train/train_sft.py` 和 `eval/evaluate.py` 的 `--condition` choices 列表已添加 `exc_type_only`, `exc_stacktrace_only`, `exc_message_only`。数据加载逻辑无需修改——已有的 `f"{condition}_train.jsonl"` 模式直接适配，训练时传 `--data_dir /root/autodl-tmp/trace-verdict-study-data/exc_subcomponent/` 即可。

### 2. Gradient Masking 评估结果

| Metric | Value | 95% CI |
|--------|-------|--------|
| **Accuracy** | **98.99%** | [98.4%, 99.5%] |
| Majority baseline | 71.5% | — |
| **Lift** | **+27.5pp** | [+25.0pp, +30.0pp] |
| Pass F1 | 0.993 | [0.989, 0.996] |
| **Fail F1** | **0.982** | [0.972, 0.991] |
| Pass P/R | 1.00 / 0.99 | — |
| Fail P/R | 0.98 / 0.99 | — |

### 3. exc_type_only 训练
已提交，tmux session `exc_type_only_seed42`，cuda:1，Train=4720 / Eval=1190。Registry 已创建（PREPARING, hypothesis + parent 已设置）。

---
