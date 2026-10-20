# ops cleanup invalid ablation output

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cleanup-invalid-ablation-output_20260521T205424_result.json`
- **Structured JSON:** [`60ed9bd6b8efc8928114.json`](../../sessions/60/60ed9bd6b8efc8928114.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

### 产出

1. **删除的文件**（7个，目录已清空后自动移除）：
   - `diagnostic_report.json`
   - `ablation_car_comparison.pdf` / `.png`
   - `ablation_tsr_comparison.pdf` / `.png`
   - `diagnostic_matrix.pdf` / `.png`

2. **创建了 `analysis/ablation_diagnostic.py`**，guard 逻辑：
   - `--detach` 和 `--random` 为必需参数
   - 启动时逐个检查所有传入的 JSON 文件是否存在
   - 缺失则立即 `sys.exit` 并打印明确错误信息，禁止 fallback

3. **Guard 验证通过**：传入不存在的路径时正确输出 `ERROR: ablation eval data not found: /nonexistent/file.json`

---
