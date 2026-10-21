# deploy exp 073 qwen7b logiqa200 seed456

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_exp-073-qwen7b-logiqa200-seed456_20260519T154156_result.json`
- **Structured JSON:** [`8f0def703f1517d53b52.json`](../../sessions/8f/8f0def703f1517d53b52.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。汇报：

**exp-073-qwen7b-logiqa200-seed456 已在 westd-25068 cuda:0 上运行**

| 项目 | 状态 |
|------|------|
| vLLM | 端口 8000 运行中（tmux: `exp073_vllm`），需 `VLLM_USE_FLASHINFER_SAMPLER=0 --enforce-eager`（Blackwell GPU FlashInfer 兼容性问题） |
| 实验 | tmux: `exp073_run`，正常推理中 |
| 输出 | `results/exp073_qwen7b_logiqa200_seed456/exp073_results.json` |
| 日志 | `results/exp073_qwen7b_logiqa200_seed456/exp073_run.log` |
| Registry | RUNNING，provenance 已更新 |

Dry-run 1 题验证通过（SICA=D ✓, SC=D ✓, 耗时 19s/题），200 题预估 ~60 分钟。

---
