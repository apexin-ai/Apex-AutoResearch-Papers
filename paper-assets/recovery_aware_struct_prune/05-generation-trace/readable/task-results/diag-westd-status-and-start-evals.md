# diag westd status and start evals

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_westd_status_and_start_evals_20260517T100826_result.json`
- **Structured JSON:** [`a44433996e35b94a0d09.json`](../../sessions/a4/a44433996e35b94a0d09.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### GPU 状态：4 张全部在忙

| GPU | 进程 | 显存 | 利用率 | 进度 |
|-----|------|------|--------|------|
| cuda:0 | eval_math500_unpruned (PID 3331) | 17,658 MiB | 91% | **393/500 (79%)**, Acc@350=0.7343 |
| cuda:1 | eval_math500_grpo_standard_20 (PID 14556) | 29,610 MiB | 99% | **17/500 (3%)**, 极慢 (~6min/sample) |
| cuda:2 | eval_humaneval_grpo_standard_20 (PID 16488) | 12,980 MiB | 96% | **34/164 (21%)**, ~12s/it |
| cuda:3 | eval_math500_grpo_rasp_20_v2 (PID 11896) | 30,078 MiB | 99% | **63/500 (13%)**, Acc@50=0.3400, 极慢 |

### eval_math500_unpruned 状态

**确认在运行**，不是 PREPARING。PID 3331，14:20 启动，已跑 ~3.8h，预计还需 ~1-1.5h 完成。cron registry 状态有误。

### 问题发现

1. **cuda:0 和 cuda:1 都不空闲**，无法启动新 eval
2. **eval_humaneval_grpo_standard_20 Pass@1=0.0000**（20 samples），这个数字很反常，可能有问题
3. cuda:1 和 cuda:3 的 MATH eval 非常慢（每个 sample 5-6 分钟），估计要跑 20+ 小时才能完成 500 题

### 25% 模型文件：全部存在

- `pruned_rasp_25/` ✓
- `pruned_standard_25/` ✓
- `sft_rasp_25/` ✓
- `sft_standard_25/` ✓

### 25% 已有结果（不需要重新跑）

- `eval_postprune_rasp_25.json` ✓ ← 你要启动的这个已经跑完了
- `eval_postprune_standard_25.json` ✓
- `eval_grpo_standard_25.json` ✓
- `eval_grpo_standard_25_n1319.json` ✓
- `eval_grpo_rasp_25_qwen_math.json` ✓
- `eval_grpo_standard_25_qwen_math.json` ✓
- `eval_sft_qwen_math_rasp_25.json` ✓
- `eval_sft_qwen_math_standard_25.json` ✓

### 磁盘

根分区 18% (25GB free)，数据盘 879GB 仅用 17GB (3%)，健康。

### 结论

无空闲 GPU 可用。eval_postprune_rasp_25 已有结果无需重跑。HumanEval Pass@1=0 需要关注。cuda:1/3 上的 GRPO eval 速度极慢，建议观察是否是 max_new_tokens 导致长生成。

---
