# check stage1 only result

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_stage1_only_result_20260517T060908_result.json`
- **Structured JSON:** [`222e52e3a75efd7387a8.json`](../../sessions/22/222e52e3a75efd7387a8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 全部更新完毕。

## 结果汇总

| Experiment | Mode | Overall SR | 含义 |
|---|---|---|---|
| **Stage1-only** (expert未动 + ACIS prune k=0.5) | acis_prune | **44.8%** | ACIS importance ranking 非常有效 |
| IMM 100K bypass (Stage2后 不剪枝) | baseline | **0.0%** | Stage2 彻底摧毁 expert |
| IMM k=0.7 bypass (Stage2后 不剪枝) | baseline | **0.0%** | k=0.7 同样彻底摧毁 expert |

### Stage1-only per-task SR
| Task | SR |
|---|---|
| alphabet soup | 22% |
| cream cheese | 60% |
| salad dressing | 42% |
| bbq sauce | 38% |
| ketchup | 58% |
| tomato sauce | 26% |
| butter | 62% |
| milk | 38% |
| chocolate pudding | 50% |
| orange juice | 52% |

### 关键结论

**Stage1 ACIS 完美有效**：用原始 Full FT expert + Stage1 训的 ACIS 做 50% token pruning，SR = 44.8%，与 Full FT baseline (~44-49%) 基本持平。ACIS 成功学会了 token importance ranking，丢弃 50% tokens 不损失性能。

**Stage2 是唯一的问题**：两个 bypass eval 都是 0% SR（所有 task 全部 timeout），无论 k=0.5 还是 k=0.7，Stage2 expert 训练都会彻底摧毁模型权重。问题不在 pruning ratio 而在 Stage2 训练机制本身。

GPU 状态：2x RTX PRO 6000 Blackwell 空闲（0% util），可随时启动新实验。

---
