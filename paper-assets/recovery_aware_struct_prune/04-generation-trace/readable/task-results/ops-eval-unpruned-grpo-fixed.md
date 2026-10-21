# ops eval unpruned grpo fixed

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval-unpruned-grpo-fixed_20260516T033838_result.json`
- **Structured JSON:** [`972fa3f597769b471aee.json`](../../sessions/97/972fa3f597769b471aee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

双卡 eval 均已成功启动，汇报如下：

### 参数确认
`--output_path` 是正确参数名（非 `--output_file`）。

### 启动状态

| Job | GPU | PID | 显存占用 | 状态 |
|-----|-----|-----|---------|------|
| eval_grpo_unpruned_v2_step100 | cuda:0 | 83594 | 17585 MiB | 运行中 (99% CPU) |
| eval_grpo_unpruned_v2_step90 | cuda:1 | 83672 | 15085 MiB | 运行中 (99% CPU) |

两个 eval 进程均已加载模型到 GPU 并开始推理，这次参数名正确，不会再失败。

---
