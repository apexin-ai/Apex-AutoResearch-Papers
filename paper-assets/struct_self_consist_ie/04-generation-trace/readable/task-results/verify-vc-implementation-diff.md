# verify vc implementation diff

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_vc_implementation_diff_20260515T044547_result.json`
- **Structured JSON:** [`bce1980123f03d27680b.json`](../../sessions/bc/bce1980123f03d27680b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果完全确认。

## 结论

```
RE (n=397 full, n=238 cond):
  实现 A (majority threshold > N/2):  full ρ=+0.3311, cond ρ=+0.1386  ← 匹配 Worker 重算值
  实现 B (all items, no threshold):   full ρ=+0.3498, cond ρ=+0.2409  ← 匹配 Registry 值 (精确匹配)

  Registry 值:   full=0.3498, cond=0.2409
  Worker 重算值: full=0.3311, cond=0.1386

NER (n=529 full, n=477 cond):
  实现 A: full ρ=+0.2524, cond ρ=+0.1405
  实现 B: full ρ=+0.3792, cond ρ=+0.3000
  差异:   full Δ=0.1268, cond Δ=0.1595  ← NER 上差异同样显著
```

**根因确认**：
- **Registry 使用的是实现 B**（无 threshold，计算所有 items 的平均 voting rate）—— 这是服务器上 `analyze_exp012_rerun_5signal.py`、`analyze_exp015_unified.py` 等代码中的实际实现
- **Worker 重算使用了实现 A**（带 majority threshold `> N/2`），错误地只保留了出现超过半数的 items

NER 上两个实现差异也很大（Δ≈0.13-0.16），说明即使是 entity 也有大量非 majority items，并非"NER 差异小因为大部分 entity 都是 majority"的假设。

**论文中正确的实现是 B**（Registry 版本，无 threshold）。

---
