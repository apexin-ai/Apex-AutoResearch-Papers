# ssh per type f1 analysis v2

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_per-type-f1-analysis-v2_20260515T055130_result.json`
- **Structured JSON:** [`8dc01cdd9c6c67f4ec16.json`](../../sessions/8d/8dc01cdd9c6c67f4ec16.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

### Per-type BCS vs F1 分析（63 types, freq≥5）

**相关性（micro_F1）**
| 指标 | r/ρ | p |
|------|-----|---|
| Pearson r | **-0.1828** | 0.1516 |
| Spearman ρ | **-0.2927** | **0.0199** |
| Partial r (控制 log-freq) | **-0.1998** | 0.1163 |

**相关性（mean_F1）**
| 指标 | r/ρ | p |
|------|-----|---|
| Pearson r | -0.1374 | 0.2830 |
| Spearman ρ | -0.2412 | 0.0568 |
| Partial r (控制 log-freq) | -0.1428 | 0.2641 |

**Quartile 对比**
- Low BCS (≤0.798): avg F1 = **0.3098**, avg freq = 2134
- High BCS (≥0.827): avg F1 = **0.2275**, avg freq = 2049
- **Δ F1 = -0.0823**（高 BCS 组 F1 低 8.2 个百分点）

**混淆变量检查**
- r(BCS, log_freq) = 0.042, p=0.74 → BCS 和 frequency **几乎不相关**
- r(log_freq, F1) = 0.250, p=0.048 → frequency 和 F1 弱正相关

### 结论

**方向支持假设「高 BCS → 低 F1」**：
- Spearman ρ = -0.29 显著 (p=0.02)，per-type 分析确认负相关方向
- Quartile 对比显示高 BCS 类型 F1 比低 BCS 低 8.2 个百分点，且两组 frequency 几乎相同（2049 vs 2134），排除 frequency 混淆
- Partial correlation 控制 log-freq 后仍为负 (r=-0.20)，但 p=0.12 未达显著
- 关键发现：**BCS 和 frequency 在 type 级别几乎不相关** (r=0.04)，说明之前 batch-level 正相关确实是 frequency 混淆，type-level 分析消除了这个混淆后方向翻转为负

输出文件：`results/per_type_analysis.json` + `results/per_type_bcs_f1_scatter.png`

---
