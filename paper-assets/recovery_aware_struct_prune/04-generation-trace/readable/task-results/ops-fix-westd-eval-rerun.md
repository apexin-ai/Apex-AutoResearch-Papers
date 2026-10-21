# ops fix westd eval rerun

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix-westd-eval-rerun_20260515T190254_result.json`
- **Structured JSON:** [`31d5f64011105c88152f.json`](../../sessions/31/31d5f64011105c88152f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

执行摘要：

1. **Kill 旧进程** — PID 55353/55286 已终止
2. **eval 脚本修复** — westd `/root/autodl-tmp/` 下的旧版 eval_gsm8k.py（6450B，无 chat template）已用 westb 正确版本（14595B，有 `apply_chat_template`）覆盖
3. **双卡 eval 已启动**：
   - `eval_sft_rasp_20_westd_n100` — PID 58234, cuda:0, 显存 12.5GB/98GB
   - `eval_sft_standard_20_westd_n100` — PID 58356, cuda:1, 显存 8.2GB/98GB
4. **Registry** — 两个实验状态已更新为 RUNNING（retry_count=1），notes 标注"重跑：修复 chat template 不匹配"

模型正在加载中，GPU 利用率会随推理开始上升。预期 N=100 eval 约 1-1.5 小时完成。

---
