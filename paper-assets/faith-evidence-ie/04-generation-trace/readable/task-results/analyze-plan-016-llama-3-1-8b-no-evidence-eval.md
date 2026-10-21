# analyze plan 016 llama 3 1 8b no evidence eval

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_plan_016_llama_3_1_8b_no_evidence_eval_20260516T132825_result.json`
- **Structured JSON:** [`b6f2cfe4a7d1be2cea0d.json`](../../sessions/b6/b6f2cfe4a7d1be2cea0d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## plan_016_llama_3_1_8b_no_evidence_eval 结果

### 核心指标

| 指标 | 数值 |
|------|------|
| **rel_f1 (F1)** | **0.5624** |
| **Ign-F1** | **0.5452** |
| rel_p (Precision) | 0.5370 |
| rel_r (Recall) | 0.5903 |
| evi_f1 | 0.0000 (预期，no-evidence 模式) |
| Format OK | 985/985 (100%) |
| Truncated | 182/985 |
| Predictions | 18,466 |

### 配置确认
- `no_evidence: true` ✓ (正确传了参数)
- W&B: 无 run ID（未上传 W&B）

### 跨模型对比

| 模型 | rel_f1 | 备注 |
|------|--------|------|
| **LLaMA-3.1-8B no-evidence** | **0.5624** | 本次结果 |
| Qwen2.5-3B no-evidence | 0.4893 | 基线 |
| LLaMA-3.1-8B with-evidence | 待出 | plan_016_llama_3_1_8b_sft_eval |

### 分析

LLaMA-3.1-8B no-evidence 的 rel_f1=0.5624，大幅超过 Qwen2.5-3B no-evidence (0.4893)，高出 **+7.31pp**。这符合预期——8B 参数模型在纯关系抽取上应强于 3B 模型。

等 plan_016_llama_3_1_8b_sft_eval（with-evidence）完成后即可计算 LLaMA 的 evidence tax = rel_f1(with-evidence) - rel_f1(no-evidence)。

---
