# ssh shuffled tokens control

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_shuffled-tokens-control_20260515T191032_result.json`
- **Structured JSON:** [`43c22d6ab3e46caf1efc.json`](../../sessions/43/43c22d6ab3e46caf1efc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成，结果如下：

**核心数据**
| 条件 | Accuracy |
|------|----------|
| Original（正常 instruction） | **100%**（10/10 task 全对） |
| Shuffled（5次平均） | **20.6% ± 7.1%**（chance = 10%） |
| 单次 shuffle | 17%, 20%, 34%, 13%, 19% |

**Per-task 分析揭示了关键模式**：

- `open_the_top_drawer_and_put_the_bowl_inside`：shuffle 后仍有 ~86% accuracy — 因为 "top", "drawer", "inside" 是 unique tokens，即使打乱也能通过 bag-of-tokens 区分
- `turn_on_the_stove`：shuffle 后 ~70% — "turn", "on" 独有
- 所有 `put_the_bowl_on_the_X` 任务：shuffle 后 **0%** — 因为这些 task 的 token 集合高度重叠（都含 "put", "the", "bowl", "on", "the"），打乱后无法区分

**结论**：Token ORDER 是 untrained VLA 创造 separable representations 的**主要因素**（accuracy 从 100% 降至 ~20%），但**不同的 token set 提供了微弱残余信号**（~2× chance）。残余信号完全由 unique vocabulary 的 task 驱动，而 vocabulary 重叠的 task（put_the_bowl_on_{plate,stove,cabinet}）在 shuffle 后完全不可区分。

这意味着 untrained LLM 不只是充当 "high-dim random projector 让 probe overfit"——它确实在利用 token 的**序列结构**产生系统性不同的表征。结果保存在 `/root/autodl-tmp/vla-ssd/results/shuffled_token_control.json`。

---
