# paper fix table s2b kstar ci

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_fix_table_s2b_kstar_ci_20260522T035958_result.json`
- **Structured JSON:** [`adeb070fd2e8c15131b7.json`](../../sessions/ad/adeb070fd2e8c15131b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。汇总：

## 修复结果

### 1. Mistral-7B 列（新增）
从 `exp019_bootstrap_ci.json` 恢复数据，K*=1：
| Pair | AUC | 95% CI |
|------|-----|--------|
| 0v1 | .9842 | [.982, .986] |
| 1v2 | .5934 | [.584, .603] |
| 2v3 | .5402 | [.530, .551] |
| 3v4 | .5233 | [.513, .534] |
| 4v5 | .5180 | [.507, .529] |

### 2. LLaMA-8B 列（填充数据）
从 `exp018_bootstrap_ci.json` 恢复，K*=2：
| Pair | AUC | 95% CI |
|------|-----|--------|
| 0v1 | .9224 | [.917, .927] |
| 1v2 | .6123 | [.603, .622] |
| 2v3 | .5273 | [.517, .538] |
| 3v4 | .5168 | [.506, .528] |
| 4v5 | .5159 | [.505, .527] |

### 3. Qwen-14B
**不存在**。Git 历史（仅 2 个 commit）和实验数据中均无 Qwen-14B。没有 `qwen14` 相关的实验目录。如需此数据，需新建实验。

### 4. 计数统一
- appendix caption: 6/9 ← 已正确
- experiments_c1.tex: 8→9 configs, 6/8→6/9, K*=1 列表增加 Pythia-6.9B
- LLaMA-8B 行：移除 "pending bootstrap CI"，补充 CI [0.603, 0.622]

### 5. 编译
20 页，无新增 overfull（原 11→10，消除的即为本表格）。表格用 `\resizebox{\textwidth}{!}{...}` 自适应页宽。

---
