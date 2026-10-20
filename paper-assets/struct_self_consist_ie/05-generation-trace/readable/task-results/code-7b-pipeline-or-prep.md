# code 7b pipeline or prep

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_7b-pipeline-or-prep_20260519T204001_result.json`
- **Structured JSON:** [`97392bdee093ebb3c39d.json`](../../sessions/97/97392bdee093ebb3c39d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 7B FewNERD Pipeline 状态

### 当前阶段
**Phase 1: QLoRA Training** — `llamafactory-cli` 运行中

| 指标 | 值 |
|------|----|
| 进度 | 13017/20590 (63%) |
| 速度 | ~2.35 s/step |
| 剩余训练时间 | ~4h 57min |
| Loss | 0.0184 (epoch 3.16, grad_norm 0.31) |
| 训练完成 ETA | ~May 20 09:37 CST |

### 后续阶段（pipeline 自动执行）
Pipeline 脚本 (`run_fewnerd_qwen25_7b_pipeline.sh`) 将自动依次执行：
- **Phase 2**: Export/Merge LoRA (~5-10min)
- **Phase 3**: Inference 3 seeds × N=8 (~30-60min for 7B on FewNERD)
- **Phase 4**: Signal Analysis (per seed)
- **Phase 5**: Entity Construction (per seed)

**整体 pipeline 完成 ETA: ~May 20 10:15-10:45 CST**

### 环境准备状态

| 项目 | 状态 |
|------|------|
| scipy + sklearn | OK |
| 磁盘空间 | 198GB 可用 (44% used) |
| compute_signals.py on server | **不在** — 但 pipeline 内建了 `analyze_fewnerd_results.py` + `wnut17_entity_construction.py` |
| GPU | 2× (CUDA_VISIBLE_DEVICES=2,3) |

### 注意事项
1. Pipeline 内建的 Phase 4/5 使用服务器上的 `analyze_fewnerd_results.py` 和 `wnut17_entity_construction.py`，会输出每个 seed 的 `report.json`、`results.json`、`entity_construction.json`
2. 本地的 `compute_signals.py`、`format_for_scaling.py`、`bootstrap_construction.py` 如需在 pipeline 完成后做**额外汇总**（如跨 seed 聚合、scaling curve 格式化），届时需上传到服务器
3. wnut17 7B 3 seeds 结果已全部就绪可供参考

---
