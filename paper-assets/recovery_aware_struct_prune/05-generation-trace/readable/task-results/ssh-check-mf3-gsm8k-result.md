# ssh check mf3 gsm8k result

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_mf3_gsm8k_result_20260523T025114_result.json`
- **Structured JSON:** [`61d5c3124082b822a380.json`](../../sessions/61/61d5c3124082b822a380.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**v3 不存在。** 只有 v2 的结果，日志显示它保存为 `eval_gsm8k_grpo_qwen_math_cka_only_20_n500_v2.json`。PID 220343 对应的就是这个 v2 运行。

## 结果汇总

| 指标 | 值 |
|------|-----|
| **Accuracy** | **48.60% (243/500)** |
| Stderr | ±2.24% |
| Mode | greedy (temperature=0) |
| EOS rate | 16.2% (81 natural / 419 truncated) |
| Avg response length | 1766.5 tokens (max 2048) |
| 运行时长 | ~11h36m (2026-05-22 23:10 → 05-23 10:47) |
| 状态 | **已完成**，结果已保存 |
| westb:1 GPU | **空闲** (0 MiB, 0% utilization) |

**关键观察**：83.8% 的样本被截断（hit max 2048 tokens），说明 GRPO 模型生成过于冗长——很多正确答案在 response 中出现了但因为模型继续重复生成（如反复输出 `#### 30`）而导致 answer extraction 失败。这是 EOS 控制不足的表现，压低了实际 accuracy。

---
