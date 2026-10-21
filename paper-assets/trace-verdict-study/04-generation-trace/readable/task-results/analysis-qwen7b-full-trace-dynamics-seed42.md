# analysis qwen7b full trace dynamics seed42

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen7b_full_trace_dynamics_seed42_20260519T063917_result.json`
- **Structured JSON:** [`33727b2bd04b72288924.json`](../../sessions/33/33727b2bd04b72288924.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。

## 结论：**SUCCESS** (hypothesis 强确认)

### 关键数据

| 指标 | full_trace | exception_only | 差距 |
|------|-----------|----------------|------|
| Step 50 accuracy | **87.39%** | 99.33% | -11.94 pp |
| Best accuracy | **88.82%** (step 350) | 99.83% (step 150) | -11.01 pp |
| Final accuracy | **88.24%** | 99.83% | -11.59 pp |
| 收敛 step | 未收敛（持续震荡） | ~150 steps | N/A |

### 核心发现

1. **信号密度效应远超预期**：full_trace 不仅收敛慢，且 ceiling 比 exception_only 低 ~11 pp，即使训练完整 epoch 也无法弥合
2. **非单调震荡**：full_trace accuracy 在 step 100 骤降 5.3 pp、step 250-300 再跌 3.5 pp，说明模型在 pass/fail 判断策略间反复摇摆
3. **Train-eval gap**：train loss 降至 0.0085 但 eval accuracy 卡在 88%，过拟合 trace 中的 spurious pattern
4. **Fail 类困难**：Fail F1 始终比 Pass F1 低 15-19 pp，failure signal 被冗余 trace 信息淹没

报告已存入 `artifacts/qwen7b_full_trace_dynamics_seed42/report/full_trace_dynamics.md`，registry 已更新为 DONE(success)。

---
