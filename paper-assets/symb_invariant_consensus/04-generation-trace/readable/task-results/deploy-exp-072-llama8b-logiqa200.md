# deploy exp 072 llama8b logiqa200

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_exp-072-llama8b-logiqa200_20260519T152221_result.json`
- **Structured JSON:** [`ea5dcf231ae1415287be.json`](../../sessions/ea/ea5dcf231ae1415287be.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成，汇报：

**exp-072-llama8b-logiqa200 部署状态**

| 项目 | 状态 |
|------|------|
| 服务器 | westd-16639, cuda:1 |
| vLLM | 启动成功，端口 8011，`VLLM_USE_FLASHINFER_SAMPLER=0`（Blackwell GPU FlashInfer 兼容性修复） |
| 实验 | 已在 tmux `exp072_run` 中运行，HTTP 请求全部 200 OK |
| Registry | RUNNING，provenance 已记录 |

**遇到的问题**：vLLM 0.21.0 首次启动因 FlashInfer sampler 不识别 Blackwell (sm_100+) 架构而 crash，设置 `VLLM_USE_FLASHINFER_SAMPLER=0` 后正常启动。

**tmux sessions**：
- `exp072_vllm` — vLLM 服务
- `exp072_run` — 实验主进程

日志位置：`results/exp072_llama8b_logiqa200/exp072_run.log`

---
