# paper fix global config count and gemma

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_fix_global_config_count_and_gemma_20260522T042752_result.json`
- **Structured JSON:** [`a4b8af9a7b94724633e1.json`](../../sessions/a4/a4b8af9a7b94724633e1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

## 结果

### Gemma-2-2B 数据（从 JSON 提取）
| Pair | AUC | 95% CI | p |
|------|-----|--------|---|
| 0v1 | 0.953 | [0.949, 0.957] | <0.001 |
| 1v2 | 0.598 | [0.588, 0.608] | <0.001 |
| 2v3 | 0.534 | [0.523, 0.545] | <0.001 |
| 3v4 | 0.503 | [0.492, 0.514] | 0.292 |
| 4v5 | 0.503 | [0.492, 0.514] | 0.342 |

**K\*=1**（1v2 AUC=0.598 < θ=0.60）

### 修改清单
| 文件 | 修改 |
|------|------|
| **main.tex** (abstract) | 8→10 model configs, 5→6 architecture families, 6/8→6/10 |
| **main.tex** (limitations) | 6/8→6/10, 5→6 families, K\*=1 list +Gemma-2-2B +Pythia-6.9B |
| **introduction.tex** | 8→10, 5→6 families, 6/8→6/10 |
| **experiments_c1.tex** | nine→ten, five→six families, 6/9→6/10, model list +Gemma-2-2B, K\*=1 list +Gemma-2-2B |
| **discussion.tex** | 8→10 tested, 6/8→6/10, K\*=1 列表加 Pythia-6.9B + Gemma-2-2B |
| **conclusion.tex** | 6/8→6/10, 5→6 families |
| **appendix.tex** (Table S2b) | 新增 Gemma-2B 列（10 data columns），caption 6/9→6/10, K\*=1 list 更新 |
| **appendix_extended.tex** | 8→10 configs, 5→6 families |

### grep 验证
- 零处 "6/8" 或 "6/9" 残留
- 零处 "8 model" 或 "9 model" 残留
- 零处 "5 families" 残留
- Gemma-2-2B 出现在所有 K\*=1 列表中

### 编译
`latexmk -pdf main.tex` 成功，20 pages，无错误。

---
