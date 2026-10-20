# ssh sync compile and progress

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_sync_compile_and_progress_20260517T083033_result.json`
- **Structured JSON:** [`0fc7de51209224e3c454.json`](../../sessions/0f/0fc7de51209224e3c454.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

| 项目 | 结果 |
|------|------|
| 同步 .tex 文件 | **12 个** |
| 编译 errors | **0** |
| Warnings | **3**（含 1 个 undefined citation） |
| Undefined refs/citations | **1**：`gao2021pile`（references.bib 中缺此条目） |
| 页数 | **23 页** |
| Label convergence | Converged |

### 实验进度

| 实验 | PID | GPU | 利用率 | 显存 | gen 进度 |
|------|-----|-----|--------|------|----------|
| pythia410m_wiki_a100_s42 | 247554 | GPU 0 | 43% | 14.4 GiB / 97.9 GiB | **gen_0 ~ gen_4**（5/11） |
| opt1b_wiki_a100_s42 | 249384 | GPU 1 | 96% | 27.2 GiB / 97.9 GiB | **gen_0 ~ gen_2**（3/11） |

两个实验均在正常运行。`gao2021pile` 需要补充到 references.bib。

---
