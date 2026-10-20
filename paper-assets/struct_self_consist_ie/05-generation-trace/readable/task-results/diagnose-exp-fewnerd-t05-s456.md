# diagnose exp fewnerd t05 s456

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_fewnerd_t05_s456_20260521T053321_result.json`
- **Structured JSON:** [`7d063f4e92cc2d5d5c23.json`](../../sessions/7d/7d063f4e92cc2d5d5c23.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论：实验已成功完成，非真正失败

### 根因
**误报（False Alarm）** — Cron 监控系统检测不到 sentinel 文件和 W&B run，将进程正常退出误判为失败。

### 关键证据

1. **日志显示 100% 完成**：37648/37648 实例全部处理，耗时 18m25s，vLLM 引擎正常 shutdown：
   ```
   Processed prompts: 100%|██████████| 37648/37648 [18:25<00:00, 34.06it/s]
   Sampling complete. Saved to output/fewnerd_t05_s456/samples.jsonl
   Report saved to output/fewnerd_t05_s456/report.json
   (EngineCore pid=307107) INFO 05-21 13:22:23 Shutdown complete
   ```

2. **产出完整**：
   - `samples.jsonl` — 714MB（37648 条 × 8 samples）
   - `report.json` — 完整的实验报告

3. **无 sentinel 文件**：输出目录中没有 `.sentinel` / `.done` / `DONE` 等标记文件。脚本本身不生成 sentinel，Cron 监控因此判定失败。

4. **无 W&B 集成**：运行命令中没有 W&B 相关参数，Cron 的 W&B 检测也为空。

### 实验结果摘要
| 指标 | 值 |
|------|-----|
| Greedy F1 | 0.7889 |
| Oracle F1 | 0.8579 |
| Oracle headroom | +0.0690 |
| Fleiss' κ (mean) | 0.6237 |
| Soft Jaccard (mean) | 0.8643 |
| Structural > Surface | YES (+0.0544) |
| Logprob AUROC (full) | 0.6988 |
| Verdict | **MARGINAL** |

### 建议
- **无需重跑** — 数据完整，结果可用
- **修复监控**：`run_mvp_pilot.py` 应在完成后写一个 sentinel 文件（如 `touch output/.../DONE`），或者 Cron 监控改为检测 `report.json` 的存在作为完成标志
- **磁盘注意**：数据盘 93% 已用（28GB 剩余），后续实验注意清理

---
