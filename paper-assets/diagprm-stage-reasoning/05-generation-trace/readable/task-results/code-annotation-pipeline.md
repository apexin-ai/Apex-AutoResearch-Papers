# code annotation pipeline

**diagprm stage reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_annotation-pipeline_20260511T145447_result.json`
- **Structured JSON:** [`7dd881dfc305e3d8b41f.json`](../../sessions/7d/7dd881dfc305e3d8b41f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

dry-run 完整跑通。结果：

- **Segmentation kappa**: 0.241 (两个 mock judge 产生不同标签，符合预期)
- **Quality kappa**: -0.111 (mock 随机差异)
- **Partially-good ratio**: 0.800 (体现了早期 sound + 晚期 flawed 的 partially-good 模式)

已写入的 6 个文件：

| 文件 | 功能 |
|------|------|
| `annotation/__init__.py` | 空包文件 |
| `annotation/data_loader.py` | JSONL 加载，自动检测字段名，返回 Trajectory/Step |
| `annotation/stage_segmentation.py` | LLM judge 阶段分割 (localize/diagnose/patch/other) |
| `annotation/quality_assessment.py` | LLM judge 质量评估 (sound/flawed) |
| `annotation/compute_agreement.py` | Cohen's kappa + bootstrap CI + partially-good 比例 |
| `annotation/run_pilot.py` | 主编排：加载→分割→评估→保存→agreement 报告 |

结果文件已保存到 `results/` 目录（segmentation_results.json、quality_results.json、agreement_report.json）。

---
