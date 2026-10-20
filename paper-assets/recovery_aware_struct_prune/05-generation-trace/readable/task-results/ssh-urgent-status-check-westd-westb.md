# ssh urgent status check westd westb

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_urgent_status_check_westd_westb_20260523T120329_result.json`
- **Structured JSON:** [`d1b6babab7e95f9ffcd7.json`](../../sessions/d1/d1b6babab7e95f9ffcd7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
Floor 0.3: ✅ 完成  accuracy=65.05% (858/1319)
Floor 0.5: 🔄 运行中  80% (1054/1319), 当前 acc≈62.4%
Floor 0.6: ❌ 失败  GRPO 训练完成但 save_model 时磁盘满 (No space left on device)
SFT Standard MATH-500 v3: 🔄 运行中  82% (409/500), PID 108574, 已运行 6h+

westd-32935 GPU:
  GPU 0: 空闲 (floor 0.3 已完成)
  GPU 1: 98%, 19.3/97.9 GB (SFT MATH-500 v3)
  GPU 2: 空闲 (floor 0.6 已失败)
  GPU 3: 99%, 29.2/97.9 GB (floor 0.5 eval 中)

westb-23072 GPU:
  GPU 0: 空闲
  GPU 1: 空闲
```

**关键问题**: `/root/autodl-tmp` 数据盘 650G 已 100% 满，导致 floor=0.6 的模型保存失败（`safetensors_rust.SafetensorError: I/O error: No space left on device`）。floor 0.6 的 GRPO 训练本身已完成（100 steps），但 `trainer.save_model()` 崩溃，后续 GSM8K eval 未执行。

需要清理磁盘空间后重跑 floor=0.6 的模型保存 + eval 步骤。

---
