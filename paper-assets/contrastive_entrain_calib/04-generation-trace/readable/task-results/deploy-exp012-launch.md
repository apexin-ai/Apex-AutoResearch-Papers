# deploy exp012 launch

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_exp012-launch_20260520T071808_result.json`
- **Structured JSON:** [`4acd447ecf455796d9ab.json`](../../sessions/4a/4acd447ecf455796d9ab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

运行正常。

---

**汇报：**

| 项目 | 状态 |
|------|------|
| Llama-3-8B-Instruct 下载 | 完成（4 shards, 15G, 耗时 ~2h57m） |
| 模型加载验证 | 通过（vocab=128000, 32 layers, hidden=4096） |
| exp-012 | **已启动**，PID 227942，tmux session `exp-012` |
| 日志 | `~/runs/contrastive_entrain_calib/exp-012.log` |
| 数据 | 362 samples, 181 complete pairs |

注意：脚本不支持 `--layers` 参数，已去掉。层选择可能在脚本内部硬编码。

---
