# ops fix westd45947 eval restart

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix-westd45947-eval-restart_20260528T030802_result.json`
- **Structured JSON:** [`ff520d977b7d86c371a6.json`](../../sessions/ff/ff520d977b7d86c371a6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 eval 进程均成功启动并开始评估：

- **eseed123** (GPU 0, 8642 MiB): Task 0 开始 — `pick up the orange juice`
- **eseed256** (GPU 1, 8442 MiB): Task 0 开始 — `pick up the orange juice`

模型加载、LoRA 注入、checkpoint 读取全部通过，没有报错。

**总结**：
1. 从 westd-35807 同步了 `a1_sdf_pi05_object_pudding_seed0_l1/30000/` checkpoint（7.2GB）到 westd-45947
2. 修复了 scp 造成的嵌套目录问题
3. 通过 tmux 重启了两个 eval 进程，均正常运行中

注意：westd-45947 数据盘已 99% 满（3.4GB 剩余），后续如需更多空间可考虑清理 `_seed2_l01_OLD`（7.1GB）。

---
