# eval exp 027 qwen3 non thinking

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_exp-027-qwen3-non-thinking_20260518T140417_result.json`
- **Structured JSON:** [`015f32221309c08348e2.json`](../../sessions/01/015f32221309c08348e2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验运行正常。

## 报告

| 项目 | 状态 |
|------|------|
| **Qwen3-14B 模型** | `/root/autodl-tmp/models/Qwen3-14B`，8/8 shards，完整 |
| **脚本路径** | `/root/symb_invariant_consensus/scripts/run_qwen3_14b_nonthinking.sh` |
| **PID** | 38106（tmux session: `exp-027-qwen3-14b-non-thinking`） |
| **vLLM** | 端口 8001，GPU 1（88281/97887 MiB，97% util），已成功启动 |
| **SICA pipeline** | 正在运行，已开始处理 folio_0（1/204） |

**修复记录**: 首次启动因 FlashInfer sampler 不兼容 Blackwell GPU (sm_100+) 失败（`RuntimeError: FlashInfer requires GPUs with sm75 or higher`）。添加 `VLLM_USE_FLASHINFER_SAMPLER=0` 环境变量后成功启动，使用 PyTorch-native sampler 替代。

---
