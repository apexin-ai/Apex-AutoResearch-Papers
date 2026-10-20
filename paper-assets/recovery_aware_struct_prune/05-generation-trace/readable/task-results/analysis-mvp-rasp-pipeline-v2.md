# analysis mvp rasp pipeline v2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mvp_rasp_pipeline_v2_20260514T135102_result.json`
- **Structured JSON:** [`2e86568e84228e208eda.json`](../../sessions/2e/2e86568e84228e208eda.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已产出并注册。核心结论：

**判定: FAILED — 实验未完成**

- **Post-prune**: 两模型均 0.15% accuracy（完全退化）
- **GRPO**: 直接跑在退化模型上，loss=0 / grad_norm=0，在 step 177/5604 (3%) 被 SIGTERM 终止
- **根因**: V2 pipeline 脚本遗漏了 SFT warmup 步骤，导致 GRPO 重复了已知的失败模式
- **Spearman ρ**: 未计算（Step 5/6 均未执行）
- **唯一有趣信号**: RASP 模型 entropy 0.34 vs Standard 0.05，RASP 偶有微弱 reward，暗示功能多样性差异，但不足以得出结论

下一步需修复 pipeline 加入 SFT warmup 再重新跑。

---
