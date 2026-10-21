# diagnose w27 failed exps

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_w27_failed_exps_20260527T134733_result.json`
- **Structured JSON:** [`c7e35c0ff1bd0e48cbdf.json`](../../sessions/c7/c7e35c0ff1bd0e48cbdf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**两个实验都已正常完成，不是失败。** 监控系统误报，可能因为日志文件路径不在标准的 `~/runs/` 或 `logs/` 目录，而是写到了项目根目录。

### 服务器状态
- **正常运行**，GPU 空闲（2x RTX PRO 6000 Black 98GB），无进程占用
- **磁盘** 81% (203G/250G)，48G 剩余，未满
- **dmesg** 无权限读取，但无 OOM 迹象（两实验均正常跑完全部 10 个 task）
- 3 个 tmux session 存在（pi05_attn_k075_long, pi05_attn_k07_long_rerun, pi05_l2norm_k07_long_rerun），均为其他实验

### 实验结果

| 实验 | 方法 | Keep | Suite | SR | 完成时间 | 耗时 |
|------|------|------|-------|----|----------|------|
| `eval_pi05_random_k085_long_seed42_strict_w27` | Random | 0.85 | libero_10 | **44.0%** | 21:33 | 169.8min |
| `eval_pi05_l2norm_k075_long_seed42_strict_w27` | L2Norm | 0.75 | libero_10 | **70.8%** | 21:34 | 139.8min |

结果 JSON 已保存到 `eval_results/` 目录。

### 误报原因
日志写到了 `/root/autodl-tmp/importance_margin_vla_compress/eval_pi05_*.log`（项目根目录），而非标准的 `~/runs/importance_margin_vla_compress/` 路径。监控系统可能在 `~/runs/` 下找不到对应日志文件，判定为空/不可读。

### GPU 可用性
两个 GPU 现在都空闲，可以立即部署新实验。

---
