# code gradient analysis prep

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gradient-analysis-prep_20260527T044244_result.json`
- **Structured JSON:** [`afaa7f7cb269ef70cb20.json`](../../sessions/af/afaa7f7cb269ef70cb20.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/v2_gradient_analysis_prep.md`。

**核心发现**:

- **3/5 条件已有简化版梯度分析结果**（Full OCC BN、Detach BN、Vanilla），核心 pattern 已确认：cosine≈0、conflict≈0.50
- **Full OCC LN v2**: `full_occ_ln_s3_v2` 在 10894 有完整 50K checkpoint，**可立即分析**（等 GPU 释放）
- **Detach LN v2**: 唯一活跃训练 `detach_ln_v2_s0c` 在 10894:cuda2 当前 10K/50K，**约 4h 后可用**
- **两台服务器 8 GPU 全部占满**，梯度分析必须等 GPU 释放

**推荐方案**: 用 `run_gradient_analysis_v2.py`（真实 RLDS 数据，800 samples）对 5 个条件统一重跑。总执行时间 ~100 min 序贯 / ~40 min 并行，每条件 ~20 min。阻塞路径是 Detach LN v2 的 50K checkpoint 完成时间。

---
