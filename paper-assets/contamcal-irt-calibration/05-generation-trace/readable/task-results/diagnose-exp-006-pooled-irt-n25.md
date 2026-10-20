# diagnose exp 006 pooled irt n25

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_006_pooled_irt_n25_20260516T134420_result.json`
- **Structured JSON:** [`9d8e40368f550b700970.json`](../../sessions/9d/9d8e40368f550b700970.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。产出已写入 `artifacts/diag_exp006_pooled_irt_n25.md`。

## 结论

| 项目 | 结果 |
|------|------|
| **失败根因** | 误报 — 实验正常完成退出，脚本无 sentinel 文件/W&B，cron 误判为 crashed |
| **实际状态** | 成功：4 chains 采样完成（157s），结果已保存（4 个 JSON 文件） |
| **需关注** | 表头显示 "4PL+γ" 但命令指定 `--model 2pl_gamma`，可能是 print 写死或 model dispatch bug |
| **修复建议** | ① 标记为成功 ② 脚本末尾加 `touch DONE` ③ 核实实际拟合的是 2PL 还是 4PL |
| **PID 764449** | 已死亡（exp_001_eval_3B_instruct_v2 进程已结束） |

---
