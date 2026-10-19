# ops seed3 diagnose fix resubmit

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_seed3-diagnose-fix-resubmit_20260520T181324_result.json`
- **Structured JSON:** [`989f28dd8e312b3d082b.json`](../../sessions/98/989f28dd8e312b3d082b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 1. Seed 3 v2: 仍在运行，未崩溃
- PID 991448 存活（Ss+，已运行 1h05m），Ray worker PID 998725 活跃
- GPU 0,1：100% util，各占 ~47GB VRAM，正在做 `ref_compute_ref_log_prob`
- Log 仅有 raylet 磁盘压力警告（disk > 95%）和 non-numeric metric 警告，**无 crash traceback**
- **不需要重提交**

### 2. 旧 Seed 3 (exp029_seed3_episode): 已失败（旧版，已被 v2 替代）
- Root cause: `AttributeError: 'int' object has no attribute 'get'` at `es_manager.py:44`
- `seed_cfg.get(mode, None)` —— seed 配置是 int 而非 dict

### 3. Cell C v2 (GPU 2,3): 运行中
- GPU 0% util 但内存已分配（~48GB each），推测在 eval batch 间隔
- Log 同样有 raylet 磁盘压力警告

### 4. bjb1 sw_info_loss: 运行中
- 评估进度 84/89 tasks，接近完成

### 5. 磁盘：危急（99%，4.3GB / 250GB）

**占用前 5：**

| 目录 | 大小 | 说明 |
|------|------|------|
| `checkpoints/8b-cell-c-v9/` | **107G** | 旧实验，仅 step 10，非当前运行 |
| `checkpoints/scienceworld-cell-a/` | **62G** | 已完成（step 15），非当前运行 |
| `cost-verify-agent-rl/` | 21G | 活跃代码库 |
| `models/` | 20G | 基础模型 |
| `checkpoints/qwen3_scienceworld_sft/` | 7.6G | Cell C v2 在用，不可删 |

`fineweb_sample/`(2G) + `expert_sft/`(800M) + `ray_tmp/`(526M) + `tmp/`(853M) + `wandb/`(210M) = **~4.4G**，杯水车薪。

### 需要你批准

**8b-cell-c-v9 (107G)** 和 **scienceworld-cell-a (62G)** 均为已完成旧实验的 checkpoint，不被任何运行中的实验使用。删除后磁盘从 99% 降至 ~32%。但两者都超过 50GB 安全清理阈值，需要你确认：

1. 删除 `8b-cell-c-v9/`（107G）？
2. 删除 `scienceworld-cell-a/`（62G）？

当前两个 westd 实验（Seed 3 v2 + Cell C v2）都面临 Ray spilling 失败的风险，随时可能因磁盘满而崩溃。

---
