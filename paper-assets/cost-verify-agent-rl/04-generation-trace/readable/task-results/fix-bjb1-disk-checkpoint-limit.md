# fix bjb1 disk checkpoint limit

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_bjb1_disk_checkpoint_limit_20260521T105849_result.json`
- **Structured JSON:** [`f7494b7ad61ec172d139.json`](../../sessions/f7/f7494b7ad61ec172d139.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 产出汇总

### 1. 磁盘状态
- `/root/autodl-tmp`: 250G 总量，已用 195G，**可用 56GB**（比预估的 73GB 少 17G）

### 2. Checkpoint 分布
| 目录 | 大小 | 说明 |
|------|------|------|
| exp029-seed4/global_step_5 | 21G | Seed 4 v2 当前唯一 ckpt |
| exp029-seed4/global_step_5_hf | 3.8G | HF 格式转换 |
| exp029-seed3/global_step_5 | 21G | Seed 3 |
| exp029/global_step_15 | 21G | Seed 1 最终 |
| qwen3_8b_sft_v1 | 31G | SFT 基座 |
| exp021_ragen_sft_v4 | 23G | 旧 SFT |
| scienceworld_sft | 7.6G | 其他项目 |

### 3. lsof 幽灵空间
无已删文件占用。

### 4. max_actor_ckpt_to_keep
已从 **3 → 2** 修改确认。

### 5. 空间评估
当前 56GB 可用。Seed 4 当前在 step 4，`max_ckpt=2` 意味着最多同时保留 2 个 checkpoint（~42GB）。当前已有 step_5（21G），后续保存 step_10 时会触发清理 step_5，保持 2 个。

**风险点**：56GB 仅够容纳 2 个完整 checkpoint（42G）+ 余量 14G，但写入新 ckpt 时旧 ckpt 还未删除的瞬间可能需要 ~63GB（3 个同时存在）。建议考虑清理以下可释放空间：
- `exp029-seed4/global_step_5_hf`（3.8G）— 如果不需要的话
- `exp021_ragen_sft_v4`（23G）— 如果是旧实验不再需要
- `scienceworld_sft`（7.6G）— 如果是其他项目

---
