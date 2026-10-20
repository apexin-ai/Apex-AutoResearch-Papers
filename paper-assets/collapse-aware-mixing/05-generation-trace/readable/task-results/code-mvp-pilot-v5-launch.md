# code mvp pilot v5 launch

**collapse aware mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp_pilot_v5_launch_20260512T154556_result.json`
- **Structured JSON:** [`7bdbe6998544eafad021.json`](../../sessions/7b/7bdbe6998544eafad021.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报：

## mvp_pilot_v5 部署结果

| 项目 | 状态 |
|------|------|
| **代码修改** | 4/4 完成 — EarlyStopOnHighLossCallback (threshold=15.0), sdpa, max_grad_norm=1.0, lr=2e-6 |
| **清理** | 完成 — G0/G1/G2 + real_data_cache 已删除 |
| **训练启动** | 运行中 — PID 32154, tmux session `mvp_pilot_v5` |
| **Loss** | **正常** — step 50: 2.6410, step 100: 2.6305, step 150: 2.5777（v4 是 106-116，现在 2.5-2.7） |
| **GPU** | RTX PRO 6000, 22GB 显存占用, 100% 利用率 |
| **EarlyStop** | 未触发（loss 远低于 threshold 15.0） |

lr=2e-6 + max_grad_norm=1.0 修复了 v4 的发散问题。G0 训练 1373 步，预计约 46 分钟完成，之后进入 evaluation + G1。

---
