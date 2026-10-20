# analysis eval plan 001 flat nli s43

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_plan_001_flat_nli_s43_20260515T213445_result.json`
- **Structured JSON:** [`00829dd3f3d440767bfb.json`](../../sessions/00/00829dd3f3d440767bfb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 评估结果: `eval_plan_001_flat_nli_s43`

### 关键指标

| 指标 | 值 | flat-NLI s42 | 差异 |
|------|-----|-------------|------|
| **rel_f1** | **0.0022** | 0.4539 | **-0.4517** |
| **ign_f1** | **0.0022** | — | — |
| **evi_f1** | 0.8533 | 0.8043 | +0.0490 |
| **edcr** | 0.9982 | 0.6431 | +0.3551 |
| precision | 0.0020 | — | — |
| recall | 0.0026 | — | — |
| evi_precision | 1.0000 | — | — |
| evi_recall | 0.7442 | — | — |
| format_ok_rate | 99.6% (981/985) | — | — |
| **field_compliance_rate** | **0.0%** | — | — |
| **evidence_format_rate** | **0.0%** | — | — |
| n_predictions | 17285 | — | — |
| n_truncated | 251/985 | — | — |
| inference_time_seconds | 3669.3 | — | — |
| TP | 32 / 16320 pred / 12151 gold | — | — |

### 诊断

**结果是灾难性的。** rel_f1 = 0.0022，比 s42 (0.4539) 下降 99.5%，比 CED RSFT mean (0.4596) 下降 99.5%。

**根因: 输出格式完全对不上。**
- `field_compliance_rate = 0.0%` — 所有预测的字段格式都不合规
- `evidence_format_rate = 0.0%` — 所有预测的 evidence 格式都不合规
- 模型输出能 parse（99.6% format_ok），但 relation/entity 字段内容与 gold 完全不匹配
- 16320 个预测只有 32 个 TP，命中率 0.2%
- EDCR = 0.9982 说明 17504/17536 个 citation 指向 distractor 句子

这**不是正常 seed 方差**——同 recipe 的 s42 有 rel_f1=0.4539，s43 几乎归零。最可能的原因：
1. s43 checkpoint 训练过程出了问题（训崩了/过拟合到错误模式）
2. 训练数据的 seed shuffle 导致 s43 收敛到退化解
3. LoRA adapter 保存不完整或加载了错误的 checkpoint

### 日志状态
- 进程正常结束，EXIT_CODE=0，无 OOM
- 251/985 文档被截断（25.5%，需关注但非主因）
- 无错误

### Registry 信息
- **checkpoint_path**: `/root/autodl-tmp/rsft_output_flat_nli_s43`
- **base_model**: `/root/autodl-tmp/models/Qwen3-4B`
- **log_path**: `~/runs/faith-evidence-ie/eval_plan_001_flat_nli_s43.log`
- **output_dir**: `/root/autodl-tmp/eval_results/rsft_flat_nli_s43/`

**建议检查 s43 的训练日志和 checkpoint，确认 adapter 是否正常。** 这个 seed 的结果不可用。

---
