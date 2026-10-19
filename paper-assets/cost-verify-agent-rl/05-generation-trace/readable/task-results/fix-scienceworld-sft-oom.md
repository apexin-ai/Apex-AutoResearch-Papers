# fix scienceworld sft oom

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_scienceworld_sft_oom_20260524T225657_result.json`
- **Structured JSON:** [`0ddaa9c2b79b809f0664.json`](../../sessions/0d/0ddaa9c2b79b809f0664.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已正常启动。

**汇报：**
- **修复**：`sft_train_v3.py` 第 87 行加入 `per_device_eval_batch_size=1`（原默认 8 导致 eval 阶段 ~75GB logits OOM）
- **新 PID**：171362，tmux session `scienceworld_sft_bjb1`
- **状态**：模型加载完成，训练已开始（0/450 steps），train 3586 样本，val 1791 样本

---
