# analysis mf2 statistical tests v4

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mf2-statistical-tests-v4_20260518T100104_result.json`
- **Structured JSON:** [`b7fe8ae861a53cf3075a.json`](../../sessions/b7/b7fe8ae861a53cf3075a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

### n=118 诊断
80 DD jailbreak + 38 test benign = 118。不是 bug，是评估需要两个 class。

### Checkpoint 覆盖
| Seed | 9class | Scrambled | Binary |
|------|--------|-----------|--------|
| 42   | ✓      | ✓         | ✗ (deleted) |
| 123  | ✓      | ✗ (never trained) | ✓ |
| 456  | ✓      | ✓         | ✓      |

### McNemar 结果：所有对比均不显著 (p>0.05)

| 对比 | Seed | K | b | c | p |
|------|------|---|---|---|---|
| 9class vs scrambled | 42 | 1 | 1 | 0 | 1.0 |
| 9class vs scrambled | 42 | 2 | 6 | 1 | 0.131 |
| 9class vs binary | 123 | 1 | 0 | 0 | 1.0 |
| 9class vs binary | 123 | 2 | 0 | 1 | 1.0 |
| 9class vs scrambled | 456 | 2 | 0 | 4 | 0.134 |
| 9class vs binary | 456 | 2 | 0 | 4 | 0.134 |
| scrambled vs binary | 456 | 1,2 | 0 | 0 | 1.0 |

### Bootstrap 95% CI
- 所有 variant 在 k=1 时 F1 ≥ 0.98，大部分达到 1.0
- seed456 的 9class 略低（k2: 0.974 [0.946, 0.994]），但 scrambled/binary 在同 seed 下均为 1.0
- 9class vs scrambled 方向在 seed 间不一致（seed42 偏 9class，seed456 偏 scrambled），说明差异来自随机波动

### 结论
三种 variant 在 DD OOD 上**无统计显著差异**。discordant pair 数量极少（最多 b+c=7），McNemar 检验 power 不足以检出差异。

结果已保存至：
- 服务器：`/root/persuasion_turn_jailbreak_detect/results/matched_seed_stats.json`
- 本地：`artifacts/matched_seed_stats.json`

---
