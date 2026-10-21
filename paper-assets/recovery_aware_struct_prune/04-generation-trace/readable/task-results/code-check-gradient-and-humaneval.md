# code check gradient and humaneval

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_check_gradient_and_humaneval_20260517T075413_result.json`
- **Structured JSON:** [`d2df4860fe26bb32d833.json`](../../sessions/d2/d2df4860fe26bb32d833.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### westb-23072: Gradient eval

**状态: Running** (PID 691565)
- `run_remaining_ablation.sh` 已自动启动，当前在 scoring_ablation_v2 tmux 中执行 gradient pipeline Step 2/4 (eval post-prune)
- 模型: `pruned_gradient_20` (actual sparsity 19.09%)
- 进度: 12/200 samples (6%), 预计 ~1.5h 剩余
- GPU 0: 13GB / 98GB, 77% util

同时 GPU 1 上还在跑 `eval_unstructured_20` (n=1319, PID 680604), 17.7GB / 98GB, 89% util。

### westd-11672: HumanEval sft_rasp_20

**状态: Completed** (PID 7528 已结束)
- **pass@1 = 7.32%** (12/164), stderr = 0.0203
- 结果已保存: `eval_humaneval_sft_rasp_20.json`
- 主要失败模式: 模型输出自然语言思考过程而非代码 (SyntaxError: unterminated string literal), 以及语法错误 (括号未闭合等)
- median response length = 512 (频繁触达 max_tokens 截断)

### GPU 利用概况

| 服务器 | GPU | 占用 | Util | 任务 |
|--------|-----|------|------|------|
| westb-23072 | cuda:0 | 13GB | 77% | gradient eval (PID 691565) |
| westb-23072 | cuda:1 | 17.7GB | 89% | unstructured eval (PID 680604) |
| westd-11672 | cuda:0 | 17.7GB | 90% | python (PID 3331) |
| westd-11672 | cuda:1 | 13GB | 88% | python (PID 3335) |
| westd-11672 | cuda:2 | 13GB | 88% | python (PID 3333) |
| westd-11672 | cuda:3 | 0MB | 0% | idle |

---
