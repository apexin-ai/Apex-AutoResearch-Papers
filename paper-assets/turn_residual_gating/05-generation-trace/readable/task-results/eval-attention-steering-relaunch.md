# eval attention steering relaunch

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_attention_steering_relaunch_20260520T092543_result.json`
- **Structured JSON:** [`d4c40ef6ecd9b3ba8192.json`](../../sessions/d4/d4c40ef6ecd9b3ba8192.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果完整，所有 6 个 β 值的数据都已存在。**不需要重跑。**

## Attention Steering 结果 (v7 TG, gen mode, N=5 convs)

| β | mid_turns_avg_GAR | avg_PPL |
|---:|------------------:|--------:|
| 0.0 | 0.0280 | 1.409 |
| 0.5 | 0.0287 | 1.387 |
| 1.0 | 0.0349 | 1.360 |
| 2.0 | 0.0620 | 1.411 |
| 5.0 | 0.6795 | 1.908 |
| 10.0 | 0.9590 | 4.220 |

关键观察：
- **β=0→1**: GAR 微增 (0.028→0.035)，PPL 略降至 1.36——steering 几乎免费
- **β=2**: GAR 翻倍至 0.062，PPL 仍与 baseline 持平 (1.41)
- **β=5**: GAR 跳至 0.68，PPL 开始上升到 1.91——steering 效果显著但代价可控
- **β=10**: GAR 接近饱和 0.96，PPL 恶化到 4.22——过度 steering 导致生成质量劣化

Registry 状态需要更新为 DONE。需要我更新吗？

---
