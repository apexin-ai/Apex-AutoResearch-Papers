# analysis walker no dt emb episodes check

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_walker_no_dt_emb_episodes_check_20260526T061722_result.json`
- **Structured JSON:** [`11ba609c4b799443102c.json`](../../sessions/11/11ba609c4b799443102c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 所有 Walker checkpoint 的 episode 数

| 实验 | 类型 | Episodes | 状态 |
|---|---|---|---|
| exp_008d_civo_trigger_s4 | civo_trigger | 112 | 完成 |
| **exp_009c_no_dt_emb_s2** | **no_dt_emb** | **20** | **完成（数据极少）** |
| exp_009d_baseline_walker_s1 | baseline | 116 | 完成 |
| **exp_084_frozen_dt_emb_walker_s0** | **frozen_dt_emb** | **112** | **完成，无进程运行** |
| exp_092_cheetah_no_dt_emb_s1 | no_dt_emb (cheetah) | 112 | 完成 |
| exp_093_cheetah_no_dt_emb_s2 | no_dt_emb (cheetah) | 112 | 完成 |
| exp_097_cheetah_008d_s3 | civo_trigger (cheetah) | 64 | **训练中** (GPU 0) |
| exp_100_walker_008a_s1 | 008a variant (walker) | 56 | **训练中** (GPU 1) |

### 关键发现

1. **no_dt_emb Walker**: 服务器上只有 exp_009c，确认只有 20 episodes。**exp_008f 和 exp_069 不存在于此服务器。** 没有其他 no_dt_emb Walker 可用。

2. **exp_084 frozen**: 已完成训练，112 episodes，与其他完成实验（008d=112, 009d=116）量级一致。无 metrics.jsonl，checkpoint 只含 `agent_state_dict` + `optims_state_dict`，无法直接读取训练步数。但 112 episodes 说明训练充分。

3. **当前 GPU 占用**: 两块 GPU 都在跑实验（exp_097 和 exp_100），如果要重跑 no_dt_emb Walker 需要等这两个完成或另找资源。

### 建议

exp_009c 的 20 episodes 确实不可用于可靠分析。需要**重新训练一个 no_dt_emb Walker 实验**到 112+ episodes。等 exp_097 或 exp_100 完成后腾出 GPU 来跑。

---
