# paper r14 citations

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_r14-citations_20260517T201145_result.json`
- **Structured JSON:** [`3bc498e430a4ad33ee71.json`](../../sessions/3b/3bc498e430a4ad33ee71.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

改动摘要：

**1. Abburi et al., 2025 (arXiv:2505.11550)**
- **注意**：该论文实际作者为 **Abburi, Bhattacharya, Bowen, Pudota**，不是 Alikhanov。arXiv ID 确认无误，但作者名有误。
- bib key: `abburi_multifaceted`，添加在 Detection 区 `semeval2024_task8` 之后
- 在 `related_work.tex` §2.1 第一句 learned classifiers 列表中插入，改写为 "learned classifiers that combine handcrafted features with neural architectures"

**2. CORN loss (Shi, Cao, Raschka, 2023)**
- 正式发表于 *Pattern Analysis and Applications*, vol. 26, pp. 941-955
- bib key: `corn_ordinal`，添加在 Machine Learning 区 `frank_hall_ordinal` 之后
- `related_work.tex` §2.1：在 ordinal classification literature 引用组中添加 `corn_ordinal`
- `method.tex` §3.4 Classifier 段：在 "CORAL, Frank-Hall" 之间插入 "CORN"

**3. AAAI 2025 Defactify 4.0 Shared Task**
- 找到的是 dataset/overview paper: Roy et al. (2025), "A Comprehensive Dataset for Human vs. AI Generated Text Detection", arXiv:2510.22874（20 位作者）
- 未找到独立的 shared task overview proceedings paper；此 dataset paper 是该 shared task 最可引用的出处
- bib key: `defactify_dataset`，添加在 Detection 区
- `related_work.tex` §2.1：在 multi-generator attribution 的 `semeval2024_task8` 引用后追加 `defactify_dataset`

---
