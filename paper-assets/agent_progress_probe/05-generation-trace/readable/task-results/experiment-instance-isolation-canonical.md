# experiment instance isolation canonical

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_instance-isolation-canonical_20260515T030609_result.json`
- **Structured JSON:** [`95f9b8ba0b0a14d490fd.json`](../../sessions/95/95f9b8ba0b0a14d490fd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

---

```
=== Canonical Instance Isolation ===

Table 2 验证: ALL MATCH ✓

Full set (与 Table 2 完全一致):
  GB all  (N=150,652): macro_f1=0.9674 ✓
  RF all  (N=150,652): macro_f1=0.9123 ✓
  GB conf≥2 (N=43,376): macro_f1=0.9919 ✓
  RF conf≥2 (N=43,376): macro_f1=0.9959 ✓

Unseen-only (去掉 284 overlap instances):
  GB all  (N=139,594): macro_f1=0.9669
  RF all  (N=139,594): macro_f1=0.9121
  GB conf≥2 (N=40,118): macro_f1=0.9917
  RF conf≥2 (N=40,118): macro_f1=0.9962

Delta (unseen - full):
  GB all:    -0.05pp
  RF all:    -0.01pp
  GB conf≥2: -0.02pp
  RF conf≥2: +0.03pp

Instance overlap: 284 (8.3% of OH, train-only)
```

**关键差异 vs 上次实验**: 上次用 trainval (13,577 windows, 1,683 instances, 356 overlap) 导致 full set 数字不匹配 Table 2。本次用 train split only (10,634 windows, 1,386 instances, 284 overlap) 精确复现了 Table 2，delta 全部 < 0.1pp。

**脚本**: `/root/autodl-tmp/agent_progress_probe/src/analysis/instance_isolation_canonical.py`  
**结果**: `/root/autodl-tmp/agent_progress_probe/artifacts/instance-isolation-canonical/results.json`

---
