# infra gpu health check

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_gpu-health-check_20260516T002520_result.json`
- **Structured JSON:** [`2799f2cd7bcc7af92d2f.json`](../../sessions/27/2799f2cd7bcc7af92d2f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇总如下：

## GPU 状态 (08:26 UTC)

| GPU | 状态 | 显存 | 利用率 |
|-----|------|------|--------|
| cuda:0 | **空闲** | 0 / 98GB | 0% |
| cuda:1 | **空闲** | 0 / 98GB | 0% |
| cuda:2 | 忙 | 15.5 / 98GB | 72% |
| cuda:3 | **空闲** | 0 / 98GB | 0% |

## 实验进度

| 实验 | 状态 | 进度 | 准确率 | 预估剩余 |
|------|------|------|--------|----------|
| acc_ds_s015_8k_v2 | **已完成** ✓ | 50/50 | **48.0%** (24/50) | — |
| acc_ds_s030_8k_v2 | 运行中 | 26/50 | 8.0% (2/25) | ~71 min |

## 关键发现

- **s015 结果**：48% accuracy，比 v1 暗示的 ~36% 好很多，说明 max_new_tokens=8192 给了模型足够的思考空间
- **s030 情况堪忧**：几乎所有 problem 都 timeout（pred=None，每个耗时 ~177s），running accuracy 仅 8%。s030 剪枝过于激进，模型基本丧失推理能力
- **3 张 GPU 空闲**（cuda:0, 1, 3），可立即用于新实验

---
