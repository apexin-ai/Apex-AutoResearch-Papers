# ops investigate rel f1 0 4549 source

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_investigate-rel-f1-0_4549-source_20260515T225704_result.json`
- **Structured JSON:** [`cdd66e825e17702352f3.json`](../../sessions/cd/cdd66e825e17702352f3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

差异来源已明确：**同一训练 run（`grpo_ced_g8_bf16`），不同 checkpoint**。

| 指标 | eval_grpo_g8_bf16 | plan_011_bf16_g8_step_eval |
|---|---|---|
| checkpoint | **step-100** | **step-70** |
| rel_f1 | 0.4549 | 0.4341 |
| 训练 run | grpo_ced_g8_bf16 | 同一 run |
| --no-quantize | ✓ | ✓ |
| --sft_adapter | ✓ | ✓ |
| eval data | 985 docs full dev | 985 docs full dev |

两次 eval 的 quantization、SFT adapter、数据集完全一致。2pp 差异纯粹是 **30 步额外训练**（step 70 → 100）带来的增益。从 batch_eval 可见 rel_f1 单调递增：step 80=0.4456, 90=0.4523, 100=0.4549，step 70=0.4341 符合这条曲线。

**论文应报 0.4549（checkpoint-100）**，这是 bf16 GRPO 的 best checkpoint 结果。0.4341 是中间 checkpoint，适合放 training dynamics 图但不应作为方法最终性能。

---
