# ssh verify alpha1p0 max completion

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_verify_alpha1p0_max_completion_20260523T191307_result.json`
- **Structured JSON:** [`4ac890c188b8f31abc90.json`](../../sessions/4a/4ac890c188b8f31abc90.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

The launch command wasn't captured in the log. The evidence is already conclusive from the training metrics though.

```
grpo_rasp_20_fair 实际 max_completion_length: 1024
证据来源: 训练日志 completions/max_length 指标
```

**证据：**
- 日志中每10步打印的 metrics 里 `completions/max_length` 始终为 **`1024`**（step 10 到 step 100 全部是 1024）
- `completions/clipped_ratio` 在 91%~96% 之间，说明生成被截断在 1024 token
- 脚本 `train_grpo_v5.py` 的 argparse 默认值是 512，但 `completions/max_length=1024` 说明启动时传入了 `--max_completion_length 1024`
- 日志中没有直接打印 argparse 参数（grep "max_completion" 为空），但 TRL GRPOTrainer 的 `completions/max_length` 指标就是实际使用的 `max_completion_length`

**结论：registry 记录的 max_completion_length=1024 是正确的，不是默认的 512。**

---
