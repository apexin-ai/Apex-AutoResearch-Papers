# code plan 004 dreeam baseline

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_004_dreeam_baseline_20260515T133326_result.json`
- **Structured JSON:** [`3f6539fcaf8f1540df85.json`](../../sessions/3f/3f6539fcaf8f1540df85.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务提交完成。当前状态：

**Phase A（运行中）**: DREEAM teacher model (RoBERTa-large) fully-supervised 训练
- 正在 epoch 0 结束时做 dev 评估（98/125 batches）
- GPU:2 使用 ~20.7GB/32GB，利用率 79%
- 预计 3-5 小时完成 30 epochs + eval
- 日志: `~/runs/faith-evidence-ie/plan_004_dreeam_baseline.log`

**Phase B（已准备）**: Self-training pipeline 脚本已写好 (`train_student.sh`)
- Step 2: Teacher inference on distant data（~2h）
- Step 3: Student self-training 5 epochs on 101K docs（~9h）
- Step 4: Fine-tune student 10 epochs（~1h）
- Step 5: Final eval with ISF
- `train_distant.json`（417MB, 101K docs）已下载就绪

**关键发现**:
- 论文报告的 Evi-F1=57.34 是 **student model 在 test set** 上的结果（dev 上是 57.55）
- Phase A 的 teacher model 预期 dev Evi-F1 ≈ 54.15
- 完整 pipeline（Phase A + B）总计约 15-17h GPU 时间，超出原始 8h 估计
- Google Drive checkpoint 从 AutoDL 不可达，必须从头训练
- 代码已修补：`AdamW` import 兼容 transformers 4.57.6

Phase A 完成后需要手动提交 Phase B。

---
