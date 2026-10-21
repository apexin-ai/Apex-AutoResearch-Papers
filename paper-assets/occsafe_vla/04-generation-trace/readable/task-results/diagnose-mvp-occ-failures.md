# diagnose mvp occ failures

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_mvp_occ_failures_20260520T164454_result.json`
- **Structured JSON:** [`e01c969348793cceebca.json`](../../sessions/e0/e01c969348793cceebca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 诊断报告

### 1. occ_s0 / s1 / s2（westd-34685）— **未失败，正在运行**

Cron 报告是**误报**。三个进程全部存活：

| 实验 | 当前 step | GPU | 显存占用 | GPU-Util |
|------|-----------|-----|----------|----------|
| occ_s0 | 584 / 50005 | GPU 0 (RTX PRO 6000 Blackwell 98GB) | 62GB | 99% |
| occ_s1 | 547 / 50005 | GPU 1 | 62GB | 99% |
| occ_s2 | 521 / 50005 | GPU 2 | 62GB | 99% |

- 训练于 `2026-05-21 00:35` 启动，运行约 10 分钟时被 cron 检查
- 日志无任何 error/traceback，step 500 时打印了正常 loss：`occ_loss=0.027~0.030, action_loss=0.22~0.30`
- Checkpoint 目录只有 `dataset_statistics.json`，尚未到达第一次 checkpoint 保存点
- **Cron 误判原因**：WANDB_MODE=disabled 导致无 W&B metrics，训练时间短没有产生 sentinel 文件 → cron 判定 "dead"
- 磁盘：329GB 可用，充足

### 2. vanilla_s2（westd-10894）— **真正失败**

**Root cause：磁盘满**

```
safetensors_rust.SafetensorError: Error while serializing: 
I/O error: No space left on device (os error 28)
```

- 训练到 step 25000 时触发 checkpoint 保存，保存 merged model（~15GB safetensors）时磁盘空间耗尽
- Crash 时间：`2026-05-21 00:20:42`
- 25000 checkpoint 目录已有 15GB 部分文件（4 个 safetensors shard + lora_adapter + action_head/proprio_projector checkpoints）
- 当前磁盘：250GB 总量，81GB 已用，170GB 可用（crash 后可能有清理）

### 3. occ_index.json 格式

**已经是正确的 `demos` dict 格式**，不是 ROADMAP 中标注的 `demo_ids` list bug：

```json
{
  "task_name": {
    "file": "/root/occsafe_vla/occ_data/xxx.hdf5",
    "demos": {
      "demo_0": 98,
      "demo_1": 84,
      ...
    }
  }
}
```

9 个 task，55370 帧已成功预加载。ROADMAP 的 "CRITICAL BUG" 标注已过时或已修复。

### 4. 建议修复方案

| 问题 | 方案 |
|------|------|
| occ_s0/s1/s2 cron 误报 | 无需修复训练本身；更新 cron 监控逻辑以支持 WANDB_MODE=disabled 场景（检查进程存活而非 W&B 数据） |
| vanilla_s2 磁盘满 | 清理 westd-10894 旧 checkpoint 后重新启动；或从已保存的 25000 checkpoint 恢复训练（文件可能不完整需验证） |
| ROADMAP "CRITICAL BUG" 标注 | 可以移除或标记为已修复 — occ_index.json 当前格式正确 |

---
