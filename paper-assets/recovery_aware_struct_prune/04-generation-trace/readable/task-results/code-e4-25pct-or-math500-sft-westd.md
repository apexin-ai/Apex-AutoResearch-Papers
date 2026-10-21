# code e4 25pct or math500 sft westd

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_e4_25pct_or_math500_sft_westd_20260518T131807_result.json`
- **Structured JSON:** [`39e62efc9a6b374f949d.json`](../../sessions/39/39e62efc9a6b374f949d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

启动成功。

**汇报**:

- **分支**: B-b（Dense Unpruned MATH-500 eval）
  - `sft_cka_only_25` 不存在 → 分支 B
  - `sft_cka_only_20` eval 已在 cuda:2 上运行（PID 2529，另一个任务提交的）→ 跳到 B-b
- **cuda:3 任务**: Dense Unpruned baseline MATH-500 eval
  - PID: 4223
  - 模型: `/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B/`
  - 输出: `/root/autodl-tmp/recovery_aware_struct_prune/results/math500_dense_unpruned.json`
  - 状态: 模型已加载（17585 MiB），正在加载 MATH 数据集
  - 预计时长: ~40-60 min（500 题生成式评测）

当前 westd-29022 GPU 占用：
| GPU | 任务 | PID |
|-----|------|-----|
| cuda:1 | math500_grpo_standard_20_fair | 2261 |
| cuda:2 | math500_sft_cka_only_20 | 2529 |
| cuda:3 | math500_dense_unpruned | 4223 |

---
