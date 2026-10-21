# verify exp002v3 gpu v2

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_exp002v3-gpu-v2_20260519T180741_result.json`
- **Structured JSON:** [`57232b249d896bc8eadd.json`](../../sessions/57/57232b249d896bc8eadd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**FAILED**: exp-002v3 已崩溃，不是端口问题，是代码 bug。

**错误**：
```
TypeError: DCGRPOTrainer.compute_rewards() takes 5 positional arguments but 7 were given
```

**调用链**：
```
run_exp002v3_dcgrpo_scaled_cosine.py:77  →  super().compute_rewards(...)
dcgrpo_trainer.py:185                    →  t.compute_rewards(...)
```

`run_exp002v3_dcgrpo_scaled_cosine.py:77` 调用 `super().compute_rewards()` 传了 7 个位置参数，但 `DCGRPOTrainer.compute_rewards()` 只接受 5 个。

**GPU 状态**：GPU 0+3 空闲（5MiB/4MiB），进程已退出（02:07:30，EXIT_CODE=1）。GPU 1+2 正常运行 exp-008v3。

需要检查 `compute_rewards()` 的函数签名是否在子类和父类之间不匹配。要我查看这两个文件的相关代码吗？

---
