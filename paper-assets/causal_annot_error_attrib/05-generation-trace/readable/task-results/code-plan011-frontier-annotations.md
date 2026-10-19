# code plan011 frontier annotations

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan011_frontier_annotations_20260522T054930_result.json`
- **Structured JSON:** [`2eb211cf8656f85eced1.json`](../../sessions/2e/2eb211cf8656f85eced1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**所有 3 个模型都返回 402 — API key 额度已用尽。**

无法继续执行标注任务。当前状态汇总：

### 已完成（OK, coverage ≥ 95%）

| Dataset | Model | Prompt | n_valid | Accuracy |
|---------|-------|--------|---------|----------|
| humaid | deepseek | zero-shot | 1500 | 0.676 |
| humaid | llama4 | zero-shot | 1500 | 0.658 |
| humaid | llama4 | few-shot-3 | 1498 | 0.666 |
| humaid | llama4 | few-shot-5 | 1471 | 0.674 |
| humaid | qwen3 | zero-shot | 1500 | 0.681 |
| civil_comments | deepseek | few-shot-5 | 1500 | 0.741 |
| civil_comments | qwen3 | few-shot-3 | 1496 | 0.811 |
| civil_comments | qwen3 | few-shot-5 | 1492 | 0.821 |
| vast | llama4 | zero-shot | 1496 | 0.523 |
| vast | llama4 | few-shot-3 | 1500 | 0.501 |

### 需要重跑（已清理错误条目，等待有效 API key）

| Dataset | Model | Prompt | 缺失条目 | 原因 |
|---------|-------|--------|----------|------|
| humaid | deepseek | few-shot-3 | 155 | 403 |
| humaid | deepseek | few-shot-5 | 263 | 403 |
| humaid | qwen3 | few-shot-3 | 77 | 402 |
| **humaid** | **qwen3** | **few-shot-5** | **1500** | 402 |
| civil_comments | deepseek | zero-shot | 1500 | 402 |
| civil_comments | deepseek | few-shot-3 | 1498 | 402 |
| civil_comments | llama4 | all 3 | 4500 | 402 |
| civil_comments | qwen3 | zero-shot | 421 | 402 |
| vast | deepseek | zero-shot | 500 | 402 |
| vast | deepseek | few-shot-3 | 1500 | 402 |
| vast | deepseek | few-shot-5 | 1500 | 402 |
| vast | llama4 | few-shot-5 | 1154 | 402 |
| vast | qwen3 | all 3 | 4500 | 402 |

**总计约 ~19,000 条需要重跑。** JSONL 文件已清理（保留有效条目、删除错误条目），resume 机制可正常工作。充值后只需运行：

```bash
cd /home/sonny/causal_annot_error_attrib
export OPENROUTER_API_KEY=[REDACTED] annotate.py --all --sample 1500
```

---
