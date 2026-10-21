# ops exp expanded downstream eval

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp_expanded_downstream_eval_20260520T170352_result.json`
- **Structured JSON:** [`09c178f92cfdf7c70cbd.json`](../../sessions/09/09c178f92cfdf7c70cbd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

PIQA 评估正常运行中，loglikelihood 推理进行中。任务正常启动，预计总运行时间约 15-20 小时（1 base + 9 策略模型，每个需训练+5 benchmark评估）。

任务总结：
- 脚本已创建并提交到 `cqa1-22115` 服务器
- 任务 `exp_expanded_downstream_eval` 已在 tmux 中运行
- 流程：base model eval → 3 策略 x 3 seeds 的 LoRA 训练+评估 → 统计分析
- 5 benchmarks: PIQA, TruthfulQA-MC2, WinoGrande, ARC-Challenge, GSM8K
- 每个模型训练后 merge LoRA、评估、然后清理 checkpoint 节省磁盘
- 结果会输出到 `results/exp_expanded_downstream_eval/summary.json`
- 日志：`~/runs/gen-depth-contamination/exp_expanded_downstream_eval.log`

---
