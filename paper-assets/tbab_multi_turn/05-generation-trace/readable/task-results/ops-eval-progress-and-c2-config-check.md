# ops eval progress and c2 config check

**tbab multi turn** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval-progress-and-c2-config-check_20260518T180059_result.json`
- **Structured JSON:** [`c20f95d1ff645c1a1718.json`](../../sessions/c2/c20f95d1ff645c1a1718.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### Eval 进度
| Session | 状态 | 进度 |
|---------|------|------|
| C4_s42 | alive | **66/91**（正在跑第 66 个） |
| C1_s137 | alive | **64/91**（正在跑第 64 个） |

GPU 占用：两个进程分别占 17160 MiB 和 17254 MiB。

### C2/C3 配置 — 均正确

- **C2** (`condition2_position_reset.yaml`): `use_bridge_tokens: false`, `use_position_reset: true` ✓
- **C3** (`condition3_bridge_standard_pos.yaml`): `use_bridge_tokens: true`, `use_position_reset: false` ✓

### C2_s42 训练 — 已崩溃

tmux session `mvp_c2_s42` 已 **dead**。日志显示启动即报错：

```
FileNotFoundError: No such file or directory: 'configs/condition2_position_reset.yaml'
```

原因：训练脚本用了**相对路径** `configs/condition2_position_reset.yaml`，而 `cwd` 不在 `/root/tbab_multi_turn/scripts/`。需要改为绝对路径或确保启动命令先 `cd /root/tbab_multi_turn/scripts/` 再运行。

---
