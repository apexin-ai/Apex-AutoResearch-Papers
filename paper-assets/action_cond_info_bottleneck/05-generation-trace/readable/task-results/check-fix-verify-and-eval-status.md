# check fix verify and eval status

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_fix-verify-and-eval-status_20260516T172455_result.json`
- **Structured JSON:** [`992bdaad59f393469ffb.json`](../../sessions/99/992bdaad59f393469ffb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报如下：

---

### 1. 代码修复确认 ✓

`select_action` 已正确包含 language conditioning 修复：
```python
def select_action(self, batch, **kwargs):
    if self.acib_config.condition_source == "language":
        self._cached_lang_condition = self._compute_lang_condition(batch)
    return self.base_policy.select_action(batch, **kwargs)
```

### 2. 当前 GPU 进程

| PID | GPU | 显存 | 运行时间 | 用途 |
|-----|-----|------|----------|------|
| 104743 | GPU 1 | 6004 MiB | ~4 min | **fixed eval seed1** (v7_contrastive, ckpt-20000, 4 suites, seed=42) |

- PID 46186（buggy seed1 eval）和 PID 101853（buggy seed2 eval）均已自行终止，无需手动 kill
- GPU 0 空闲，GPU 1 仅 fixed eval 占用（6GB / 98GB）

### 3. Fixed eval 运行状态 ✓

- **PID 104743 正在运行**，正在跑 libero_spatial 第一个 suite
- 进度：4/50 episodes（8%），running_success_rate=75%
- 日志确认 `[EVAL] Using language conditioning, shape=torch.Size([1, 960])` 每步都在输出 — **修复生效**

### 4. 无需重新启动

Fixed eval 已在运行，无需操作。

### 5. 预计完成时间

当前速率 ~31s/episode。每 suite 50 episodes ≈ 26 min。4 suites (spatial/object/goal/10) ≈ **1.7-2.5 小时**（libero_10 可能更慢因 episode 更长）。预计完成时间约 **03:30-04:00 UTC**。

---
