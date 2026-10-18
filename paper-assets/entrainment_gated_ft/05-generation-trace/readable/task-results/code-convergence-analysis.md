# code convergence analysis

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_convergence_analysis_20260518T205617_result.json`
- **Structured JSON:** [`2b641ddd5267b416db83.json`](../../sessions/2b/2b641ddd5267b416db83.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。完整结果如下：

---

## 数据概览

三个架构 (GDN, RetNet, HGRN2) × 五个 attention 层数 (0, 1, 2, 4, 8)，共 15 个模型。

## 各 Benchmark 跨架构 std 和 range

### LAMBADA acc
| attn | GDN | HGRN2 | RetNet | std | range |
|------|------|-------|--------|------|-------|
| 0 | 0.5430 | 0.4842 | 0.5166 | 0.0240 | 0.0588 |
| 1 | 0.5397 | 0.5003 | 0.5152 | 0.0162 | 0.0394 |
| 2 | 0.5337 | 0.5030 | 0.5071 | 0.0136 | 0.0307 |
| 4 | 0.5110 | 0.5088 | 0.4972 | 0.0061 | 0.0138 |
| 8 | 0.5135 | 0.5139 | 0.5032 | 0.0049 | 0.0107 |

### HellaSwag acc_norm
| attn | GDN | HGRN2 | RetNet | std | range |
|------|------|-------|--------|------|-------|
| 0 | 0.6080 | 0.5983 | 0.5799 | 0.0117 | 0.0282 |
| 1 | 0.5970 | 0.6026 | 0.5822 | 0.0086 | 0.0204 |
| 2 | 0.6103 | 0.6054 | 0.5882 | 0.0095 | 0.0221 |
| 4 | 0.6047 | 0.6049 | 0.5852 | 0.0092 | 0.0196 |
| 8 | 0.6031 | 0.6027 | 0.5778 | 0.0118 | 0.0253 |

### Winogrande acc
| attn | GDN | HGRN2 | RetNet | std | range |
|------|------|-------|--------|------|-------|
| 0 | 0.6077 | 0.5919 | 0.6038 | 0.0067 | 0.0158 |
| 1 | 0.6283 | 0.6093 | 0.5770 | 0.0212 | 0.0513 |
| 2 | 0.6117 | 0.6054 | 0.5888 | 0.0097 | 0.0229 |
| 4 | 0.5927 | 0.5983 | 0.6109 | 0.0076 | 0.0182 |
| 8 | 0.6062 | 0.6077 | 0.5904 | 0.0078 | 0.0174 |

### ARC-Easy acc_norm
| attn | GDN | HGRN2 | RetNet | std | range |
|------|------|-------|--------|------|-------|
| 0 | 0.6418 | 0.6654 | 0.6477 | 0.0100 | 0.0236 |
| 1 | 0.6305 | 0.6763 | 0.6423 | 0.0195 | 0.0459 |
| 2 | 0.6292 | 0.6696 | 0.6557 | 0.0168 | 0.0404 |
| 4 | 0.6578 | 0.6671 | 0.6570 | 0.0046 | 0.0101 |
| 8 | 0.6486 | 0.6460 | 0.6456 | 0.0013 | 0.0029 |

### ARC-Challenge acc_norm
| attn | GDN | HGRN2 | RetNet | std | range |
|------|------|-------|--------|------|-------|
| 0 | 0.3925 | 0.4002 | 0.3771 | 0.0096 | 0.0230 |
| 1 | 0.3942 | 0.4019 | 0.3831 | 0.0077 | 0.0188 |
| 2 | 0.3857 | 0.4044 | 0.3959 | 0.0077 | 0.0188 |
| 4 | 0.3882 | 0.4053 | 0.3746 | 0.0126 | 0.0307 |
| 8 | 0.4044 | 0.3874 | 0.3720 | 0.0132 | 0.0324 |

### MMLU acc
| attn | GDN | HGRN2 | RetNet | std | range |
|------|------|-------|--------|------|-------|
| 0 | 0.2606 | 0.2387 | 0.2452 | 0.0092 | 0.0219 |
| 1 | 0.2441 | 0.2337 | 0.2322 | 0.0053 | 0.0118 |
| 2 | 0.2541 | 0.2344 | 0.2389 | 0.0084 | 0.0197 |
| 4 | 0.2573 | 0.2403 | 0.2517 | 0.0071 | 0.0170 |
| 8 | 0.2431 | 0.2416 | 0.2508 | 0.0040 | 0.0093 |

## Spearman 相关性检验 (attn_layers vs cross-arch std)

| Benchmark | rho | p-value | 趋势 | 显著性 |
|-----------|------|---------|------|--------|
| LAMBADA acc | **-1.000** | **0.000** | **CONVERGING** | **significant** |
| HellaSwag acc_norm | 0.300 | 0.624 | DIVERGING | not significant |
| Winogrande acc | 0.100 | 0.873 | DIVERGING | not significant |
| ARC-Easy acc_norm | -0.700 | 0.188 | CONVERGING | not significant |
| ARC-Challenge acc_norm | 0.600 | 0.285 | DIVERGING | not significant |
| MMLU acc | -0.700 | 0.188 | CONVERGING | not significant |

## 结论

**Equalizer 效应部分成立，但不是普遍现象：**

1. **LAMBADA：完美趋同**（rho=-1.0, p<0.001）。跨架构 std 从 0.024 (pure) 单调下降到 0.005 (h3-1)，range 从 0.059 降到 0.011。这是最强的 equalizer 证据。

2. **ARC-Easy 和 MMLU：趋同趋势明显但未达统计显著**（rho=-0.7, p≈0.19）。ARC-Easy 的 range 从 0.024 降到 0.003，收敛幅度很大。

3. **HellaSwag、Winogrande、ARC-Challenge：无趋同**。这三个 benchmark 的跨架构差异在不同 attention 层数下波动，没有系统性下降。HellaSwag 和 ARC-Challenge 在 h3-1 (attn=8) 时 std 反而最高。

4. **核心模式**：RetNet 在多数 benchmark 上始终弱于 GDN 和 HGRN2，这个差距在 HellaSwag 等 benchmark 上并未随 attention 增加而缩小，说明 attention 层无法完全抹平架构间的固有差异。

**总结**：Reviewer 观察到的 h3 趋同效应在 recall-heavy 任务（LAMBADA）和知识检索任务（ARC-Easy, MMLU）上成立，但在需要更复杂推理的任务（HellaSwag, ARC-Challenge, Winogrande）上不成立。Equalizer 效应是 task-dependent 的。

---
