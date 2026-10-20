# code gradient stopping audit

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gradient_stopping_audit_20260515T141005_result.json`
- **Structured JSON:** [`0de251244314c5b4d8c5.json`](../../sessions/0d/0de251244314c5b4d8c5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审查完成。核心发现：

**只需修复一条梯度路径** — WorldModel._train 中 `reward_loss → feat → deter → GRU → dt_emb.weight`。Imagination 路径因 `RequiresGrad(self.actor)` 天然安全，value training 因 `target.detach()` 天然安全。

**方案**: 在 `self._model_opt(mean_model_loss, ...)` 调用前，用 `torch.autograd.grad` 预计算 reward loss 对 dt_emb 的 scaled 梯度，注册 backward hook 在 optimizer backward 时减去该分量。约15行代码，config flag `reward_dt_emb_detach`。

**关键难点**: dt_emb 通过 GRU 不可逆融合到 `deter` 中（`networks.py:255-260`），无法在 `get_feat` 层面分离——这就是为什么需要 hook-based gradient subtraction 而非简单 detach。

详见 `artifacts/gradient_stopping_code_audit.md`。

---
