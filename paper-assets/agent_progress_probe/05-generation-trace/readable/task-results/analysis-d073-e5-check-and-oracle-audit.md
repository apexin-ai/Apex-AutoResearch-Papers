# analysis d073 e5 check and oracle audit

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d073-e5-check-and-oracle-audit_20260516T041035_result.json`
- **Structured JSON:** [`4bddb13f03c1bbc2a0e7.json`](../../sessions/4b/4bddb13f03c1bbc2a0e7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Diagnostic is conclusive. Now the full picture:

## E5-large Probe Status
**进行中** — Step 1 (OH embedding) at 96%, ETA ~6 min for embedding to finish, then cross-agent eval still needs to run.

- 进程: PID 436734, `d073_e5_cross_agent.py`
- 进度: 144,000 / 150,652 windows embedded (~96%)
- 速度: ~18.3 it/s, embedding剩余约6分钟
- GPU: RTX 5090, 94% utilization, 2.4 GB / 32.6 GB VRAM
- Embedding后还需训练probe + cross-agent eval，预计总完成还需15-30分钟

关键数字暂无——脚本尚未进入eval阶段。

---

## Oracle Bug Audit
**无 bug。** 两个 oracle 产出 identical 数字是数学上的必然，不是变量泄漏。

**诊断结果：**
- 2-gram (t=0.70) 和 3-gram (t=0.0) 的二分类预测在全部 150,652 个 window 上 **100% 一致**（0 个差异）
- 两者都把同一组 37,051 个 window 判为 stagnating

**根因：** 动作词表太小（~8类：edit/search/nav/submit/python/test/other/empty），导致 3-gram repeat ratio 的分布是**二元退化**的——要么 0（无重复），要么 >0.50（大量重复），中间区间是空的：

```
3-gram threshold sweep:
  t=0.00 → 0.50: 全部 macro_f1=0.5517, n_stag=37051（完全相同）
  t=0.70:         macro_f1=0.5295, n_stag=11868（断崖下降）

2-gram threshold sweep:
  t=0.70: macro_f1=0.5517, n_stag=37051 ← 与3-gram完全重合
```

数学上：在这个粗粒度词表下，`3gram_ratio > 0` ⟺ `2gram_ratio > 0.70`。一个序列只要有任何重复 3-gram，其 2-gram 重复率必然 >70%（因为重复 3-gram 隐含大量重复 2-gram）；反之亦然。

**结论：** oracle 数字无需修正。可以在论文中只报告一行 "n-gram oracle" 并加脚注说明两者退化等价，或只报 2-gram oracle（更直观，threshold 有实际物理意义）。

---
