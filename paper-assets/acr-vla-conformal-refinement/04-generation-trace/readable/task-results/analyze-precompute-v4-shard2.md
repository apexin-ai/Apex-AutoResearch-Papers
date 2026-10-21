# analyze precompute v4 shard2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_precompute-v4-shard2_20260513T201045_result.json`
- **Structured JSON:** [`f7fdb2645df80cb04ec9.json`](../../sessions/f7/f7fdb2645df80cb04ec9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据验证完毕。

---

## 报告

### shard2 完成状态: **SUCCESS**
- spatial: 4055 samples 处理完毕，0.46s/sample，无 error
- object: 4856 samples 处理完毕，0.48s/sample，无 error
- EXIT_CODE=0，两个 benchmark 均触发 merge 并成功合并

### Cache 完整性

| Benchmark | Samples | Trajectories | obs_features | expert_actions | k_samples | 状态 |
|-----------|---------|-------------|--------------|----------------|-----------|------|
| spatial | 12,167 | 100 (10 tasks × 10 demos) | [12167, 960] | [12167, 5, 6] | [12167, 10, 5, 6] | OK |
| object | 14,570 | 100 (10 tasks × 10 demos) | [14570, 960] | [14570, 5, 6] | [14570, 10, 5, 6] | OK |

- 总大小: **264MB**
- K=10 calibration samples, h_eff=5 action horizon, obs_dim=960, action_dim=6
- 3 个 shard 的 partial 文件均完整（spatial: 9 partials × 3 shards = 27, object: 10 partials × 3 shards = 30）
- manifest.json 正确记录了合并后的元数据
- 所有 .pt 文件可正常 `torch.load`，tensor shape 一致

### 结论
**可以开始 CRM 训练。** 无异常或警告。

---
