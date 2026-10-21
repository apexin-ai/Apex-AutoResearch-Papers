# analysis multiseed selection f1

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_multiseed_selection_f1_20260515T124808_result.json`
- **Structured JSON:** [`231acdf3bd8e52df2d7d.json`](../../sessions/23/231acdf3bd8e52df2d7d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总结果：

## 结果摘要

### 5 个实验组，3 seeds (42, 123, 456)，bootstrap 10000 次

| 配置 | N | 最佳 Signal | Δ greedy | p (Fisher) |
|------|---|------------|----------|------------|
| **Qwen SciERC NER N=16** | 529 | LP | +0.0047 | 0.066 |
| **Qwen SciERC RE N=16** | 397 | LP | +0.0101 | 0.053 |
| **Qwen SciERC NER N=8** | 529 | LP | +0.0004 | 0.541 |
| **LLaMA SciERC NER N=8** | 529 | FK | -0.0014 | 0.698 |
| **LLaMA CoNLL NER N=16** | 2756 | VC | +0.0028 | **0.0001** |

**关键发现：**
- **CoNLL N=16** 是唯一所有 signal 都显著优于 greedy 的配置（p < 0.001，Fisher 合并），所有 5 个 signal 一致显著
- **SciERC 上无论 NER 还是 RE**，没有 signal 在 3-seed 合并后达到 p < 0.05（LP 最接近，p ≈ 0.05-0.07）
- VC 在 SciERC 上一致 **低于** greedy（Δ ≈ -0.03），说明 voting confidence 在 SciERC 这种复杂 schema 上会 hurt
- Oracle F1 远高于 greedy（SciERC NER: +17.6pp, RE: +23.8pp），说明有大量 room for improvement，但现有 signal 还不够好

**产出文件：**
- 脚本：`code/compute_selection_f1.py`
- JSON 数据：`output/multiseed_selection_f1.json`
- Markdown 报告：`artifacts/multiseed_selection_f1_report.md`

---
