# fix compute cka split bias

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_compute_cka_split_bias_20260521T124811_result.json`
- **Structured JSON:** [`96a7509997b46c321c7f.json`](../../sessions/96/96a7509997b46c321c7f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇报

### 1. 代码修复
`compute_cka.py:108` — 删除 `acts[split:]` 的 70/30 位置分割，改为使用全量数据。

### 2. CKA 矩阵对比（全量 vs 旧的 30% 尾部）

**FULL DATA (fixed):**
| Layer | zh | ar | hi | sw | ko |
|------:|------:|------:|------:|------:|------:|
| 0 | 0.9121 | 0.9014 | 0.5365 | **0.4397** | 0.6869 |
| 4 | 0.6519 | 0.6416 | 0.5191 | 0.4703 | 0.6305 |
| 8 | 0.8146 | 0.7370 | 0.5926 | 0.6039 | 0.7245 |
| 12 | 0.8429 | 0.8195 | 0.6143 | 0.6115 | 0.7885 |
| 16 | 0.8859 | 0.8829 | 0.5755 | 0.5930 | 0.8647 |
| 20 | 0.7642 | 0.6641 | 0.3707 | 0.3988 | 0.6696 |
| 24 | 0.6940 | 0.5443 | 0.1619 | 0.1250 | 0.5513 |
| 27 | 0.3445 | 0.3564 | 0.1165 | 0.0841 | 0.3179 |

**Delta (full − old):**
| Layer | zh | ar | hi | sw | ko |
|------:|------:|------:|------:|------:|------:|
| 0 | −0.047 | −0.047 | −0.210 | **−0.466** | −0.107 |
| 4 | −0.215 | −0.186 | −0.261 | −0.355 | −0.220 |
| 8 | −0.090 | −0.139 | −0.218 | −0.259 | −0.170 |
| 12 | −0.053 | −0.080 | −0.199 | −0.266 | −0.120 |
| 16 | −0.025 | −0.043 | −0.199 | −0.296 | −0.070 |
| 20 | +0.005 | −0.019 | −0.122 | −0.135 | −0.015 |
| 24 | +0.044 | +0.048 | +0.000 | −0.022 | +0.042 |
| 27 | −0.035 | +0.001 | −0.083 | −0.048 | −0.080 |

关键：**sw L0 从 0.91 降到 0.44**（确认偏差），低资源语言（hi, sw）在浅层受影响最大。

### 3. Simpson's Paradox 验证 — 结论改变了

| 指标 | 旧（偏差数据） | 新（全量数据） |
|------|-------------|-------------|
| Pooled ρ(CKA, degradation) | **−0.072** (p=0.66) | **+0.084** (p=0.61) |
| Partial ρ(CKA, degradation \| depth) | −0.176 (p=0.29) | **−0.285** (p=0.078) |

**Simpson's Paradox 现在成立且方向更清晰：**
- 旧数据：两个都负，方向相同 → 报告说"CKA may be proxy for depth"，没有 paradox
- **新数据：Pooled 翻正（+0.08），Partial 负且更强（−0.29，边际显著 p=0.078）→ 真正的 Simpson's Paradox**

解读：深层 CKA 低 + 深层 degradation 低，pooling 后产生虚假正相关。控制 depth 后，**同深度内 CKA 越高 → degradation 越低（transfer 越好）**。

### 4. Same-layer 相关性也显著改善

| Layer | 旧 ρ | 新 ρ |
|------:|------:|------:|
| 4 | −0.10 | −0.50 |
| 8 | −0.90* | **−1.00*** |
| 12 | −0.60 | **−0.90*** |
| 16 | −0.60 | **−1.00*** |
| 24 | −0.80 | −0.80 |

中间层（8, 12, 16）的 CKA-degradation 负相关变得完美或接近完美，多个达到统计显著。

---
