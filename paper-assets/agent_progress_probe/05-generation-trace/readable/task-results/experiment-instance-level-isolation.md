# experiment instance level isolation

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_instance-level-isolation_20260515T024202_result.json`
- **Structured JSON:** [`9960380061ec4ae2ec47.json`](../../sessions/99/9960380061ec4ae2ec47.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果汇总：

---

## Instance-Level Cross-Agent Isolation 结果

### Instance Overlap
| | Count |
|---|---|
| SWE-Agent training instances | 1,683 |
| OpenHands instances | 3,409 |
| **Overlap** | **356 (10.4% of OH)** |
| OH non-abstain windows in overlap | 13,805 |
| OH non-abstain windows unseen | 136,847 |
| OH conf≥2 windows in overlap | 4,044 |
| OH conf≥2 windows unseen | 39,332 |

### Cross-Agent Evaluation

| Setting | Subset | N | GB macro_f1 | RF macro_f1 |
|---------|--------|-------|-------------|-------------|
| Full | all | 150,652 | 0.9035 | 0.9657 |
| Unseen-only | all | 136,847 | 0.9035 | 0.9651 |
| Full | conf≥2 | 43,376 | 0.9974 | 0.9984 |
| Unseen-only | conf≥2 | 39,332 | 0.9977 | 0.9987 |

### Delta (unseen - full)

| Subset | GB | RF |
|--------|------|------|
| all | **+0.01pp** | **-0.06pp** |
| conf≥2 | **+0.03pp** | **+0.03pp** |

### 结论

Instance overlap 确实存在（356 instances, 10.4%），但**完全不影响 cross-agent F1**。所有 delta 均 <0.1pp，且方向不一致（有正有负），说明 overlap instances 上的性能与 unseen instances 无统计差异。这直接反驳了 dream review 关于 instance-level 数据泄露的质疑。

脚本：`/root/autodl-tmp/agent_progress_probe/src/analysis/instance_level_isolation.py`
结果：`/root/autodl-tmp/agent_progress_probe/artifacts/instance-isolation/results.json`

---
