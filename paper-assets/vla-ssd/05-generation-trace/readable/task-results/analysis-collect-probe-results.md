# analysis collect probe results

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_collect_probe_results_20260519T074812_result.json`
- **Structured JSON:** [`6e9d8a72197a9c27935e.json`](../../sessions/6e/6e9d8a72197a9c27935e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已保存到本地 `artifacts/libero_finetuned_probe_profile.json`。

## 关键数据摘要

**模型**: openvla-7b-finetuned-libero-goal | **方法**: PCA256 + LogReg, 10-fold LOOCV

### Cross-instruction probe (last_preaction token)

| Layer | Accuracy | Std |
|-------|----------|-----|
| L0 | 0.100 | 0.000 |
| L1 | 0.997 | 0.003 |
| L2-L31 | **1.000** | 0.000 |

Fine-tuning 后 L1 起即近乎完美分类，L2+ 全部 100%，零方差。

### image_mean token (控制)

所有层 ~0.1 (chance, 10 tasks)。图像 token 均值不携带 instruction-discriminative 信息。

### 四条件对比 (last_preaction)

| Layer | Untrained | Llama2-base | OpenVLA-7B | LIBERO-finetuned |
|-------|-----------|-------------|------------|------------------|
| L0 | 0.100 | 0.100 | 0.100 | 0.100 |
| L1 | **1.000** | 0.802 | 0.996 | 0.997 |
| L8 | 0.986 | 0.999 | 1.000 | 1.000 |
| L31 | **0.820** | 1.000 | 1.000 | 1.000 |

关键发现：fine-tuned 模型的 cross-instruction probe profile 与 OpenVLA-7B pretrained 几乎完全一致（L1+ 均饱和于 1.0），task-specific fine-tuning 没有显著改变 instruction 的线性可分性 pattern。Untrained 模型 L31 只有 0.82 仍然是最显著的差异点。

---
