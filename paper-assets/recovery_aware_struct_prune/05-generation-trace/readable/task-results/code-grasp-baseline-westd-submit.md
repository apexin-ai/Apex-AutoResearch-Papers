# code grasp baseline westd submit

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_grasp-baseline-westd-submit_20260515T134521_result.json`
- **Structured JSON:** [`3836ba44809cbfe92d36.json`](../../sessions/38/3836ba44809cbfe92d36.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 执行结果

**GraSP 剪枝**: 已完成（由前一个 Worker 执行）。模型在 `/root/autodl-tmp/recovery_aware_struct_prune/pruned_graspune_20/`。使用 GRASPrune 库，keep_ratio=0.80, rescale_alpha=0.5, 512 samples, 4 epochs gate training。

**Eval**: 正在 westd GPU 0 上全量跑（1319 样本, PID 34206），已完成 69/1319, 预计还需 ~17.5 小时。

**50 样本 checkpoint 结果**:

| 指标 | GraSP 20% | RASP 20% |
|------|-----------|----------|
| Post-prune accuracy | **8.0%** | **29-31%** |
| EOS rate | 2% | — |
| Avg response length | 4019 (几乎全部截断) | — |

GraSP 剪枝后模型严重退化：98% 的回答没有自然结束（没生成 boxed answer），一直输出到 4096 token 上限。RASP 的优势非常显著（~3.6x）。

**问题**: 全量 eval 还要跑 ~17.5 小时。要不要 kill 掉改用 `--max_samples 100`？100 样本 ~85 分钟就够了，50 样本的趋势已经很明确。

---
