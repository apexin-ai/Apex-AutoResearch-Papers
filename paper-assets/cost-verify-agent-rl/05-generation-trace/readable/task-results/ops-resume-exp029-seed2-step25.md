# ops resume exp029 seed2 step25

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_resume-exp029-seed2-step25_20260518T173311_result.json`
- **Structured JSON:** [`899cc7ecce72e9967dba.json`](../../sessions/89/899cc7ecce72e9967dba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

日志确认从 step_15 成功加载了 model、optimizer、rng、lr_scheduler。正在做 val_before_train。

---

## 执行总结

| 项目 | 结果 |
|---|---|
| **h20 残留清理** | hsweep_h20 tmux session 已 kill（PID 57985） |
| **磁盘清理** | 24GB → 103GB（删除 step_5/10/20/25，释放 ~79GB） |
| **step_25 完整性** | **损坏**——optimizer 文件被截断（5.47GB/5.10GB vs 正常 6.88GB），缺少 extra_state/fsdp_config/huggingface。回退到 step_15 |
| **Config 修改** | `max_actor_ckpt_to_keep: 10 → 3` ✓, `resume_mode: auto` ✓, `optimizer_offload: false` ✓ |
| **恢复确认** | 从 **step_15** 恢复（非 step_25）。日志显示成功加载 model/optimizer/rng/lr_scheduler from global_step_15 |
| **环境修复** | 需用 `conda activate base`（非 verl-agent），verl-agent 环境缺少 `omega_conf_to_dataclass` |
| **新 PID** | 66897 |
| **W&B run ID** | `25d60jf4` |
| **Log** | `/root/runs/cost-verify-agent-rl/exp029_seed2_resume_step15.log` |
| **GPU 显存** | GPU 0: 43205MiB, GPU 1: 43173MiB |
| **Registry** | RUNNING, spec 已更新 |
| **Cron 监控** | 每 15 分钟检查一次 |

**关键发现**：step_25 checkpoint 在磁盘满时写入不完整（optimizer 文件截断 + 缺少元数据文件），无法用于恢复。实际从 step_15 恢复，损失 step 15-25 的训练进度（约 10 步）。

---
