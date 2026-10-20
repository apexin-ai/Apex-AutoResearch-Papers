# ops kill r3 fix rsft submit r4

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill_r3_fix_rsft_submit_r4_20260516T175811_result.json`
- **Structured JSON:** [`4d1646fd95f10e43ef29.json`](../../sessions/4d/4d1646fd95f10e43ef29.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成，eval r4 正常运行中。关键确认：

1. **Kill r3 (368368)** — 已终止 ✓
2. **额外 kill 旧 eval (370325)** — 参数反的旧进程，已终止 ✓
3. **脚本修复** — `run_plan002_test.sh` 的 model_path/sft_adapter 已修正 ✓
4. **cuda:1 释放 → 0 MiB** — C001 满足 ✓
5. **r4 已提交** — PID 370795 在 cuda:1 运行，10396 MiB ✓
6. **模型加载正确**：
   - Base model: `Qwen3-4B`
   - SFT adapter merged: `/root/autodl-tmp/sft_output`
   - RSFT LoRA loaded: `/root/autodl-tmp/rsft_output_ced_s43/checkpoint-510`
7. **推理进行中** — 500 docs, 7473 triples, 124 batches, 已开始推理
8. **Registry** — RUNNING, hypothesis/plan_id/parent 全部设置 ✓

---
