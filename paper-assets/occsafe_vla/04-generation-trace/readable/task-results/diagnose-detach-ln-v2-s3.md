# diagnose detach ln v2 s3

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_detach_ln_v2_s3_20260528T034649_result.json`
- **Structured JSON:** [`aef668cfca5076477b76.json`](../../sessions/ae/aef668cfca5076477b76.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**失败根因：**
原始 SIGHUP 崩溃日志已被新的重启尝试覆盖，无法直接确认根因。但综合证据指向 **tmux session 断开或 SSH 会话丢失**：
- 两个实验几乎同时崩溃（SIGHUP = 控制终端挂断信号）
- 不是 OOM（崩溃前正常保存了 40000 checkpoint）
- 不是磁盘满（123GB 可用）
- detach_ln_v2_s2 在同一服务器存活，说明 cuda:2/cuda:3 的实验可能在同一个 tmux session 中运行，而该 session 崩溃了

**关键发现：两个实验实际已跑到 step 40000（远超报告的 17808）。** 服务器时区为 UTC+8，40000 checkpoint 保存时间 11:40-11:42 Beijing = 03:40-03:42 UTC，与报告的崩溃时间吻合。报告的 step 17808/50005 可能是 batch_idx（resume 后从 0 重新计数），实际全局 step 已到 40000。

**当前状态：两个实验的重启尝试也失败了：**
- `full_occ_ln_v2_s3`：`FileNotFoundError: '/root/autodl-tmp/models/openvla-7b/proprio_projector--40000_checkpoint.pt'` — `--vla_path` 指向了 base model 目录而非 40000 checkpoint 目录
- `detach_ln_v2_s3`：日志只有 TF 初始化输出，无训练进程在运行
- **两个实验当前都未在运行**

**可用 checkpoint（两个实验均有完整文件）：**
- 25000, 30000, 35000, **40000**（最新，含 action_head/occ_head/proprio_projector/lora_adapter）

**GPU 状态：** cuda:1/2/3 空闲可用，cuda:0 被 detach_ln_v2_s2 占用

**detach_ln_v2_s2 (cuda:0)：** PID 47162，运行 1h38m，状态正常

**磁盘：** /root/autodl-tmp 123GB 可用（66%），充足

**需要行动：** 用正确的 `--vla_path`（指向各自的 `--40000_chkpt` checkpoint 目录）和 `--resume_step 40000` 重新启动两个实验。

---
