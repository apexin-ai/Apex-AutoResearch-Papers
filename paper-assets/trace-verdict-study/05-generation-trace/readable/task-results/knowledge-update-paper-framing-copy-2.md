# knowledge update paper framing

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_knowledge_update-paper-framing_20260515T192754_result.json`
- **Structured JSON:** [`d41e63273f8b99337448.json`](../../sessions/d4/d41e63273f8b99337448.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

paper_framing.md 已更新至 v2.5。主要增量变更：

1. **Core Insight** — 加入 VOTA repositioning 段落（fault indicator isolation, not compression）
2. **Claim 1** — cross-model gap 改为 0pp (best checkpoint) / 0.50pp (final)，加入 epoch1→epoch3 退化引用
3. **Claims 2 & 3** — 所有数量 claim 旁标注 exp_id（`[exp_name]` 格式），精确数值对齐 registry（86.22%/85.63%/81.76%）
4. **Cross-Model Evidence Summary** — 新增 4-condition 汇总表 + key insight
5. **VOTA Repositioning** — 新增独立 section，含证据链、论文表述建议、对 Method section 影响
6. **Calibration 表** — 扩展为含 Accuracy 列的 7-condition 完整表
7. **D7: Early stopping** — 新增 discussion point（DeepSeek epoch1 > epoch3 + signal complexity 与 optimal epochs 的关系）
8. **Reviewer concerns** — 新增"只有 2 个模型 universality 太强"和"epoch1 vs epoch3"两条
9. **Headline result** — 升级为 "0pp gap on both models"，VOTA 定位改为 fault indicator isolation
10. **对比表** — 新增 VOTA 定位、Early stopping、Narrative arc 三行

---
