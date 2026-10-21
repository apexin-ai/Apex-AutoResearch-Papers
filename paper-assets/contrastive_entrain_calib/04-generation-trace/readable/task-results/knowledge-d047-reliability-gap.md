# knowledge d047 reliability gap

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_knowledge_d047-reliability-gap_20260521T114444_result.json`
- **Structured JSON:** [`1c21c0c5dc139654d46c.json`](../../sessions/1c/1c21c0c5dc139654d46c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

paper_framing.md 第 150 行的 "near its ceiling" 指的是 R3 reward 饱和到 ~1.0 的上限，不是 "vanilla ceiling" 叙事，保留不动。

ROADMAP.md 第 3/29/68 行出现的 "vanilla ceiling" 都在描述 D047 修正本身的历史记录（"从 vanilla ceiling 改为..."），是决策日志的忠实记录，保留不动。

所有 4 项修改完成：

1. **"vanilla ceiling" 替换** — paper_framing.md 全部改为"围绕 vanilla 不稳定振荡 + reliability gap"；ROADMAP.md 6 处已更新
2. **Reliability gap 对比框架** — 在三层区分总结后新增 ACT 13/13、R3-only s1 3/12、s2 0/7、效率差 ~16x
3. **论文 Table 报告方式** — R3-only 轨迹表后新增 blockquote 注释（附 late-training range 和 mean）
4. **不稳定性发作时间泛化** — spike-regression 段落中新增跨 seed 发作时间描述（seed 1 ~step 6000, seed 2 ~step 3500），强调是方法固有特征

---
