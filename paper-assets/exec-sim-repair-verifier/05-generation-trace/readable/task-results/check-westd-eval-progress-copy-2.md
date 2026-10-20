# check westd eval progress

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_westd-eval-progress_20260514T015342_result.json`
- **Structured JSON:** [`99065b8a2f5f639bad6e.json`](../../sessions/99/99065b8a2f5f639bad6e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Eval 状态汇总

| # | Session | GPU | 进度 | Accuracy | 状态 | ETA |
|---|---------|-----|------|----------|------|-----|
| 0 | eval_cwm_seed123 | 88%, 13G/33G | **472/9784** (4.8%) | 57.2% | RUNNING | ~16.8h |
| 1 | eval_cwm_v12 | 88%, 13G/33G | **472/9784** (4.8%) | 59.1% | RUNNING | ~16.8h |
| 2 | eval_cls_v5 | 100%, 18G/33G | **160/9784** (1.6%) | 53.1% | RUNNING (刚启动) | ~27min* |
| 3 | eval_cls_8b | 100%, 21G/33G | **80/9784** (0.8%) | 68.8% | RUNNING (刚启动) | ~40min* |

### 细节

**GPU 0 — CWM seed123**: 稳定运行，每 8 samples ~52s。accuracy 从上次的 56.9% 波动到 57.2%，基本持平。

**GPU 1 — CWM v12**: 同速运行。accuracy 从上次 60.4% 下降到 59.1%，有一定回落趋势。

**GPU 2 — CLS v5**: 重启成功，09:53:25 创建 session，09:53:35 模型加载完毕，已跑到 160 samples。CLS 任务比 CWM 快很多（batch 160 vs 8）。

**GPU 3 — CLS 8b**: 重启成功，同时间创建。8B 模型更大（21G vs 18G），batch 更小（80 vs 160），但 accuracy 68.8% 目前最高。

*CLS 的 ETA 只有 1 个数据点，估算很粗糙。CWM 两个 eval 预计明天凌晨 ~2:00 完成。

---
