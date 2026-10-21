# ssh kill all restart verified

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_kill_all_restart_verified_20260523T202803_result.json`
- **Structured JSON:** [`a08cac8153bb008d2074.json`](../../sessions/a0/a08cac8153bb008d2074.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 7 个 judge 启动完毕，等待 ~4.5 分钟后自动回来验证 throughput。

当前状态汇总：
- **Step 1** ✅ 无旧进程
- **Step 2** ✅ 确认了 config 结构（`rpm` 字段，configs 在 exp001 根目录）
- **Step 3** ✅ RPM 已修改（sonnet=150, gemini/deepseek/qwen3=100）
- **Step 4** ✅ 7 个 collect.py 全部在跑 with `--workers 10`
- **Step 5** ✅ Baseline 已记录
- **vLLM** ✅ 3 个本地模型服务已启动（需要 `VLLM_USE_FLASHINFER_SAMPLER=0` 绕过 Blackwell GPU 的 FlashInfer 兼容性问题）

---
