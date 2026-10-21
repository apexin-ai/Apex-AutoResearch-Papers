# diag exp016 status check

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_exp016-status-check_20260519T014647_result.json`
- **Structured JSON:** [`0c595ad45814511692f7.json`](../../sessions/0c/0c595ad45814511692f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-016 结果

**状态**: 已完成（06:46 ~ 09:45，约 3 小时）

**GPU 3**: 空闲（0% utilization, 4 MiB memory）

### 评估结果

| Alpha | NoF | WRR | n_valid | n_invalid |
|-------|-----|-----|---------|-----------|
| 0.0 | 0.696 | 0.271 | 181 | 181 |
| 0.5 | 0.696 | 0.271 | 181 | 181 |
| 1.0 | 0.696 | 0.271 | 181 | 181 |
| 2.0 | 0.696 | 0.271 | 181 | 181 |
| 5.0 | 0.696 | 0.271 | 181 | 181 |

### 关键问题

**所有 alpha 的结果完全相同**，包括 alpha=0.0（无 steering）和 alpha=5.0（强 steering）。这强烈说明 steering hooks 没有实际生效。可能原因：

1. **Hook 未正确注入到 forward pass** — 注册了但没被调用，或被 model 的 generation pipeline 绕过
2. **Direction 被加在了错误的位置** — 比如加在 attention output 而非 residual stream
3. **Generation 用了 cache** — 如果用了 KV cache，hook 只在第一个 token 的 prefill 阶段起作用，后续 decode 步骤不经过被 hook 的层
4. **Direction 向量量级太小** — 相对于 activation norm 可忽略（但 alpha=5 也没变化，排除此项）

需要检查 `run_exp016_actadd_steering.py` 中 hook 的实现逻辑。

---
