# analysis bootstrap voting conf fix

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bootstrap_voting_conf_fix_20260514T215616_result.json`
- **Structured JSON:** [`8fa1b3198409101d82fc.json`](../../sessions/8f/8fa1b3198409101d82fc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有文件已生成。最终汇总：

---

**更新的文件：**

| 文件 | 位置 |
|------|------|
| `bootstrap_ci_nscaling/results.json` | 服务器 `output/` + 本地通过 summary 引用 |
| `bootstrap_ci_summary.json` | 服务器 `output/` + 本地 `artifacts/` |
| `bootstrap_ci_tables.tex` | 服务器 `output/` + 本地 `artifacts/` |

**voting_conf ρ 验证结果（全部 ±0.01 内匹配）：**

| 设置 | 新 ρ | 参考值 | 差值 |
|------|------|--------|------|
| Qwen CoNLL | 0.4286 | 0.429 | -0.0004 |
| LLaMA CoNLL | 0.4554 | 0.455 | +0.0004 |
| LLaMA SciERC | 0.4515 | 0.452 | -0.0005 |
| Qwen SciERC | 0.4408 | 0.441 | -0.0002 |

**额外修复：**
- Qwen SciERC 3-seed 的 EM 和 voting_conf 已从 `all_signals_report.json` 补入 summary（之前标记为 missing）
- EM full mean = 0.329, voting_conf full mean = 0.422

---
