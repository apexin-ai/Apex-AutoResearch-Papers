# ops submit evals gpu3 gpu5

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_submit-evals-gpu3-gpu5_20260515T110317_result.json`
- **Structured JSON:** [`7303656d7d380d544a32.json`](../../sessions/73/7303656d7d380d544a32.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结果报告：**

两个 GPU 都已被另一个 agent 占用：
- **cuda:3** → PID 551219: `3B_d000_s123` aligned eval (8985 MiB, 92%)
- **cuda:5** → PID 551290: `3B_d005_s42` aligned eval (8985 MiB, 92%)

**完整经过：**

1. 初始候选 P1（1.5B d005/d025 s123）→ 失败，checkpoint 仍在训练（PID 549858/549516 在 GPU 0/1 上运行 SFT，adapter_model.safetensors 不存在）

2. 全面扫描 aligned eval 缺口后，发现唯一真正缺少的是 **3B_d005_s42 aligned**（只有 DEPRECATED v1）。其余所有完整 checkpoint 都已有 4 个 benchmark 的 eval_results.json

3. 尝试提交 3B_d005_s42 时发现 registry 中已为 RUNNING 状态——另一个 agent 已先一步提交。我误创建了重复进程（PID 551723），发现后立即 kill，避免 output-dir 数据腐败

4. 另一个 agent 同时还提交了 3B_d000_s123 aligned eval 到 cuda:3

**当前状态：** cuda:3 和 cuda:5 均已被占用，无需额外操作。已清理所有失败/重复的 registry 条目。

---
