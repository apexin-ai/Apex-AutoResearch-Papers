# ops westd disk cleanup phase2

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd_disk_cleanup_phase2_20260520T050829_result.json`
- **Structured JSON:** [`5cae3d18dbb014ecc1d4.json`](../../sessions/5c/5cae3d18dbb014ecc1d4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据收集完毕。汇报三部分结果。

---

## 1. 删除结果

`scienceworld_sft` 已删除。
```
/dev/md0   250G  172G  79G  69%  /root/autodl-tmp
```
可用空间 52GB → **79GB**，释放 ~27GB。

---

## 2. 磁盘审计（/root/autodl-tmp，250GB 总量，172GB 已用）

| 目录 | 大小 | 说明 | 可清理？ |
|------|------|------|----------|
| `checkpoints/8b-cell-c-v9` | **92GB** | v9d 活跃训练 checkpoint | ⛔ 禁删 |
| `cost-verify-agent-rl/` | 21GB | 项目代码+数据 | ⛔ |
| `models/Qwen3-8B` | 16GB | 模型权重 | ⚠️ 看是否还需要 |
| `models/Qwen3-1.7B` | 3.8GB | 模型权重 | ⚠️ 看是否还需要 |
| `alfworld/` | 2.2GB | 环境数据 | ⚠️ 看是否还需要 |
| `fineweb_sample/` | 2.0GB | 数据集 | ⚠️ 看是否还需要 |
| `expert_sft/` | 797MB | SFT 数据 | ⚠️ 看是否还需要 |
| `tmp/` | 837MB | 杂项临时文件 | ✅ 可清理 |
| `wandb/` | 199MB | 实验日志 | ⚠️ |
| `ray_tmp/` | 128MB | Ray 临时 | ✅ 可清理 |
| 空目录 (4个) | 0 | 7b-sft-eval-ood, 7b-zeroshot-eval, 8b-cell-c, gae_baseline | ✅ |

**/root/.cache（根分区）：**

| 目录 | 大小 | 可清理？ |
|------|------|----------|
| `alfworld` | 2.2GB | ⚠️ 可能与 autodl-tmp/alfworld 重复 |
| `pip` | 1.4GB | ✅ `pip cache purge` |

**关键发现：** 172GB 中，92GB (53%) 是 v9 训练 checkpoint，21GB 是项目代码，20GB 是模型权重。这三项占 133GB/172GB (77%)。剩余可清理空间有限，最大潜力是 Qwen3 模型（如果不再需要可释放 ~20GB）。

---

## 3. Checkpoint 轮换逻辑分析

**结论：delete-then-write（安全模式）**

关键代码在 `fsdp_checkpoint_manager.py:180-367`：

```python
def save_checkpoint(self, local_path, ..., max_ckpt_to_keep=None):
    # === STEP 1: 先删旧的 (line 207-214) ===
    if (self.rank == 0
        and max_ckpt_to_keep
        and len(self.previous_saved_paths) >= max_ckpt_to_keep):
        keep_start = len(self.previous_saved_paths) - max_ckpt_to_keep + 1
        self.remove_previous_save_local_path(self.previous_saved_paths[:keep_start])
        self.previous_saved_paths = self.previous_saved_paths[keep_start:]

    # === STEP 2: 写新 checkpoint (line 215-366) ===
    # ... save model, optimizer, tokenizer, etc ...

    # === STEP 3: 记录新路径 (line 367) ===
    self.previous_saved_paths.append(local_path)
```

**执行顺序：** 删除旧 checkpoint → 写入新 checkpoint → 记录路径

**峰值磁盘占用 = `max_ckpt_to_keep × checkpoint_size`**

以 `max_actor_ckpt_to_keep=2`、每个 checkpoint 37GB 为例：
- 保存前：2 个 checkpoint (74GB)
- Step 1 删除最旧的 → 剩 1 个 (37GB)
- Step 2 写入新的 → 恢复 2 个 (74GB)
- 峰值 = 74GB，**不会出现 3×37GB = 111GB 的瞬时峰值**

---
