# infra westd 10894 safe cleanup deploy

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_westd-10894-safe-cleanup-deploy_20260521T104359_result.json`
- **Structured JSON:** [`386f58416c5344039ad9.json`](../../sessions/38/386f58416c5344039ad9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。汇报如下：

---

## 状态汇报

### 1. 崩溃实验

| 实验 | 失败原因 | 最后到达 step | 最新可用 checkpoint |
|------|---------|-------------|-------------------|
| **ablation_occ_detach_s0** (原) | `No space left on device` (磁盘满) | step 10001 | 10000_chkpt (15G, 完整) |
| **ablation_random_occ_s0** | `OSError: Incorrect path_or_model_id: '...2500_chkpt'`（vla_path 被旧 rotation 脚本删除） | step ~12501 | **15000_chkpt (819M, 不完整)** — 仅 LoRA adapter，合并失败。12500_chkpt 被本次清理脚本首轮运行时删除。 |

### 2. 存活实验 (3 个)

| 实验 | PID | GPU | 当前 step | vla_path |
|------|-----|-----|----------|----------|
| **ablation_occ_detach_s0** (已被重启) | 515223 | cuda:0 | ~12196 (resume+2196) | `...10000_chkpt` (**已加入保护列表**) |
| **ablation_occ_detach_s1** | 517869 | cuda:2 | ~804 | base model (openvla-7b) |
| **ablation_random_occ_s1** | 519025 | cuda:3 | ~804 | base model (openvla-7b) |

### 3. 保护列表
- `ablation_occ_detach_s0/...--10000_chkpt` (重启实验的 vla_path，**关键保护**)
- `/root/autodl-tmp/models/openvla-7b` (base model)

### 4. 清理循环
- PID: 521309 (tmux session: `safe_cleanup`)
- 每 30 分钟一轮
- 首轮已执行：删除了 random_occ_s0 的 12500_chkpt

### 5. 磁盘
- **清理前**: 111G/250G (45%)
- **清理后**: 97G/250G (39%)
- 释放约 14G

### 6. 需要重启的实验
**ablation_random_occ_s0** (cuda:1 空闲)
- 15000_chkpt 不完整（仅 LoRA adapter，无合并模型），其 LoRA 是基于已删除的 2500_chkpt 训练的，无法独立恢复
- **只能从 base model 重新开始**，损失约 12500 步进度

### 7. ablation_random_occ_s0 的 vla_path
原 vla_path 是 `ablation_random_occ_s0/...--2500_chkpt`（step 2500 的合并模型），**不是 base model**。该文件已被旧 rotation 脚本删除，导致后续 checkpoint 保存时崩溃。

---
