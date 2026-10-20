# research check tex math data

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_check-tex-math-data_20260517T145024_result.json`
- **Structured JSON:** [`83cafcf595740308afe5.json`](../../sessions/83/83cafcf595740308afe5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。以下是所有 MATH 相关引用的逐条结果。

---

## `docs/paper/`（最新版本）— 全部正确

| 文件:行号 | 当前值 | 正确? |
|---|---|---|
| `docs/paper/abstract.tex:2` | N=795, p=0.81 | **Y** |
| `docs/paper/introduction.tex:24` | N=795, 73.5% vs 73.0%, p=0.81 | **Y** |
| `docs/paper/introduction.tex:35` | N=795, p=0.81 | **Y** |
| `docs/paper/experiments.tex:32` | N=795, +0.5pp, p=0.81 | **Y** |
| `docs/paper/experiments.tex:50` | MATH & 795 (表格行) | **Y** |
| `docs/paper/experiments.tex:54` | caption 提及 MATH balanced labels | **Y** |
| `docs/paper/experiments.tex:61` | N=795, labels balanced (95:107) | **Y** |
| `docs/paper/experiments.tex:65` | summary 段, 95:107 | **Y** |
| `docs/paper/discussion.tex:5` | p=0.81 | **Y** |
| `docs/paper/conclusion.tex:3` | "no routing signal" (无具体数值) | **Y** |
| `docs/paper/method.tex:39` | 仅提及 MATH 名称 | **Y** |
| `docs/paper/main.tex:35` | Limitations 段, 无旧数据 | **Y** |

---

## `artifacts/_project/paper/latex/`（旧版本）— 3 处引用旧数据

| 文件:行号 | 当前值 | 正确? |
|---|---|---|
| `latex/discussion.tex:5` | **N=300, 81.0% vs 76.7% (+4.3pp), p=0.079** | **N** |
| `latex/conclusion.tex:3` | **N=50 ("preliminary MATH pilot 50 problems")** | **N** |
| `latex/main.tex:28` | **N=50, 80% vs 72%, 88% no-pref** | **N** |

---

## `artifacts/_project/paper/`（根目录版本）— 1 处旧数据

| 文件:行号 | 当前值 | 正确? |
|---|---|---|
| `cross_env_summary_table.tex:11` | **MATH & 300** (N=300, 5.7%, 10.0%, 84.3%) | **N** |
| `conclusion.tex:5` | 仅提及 MATH 作为 future work | **Y** |
| `abstract.tex:2` | 无 MATH 引用 | **Y** |

---

## `artifacts/dream_reports/`（自动生成草稿）— 非正式论文，数据均为虚构

| 文件:行号 | 值 | 备注 |
|---|---|---|
| `best/paper.tex:248` | 71.4% vs 58.2%, N=500 | dream report |
| `median/paper.tex:254,269` | n=500 | dream report |
| `worst/paper.tex:243` | 提及 MATH 作 future work | dream report |

---

## 总结

**`docs/paper/`（最新主版本）：12 处 MATH 引用全部正确，均使用 N=795 / +0.5pp / p=0.81。**

**仍引用旧数据的位置（4 处）：**

1. **`artifacts/_project/paper/latex/discussion.tex:5`** — N=300, +4.3pp, p=0.079
2. **`artifacts/_project/paper/latex/conclusion.tex:3`** — N=50
3. **`artifacts/_project/paper/latex/main.tex:28`** — N=50, 80% vs 72%
4. **`artifacts/_project/paper/cross_env_summary_table.tex:11`** — N=300

这 4 处均在 `artifacts/_project/paper/` 路径下（历史版本），不在 `docs/paper/`（当前主版本）中。如果 `artifacts/_project/paper/` 仍会被引用或编译，需要更新；如果仅作归档，可忽略。

---
