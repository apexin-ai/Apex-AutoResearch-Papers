# ops submit 8b candidates r2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_submit_8b_candidates_r2_20260517T015455_result.json`
- **Structured JSON:** [`f0241f8e799c7368d4b0.json`](../../sessions/f0/f0241f8e799c7368d4b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个任务完成。

---

## 任务 1 结果

**plan_006_qwen3_8b_rsft_candidates_r2** 已提交到 cuda:3，PID 400132，18.1GB 显存已载入。
- tmux session: `plan_006_8b_cand_r2`
- 从 idx 2701 resume（已完成 2701/3027 docs）
- output_dir: `/root/autodl-tmp/freige/outputs/rsft_candidates_8b`（已修正，原命令中的路径不存在）
- Registry 已更新为 RUNNING

## 任务 2 结果

**PID 390436** 是正在运行的 eval 推理：
- 实验：`plan_002_test_rsft_s43`
- 模型：`/root/autodl-tmp/rsft_output_ced_s43/checkpoint-510` (Qwen3-4B)
- GPU：cuda:1，占用 11.4GB
- 已运行 ~141 分钟
- split: test, batch_size: 4

---
