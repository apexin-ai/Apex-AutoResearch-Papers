# ssh verify cron and fallback

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_verify_cron_and_fallback_20260518T014347_result.json`
- **Structured JSON:** [`5c8c536f0da3392b51b5.json`](../../sessions/5c/5c8c536f0da3392b51b5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总结果：

---

### 产出

| 项目 | 结果 |
|------|------|
| **1. Cron 判定机制** | Cron 监控 tmux session `acib_v73_connector_lora`，日志写入 `/root/runs/action_cond_info_bottleneck/acib_v73_connector_lora.log`。训练 PID 745668 存活即判定 running，wrapper PID 死亡会触发误报（C002 约束）。 |
| **2. Probe dry-run** | `run_v73_probe.sh` 存在且可执行，指向 `checkpoint-20000`；`cross_task_probe.py` 存在（17KB）；checkpoint 格式为 `checkpoint.pt` 单文件。参数与 watch 脚本对齐。 |
| **3. Fallback watch 脚本** | `/root/acib/watch_lora_and_probe.sh` — 监控 PID 745668 退出后检查 `checkpoint-20000/checkpoint.pt`，存在则自动启动 probe，输出到 `/root/autodl-tmp/v73_eval/probe`。 |
| **4. Watch 进程 PID** | **806193**（已确认存活，正在 polling） |
| **5. LoRA 当前 step** | **17900/20000**，1.8 steps/s，预计 ~18 分钟完成 |

---
