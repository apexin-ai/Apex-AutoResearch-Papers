# check experiment progress and compile

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_experiment_progress_and_compile_20260518T163411_result.json`
- **Structured JSON:** [`42be5cac0de4374129a8.json`](../../sessions/42/42be5cac0de4374129a8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总报告

### 1. P8b DocRED Latency (westd-21461)
- **Unconstrained**: 200/200 ✅ 已完成
- **Constrained**: 48/200 进行中 (24%)
- 平均 ~19s/doc，剩余 152 docs
- **预估完成**: ~50 分钟后

### 2. 70B DocRED (westd-16980)
- **Unconstrained**: 428/998 (42.9%)，GPU 0
- **Constrained**: 429/998 (43.0%)，GPU 1
- 两个进程并行运行，已跑 ~3h47m (20:48 启动)
- 速率: ~1.89 docs/min (~32s/doc)
- 剩余 ~570 docs，**预估还需 ~5h**，ETA ~05:35 CST

### 3. 论文编译
- **编译成功**: 17 pages, 305KB，无错误
- **Undefined citations: 0** — 完全干净
- **BibTeX warnings: 0**
- Bib 文件已从本地同步到远程（506→623行，新增了 2026-05-18 batch）

**关于指定 cite keys 的检查**:
- `schall2025hiddencost` — 已被论文引用 ✅
- 以下 keys 存在于 bib 中但**论文尚未引用**（需要在 tex 中加 `\cite{}`）:
  - `boostcd2025`, `grammar_aligned_2024`, `formattax2026`, `dccd2026`, `slot2025`, `guidex2025`, `schema_rl2025`, `jsonschemabench2025`
- Worker 生成的变体 keys (`sakota2025boostcd`, `park2024grammaraligned` 等) 均不存在于 bib 中，也未被引用

### 附带发现
- **westd-16980 上 `llama_wikievents_full` 已 crash** (51/246): `AttributeError: 'list' object has no attribute 'get'` — `run_constrained_extraction.py:985`

---
