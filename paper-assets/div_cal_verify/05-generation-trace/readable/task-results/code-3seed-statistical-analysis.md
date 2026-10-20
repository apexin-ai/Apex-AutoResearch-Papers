# code 3seed statistical analysis

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_3seed_statistical_analysis_20260513T193108_result.json`
- **Structured JSON:** [`856310c3d91b13e30639.json`](../../sessions/85/856310c3d91b13e30639.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**脚本**: `/root/div_cal_verify/run_3seed_stats.py`（服务器）、`artifacts/code/run_3seed_stats.py`（本地）

**运行**: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 /root/div_cal_verify/run_3seed_stats.py`

**当前结果**:
| 方法 | seeds | gen7 PPL | gen7 rare | gen7 RankMe |
|------|-------|----------|-----------|-------------|
| uncurated | 3 ✓ | 47.04±2.90 | 0.009±0.000 | 289.83±1.77 |
| random_50 | 3 ✓ | 43.18±1.42 | 0.010±0.000 | 290.99±0.98 |
| external_only | 2 | 47.59±2.93 | 0.010±0.000 | 290.82±0.01 |
| rgds | 2 | 78.32±4.59 | 0.006±0.001 | 295.54±3.98 |

**t-test**: 3对比较均输出 PARTIAL（rgds 和 external_only 各缺 seed=456），记录了2-seed均值差。seed=456 完成后重跑即可得到完整 p-value 和 Cohen's d。

---
