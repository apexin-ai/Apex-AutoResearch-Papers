# code analysis pipeline

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_analysis-pipeline_20260515T120937_result.json`
- **Structured JSON:** [`c43359597afeeec6739b.json`](../../sessions/c4/c43359597afeeec6739b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本 `/root/vla-ssd/scripts/analyze_mvp.py` 已就绪，dry-run 验证通过。

**输出文件**（全部正常生成）：
- `layer_rho_profile.pdf/png` — 三条线（trained/untrained/DINO），标注 best layer
- `per_task_analysis.pdf/png` — per-task ρ 对比柱状图
- `verdict.json` — 完整 summary（best_layer, best_rho, delta_rho, CI, 各判定条件, verdict）
- Console 打印三分支判定表

**Probe 训练完成后运行**：
```bash
python scripts/analyze_mvp.py \
  --trained_dir results/trained/temporal_distance/ \
  --untrained_dir results/untrained/temporal_distance/ \
  --output_dir results/mvp_analysis/
```

---
