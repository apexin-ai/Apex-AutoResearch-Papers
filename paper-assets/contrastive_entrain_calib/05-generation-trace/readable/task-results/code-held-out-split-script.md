# code held out split script

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_held-out-split-script_20260523T000249_result.json`
- **Structured JSON:** [`49cc8eb831202f4c86e0.json`](../../sessions/49/49cc8eb831202f4c86e0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== 原始数据结构 ===
字段: [pair_id, condition, domain, ground_truth, wrong_answer, pressure_answer, evidence_strength, turns, gt_verified]
pair_id 数: 181
Domain × Strength 交叉表 (pair counts):
  commonsense × medium: 10, commonsense × strong: 10, commonsense × weak: 17
    geography × medium: 10, geography × strong: 10, geography × weak: 18
      history × medium: 10, history × strong: 10, history × weak: 15
         math × medium: 10, math × strong: 10, math × weak: 14
      science × medium: 14, science × strong: 12, science × weak: 11

=== Split 结果 ===
Train: 146 pairs, 292 lines
Held-out: 35 pairs, 70 lines

=== Train 分布 ===
Domain: {commonsense: 60, geography: 62, history: 56, math: 54, science: 60}
Strength: {medium: 88, strong: 84, weak: 120}

=== Held-out 分布 ===
Domain: {commonsense: 14, geography: 14, history: 14, math: 14, science: 14}
Strength: {medium: 20, strong: 20, weak: 30}

=== 验证 ===
Overlap: 无
文件已生成到 28034: 是（直接在 28034 上跑脚本生成，结果一致）
```

两台服务器（29046、28034）均已生成 `train_split.jsonl`（292 lines）和 `eval_held_out.jsonl`（70 lines），分层抽样覆盖全部 15 个 domain × strength 组合，无 overlap。

---
