# experiment scienceworld info loss eval

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_scienceworld-info-loss-eval_20260520T141325_result.json`
- **Structured JSON:** [`d4a0fe082eb72f32abc5.json`](../../sessions/d4/d4a0fe082eb72f32abc5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个 boil episodes 完成（全部 100 步 FAIL）。第三个 format rate 恢复正常（92%），前两个可能是特别难的变体。

**当前进度**: 3/89 episodes, ~142s/episode。预估：
- Full context eval: ~3 小时（到 ~01:30 CST）
- h=2 eval: ~1.5 小时（到 ~03:00 CST）

实验在后台稳定运行，后续可通过以下方式检查进度：
```
wc -l /root/autodl-tmp/eval_info_loss/scienceworld_full_t0.jsonl  # 已完成 episodes
tail -5 /root/autodl-tmp/eval_info_loss/run.log  # 最新结果
```

**关键参数汇总**：
| 条件 | 温度 | Context | GPU | Episodes |
|------|------|---------|-----|----------|
| scienceworld_info_loss_full | T=0 | full | westd cuda:0,1 | 89 |
| scienceworld_info_loss_h2 | T=0 | h=2 | westd cuda:0,1 | 89 |

**已知参考数据**（不同温度）：
- Full context, T=0.4 → 30.1% (1796 eps, bjb1 eval_v2)
- Cell A val_before_train (h=2, T=0.4) → reward_mean ~0.1/10 ≈ 1% (32 eps)

Registry 已创建 `scienceworld_info_loss_full`（RUNNING）和 `scienceworld_info_loss_h2`（QUEUED）。cuda:2,3 Cell C 未受影响。

---
