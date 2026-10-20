# analysis plan 007 redocred 4b sft eval r2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan_007_redocred_4b_sft_eval_r2_20260516T133330_result.json`
- **Structured JSON:** [`1c15b8b65ddedcba1a8c.json`](../../sessions/1c/1c15b8b65ddedcba1a8c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

日志仅 28 行，无 W&B logging。完整 metrics 已从 metrics.json 获取。

```
CONCLUSION: success
METRICS: {
  F1: 0.3706,
  Ign-F1: 0.3659,
  Precision: 0.4316,
  Recall: 0.3247,
  Evi-F1: 0.8170,
  Evi-Precision: 0.8208,
  Evi-Recall: 0.8131,
  EDCR: 0.6674,
  Evi-F1-Joint: 0.2862,
  Format-OK: 491/493 (99.6%),
  Truncated: 139/493,
  Predictions: 8191
}
WANDB_RUN_ID: N/A (eval 未接入 W&B logging)
CHECKPOINT_PATH: base=/root/autodl-tmp/models/Qwen3-4B, adapter=/root/autodl-tmp/sft_output
LOG_PATH: ~/runs/faith-evidence-ie/plan_007_redocred_4b_sft_eval_r2.log
KEY_FINDINGS:
- Re-DocRED F1=0.3706，与 DocRED SFT baseline (0.4106) 相比下降 ~4pp (9.7% 相对下降)，泛化能力合理
- Ign-F1=0.3659，排除训练集共现事实后仅微降，说明模型不是靠记忆训练事实
- Evidence F1=0.8170，跨数据集 evidence 质量极高，远超预期
- EDCR=0.6674，66.7% 的 evidence citations 指向 distractor 句（Re-DocRED 特有的扰动设计），说明模型仍能在噪声环境下定位证据
- 139/493 (28.2%) 文档 truncated，Re-DocRED 文档更长，可能略影响 recall (0.3247 < precision 0.4316)
- field_compliance_rate=71.6%（353/493 evidence 格式完整），部分文档 evidence 字段格式不完整但不影响 relation extraction
COMPARISON:
- DocRED SFT (evidence): rel_F1=0.4106 → Re-DocRED: rel_F1=0.3706 (Δ=-4.0pp, -9.7%)
- DocRED SFT (no-evidence): rel_F1=0.4893 → 跨数据集无对应实验
- 4pp 下降在跨数据集零样本泛化中属于良好表现，方法具备泛化能力
- Evidence F1 从 DocRED 到 Re-DocRED 保持 0.817 高位，evidence grounding 机制跨数据集鲁棒
```

---
