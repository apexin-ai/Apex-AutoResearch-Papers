# ops check all eval progress

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-all-eval-progress_20260515T212327_result.json`
- **Structured JSON:** [`d48f402e58b049f920e9.json`](../../sessions/d4/d48f402e58b049f920e9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验进度汇总

| # | 实验 | GPU | 进度 | 已用时间 | 预估剩余 | 状态 |
|---|------|-----|------|---------|---------|------|
| 1 | eval_plan_001_flat_nli_s43 | cuda:0 (88%, 19.5G) | **53/62 batch (85%)** | 53 min | ~9 min | ✅ 运行中 |
| 2 | plan_011_bf16_g8_step_eval | cuda:1 (77%, 15.8G) | step30 ✅ done, **step50: 27/62 (44%)** | 1h24m | step50 ~33 min + step70 ~60 min | ✅ 运行中 |
| 3 | eval_plan_012_dpo_ced_1ep | cuda:2 (0%, 0G) | — | — | — | ❌ 异常 |
| 4 | eval_plan_008_rsft_topk3 | cuda:3 (74%, 16.5G) | **13/62 batch (21%)** | 14 min | ~48 min | ✅ 运行中 |

### 实验 2 已完成 step 的结果
- **Step 30**: F1=0.4340, Evi-F1=0.8063, EDCR=0.6807, Format OK=99.8%

### 实验 3 异常详情

日志 `eval_plan_012_dpo_ced_1ep.log` 不存在。找到两个相关日志：

- **eval_plan_012_dpo_ced.log** — 已完成（更早的 eval），结果：F1=0.3429, Evi-F1=0.8403, EDCR=0.7294
- **eval_plan_012_dpo_ced_ckpt400.log** — **CUDA OOM 后被 Terminated (exit code 129)**。多个 batch 连续 OOM，进程被杀。cuda:2 当前空闲，无进程在跑。

需要重新启动实验 3 的 ckpt400 eval（可能需要减小 batch size 或指定独立 GPU 避免显存冲突）。

---
