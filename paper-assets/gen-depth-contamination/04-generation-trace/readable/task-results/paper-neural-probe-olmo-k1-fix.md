# paper neural probe olmo k1 fix

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_neural_probe_olmo_k1_fix_20260521T170108_result.json`
- **Structured JSON:** [`abb55f061e4c4c31deff.json`](../../sessions/ab/abb55f061e4c4c31deff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

5 处修改完成，编译通过（20 页无报错）：

| 文件 | 行 | 修改 |
|------|-----|------|
| `experiments_c1.tex:96` | 正文 | Pythia K*=2 / OLMo K*=1 分开描述，补 1v2 AUC=0.5054 |
| `experiments_c1.tex:110` | 表格行 | K* 2→1，加脚注说明 1v2 AUC |
| `discussion.tex:20` | 表征依赖段 | 拆分 Pythia/OLMo，OLMo K*=1 |
| `appendix_extended.tex:52` | 扩展讨论 | 同上，补 1v2 AUC 数值 |
| `main.tex:72` | Limitations | "$2$ for Pythia, $1$ for OLMo" |

产出清单写入 `artifacts/neural_probe_olmo_k1_fix.md`。

---
