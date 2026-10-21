# research base vs instruct metadata

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_base_vs_instruct_metadata_20260522T174407_result.json`
- **Structured JSON:** [`402f8c67453382e83c37.json`](../../sessions/40/402f8c67453382e83c37.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研完成。核心发现：

- **没有显式 base/instruct 标注**，但 `training_method` 列为 551 个模型提供了 ground-truth（DPO/SFT/ORPO/PPO/KTO）
- **启发式分类结果**: base 4,109 (78.6%) vs instruct 1,118 (21.4%)
- **MH-DIF 可行**: 四个子组（base/instruct × 2023/2024）均 n≥200，远超 n=80 阈值
- **注意事项**: "base" 组里混有一些未标注的 fine-tuned 模型（约 234 个有歧义名称），2023 cohort 中 base 和 instruct 的 accuracy 分布差异较大（均值差 0.05），需要 theta 匹配

产出已写入 `artifacts/r18_base_instruct_survey/`。

---
