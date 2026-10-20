# urgent critical data fix

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_critical_data_fix_20260514T092259_result.json`
- **Structured JSON:** [`d5b89a63b8470f706404.json`](../../sessions/d5/d5b89a63b8470f706404.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部修正完成，无遗漏。汇总如下：

---

## 修正前后对比

### CRITICAL 1: Random 显著性计数
| 位置 | 旧值 | 新值 |
|------|------|------|
| abstract.tex L8 | `0/8 conditions significant` | `7/8 conditions not significant; single exception (Qwen s=0.30, p=0.012) negligible d=-0.04` |
| conclusion.tex L8 | `0/8 conditions significant` | 同上等价表述 |
| introduction.tex L16 | `all four sparsity levels fail` | `7/8 conditions...fail; single exception` |
| discussion.tex L21 | `8/8 FAIL` | `7/8 FAIL; single exception...negligible` |
| discussion.tex L88-90 | re-bootstrap reversed to FAIL p=0.111（与数据矛盾） | 改为正确描述 p=0.012 PASS but d=-0.04 negligible |

### CRITICAL 2: Crossover 数值 (s=0.25)
| 位置 | 旧值 | 新值 |
|------|------|------|
| abstract.tex L9 | Imp high=0.584, Rand high=3.002, Imp low=30.903, Rand low=2.915 | **0.032, 0.818, 7.196, 1.363** |
| conclusion.tex L12 | 同上 | 同上 |
| discussion.tex L13 | 同上 + ">10× severity inflation" | **新值 + ">5× severity inflation"** |

### WARNING 1: "paired" 标签
| 位置 | 旧值 | 新值 |
|------|------|------|
| abstract.tex L7 | `paired Cohen's $d$` | `Cohen's $d$` |
| conclusion.tex L10 | `paired effect sizes` | `effect sizes` |
| introduction.tex L14 | `paired effect sizes` | `effect sizes` |
| results.tex L175 | `paired Cohen's $d_z$` | `Cohen's $d$` |
| results.tex L180 (caption) | `Paired Cohen's $d_z$` | `Cohen's $d$` |
| results.tex L184 (header) | `DeepSeek $d_z$` / `Qwen $d_z$` | `DeepSeek $d$` / `Qwen $d$` |

### INFO: d≥0.55 精度
| 位置 | 旧值 | 新值 |
|------|------|------|
| abstract.tex L10 | `$d \geq 0.55$` | `$d > 0.5$` |
| conclusion.tex L16 | `$d \geq 0.55$` | `$d > 0.5$` |
| introduction.tex L15 | `$d \geq 0.55$` | `$d > 0.5$` |
| results.tex L124 | `$d \geq 0.55$` | `$d > 0.5$` |
| results.tex L196 | `$d \geq 0.55$` | `$d > 0.5$` |

### paper_framing.md
- C1/C3/Narrative Arc 中 `8/8 FAIL` → `7/8 FAIL` + 例外说明
- C3 crossover 值更新为 bf16 数据

**WARNING 2 决策**：保持 0.39→14.59（difference of medians），Abstract 措辞 "median Interaction Index difference" 与 summary table 定义一致，无需改动。

---
