# diagnose server recovery v2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_server-recovery-v2_20260520T062501_result.json`
- **Structured JSON:** [`d056dc8f20be53321915.json`](../../sessions/d0/d056dc8f20be53321915.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### GPU 状态
4x RTX 5090 全部空闲，0% 利用率，2MiB 显存占用，无运行进程。

### 实验状态

| 实验 | PID | 状态 | 最后进度 | 可恢复？ |
|------|-----|------|----------|----------|
| plan017_14b_rsft_generate | 712685 | **死亡** | 1712/3027 | 需从 0 重跑 |
| llama_sft_s43_train_eval_r2 | 754413 | **死亡** | 训练 100% 完成，eval 1/247 | 需完全重跑 |
| llama_sft_s44_train_eval_r2 | 754497 | **死亡** | 训练 100% 完成，eval 1/247 | 需完全重跑 |

### 数据损失（严重）

重启后**几乎所有训练产出丢失**——目录结构保留但文件内容为空：

- `sft_output_llama_3_1_8b_s43/` — 空（训练已完成，模型已保存但丢失）
- `sft_output_llama_3_1_8b_s44/` — 空（同上）
- `rsft_generations_14b/` — 空（1712 个生成文件全丢）
- `rsft_output_qwen3_8b_k1_s43/`, `s44/` — 空（连 May 18 的旧 checkpoint 也丢了）
- `rsft_output_llama_3_1_8b_k1_s43/`, `s44/` — 空

**唯一幸存**的训练产出：`grpo_bf16_g4/` (adapter 528MB + 2 checkpoints)。基础模型 (39G) 和数据集完整。

磁盘 95% 满（48G/50G），疑似 AutoDL 重启引发文件系统级丢失。

### 恢复方案
- **s43/s44**: 训练本身只需 ~57 分钟/个，但 checkpoint 全丢，无法 resume，需完全重跑训练 + eval
- **14b generate**: `rsft_generate.py` 有 progress.json 断点续传机制，但 progress.json 也丢了，必须从头开始（预估 ~56% 已完成的工作量全部作废）
- 建议先确认 AutoDL 数据盘是否可恢复（联系客服/检查快照），否则以上全部需要重跑

---
