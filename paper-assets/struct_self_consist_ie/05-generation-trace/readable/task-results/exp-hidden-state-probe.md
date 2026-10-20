# exp hidden state probe

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_hidden_state_probe_20260518T103419_result.json`
- **Structured JSON:** [`9c7e2fe98174605dc928.json`](../../sessions/9c/9c7e2fe98174605dc928.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总结果：

```
===========================================================================
Method              Dim    Spearman ρ    Selection F1    Gap Closure
---------------------------------------------------------------------------
LP (mean pool)        1      0.2207        0.6087          -0.4%
DeBERTa             768      0.3290        0.6114         -26.5%
Hidden Linear      4096      0.2346        0.6206           7.0%
Hidden MLP         4096      0.4611        0.6317          13.9%
Oracle                —           —        0.7692         100.0%
===========================================================================
```

**核心发现**:

1. **Hidden states 包含比 LP 更多的 quality-relevant 信息** — MLP probe ρ=0.461 远超 LP ρ=0.221 (2x+)，支持 hypothesis
2. **Linear probe (ρ=0.235) 仅略好于 LP** — 说明 quality-relevant 信息在 hidden space 中以非线性方式编码
3. **MLP probe gap closure = 13.9%** — 首次在 selection F1 上实现正向 gap closure（LP=-0.4%, DeBERTa=-26.5% 均为负）
4. **信息存在但 LP 无法捕获** — LP 将 4096-dim 压缩为 1-dim scalar，丢失大量 quality 信号

输出文件:
- `hidden_states.pt` (69MB, [4408, 4096])
- `labels.pt`, `logprobs.pt`
- `results.json` (含 per-seed breakdown)
- `metadata.json` (含每个 sample 的详细 meta)

---
