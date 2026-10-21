# search pi05 baseline results

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_search_pi05_baseline_results_20260524T235224_result.json`
- **Structured JSON:** [`88c1e7bb9eba8a5cd62f.json`](../../sessions/88/88c1e7bb9eba8a5cd62f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。汇总如下：

## π0.5 Baseline (k=1.0, no pruning) 全 4 Suite 结果

| Suite | SR | 来源文件 | 服务器 | Registry 更新 |
|-------|------|---------|--------|--------------|
| Object | **98.2%** (491/500) | `eval_results/pi05_baseline_libero_object.json` | westd-41074 | metrics 已补录 |
| Spatial | **97.2%** (486/500) | `eval_results/pi05_baseline_libero_spatial_seed42.json` | westd-38929 | 已有 metrics ✓ |
| Goal | **96.4%** (482/500) | `eval_results/pi05_baseline_libero_goal_seed42.json` | westd-38929 | 已有 metrics ✓ |
| Long | **92.8%** (464/500) | `eval_results/pi05_baseline_libero_10_seed42.json` | westd-38929 | metrics 已补录，conclusion 从 negative→success |

## Goal 88.4% 不一致分析

**结论：88.4% 是错误引用，正确 Goal baseline = 96.4%。**

- Registry 中 `eval_pi05_baseline_goal_seed42` 正确记录 overall_sr=0.964
- 实际结果文件 (westd-38929, 2026-05-22) 确认 96.4%
- seed43 重复实验 (cqa1-33015) 也是 96.4%，高度一致
- **88.4% 无对应结果文件**——搜遍 4 台服务器未找到任何 π0.5 Goal baseline = 88.4% 的 JSON
- 88.4% 最可能来源：分析中将 **pre-fix L2norm k=0.95 Goal 结果**误标为 "baseline"。Post-fix L2norm k=0.95 Goal = 90.8%，pre-fix 可能略低于此
- No-pruning baseline 不受 CPU RNG 修复影响（无随机性），所以 96.4% 在 pre/post-fix 下一致
- D203 "L2norm k=0.95 Goal = 90.8%，超 baseline (88.4%) +2.4pp" **应修正为**：vs 实际 baseline 96.4%，即 L2norm k=0.95 **低于** baseline -5.6pp

---
