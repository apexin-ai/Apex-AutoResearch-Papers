# train scienceworld sft bjb1

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_scienceworld_sft_bjb1_20260524T220948_result.json`
- **Structured JSON:** [`516ddbe1452f4bdaa3ea.json`](../../sessions/51/516ddbe1452f4bdaa3ea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正常启动，正在 tokenize 数据集（33% 进度）。

**汇报：**

- Checkpoint 不存在，已启动新 SFT 训练
- 实验 ID: `scienceworld_sft_bjb1`，状态: RUNNING
- 配置：Qwen3-1.7B → ScienceWorld 3586 条 expert trajectories，单 GPU (cuda:0)，LR=5e-6 cosine，2 epochs，effective batch 16，max_seq_len=16384，每 112 步保存（约半 epoch）
- 输出：`/root/autodl-tmp/checkpoints/scienceworld_sft_bjb1/final/`
- ~448 训练步，预计 2-4 小时完成（取决于序列长度分布和 packing 效率）

---
