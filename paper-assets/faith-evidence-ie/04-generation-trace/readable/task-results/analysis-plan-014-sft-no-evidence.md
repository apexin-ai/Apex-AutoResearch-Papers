# analysis plan 014 sft no evidence

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan_014_sft_no_evidence_20260515T170422_result.json`
- **Structured JSON:** [`11d494032fb21d11374f.json`](../../sessions/11/11d494032fb21d11374f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练结果摘要：plan_014_sft_no_evidence

| 项目 | 值 |
|------|-----|
| 状态 | **完成** (EXIT_CODE=0) |
| 模型 | Qwen3-4B + QLoRA 4-bit |
| 模式 | NO-EVIDENCE（只输出 relation triples） |
| 数据 | DocRED: 3027 train / 985 eval |
| 可训练参数 | 132M / 4.15B (3.18%) |
| Epochs / Steps | 3 / 570 |
| 训练耗时 | ~64 min |
| Checkpoint | `/root/autodl-tmp/sft_no_evidence_output` |

### Loss 曲线

| Epoch | Loss | Token Acc |
|-------|------|-----------|
| 0.05 | 1.547 | 0.715 |
| 0.16 | 0.847 | 0.800 |
| 0.26 | 0.802 | 0.810 |
| 0.95 | 0.761 | 0.820 |
| 1.0 | 0.825 | 0.804 ← epoch boundary spike |
| 2.85 | 0.562 | 0.858 |
| 3.0 | 0.606 | 0.849 |

**最终指标：** train_loss=0.7077, eval_loss=0.8781, eval_token_accuracy=0.8086

**W&B：** 未配置，无远程日志。

### Dev Eval 状态

- **PID:** 229663, cuda:1, 正在运行
- **进度：** 1/124 batches, ~48s/batch → 预计 ~99 min 完成
- **输出目录：** `/root/autodl-tmp/eval_plan_014_no_evidence`
- **注意：** inference.py 无 `--no_evidence` 参数，但 evaluator 对缺失 evidence 用 `get("evidence", [])` 处理，rel_f1 正常计算，evi_f1 预计 ~0

### 待 eval 完成后对比

| 模型 | rel_f1 | evi_f1 | EDCR |
|------|--------|--------|------|
| SFT (with evidence) | 0.4057 | 0.7979 | 0.7118 |
| SFT (no evidence) | **待出** | ~0 | N/A |
| RSFT mean | 0.4596 | 0.8143 | - |
| CED reranker | 0.4864 | 0.8188 | - |

---
