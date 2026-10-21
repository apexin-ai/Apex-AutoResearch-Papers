# eval plan 002 test eval

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_plan_002_test_eval_20260516T174147_result.json`
- **Structured JSON:** [`d599363ab11ba5980d33.json`](../../sessions/d5/d599363ab11ba5980d33.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已部署完成。

**状态总结：**
- `plan_002_test_rsft_s43` 已在 tmux 会话 `plan_002_test` 中启动
- 脚本正在轮询等待 cuda:1 空闲（当前 10291 MiB，需 < 2000 MiB）
- cuda:1 上的 re-docred dev eval (PID 368368) 已跑约 5 分钟，预计 15-30 分钟内完成
- 一旦 cuda:1 释放，eval 自动启动
- DocRED test set 无标注，产出为 `codalab_submission.json`（需提交 CodaLab 获取分数）

**参数确认：**
- Base model: `/root/autodl-tmp/models/Qwen3-4B` ✓
- Adapter: `/root/autodl-tmp/rsft_output_ced_s43/checkpoint-510` ✓
- D076 统一协议: batch_size=4, max_new_tokens=1024, seed=42, --no-quantize ✓
- CUDA_VISIBLE_DEVICES=1 ✓ (C002)

**监控：**
- 日志: `tail -f /root/autodl-tmp/eval_results/plan_002_test_rsft_s43.log`
- 产出目录: `/root/autodl-tmp/eval_results/plan_002_test_rsft_s43/`

---
