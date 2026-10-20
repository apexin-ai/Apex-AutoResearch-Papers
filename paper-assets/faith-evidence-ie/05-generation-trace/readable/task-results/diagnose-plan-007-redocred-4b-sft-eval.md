# diagnose plan 007 redocred 4b sft eval

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_plan_007_redocred_4b_sft_eval_20260516T123325_result.json`
- **Structured JSON:** [`1b0928c80a362abac1b2.json`](../../sessions/1b/1b0928c80a362abac1b2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成：

**根因**：Qwen3-4B 基座模型和 SFT adapter 均不存在。
- `/root/autodl-tmp/models/Qwen/Qwen3-4B/` — 未下载（服务器只有 Qwen3-1.7B 和 Qwen3-8B）
- `/root/autodl-tmp/sft_output_qwen3_4b/` — 不存在（4B 未训练过）

inference.py 因本地路径不存在回退到 HF Hub 查找，路径格式不符合 repo_id 规范，触发 `HFValidationError`。

**修复**：需先下载 Qwen3-4B 模型 → 完成 SFT 训练 → 再提交 eval。已更新 registry notes。

---
