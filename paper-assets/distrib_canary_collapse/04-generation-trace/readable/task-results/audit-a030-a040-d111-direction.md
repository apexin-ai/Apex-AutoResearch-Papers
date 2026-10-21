# audit a030 a040 d111 direction

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_a030_a040_d111_direction_20260519T225537_result.json`
- **Structured JSON:** [`d01dc61e21eb8864b8e8.json`](../../sessions/d0/d01dc61e21eb8864b8e8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

写入完成。`artifacts/d111_a030_a040_audit.md`

核心发现：

**α=0.30**: naive 8/8→**5/8**, diff 4/8→**3/8**, K≥3 6/8→**3/8**, K≥4 不变 3/8
**α=0.40**: naive 8/8→**4/8**, diff 3/8→**0/8**, K≥3 6/8→**1/8**, K≥4 1/8→**0/8**

两个 α 的 ece→* 4 对 naive_lag 全部 ≤0（反向），与 C4 audit 一致。α=0.40 的 diff 全部 peak_lag 为负，diff_fwd 归零，K≥3 从 6/8 塌到 1/8。

---
