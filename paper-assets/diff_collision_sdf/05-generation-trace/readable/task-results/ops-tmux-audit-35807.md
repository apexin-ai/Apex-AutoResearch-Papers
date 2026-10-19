# ops tmux audit 35807

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_tmux_audit_35807_20260527T024719_result.json`
- **Structured JSON:** [`a6440c4e6caa390ed406.json`](../../sessions/a6/a6440c4e6caa390ed406.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 审计报告：westd-35807 tmux timeout

### 1. tmux timeout 配置

**tmux 本身无任何 timeout 设置：**
- 无 `/etc/tmux.conf`
- 无 `~/.tmux.conf`
- `destroy-unattached off`（session 不会因 detach 被销毁）
- `lock-after-time 0`（无锁屏超时）

**timeout 来源不是 tmux，是 `submit_training_job` 注入的 shell `timeout` 命令。**

### 2. 各进程 timeout 风险分析

| GPU | 任务 | 启动方式 | timeout 设置 | 进度 | 已运行 | 预计剩余 | 风险 |
|-----|------|----------|-------------|------|--------|---------|------|
| cuda:0 | ~~spatial_bowl SDF~~ | submit_training_job | `timeout 129600` (36h) | **已完成** EXIT_CODE=0 @ 05-26T22:28Z | — | — | ✅ 无 |
| cuda:0 | eval_stepwise_s1_l1_22k | submit_training_job | `timeout 86400` (24h) | 运行中 | ~20min | eval任务，远不到24h | ✅ 无 |
| cuda:1 | λ=0.1 s0 (object_pudding) | **nohup** | **无 timeout** | 84% (25095/30000) | ~27h34m | ~6h19m | ✅ 无 |
| cuda:2 | λ=0.1 s1 (object_pudding) | **nohup** | **无 timeout** | 82% (24556/30000) | ~26h56m | ~7h01m | ✅ 无 |
| cuda:3 | LoRA baseline spatial_bowl | **手动 tmux + tee** | **无 timeout** | 49% (14833/30000) | ~14h19m | ~19h26m | ✅ 无 |

### 3. 结论

**westd-35807 上无训练面临 timeout 风险。**

- 3 个活跃训练（cuda:1/2/3）均未通过 `submit_training_job` 提交，不含 `timeout` 包装
- cuda:1/2 用 `nohup`，cuda:3 用手动 tmux session `plan015`，都没有时间限制
- 唯一含 timeout 的 spatial_bowl SDF 训练已正常完成（EXIT_CODE=0）
- westd-45947 的 timeout 问题是 `submit_training_job` 的 `timeout_hours` 参数导致的（默认 24h → 注入 `timeout 86400`），与 tmux 配置无关

### 4. 对 westd-45947 事故的根因确认

westd-45947 上 `train_pi05_lora_baseline_s2` 的 EXIT_CODE=124 是 `timeout` 命令的退出码，说明是 `submit_training_job` 注入的 `timeout 86400`（24h）杀死了进程。下次提交预估 >24h 的训练时，需设置更大的 `timeout_hours` 参数，或按 C002 约束改用手动 tmux 启动。

---
