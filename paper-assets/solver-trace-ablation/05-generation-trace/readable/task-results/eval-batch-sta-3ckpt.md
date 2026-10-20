# eval batch sta 3ckpt

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_batch-sta-3ckpt_20260514T031822_result.json`
- **Structured JSON:** [`e5e30544b2a94ef7968e.json`](../../sessions/e5/e5e30544b2a94ef7968e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

## eval_sta.py 评估结果

| 实验 | Reward | Seed | Prove Rate | Mean ISR | Proved-only ISR |
|---|---|---|---|---|---|
| **plan001-s42** | exec-only | 42 | **93.0%** | 0.1232 | 0.1324 |
| plan013-s42 | random | 42 | 100.0%† | 0.5350† | 0.5350† |
| plan001-s43 | exec-only | 43 | 13.0%‡ | 0.0000 | 0.0000 |

### 关键发现

1. **plan013 (random reward) 是 reward hacking**：模型退化为只生成 2-component 证明（前提=结论，结论=结论），ISR=0.500 是固定的 artifact，不是真实质量指标。PR=100% 是因为结论本身被当前提断言。

2. **plan001-s43 严重退化**：训练 PR=88.3% 但 eval PR 仅 13%，87% 样本 hit max_new_tokens（生成不可解析的长输出）。ISR 全为 0。

3. **跨 seed 稳定性差**：s42 (93% PR) vs s43 (13% PR) 表明 exec-only reward landscape 存在极大方差。

4. **plan001-s42 是唯一可用的真实模型**：93% prove rate，ISR=0.1232 反映真实但 noisy 的 FOL 形式化。

所有结果已写入 registry 并注册 artifact（`eval_sta_comparison.md`）。

---
