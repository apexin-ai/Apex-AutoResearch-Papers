# ops diagnose plan014 and monitor s43

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_diagnose-plan014-and-monitor-s43_20260516T013110_result.json`
- **Structured JSON:** [`e859db80aaf196bb15f8.json`](../../sessions/e8/e859db80aaf196bb15f8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### 任务 A: eval_plan_014_no_evidence 失败原因

**根因**: `inference.py:299` 抛出 `ValueError` — 模型路径 `/root/autodl-tmp/sft_no_evidence_output` 包含 `adapter_config.json`（是 LoRA adapter），但命令未设置 `--sft_adapter`。eval 脚本的逻辑是：发现 LoRA adapter 就要求 `--sft_adapter` 指向 SFT adapter 目录。

**问题本质**: 这个模型本身就是 SFT adapter，不是建在 SFT 之上的 RSFT adapter。eval 脚本没有区分这两种情况。

**修复方案**: 用 base model 作为 `--model_path`，加 `--sft_adapter /root/autodl-tmp/sft_no_evidence_output`，去掉多余的 `--base_model` 参数。或者在 `inference.py` 中增加直接评估 SFT LoRA adapter 的路径。

### 任务 B: rsft_ced_s43_train_r3 状态

- **仍在运行** — PID 277310, 已运行 1h10m
- **进度**: 340/510 步 (67%)，当前正在执行 step-340 的 eval（每 170 步触发一次）
- **GPU 1**: 28.6GB/32.6GB, 36% utilization，正常活跃
- **预估剩余**: eval 完成后还剩 170 步 × ~5.5s/步 ≈ 15 分钟训练 + step-510 的最终 eval

---
