# ops d143 pipeline launch

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d143-pipeline-launch_20260519T121904_result.json`
- **Structured JSON:** [`05f44c61e345ab33e605.json`](../../sessions/05/05f44c61e345ab33e605.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Pipeline 已成功启动并正在训练。汇报：

### D143 状态

| 项目 | 状态 |
|------|------|
| **LLaMA 重复进程** | 只有 1 个下载进程 (PID 387234)，无需 kill |
| **训练数据** | `train_500_seed42.jsonl` (484KB, 500 行) — 遵循 C001，未用 `proofwriter_fol_500.jsonl` |
| **评估数据** | `proofwriter_fol_100.jsonl` (97KB, 100 行) — 遵循 C008 |
| **磁盘** | `/root/autodl-tmp` 209G 可用 (17%) |
| **Pipeline 脚本** | `/root/autodl-tmp/d143_proofwriter_pipeline.sh` |
| **tmux session** | `d143` (创建于 20:22:16) |
| **训练 PID** | 387836，GPU:0 占用 82GB/98GB，85% util |
| **首个实验** | `pw_exec_s42` 已开始训练，step 1/500 完成，~7.6s/it，reward=0.25，预计 ~63 min |

### 6 个实验串行顺序
1. `d143_pw_exec_s42` — execution_only, seed=42 ← **正在运行**
2. `d143_pw_exec_s43` — execution_only, seed=43
3. `d143_pw_exec_s44` — execution_only, seed=44
4. `d143_pw_sta_s42` — additive_bonus β=0.3, seed=42
5. `d143_pw_sta_s43` — additive_bonus β=0.3, seed=43
6. `d143_pw_sta_s44` — additive_bonus β=0.3, seed=44

每个实验完成 eval+classify 后自动清理 weights（M008）。每个实验 train ~63min + eval ~15min，预计总时长 ~8h。

---
