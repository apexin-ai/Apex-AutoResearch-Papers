# writing r36 r37 tweaks

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_r36_r37_tweaks_20260521T071634_result.json`
- **Structured JSON:** [`ca194b2ab2c1ec058cb7.json`](../../sessions/ca/ca194b2ab2c1ec058cb7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

编译成功，35 页，0 warnings，无 undefined citations。

**修改摘要：**

| 任务 | 状态 | 详情 |
|------|------|------|
| **3a** Discussion 术语修正 | 已是最新 | `non-autoregressive` 已不存在，当前文本已经是 `alternative decoding strategies (greedy, top-$k$)` |
| **3b-1** Tulchinskii et al. | 已存在 | `intrinsic_dim_detection` 已在 bib 中（NeurIPS **2023**，非 2024），且已在 §2.1 引用 |
| **3b-2** Briesch et al. | **已添加** | `briesch_self_consuming` 加入 references.bib（arXiv:2311.16822, 2023），在 §2.2 第一句 model collapse 引用列表中引用 |
| **3c** Figure 3 caption | **已添加** | 末尾追加 "Inference costs measured on a single NVIDIA RTX 5090." |

修改文件已同步至 `docs/paper/`（references.bib, related_work.tex, results.tex）。

---
