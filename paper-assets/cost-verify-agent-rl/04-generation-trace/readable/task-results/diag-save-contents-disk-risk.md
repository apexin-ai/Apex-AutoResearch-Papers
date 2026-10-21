# diag save contents disk risk

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_save_contents_disk_risk_20260521T083854_result.json`
- **Structured JSON:** [`247c091e9fe1eb604956.json`](../../sessions/24/247c091e9fe1eb604956.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据收集完毕。汇总报告如下：

---

## 磁盘风险评估报告

### 1. save_contents 配置

| Seed | YAML 中显式设置 | 解析后实际值 | save_freq | max_ckpt_to_keep |
|------|----------------|-------------|-----------|------------------|
| Seed 4 (bjb1) | 未设置 | `[model, optimizer]` (verl 默认) | 5 | **3** |
| Seed 5 (westd) | 未设置 | `[model, optimizer]` (verl 默认) | 5 | 10 |
| Seed 6 (westd) | 未设置 | `[model, optimizer]` (verl 默认) | 5 | 10 |

三个 seed **都没有显式设置 `save_contents`**。verl 默认值为 `["model", "optimizer", "extra"]`，hydra 解析后为 `[model, optimizer]`。**optimizer 包含在内。**

### 2. verl 默认行为

`verl/trainer/config/config.py:36`: `save_contents = ["model", "optimizer", "extra"]`

`hf_model` 不在默认列表中，`global_step_X_hf` 目录是**手动创建**的（bjb1 上的 `global_step_5_hf` 时间戳晚于 checkpoint 4.5 小时），训练过程不会自动生成。

### 3. 每个 checkpoint 实际大小（已验证）

| 组件 | 大小 |
|------|------|
| model (2 ranks × 3.8GB) | 7.6GB |
| optimizer (2 ranks × 6.5GB) | 13.0GB |
| extra + huggingface/tokenizer | ~16MB |
| **合计** | **~21GB** |

### 4. 磁盘风险评估

#### bjb1-17606 (Seed 4) — ✅ 安全

| 项目 | 数值 |
|------|------|
| 可用空间 | 73GB (`/root/autodl-tmp`) |
| 已保存 | step 5 = 21GB + step_5_hf = 3.8GB (手动) |
| 剩余需求 | step 10 + step 15 = 42GB |
| 剩余空间 | 73 - 42 = **31GB 余量** |

#### westd-47453 (Seed 5 + 6) — ❌ 会磁盘满

| 项目 | 数值 |
|------|------|
| 可用空间 | 107GB (`/root/autodl-tmp`) |
| 已保存 | 0 (尚未到 step 5) |
| 总需求 | 2 seeds × 3 checkpoints × 21GB = **126GB** |
| **缺口** | **19GB** |

### 5. 缓解方案

**westd 上可清理的空间：**

| 路径 | 大小 | 说明 |
|------|------|------|
| `/root/autodl-tmp/checkpoints/exp029-seed3/` | **66GB** | 已完成的旧实验（含 step 5/10/15 + 15_hf） |
| `/root/autodl-tmp/checkpoints/scienceworld_sft/` | 7.6GB | 旧 SFT checkpoint |
| 多个空目录 | 0 | gae_baseline, 7b-*, 8b-cell-c 等 |
| `/root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4` | 3.3GB | ⚠️ **禁删** — 三个 seed 的 base model |

**推荐操作**：立即删除 `exp029-seed3/`（66GB），释放后总可用 173GB，满足 126GB 需求并留 47GB 余量。

**时间窗口**：训练尚未到 step 5，但需要在第一个 checkpoint 产生前完成清理。按每步训练时间估算，窗口有限。

是否要执行清理？

---
