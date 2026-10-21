# infra c4 ood data prep

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_c4_ood_data_prep_20260517T215246_result.json`
- **Structured JSON:** [`6d379a43c4d1be48d46c.json`](../../sessions/6d/6d379a43c4d1be48d46c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/c4_ood_prep_status.md`。

**核心结论**：

1. **westd-34887**: C4 数据完备 (~783M Arrow 格式)，评估脚本齐全，已有 50% sparsity 的完整对比结果 (Dense 9.21 / KL 18.40 / TEAL 38.75)
2. **westd-41718**: 有原始 json.gz (419M hub cache) 但缺少代码直接读取的 `/root/autodl-tmp/data/c4_val/` Arrow 目录；30% sparsity 的 eval 已启动但 metrics 为空
3. **代码支持**: `benchmark_eval.py` 已支持 `--tasks c4`，另有两个专用脚本 `eval_c4_ood.py` / `eval_c4_predictor.py`
4. **待做**: westd-41718 需从 34887 rsync 或从本地 cache 构建 Arrow 目录，约 1 分钟即可完成

---
