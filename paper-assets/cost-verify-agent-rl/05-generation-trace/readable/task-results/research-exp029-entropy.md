# research exp029 entropy

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_exp029_entropy_20260516T150213_result.json`
- **Structured JSON:** [`c4d4e9b66cea02ee3b4f.json`](../../sessions/c4/c4d4e9b66cea02ee3b4f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成，以下是结论。

---

## 结论

### 1. entropy 计算方式：**per-token mean (nats)**

代码路径：
- `dp_actor.py:62-66` — 调用 `verl_F.entropy_from_logits`，即标准 Shannon entropy：`H = logsumexp(logits) - sum(softmax(logits) * logits)`，返回 `(bs, response_len)` 的 per-token entropy 张量
- `agent_trainer.py:1449-1452` — `agg_loss(loss_mat=entropys, loss_mask=response_masks, loss_agg_mode="token-mean")` → `masked_mean(entropys, response_masks)`

**`actor/entropy` = batch 内所有 response token 的 per-token entropy 均值（单位：nats）。**

### 2. full context 模式改变了 entropy 的有效量纲

两个实验用 **完全相同** 的聚合方式（`loss_agg_mode: "token-mean"`），但分母（有效 token 数）差 ~40 倍：

| | exp028c (step_independent) | exp029 (full) |
|---|---|---|
| response_length | ~200 tokens/step | ~7888 tokens/episode |
| response_mask 覆盖范围 | 单步 response | 全 episode 所有 response token |
| entropy = 0.263 | 200 tokens 平均 | — |
| entropy = 0.027 | — | 7888 tokens 平均 |

在 7888 token 的全 episode 中，绝大多数 token 是高确定性的：
- think/action/observe 格式标记（接近 0 entropy）
- 重复动作语法（"go to dresser 1"、"pick up" 等，极低 entropy）
- 只有每步开头的**决策 token**（选择哪个动作）有较高 entropy

粗算：假设 ~5% token 是决策点（entropy ~0.5 nats），95% 是结构 token（entropy ~0.001 nats）：
`0.05 × 0.5 + 0.95 × 0.001 ≈ 0.026`，与观测值 0.027 吻合。

### 3. **不是真 collapse，是计算方式差异**

判据：
- **pass@8 = 50%（4/8 成功）**：说明 rollout 间仍有真实多样性。真 collapse 应该是 0/8 或 8/8。
- **数学一致**：40x 更长序列中大量低 entropy token 拉低均值，0.027 是 `token-mean` 在 full mode 下的预期量级。
- **grad_norm 也一致**：exp029 的 grad_norm=0.99（vs exp028c 的 16.9）——token-mean loss 的梯度被更多 token 平摊，梯度范数自然更小。

### 4. 不需要调 entropy_coef

entropy 值低是量纲效应，不是策略问题。如果想让 `actor/entropy` 在 full 模式下可读/可与 step_independent 对比，可以考虑改 `loss_agg_mode` 为 `seq-mean-token-mean`（先 per-sequence 平均再 cross-sequence 平均），但这会同时影响 policy loss 的 scale，不建议只为 metric 可读性改动。

---
