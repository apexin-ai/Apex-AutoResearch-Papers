# ssh cleanup westd orphans and convert seed100

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_cleanup_westd_orphans_and_convert_seed100_20260522T195310_result.json`
- **Structured JSON:** [`b23179f60f061b6347fa.json`](../../sessions/b2/b23179f60f061b6347fa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报如下：

---

## Part 1: GPU 2,3 清理 — **未执行（需确认）**

PID 132938/132939 **不是孤儿进程**，属于活跃的 seed200 v3 训练会话（tmux session `exp029_seed200_episode_v3`，主进程 PID 129828，启动于 03:03，已运行 ~1 小时）。GPU 2,3 各占用 ~45GB，100% 利用率。Kill 这两个 PID 会终止整个 seed200 训练。**请确认是否要 kill。**

---

## Part 2: seed100 训练模式 — **Healthy**

W&B run ID: `zsrodv2f`，run name: `exp029-seed100-episode-level`

**训练已完成（5/5 steps），进程已退出。**

| Metric | Step 1 | Step 2 | Step 3 | Step 4 | Step 5 |
|--------|--------|--------|--------|--------|--------|
| train/success | 19.5% | 16.4% | **28.1%** | 9.4% | **24.2%** |
| train/pass@8 | 75% | 68.8% | 68.8% | 50% | **81.3%** |
| train/action_is_valid | 0.741 | 0.694 | 0.650 | 0.723 | 0.746 |
| train/response_length | 2017 | 2180 | 2039 | 3945 | 3031 |
| actor/ppo_kl | ~0 | 0.0001 | 0.0003 | 0.0018 | 0.0100 |
| critic/score/mean | 1.95 | 1.64 | 2.81 | 0.94 | 2.42 |

| Val Metric | Initial | Final (step 5) |
|------------|---------|----------------|
| pass@1 | 6.25% | **18.75%** |
| action_is_valid | 0.780 | **0.857** |
| response_length | 4404 | **3769** ↓ |
| reward/mean@32 | 0.625 | **1.875** |
| reward/best@32 | 8.67 | **9.98** |

**判断依据：**
- response_length 稳定（train 2000-3900，val 从 4404 降至 3769），无 inflate
- pass@1 3x 提升（6.25% → 18.75%），action_is_valid 上升
- KL 平稳增长，在控制范围内
- Step 4 有 dip（success 9.4%, pass@8 50%），但 step 5 恢复
- 注意：val 用了 16 episodes（3/16 成功），需要 OOD eval 确认泛化能力

---

## Part 3: HF checkpoint — **完成**

- **HF 路径**: `/root/autodl-tmp/checkpoints/exp029_seed100_step5_hf`
- **Symlink**: `qwen_exp029_seed100_step5_hf` → `exp029_seed100_step5_hf`
- **验证**: 1720.6M params，2 个 safetensors shard (~4.6GB + ~1.8GB)
- FSDP DTensor shards 已合并（2-rank Shard(dim=0) → 完整 tensor）

---
