# gpu exp 068 qwen3 logiqa200

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_exp-068-qwen3-logiqa200_20260519T110514_result.json`
- **Structured JSON:** [`5e001dcb5db209510cd8.json`](../../sessions/5e/5e001dcb5db209510cd8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全量运行正常进行中。

**exp-068 部署完成：**

| 项目 | 详情 |
|------|------|
| 服务器 | westd-16639, cuda:1, port 8001 |
| 模型 | Qwen3-14B (non-thinking, `--default-chat-template-kwargs`) |
| 脚本 | `run_logiqa.py`（非 `run_full_mvp.py`，后者无 `--logiqa-data` 参数） |
| 数据 | `logiqa_200.json`, 200 题 |
| Dry-run | 3/3 全对, SICA=SC=100%, ~50s/题，无 thinking tokens |
| tmux | `exp068_vllm` (vLLM), `exp068_run` (实验) |
| 预计时间 | ~200×50s ≈ 2.8 小时 |
| Registry | exp-068-qwen3-logiqa200, status=RUNNING |

---
