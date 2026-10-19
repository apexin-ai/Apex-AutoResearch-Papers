# ops fix longbench data resubmit

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix-longbench-data-resubmit_20260516T131704_result.json`
- **Structured JSON:** [`38a0e5d24bc5ca9f6c42.json`](../../sessions/38/38a0e5d24bc5ca9f6c42.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都已成功进入 lm-eval 评估阶段，数据加载正常，无报错。

## 总结

| 项目 | 结果 |
|------|------|
| **数据下载** | 4 个子集全部成功：narrativeqa(200), qasper(200), gov_report(200), multi_news(200) |
| **根因** | lm_eval 用 `Xnhyacinth/LongBench`（非 THUDM/LongBench），旧版 THUDM 依赖已废弃的 dataset scripts |
| **旧实验 registry** | longbench_kl30_uniform、longbench_dense 已标记 DONE/failed |
| **longbench_kl30_uniform_v2** | cuda:0, PID=234888, 已进入 eval（sparsity 30% uniform, model-level=0.300） |
| **longbench_dense_v2** | cuda:1, PID=235029, 已进入 eval（dense baseline） |

---
