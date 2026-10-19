# monitor exp002v3 r1 signal

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_exp002v3-r1-signal_20260519T180927_result.json`
- **Structured JSON:** [`481259a2eee378580abd.json`](../../sessions/48/481259a2eee378580abd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

问题定位清楚了。

```
进程状态：死亡（首步崩溃，EXIT_CODE=1）
当前步数：0（未完成任何训练步）
GPU 0 显存占用：5 MiB（空闲）
GPU 1 显存占用：31432 MiB（残留/其他进程）
GPU 2 显存占用：30670 MiB（残留/其他进程）
GPU 3 显存占用：4 MiB（空闲）

R1 信号分析：无（未产生任何训练数据）

异常：进程死亡
结论：进程死亡，需修复后重启
```

## 崩溃原因

`run_exp002v3_dcgrpo_scaled_cosine.py:77` 的 `Exp002v3Trainer.compute_rewards()` 调用 `super().compute_rewards()` 时多传了 2 个参数：

**子类调用（6 个参数）：**
```python
super().compute_rewards(
    completions, conditions, pair_ids, batch_activations, r1_ema, ema_alpha
)
```

**父类签名（4 个参数）：**
```python
def compute_rewards(self, completions, conditions, pair_ids, batch_activations):
```

`r1_ema` 和 `ema_alpha` 是子类新增的参数，父类 `DCGRPOTrainer.compute_rewards()` 不接受。

## 修复

`run_exp002v3_dcgrpo_scaled_cosine.py:77` 改为只传父类接受的 4 个参数：

```python
rewards, components = super().compute_rewards(
    completions, conditions, pair_ids, batch_activations
)
```

`r1_ema` 和 `ema_alpha` 留在子类签名中供子类自身逻辑使用即可。需要修复后重启训练。

---
