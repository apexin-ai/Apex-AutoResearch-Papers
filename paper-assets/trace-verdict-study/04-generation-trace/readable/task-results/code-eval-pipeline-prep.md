# code eval pipeline prep

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_eval_pipeline_prep_20260514T223755_result.json`
- **Structured JSON:** [`c517a5e22d1fc6616f61.json`](../../sessions/c5/c517a5e22d1fc6616f61.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。`/root/trace-verdict-study/eval/bootstrap_compare.py` 已创建并通过 dry-run 验证。

**脚本功能**：
- **3 种模式**：`--dry-run`（验证路径/依赖）、`--run-inference`（跑推理+对比）、`--predictions-dir`（加载已有预测）
- **逐样本对齐的 paired bootstrap**：N=10000, seed=42，计算 3 对条件间 accuracy 差异的 95% CI
- **自动 MVP 判定**：按 D001 标准输出 PASS / WEAK PASS / FAIL
- **per-condition 指标**：accuracy, precision, recall, F1, majority baseline, lift
- **输出**：可读表格 + JSON（`results/bootstrap_compare.json`）
- `--save-predictions` 可保存逐样本预测供复用

**Dry-run 结果**：3 个条件的 checkpoint (LoRA final) 和测试数据均就绪，依赖完整（torch 2.10 + CUDA + peft 0.19）。

**下一步**：用 `--run-inference --save-predictions /root/trace-verdict-study/results/predictions/` 执行全量评估（3×1190 样本推理，约需 15-30 分钟）。

---
