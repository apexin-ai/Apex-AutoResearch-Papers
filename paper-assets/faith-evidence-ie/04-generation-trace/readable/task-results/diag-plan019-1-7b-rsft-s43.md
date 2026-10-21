# diag plan019 1 7b rsft s43

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_plan019_1_7b_rsft_s43_20260519T033008_result.json`
- **Structured JSON:** [`6b5605de8c1b819c6411.json`](../../sessions/6b/6b5605de8c1b819c6411.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断结果：

**三个实验都不是真正失败，是监控误判。**

| 实验 | 监控判定 | 实际状态 |
|------|---------|---------|
| s43 训练 | failed | **已完成** 567/567 steps, loss=0.55, acc=0.87 |
| s44 训练 | miss 1/5 | **已完成** 567/567 steps, loss=0.55, acc=0.87 |
| d112 CED scoring | failed | **仍在运行** 3500/24216, 预计 ~12:33 完成 |

**共同根因**：
1. 服务器无 `WANDB_API_KEY` → `report_to="none"` → 监控检测不到 W&B run
2. `rsft_trainer.py` 无 sentinel 文件写入逻辑 → 监控检测不到完成标记
3. 训练脚本无 `tee` 重定向 → tmux session 消失后日志丢失

**结论**: s43 和 s44 的 adapter 已完整保存，可直接用于下游 eval。d112 CED scoring 正常推进中，无需干预。

报告已写入 `artifacts/diag_plan019_1_7b_rsft_s43.md`。

---
