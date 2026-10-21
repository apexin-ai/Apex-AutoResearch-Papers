# fix batch size consistency

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_batch_size_consistency_20260521T084015_result.json`
- **Structured JSON:** [`f9f18310625fdbb53886.json`](../../sessions/f9/f9f18310625fdbb53886.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 已开始加载（2 个进程各 550 MiB，模型加载中）。训练正常启动。

---

## 汇总

### 1. Seed 1/3 四个关键参数

| 参数 | Seed 1 (bjb1) | Seed 3 (westd) |
|------|---------------|----------------|
| train_batch_size (env_groups × group_size) | 16 × 8 = **128** | 16 × 8 = **128** |
| es_manager.train.env_groups | **16** | **16** |
| ppo_mini_batch_size | **16** | **16** |
| ppo_max_token_len_per_gpu | **65536** | **65536** |

### 2. 需要修复的 seed

**仅 Seed 4** 是异类。Seed 1/3/5/6 全部一致。

### 3. Seed 4 修复 diff

| 参数 | 修改前 | 修改后 |
|------|--------|--------|
| `ppo_mini_batch_size` | 8 | **16** |
| `actor.ppo_max_token_len_per_gpu` | 16384 | **65536** |
| `es_manager.train.env_groups` | 8 | **16** |
| `es_manager.train.n_groups` | [8] | **[16]** |

保持不变的约束项：save_freq=5, CUDA_VISIBLE_DEVICES=0,1, optimizer_offload=false, seed train=123/val=456 — 全部已确认。

### 4. 新进程

- **PID**: 302056 (wrapper), 子进程 305501/305502 (GPU worker)
- **状态**: GPU 已开始加载，训练正常初始化
- **服务器**: bjb1-17606, GPU 0,1

### 5. GPU 信息

bjb1-17606: **2× NVIDIA RTX PRO 6000 Blackwell Server Edition, 96GB each** — 与 westd 相同，完全支持 batch_size=128。

---
