# prep analysis pipeline validation

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_analysis-pipeline-validation_20260515T005345_result.json`
- **Structured JSON:** [`74ba18ee43de57c5172d.json`](../../sessions/74/74ba18ee43de57c5172d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已保存到 `artifacts/report_analysis_pipeline_ready.md`。

验证结果总结：

**分析脚本：✅ 就绪**。`analyze_n500_unified.py` 对 DeepSeek 和 Qwen 的 s015/s020 conditions 成功运行，输出 median II diff、bootstrap CI (B=10000)、Bonferroni 校正 p 值、d_z、dose-response 等全部指标。缺失 condition 优雅降级。

**实验进度：**
- s015/s020：全部 8 条完成 ✅
- s025：4 条运行中（46%-73%）
- s030：尚未开始，s025 完成后自动启动

**初步结果亮点：** importance masking 在两个模型上都显著（p_bonf=0.0000），random 均不显著（p_bonf=1.0000），符合预期。DeepSeek 效应量明显大于 Qwen。

---
