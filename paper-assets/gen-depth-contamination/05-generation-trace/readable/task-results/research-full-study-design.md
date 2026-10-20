# research full study design

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_full_study_design_20260512T124814_result.json`
- **Structured JSON:** [`f36be58aeabcb0142a3f.json`](../../sessions/f3/f36be58aeabcb0142a3f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/full_study_plan.md`。

**核心结论**:

- **P0 (核心论文支撑)**: ~50h GPU — 8 个 corpus 配置 + 分类器 + K* 分析 + 下游过滤评估
- **P0+P1**: ~101h GPU — 加 retrain-chain、更多下游评估、额外 baselines
- **P0+P1+P2+buffer**: ~148.5h GPU — 1×4090D 13 天 (260h 可用) 完全可以覆盖
- **瓶颈是 wall-clock 串行依赖**，不是 GPU 总量：depth chain 内部必须串行，关键路径 P0 在 Day 8 完成，P0+P1 在 Day 12 完成
- **建议申请 1 块额外 4090D**：主卡跑 1B 级实验，副卡跑 7B chain (10h) + 下游评估 (24h)，两卡并行可 Day 9 完成全部 P0+P1
- **Retrain-chain** 用 Pythia-1.4B LoRA (rank=16, alpha=32, 3 epochs)，每轮 ~67 min，5 轮总计 ~6.5h
- **必须先修复**: left-padding、batch_size 调大、flash-attn

---
