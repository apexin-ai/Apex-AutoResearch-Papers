# analysis fewnerd micro f1 construction

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_fewnerd-micro-f1-construction_20260524T085638_result.json`
- **Structured JSON:** [`7f2383070ca49191cf0c.json`](../../sessions/7f/7f2383070ca49191cf0c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**Construction 在 micro-F1 下全面为负，论文 construction claim 不成立。**

### 核心数据

| 数据集 | LP micro-F1 Δ | p-value | LP inst-avg Δ |
|--------|---------------|---------|---------------|
| FewNERD 3ep (2 seeds) | **-1.44±0.08pp** | 1.0000 | +0.36±0.48pp |
| FewNERD 5ep (2 seeds) | **-0.89±0.02pp** | 1.0000 | -0.12±0.10pp |
| SciERC (1 seed) | **-0.90pp** | 0.9469 | -0.55pp |

### 关键发现

1. **FewNERD 3-epoch**: micro-F1 下 LP Δ = -1.53pp (seed42), -1.36pp (seed456)，bootstrap p=1.0000，construction 显著差于 greedy
2. **FewNERD 5-epoch**: LP Δ = -0.91pp / -0.88pp，同样 p=1.0000
3. **SciERC**: LP Δ = -0.90pp，p=0.9469（CI 上界 +0.18pp 勉强过零）
4. **Theta sweep**: FewNERD 3ep 最优 θ=0.30 仍为 -0.92pp，**无法通过调 threshold 挽救**
5. **SciERC greedy micro-F1 = 66.51%**（论文报 66.33%），论文 "+0.32pp" 确认是用 instance-averaged F1 算的

### 根因

Instance-averaged F1 每个 instance 权重相等；micro-F1 按实体数加权。实体多的 instance 在 construction 中 recall 下降更严重（投票过滤掉了部分实体），导致 pooled TP 下降，micro-F1 变差。

结果已保存到服务器 `output/micro_f1_construction_verification.txt` 和本地 artifact。

---
