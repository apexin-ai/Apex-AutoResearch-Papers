# code sta bugfix p1

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_sta-bugfix-p1_20260513T175253_result.json`
- **Structured JSON:** [`3d2e4129ee29bdc6cccf.json`](../../sessions/3d/3d2e4129ee29bdc6cccf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部通过。

**Bug #3 修复**：
- `ablate_component()` 新增 `original_result: Optional[SolverResult] = None` 参数，None 时自行计算（保持独立可调用性）
- `run_sta()` 同样新增该参数，内部只证明一次原始问题，传给所有 `ablate_component()` 调用
- `sta_reward()` 也顺带优化——把已算好的 `proof_result` 传给 `run_sta()`，消除额外冗余调用

**Optimization #4**：
- `fast_isr_fol()` 在 `isr.py` 中实现，仅 2 次 solver 调用（原始证明 + tautology 检查）
- `fast_sta_reward()` 在 `reward.py` 中实现，内部调用 `fast_isr_fol()`

功能测试：`fast_isr_fol(['all x (P(x) -> Q(x))', 'P(a)'], 'Q(a)', solver)` 返回 `fast_isr=1.0`（前提必要，非 tautology），耗时 4ms。

---
