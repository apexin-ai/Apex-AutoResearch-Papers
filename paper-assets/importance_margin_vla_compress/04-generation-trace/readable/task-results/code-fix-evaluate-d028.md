# code fix evaluate d028

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-evaluate-d028_20260516T030248_result.json`
- **Structured JSON:** [`396a0d7555060183ae15.json`](../../sessions/39/396a0d7555060183ae15.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个 Bug 全部修复验证通过。关键结果：

### Bug 1 验证：eps=0 pruneTrue vs pruneFalse action_loss 不同

| 条件 | action_loss |
|------|-------------|
| eps0.0_pruneFalse | **0.02777** |
| eps0.0_pruneTrue | **0.01076** |

值不同 ✓ — 之前 Bug 导致两者相同。

### Bug 2 验证：pruneTrue 使用 hard binary mask（model.eval()）

pruneTrue 的 action_loss 显著低于 pruneFalse，说明 hard mask 正确保留了重要 token，而非使用 soft sigmoid mask。

### Bug 3 验证：相同 batch 用于所有条件

所有 eps+pruning 组合的 preservation_rate 和 kendall_tau 在相同 eps 下趋势一致，说明各条件使用了相同的 batch 子集（预收集模式）。

### 修复总结

| Bug | 修复方法 | 标记 |
|-----|----------|------|
| Bug 1: eps=0 绕过 pruning | pruning=True 走 `model(eval_input)`（ACIS hard mask），pruning=False 走 `baseline_forward()`（无 ACIS） | D028 |
| Bug 2: eval 用 model.train() + soft mask | 全程 `model.eval()`，MarginAwareTokenSelector 自动走 `_hard_forward` | D028 |
| Bug 3: per-condition seed 污染 dataloader | 预收集所有 batch + 本地 Generator 生成确定性 noise/time | D028 |

---
