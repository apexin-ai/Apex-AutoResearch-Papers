# ops gpu check urgent

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-check-urgent_20260516T065842_result.json`
- **Structured JSON:** [`b860465ebb5eccb98129.json`](../../sessions/b8/b860465ebb5eccb98129.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态
| GPU | VRAM | Util | 进程 |
|-----|------|------|------|
| cuda:0 | 0/97887 MiB | 0% | **空闲** — bench_dense 已完成 |
| cuda:1 | 37017/97887 MiB | 0% | eval_bce_v3_s42 Phase 2 运行中 (PID 211882) |

## bench_dense
状态: **completed** (EXIT_CODE=0)

| Metric | Value |
|--------|-------|
| wikitext2_ppl | 6.1173 |
| arc_challenge (acc/acc_norm) | 0.5478 / 0.5828 |
| winogrande | 0.7806 |
| mmlu | 0.6527 |
| gsm8k | 0.4875 |

Registry: 已更新 (metrics + conclusion=success, 已是 DONE 状态)

## d030_kl40_uniform
状态: **failed** — 启动即崩溃，wandb API key 未配置
```
wandb.errors.UsageError: No API key configured. Use `wandb login` to log in.
```
Registry: 未注册（从未成功启动），无 cron。**cuda:0 现在空闲可用。**

## eval_bce_v3_s42
状态: **running** — Phase 2 (benchmark_eval.py downstream)

Phase 1 已完成:
| Metric | Value |
|--------|-------|
| dense_ppl | 6.12 |
| predictor_hard_mask_ppl | 22.51 |
| teal_sparse_ppl | 27.97 |

Phase 2 正在处理 MMLU 子任务（使用 HF 缓存，网络不可达但缓存 OK）。预计 ~20-30 min 完成。

Registry: RUNNING（保持不变）

## 待跑实验列表
- **PREPARING**: 7 个实验，全部 conclusion=killed，无可提交实验
- **QUEUED**: 0 个

**可用资源**: cuda:0 空闲，可立即提交新实验。d030_kl40_uniform 需要先 `wandb login` 后才能重跑。

---
