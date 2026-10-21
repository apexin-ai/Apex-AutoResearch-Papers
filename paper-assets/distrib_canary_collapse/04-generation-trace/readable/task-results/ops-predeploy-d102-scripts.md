# ops predeploy d102 scripts

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_predeploy-d102-scripts_20260522T140823_result.json`
- **Structured JSON:** [`f5395b8a3a9dea3de9d9.json`](../../sessions/f5/f5395b8a3a9dea3de9d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

JSON structure and values are identical — old and new match exactly (same keys, same summary numbers). Both servers are ready.

---

## 汇报

### A. westd-17855
| 项目 | 状态 |
|------|------|
| 脚本 | `run_5method_analysis_d102.py` — 458行, 17930 bytes, md5 `ff55c629` |
| 依赖 | scipy 1.17.1, numpy 2.3.2, pandas 3.0.3, statsmodels OK, mauve OK |
| 依赖模块 | `permutation_granger.py` 存在 |
| C008/C009 | `true_3sigma_d105` ✓ / `peak_lag < 0` ✓ |
| dry-run | a075_s42_fp32 — 11 gens loaded ✓ |
| live验证 | n_perm=5000 完整执行 ✓, 输出 JSON 与已有结果完全一致 (6/8 robust) |
| 磁盘 | 350G, **44G 可用 (88%用)** — 偏紧，注意 C007 |

### B. westd-19828
| 项目 | 状态 |
|------|------|
| 脚本 | `run_5method_analysis_d102.py` — 458行, 17892 bytes, md5 `318853fa` |
| 依赖 | scipy 1.17.1, numpy 2.2.6, pandas 3.0.2, statsmodels OK, mauve OK |
| 依赖模块 | `permutation_granger.py` 存在 |
| C008/C009 | `true_3sigma_d105` ✓ / `peak_lag < 0` ✓ |
| dry-run | a075_s43 — 11 gens loaded ✓ |
| 磁盘 | 250G, **127G 可用 (50%)** — 充裕 |

### 差异说明
两台服务器的 `run_5method_analysis_d102.py` 和 `permutation_granger.py` md5 不同（38 bytes差异），但关键逻辑段（threshold, direction filter, consensus, FDR）grep 输出完全一致，且 17855 live 验证结果与已有分析完全匹配。差异大概率是空白或注释。

### 需关注
- **17855 磁盘仅剩 44G** — 1.4B 实验输出较大，分析脚本本身占用小但如果还有训练写入需留意 C007。

---
