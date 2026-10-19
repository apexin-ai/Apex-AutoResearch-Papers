# check multiseed status collect

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_multiseed_status_collect_20260517T105807_result.json`
- **Structured JSON:** [`73db0bb8000016f63d95.json`](../../sessions/73/73db0bb8000016f63d95.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态

| GPU | Config | 状态 |
|-----|--------|------|
| cuda:0 (KL 50%) | **DEAD** | s123 训练完成 (1000/1000)，eval 崩溃 (HF Hub httpx client closed)。`set -e` 导致脚本退出，s456 未开始。GPU 空闲 0 MiB。 |
| cuda:1 (KL 30%) | **RUNNING** | s123 训练中 step 840/1000，约 5-6 分钟完成训练。eval + s456 待运行。 |

## 已完成结果

| Config | Seed | Training | Checkpoint | Eval |
|--------|------|----------|------------|------|
| KL 50% | 123 | done (loss=0.30, sparsity=0.484) | `predictor_kl_normalized.pt` (145MB) | **FAILED** — HF Hub 连接错误 |
| KL 50% | 456 | 未开始 | — | — |
| KL 30% | 123 | step 840/1000 (~84%) | 未保存 | — |
| KL 30% | 456 | 未开始 | — | — |

## KL 30% s123 训练指标 (最近)
- Step 840: loss=0.177, sparsity=0.281, lambda=5000, tau=0.244
- 收敛良好，sparsity 稳定在 ~0.28

## 问题
KL 50% 的 `benchmark_eval.py` 在加载 wikitext2 数据集时 HF Hub httpx 报 `RuntimeError: Cannot send a request, as the client has been closed.`。需要在 cuda:0 上重启 eval + s456 流程。

是否要我现在重启 cuda:0 上的 KL 50% eval 和 s456？

---
