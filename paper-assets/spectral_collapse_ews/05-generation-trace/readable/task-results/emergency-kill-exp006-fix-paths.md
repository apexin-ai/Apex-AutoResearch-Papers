# emergency kill exp006 fix paths

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_emergency_kill-exp006-fix-paths_20260517T174938_result.json`
- **Structured JSON:** [`349a809ce0fff1ecb456.json`](../../sessions/34/349a809ce0fff1ecb456.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

路径确认正确。

---

## 汇报

| # | 项目 | 结果 |
|---|------|------|
| 1 | **exp_006 kill** | PID 133199 (shell) + 133204 (python) 均已 kill，cuda:0 已释放 |
| 2 | **备份** | results JSON → `phase1_adaptive_k20_seed42_results.json.bak`；checkpoints → `adaptive_k20_seed42_backup/` |
| 3 | **代码修改** | `run_phase1.py` 三处路径 (`ckpt_dir`, `results_filename`, `summary_path`) 改为使用 `run_tag`。adaptive 条件下格式 `{condition}_k{k}_seed{seed}`，其他条件保持原 `{condition}_seed{seed}` |
| 4 | **exp_005 完好性** | PID 116947 存活（运行 277min），Results JSON 含 Gen 0-3，Checkpoints gen_0~gen_3 完整，正在处理 Gen 4 |
| 5 | **exp_006 重启** | 新 PID **134913**，checkpoint 路径 `adaptive_k10_seed42`，results 路径 `phase1_adaptive_k10_seed42_results.json`，已开始 Gen 0 评估 |

---
