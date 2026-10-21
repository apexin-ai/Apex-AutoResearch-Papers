# diagnose ssh failure westd45947

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_ssh_failure_westd45947_20260525T042100_result.json`
- **Structured JSON:** [`d424e50b5aed6f45c1ba.json`](../../sessions/d4/d424e50b5aed6f45c1ba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### SSH 连接状态
- **westd-45947**: ❌ 连接失败 — `Unable to connect to port 45947 on 36.103.198.204`
- **westd-35807**: ❌ 同样不可达（同一 IP `36.103.198.204`，不同端口）
- **原因**: SeetaCloud (connect.westd.seetacloud.com) 实例关机或端口变更。两台实例共用同一 HostName，说明是同一提供商，可能是账户级别的网络问题或实例过期。

### 训练完成状态：**大概率已完成，但无法确认**

| 实验 | 启动时间 | 墙钟时间 | GPU 时间 | 目标 |
|------|---------|---------|---------|------|
| s0 (seed 0, cuda:0) | 05-24 11:25 | 16.9h (60,860s) | 16.91h | 30K steps |
| s1 (seed 1, cuda:1) | 05-24 11:25 | 16.9h (60,865s) | 16.91h | 30K steps |

**推算**: 根据 M034 记录，LoRA baseline 无 Phase 2 解冻，全程 ~1.3s/step，30K steps 理论需 ~10.8h。17h 墙钟时间 > 理论完成时间，训练极可能已跑完 30K steps。但因 `WANDB_MODE=offline`，无远程指标可验证。

### 失败根因
不是训练失败，是**监控基础设施断连**：
1. 实例在训练期间或训练完成后 SSH 端口变更/实例关机
2. Cron 5 次 SSH 重试均失败 → 标记 `conclusion: failed`
3. 已有 cron hook 更新了 registry notes 说明此情况

### 建议恢复方案

1. **去 SeetaCloud 控制台** 检查两台实例状态：
   - 如果关机 → 开机后获取新端口 → 更新 `~/.ssh/config`
   - 如果已到期/释放 → 数据可能丢失

2. **SSH 恢复后立即执行**：
   ```bash
   # 检查训练日志确认完成
   tail -20 /root/runs/diff_collision_sdf/train_pi05_lora_baseline_s0.log
   tail -20 /root/runs/diff_collision_sdf/train_pi05_lora_baseline_s1.log
   # 检查 checkpoint
   find /root/colliforce-vla/checkpoints -name "*lora_baseline*" -type d
   ```

3. 如果训练确认完成 → 更新 registry `conclusion` 为 `success` → 进入 eval 流程

---
