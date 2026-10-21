# research paper claim2 prep

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_paper-claim2-prep_20260515T210754_result.json`
- **Structured JSON:** [`a880b2f400ed37740063.json`](../../sessions/a8/a880b2f400ed37740063.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。产出文件 `claim2_evidence_brief.md` 已注册为 artifact (`art_20260515_d4f55f`)。

内容概要：

1. **数据表格**：5 张表覆盖核心 accuracy、gap 分解（25% gradient dilution / 75% information overload）、统计检验（所有对比 p<0.001）、跨模型数据、per-class 指标
2. **论证逻辑**：label-only loss 作为 oracle intervention 的因果链 — 即使完全消除 gradient dilution，仍有 13pp 残差 gap，只有 trace compression 能修复
3. **校准独立证据**：label-only ECE (0.1107) 反而比 full_trace (0.0958) 更差，说明 gradient fix 制造了新问题，VOTA 同时解决 accuracy 和 calibration
4. **图表建议**：4 张图按优先级排列 — gap 分解柱状图 > reliability diagram > waterfall > 跨模型对比
5. **Reviewer 防御**：6 个攻击点 + 预案（additivity 假设、ECE 反常、epoch 不足等）
6. **Open items**：DeepSeek full_trace v3 和 exception_only seed456 仍在运行

---
