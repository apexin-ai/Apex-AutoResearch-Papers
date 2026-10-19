# ssh negative difficulty margin

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_negative_difficulty_margin_20260513T191124_result.json`
- **Structured JSON:** [`a602e0440eb5f1c8ce15.json`](../../sessions/a6/a602e0440eb5f1c8ce15.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果汇总：

## Margin 分析结果

| 策略 | Encoder | Pos Sim | Neg Sim | **Margin** | Margin Std | %Pos>Neg |
|------|---------|---------|---------|-----------|------------|----------|
| Random | Qwen | 0.980 | 0.899 | **0.082** | 0.230 | 77.8% |
| Random | StarCoder | 0.757 | 0.553 | **0.204** | 0.324 | 72.8% |
| Embedding | Qwen | 0.980 | 0.960 | **0.021** | 0.115 | 60.7% |
| Embedding | StarCoder | 0.784 | 0.668 | **0.116** | 0.256 | 59.2% |
| Dataflow | Qwen | 0.981 | 0.950 | **0.031** | 0.141 | 67.4% |
| Dataflow | StarCoder | 0.761 | 0.659 | **0.102** | 0.257 | 62.8% |

## 关键发现

**StarCoder margin 是 Qwen 的 2.5x-5.5x：**
- Random: 0.204 vs 0.082 (2.50x)
- Embedding: 0.116 vs 0.021 (5.54x)
- Dataflow: 0.102 vs 0.031 (3.30x)

**结论：支持 "StarCoder already knows" 假说。** StarCoder pretrained 模型天然有更强的正负样本分辨力（更大的 margin），训练的边际收益空间更小。Qwen 的 margin 极小（embedding/dataflow 仅 0.02-0.03），说明 Qwen pretrained 几乎无法区分正负样本，训练空间更大。

但也要注意：**%Pos>Neg 两个 encoder 接近**（59-78% vs 59-73%），说明虽然 StarCoder margin 绝对值大，但正确排序的比例并没有显著高于 Qwen。差距主要来自 StarCoder 在"能区分"的 pair 上 margin 更大。

**产出文件：**
- 统计：`/root/autodl-tmp/structfuse/artifacts/negative_difficulty_stats_v2.json`
- 图表：`/root/autodl-tmp/structfuse/artifacts/negative_difficulty_margin_{distribution,bars,violin}.{png,pdf}`
- 脚本：`/root/structfuse/analysis/negative_difficulty_margin.py`

---
