# diagnose exp023c completion check

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp023c-completion-check_20260515T050819_result.json`
- **Structured JSON:** [`3789ea6275493f1a98c3.json`](../../sessions/37/3789ea6275493f1a98c3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

没有活跃的 cron job，无需清除。

---

## exp023c_grpo_serial 结果

**状态：崩溃（磁盘满）**

| 项目 | 值 |
|------|-----|
| 完成步数 | 8 / 30 |
| 崩溃原因 | `OSError: [Errno 28] No space left on device`（/root/autodl-tmp 94% 占用，233G/250G） |
| 崩溃位置 | Step 9 rollout reset，textworld/fast_downward 复制 libdownward.so 到 /root/autodl-tmp/tmp/ 时 |
| Checkpoint | `/root/autodl-tmp/checkpoints/exp023c/global_step_5`（仅此一个） |
| Log | `/root/autodl-tmp/checkpoints/exp023c/train.log` |

**Metrics 趋势（step 1 → step 8）：**

| 指标 | Step 1 | Step 8 | 趋势 |
|------|--------|--------|------|
| success | 29.7% | 23.4% | 下降 |
| action_is_valid | 79.1% | 77.9% | 持平 |
| entropy | 0.0652 | 0.0555 | 下降 |
| pass@16 | 75% | 50% | 下降 |
| KL | 0.000156 | 0.000475 | 上升 |
| step time | ~240s | ~365s | 变慢 |

即使没有磁盘问题，模型在 8 步内也在持续退化——success rate 和 pass@16 均下降，entropy 收缩，GRPO 未能在 SFT baseline 上产生改善。

---
