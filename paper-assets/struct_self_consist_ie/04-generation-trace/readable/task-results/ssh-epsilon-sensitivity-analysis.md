# ssh epsilon sensitivity analysis

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_epsilon_sensitivity_analysis_20260522T002953_result.json`
- **Structured JSON:** [`70f28cc2d842ad81d0dd.json`](../../sessions/70/70f28cc2d842ad81d0dd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果如下：

---

### 核心表格：ε vs LP compression

| ε | compressed% | ρ(LP,F1) non-comp | ρ(LP,F1) all | MV F1 | LP-best F1 |
|---|---|---|---|---|---|
| 0.01 | 9.3% | 0.6824 | 0.6325 | 0.7587 | 0.7927 |
| 0.03 | 19.9% | 0.6945 | 0.6325 | 0.7587 | 0.7927 |
| **0.05** | **34.5%** | **0.7095** | **0.6325** | **0.7587** | **0.7927** |
| 0.10 | 60.2% | 0.7328 | 0.6325 | 0.7587 | 0.7927 |
| 0.15 | 75.9% | 0.7228 | 0.6325 | 0.7587 | 0.7927 |
| 0.20 | 92.5% | 0.7196 | 0.6325 | 0.7587 | 0.7927 |

### LP-best selection advantage by LP range bucket

| LP range bucket | n | MV F1 | LP F1 | LP-MV gap |
|---|---|---|---|---|
| [0.00, 0.01) | 3018 | 0.8180 | 0.8257 | +0.8pp |
| [0.01, 0.03) | 3457 | 0.8119 | 0.8271 | +1.5pp |
| [0.03, 0.05) | 4744 | 0.7862 | 0.8090 | +2.3pp |
| [0.05, 0.10) | 8374 | 0.7398 | 0.7827 | +4.3pp |
| [0.10, 0.20) | 10537 | 0.7006 | 0.7586 | +5.8pp |
| [0.20, inf) | 2435 | 0.7714 | 0.8072 | +3.6pp |

### 结论

**ε=0.05 是合理的 default。** 理由：

1. **Elbow point 位置**：fine-grained sweep 显示 delta% 在 ε≈0.035-0.055 区间最大（每步 +3.5~3.7%），之后 delta 逐步减小。ε=0.05 处于增长率开始放缓的拐点。
2. **coverage vs discrimination trade-off**：ε=0.05 标记 34.5% 为 compressed（约三分之一）。LP-best 在 compressed 区间（range<0.05）的优势仅 +0.8~2.3pp，而在 non-compressed 区间优势为 +4.3~5.8pp。这说明 ε=0.05 有效划分了 LP 信号有/无区分度的两类 instance。
3. **ρ on non-compressed 提升**：过滤掉 compressed 后 ρ 从 0.6325 升到 0.7095（ε=0.05），说明被过滤的确实是 LP 噪声实例。

### 产出文件

- 脚本：`/root/autodl-tmp/struct_self_consist_ie/code/epsilon_sensitivity.py`
- 结果文本：`/root/autodl-tmp/struct_self_consist_ie/output/epsilon_sensitivity_results.txt`
- 结果 JSON：`/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_mf4v2_seed42_v3/epsilon_sensitivity.json`

---
