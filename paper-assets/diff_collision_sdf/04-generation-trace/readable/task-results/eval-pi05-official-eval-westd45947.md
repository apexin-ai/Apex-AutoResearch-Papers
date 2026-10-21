# eval pi05 official eval westd45947

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_pi05_official_eval_westd45947_20260522T194044_result.json`
- **Structured JSON:** [`d31c1f50407f09f4ade3.json`](../../sessions/d3/d31c1f50407f09f4ade3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整 eval 已在运行，4/4 成功。总结：

### 结果

| 项 | 状态 |
|---|---|
| **Server** | `tmux: pi05_server`，cuda:1，port 8000，pi05_libero checkpoint 已加载 |
| **Eval** | `tmux: pi05_eval`，libero_spatial，50 trials/task |
| **Pilot TSR** | **95%**（20 episodes，仅 task 5 "top drawer" 失败 1 次） |
| **每 episode 耗时** | ~6 秒 |
| **完整 eval 预计耗时** | ~50 分钟（500 episodes） |
| **orbax 修复** | 已 patch `/root/autodl-tmp/openpi/src/openpi/models/model.py`（`metadata.item_metadata` 兼容） |
| **cuda:0 A3 训练** | 未受影响 |

完整 eval 日志在 `/tmp/pi05_eval_full.log`，视频在 `/root/autodl-tmp/pi05_eval_videos_full/`。

---
