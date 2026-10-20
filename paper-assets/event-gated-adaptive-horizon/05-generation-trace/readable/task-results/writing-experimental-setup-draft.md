# writing experimental setup draft

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_experimental-setup-draft_20260514T185802_result.json`
- **Structured JSON:** [`9a5b087bc833eeeac08e.json`](../../sessions/9a/9a5b087bc833eeeac08e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。文件在 `paper/sections/experimental_setup.md`，约 1.8 页 CoRL 格式。

覆盖内容：
- **3.1 Base Architecture**: RSSM + 三类 dt_embedding 配置 + subsample + imagination dt/horizon
- **3.2 Environment**: Walker Walk (primary) + Cheetah Run / Cartpole Swingup (cross-env, 标注 in progress)
- **3.3 Factorial Design**: 实验表（Table 1）列出 001/005/006/007/008a-f 全部条件，标注 4 组 key controlled comparisons（008d vs 008f, 008c vs 008a, 006 vs 008a, 008e_v3），多 seed 复制说明
- **3.4 Diagnostic Framework**: normalized v/e ratio 定义（公式 1-2）、三档阈值（>1.5 pathological, 0.8-1.2 normal, <0.7 suppression）、late-training v/R 补充信号
- **3.5 Training Details**: 超参数、训练时长、评估协议、可复现性

设计决策：
- 008d vs 008f 作为 cleanest causal pair（仅 dt_embed_dim 不同），与 memory.md 中 Director 修正一致
- cross-environment 实验标注 footnote 说明 in progress，未 claim 结果
- 表格用 F-A/F-C/F-D/F-E/F-F 短名，方便后续 Results 引用

---
