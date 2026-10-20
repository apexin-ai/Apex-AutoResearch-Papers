# paper rank32 ablation update

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_rank32-ablation-update_20260515T194553_result.json`
- **Structured JSON:** [`322dbaff8f762b7d8fe7.json`](../../sessions/32/322dbaff8f762b7d8fe7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。变更总结：

**experiments.tex 更新：**
- §3.7(h) LoRA rank sensitivity：原段落文字改为引用新表格 `tab:rank_ablation`，包含 rank=16 baseline、rank=32 (α=32, ratio=1)、rank=32 (α=64, ratio=2) 三行完整数据（Acc/Fail F1/Pass F1/Δ），并说明 α/r=2 corrected 排除了 scaling factor 混淆变量
- §3.6 seq_length ablation：数字已验证一致（83.52→82.83, -0.69pp），添加了 exp_id 注释
- 所有 exp_id 以 LaTeX 注释标注（`cwm-baseline`, `cwm-rank32-ablation-v2`, `cwm-rank32-alpha64-ablation`, `model-size-scaling-cls8b`, `cls8b-s42-ckpt1000-test-seq2048-ablation`）

**产出：**
- `artifacts/rank_ablation_data.json` 已创建并注册（art_20260515_0557df），包含两组 ablation 的完整数据和 exp_id 溯源
- `review_issues.yaml` R1-C3 状态更新为 done

---
