# audit cross seed volume appendix

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_cross-seed-volume-appendix_20260523T102207_result.json`
- **Structured JSON:** [`ef6e452ad98a269036bd.json`](../../sessions/ef/ef6e452ad98a269036bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。报告写入 `artifacts/data_audit_part3_crossseed_volume.md`。

**结果：未发现数据不一致。** 核心发现：

- **Volume control**：9 个原始精度值中 7 个在 cqa1 上直接验证一致，分解比例（45/55%、43/57%、53/47%）重新计算全部正确。Appendix 表与主文完全一致。
- **Cross-seed table**：Qwen-7B 和 Falcon3 从原始 JSON 逐项验证通过（6 个 seed×dosage 组合全部精确匹配）；Phi-4 从 westd registry 验证通过。方向一致性 5/6 和严格符号一致性 3/6 均可从表中复现。
- **tab:gsm8k_dose**：Qwen-7B 5 个 dosage 的 GSM8K 精度全部精确匹配原始文件。其余模型 registry 值一致。
- **tab:gsm8k_transfer**：6 个模型的 MMLU/GSM8K delta 均从源数据复现一致。

**3 个低优先级注意项**：
1. Falcon3 d000 MMLU/ARC 原始 JSON 不在 cqa1 上（目录为空），58.77%/81.57% 来自 westd
2. Qwen-14B GSM8K d050 (81.05%) registry 显示 PREPARING 状态，建议确认 westd 上的原始文件
3. Phi-4 在 tab:gsm8k_dose (+1.14pp, s0) 和 tab:gsm8k_transfer (−0.5pp, s123) 使用不同 seed 但后者缺少 footnote 标注

---
