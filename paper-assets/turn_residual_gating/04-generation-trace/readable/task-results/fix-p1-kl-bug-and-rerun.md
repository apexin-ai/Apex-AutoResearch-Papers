# fix p1 kl bug and rerun

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_p1_kl_bug_and_rerun_20260524T063026_result.json`
- **Structured JSON:** [`9c67dcd44b50b586bd19.json`](../../sessions/9c/9c67dcd44b50b586bd19.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

运行中。模型已加载，GPU 87% 利用率 / 38GB VRAM。

修复总结：
- **Bug**: `register_gating_hooks()` 返回 `(hooks, turn_features_ref, gate_values)` 3 个值，但 line 56 只解包 2 个 → `ValueError: too many values to unpack`
- **Fix**: 改为 `hooks, turn_features_ref, gate_values_ref = register_gating_hooks(...)` 并删除后面的 `turn_features_ref = [None]`（该行会破坏 hook 内部对 `turn_features_ref` 的引用）
- **Status**: PID 152928，Step 1 (Base model) 正在执行，GPU 正常工作

---
