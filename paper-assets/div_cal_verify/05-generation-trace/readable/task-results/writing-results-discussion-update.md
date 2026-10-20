# writing results discussion update

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_results-discussion-update_20260513T214605_result.json`
- **Structured JSON:** [`bd06c8db63c1c40466f7.json`](../../sessions/bd/bd06c8db63c1c40466f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。报告如下：

---

**已修改/创建的文件：**

| 文件 | 操作 | 字数 |
|------|------|------|
| `main.tex` | 添加 `\placeholder` 命令定义，`\input{discussion}`，移除独立 Limitations 占位 | — |
| `experiments.tex` §5.6 | 替换 TODO，添加 GPT2-medium uncurated 8-gen 表格 + 分析段落 + pending 占位 | 779 |
| `results.tex` §5.8 | 新增 "Scaling to GPT2-Medium (355M)" 小节 | 882 |
| `discussion.tex` | 新建，6 个小节 | 895 |

**discussion.tex 引用清单（6 unique keys，全部已在 introduction.tex 中出现）：**
- `gao2023scaling`, `karwowski2024goodhart` — Goodhart's law
- `shumailov2024ai`, `seddik2024how` — model collapse theory
- `lu2019learning`, `gama2014survey` — concept drift
- `jing2022understanding` — dimensional collapse

**无新 figure 需求。** Table `\ref{tab:medium_uncurated}` 已在 experiments.tex 中定义。

**`\placeholder{}` 占位项（待 medium 实验完成后填充）：**
- experiments.tex: GPT2-Medium RGDS/External/Random Gen~7 metrics
- results.tex: GPT2-Medium RGDS Gen~7 PPL 和 selection ratio

---
