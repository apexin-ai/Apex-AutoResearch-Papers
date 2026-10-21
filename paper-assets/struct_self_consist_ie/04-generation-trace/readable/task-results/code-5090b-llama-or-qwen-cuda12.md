# code 5090b llama or qwen cuda12

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_5090b_llama_or_qwen_cuda12_20260518T200221_result.json`
- **Structured JSON:** [`38d05c79f2e117c69923.json`](../../sessions/38/38d05c79f2e117c69923.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

**LLaMA checkpoint**: 不存在，走方案 2。

**4 GPU 全部在跑**：

| GPU | 任务 | 进度 | 状态 |
|-----|------|------|------|
| cuda:0 | Qwen FewNERD s456 | 110864/301184 (37%) | ~39 min 已跑，预计还需 ~1h |
| cuda:1 | Qwen FewNERD s789 | 96/301184 (~0%) | 刚启动，模型已加载，开始推理 |
| cuda:2 | Qwen SciERC s789 | 88/4408 (~2%) | 已启动，正常推理中（SciERC 数据量小很多，4408 prompts vs 301184） |
| cuda:3 | Qwen FewNERD s123 | 164688/301184 (55%) | ~58 min 已跑，预计还需 ~50 min |

SciERC s789 首次启动时因 `--data_dir` 指向 `data/scierc/` 而非 `data/scierc/processed_data/` 报错，已修复重启。

---
