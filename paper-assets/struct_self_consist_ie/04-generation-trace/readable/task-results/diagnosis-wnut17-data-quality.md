# diagnosis wnut17 data quality

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_wnut17_data_quality_20260514T140815_result.json`
- **Structured JSON:** [`411d4be40fa0fbcd8f8a.json`](../../sessions/41/411d4be40fa0fbcd8f8a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**根因：训练数据 63.8% 空实例**（2166/3394 无实体），模型习得过强的"空输出"先验。

核心数据：
- 355 个 F1=0 实例中 **260 个（73%）模型直接输出空**
- 空预测的 mean_logprob = -0.007（极高置信），非空预测 = -0.05 → 这直接解释了 logprob rho = -0.41（反向相关）
- 155 个实例 16 个 sample 全空（SJ=1.0, F1=0）→ 解释了 SJ rho ≈ 0.09
- Conditional 集（F1>0）上 SJ rho=0.288, logprob rho=0.350 → 方法在非空预测上有效

**不是数据转换 bug**，数据转换逻辑正确。

**修复建议**：P0 — 将训练空实例从 63.8% 下采样到 ≤25% 后重训；P1 — 使用 epoch 3 checkpoint（eval_loss 最低 0.077）替代 epoch 5。

报告已写入 `artifacts/wnut17_diagnosis_report.md` 并注册。

---
