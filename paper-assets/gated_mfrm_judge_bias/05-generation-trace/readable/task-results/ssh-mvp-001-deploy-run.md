# ssh mvp 001 deploy run

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_mvp_001_deploy_run_20260521T175859_result.json`
- **Structured JSON:** [`97a4196b539e86967722.json`](../../sessions/97/97a4196b539e86967722.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报如下：

| 步骤 | 结果 |
|------|------|
| **1. SSH 连接** | 正常 |
| **2. 环境信息** | Python 3.12.3 (conda base), numpyro=0.21.0, jax=0.10.1, arviz=1.1.0 |
| **3. 文件部署** | data_gen.py: 87行, evaluate.py: 164行, models.py: 193行, run_mvp.py: 149行 — 均与本地一致 |
| **4. s_j (judge-level confounding)** | **已包含** — 第4/8/33/57/58/63/65行均有 s_j 相关代码，Bug 4 修复已部署 |
| **5. Dry-run** | 通过 — responses shape (5,10,2), true_params 含 6 个 key (theta/b/d/c/e/s), raw average RMSE=0.3911, `DRY-RUN OK` |
| **6. MVP 进程** | 已启动 — PID 9423, nohup 后台运行, 日志写入 `/tmp/mvp_run.log`, 进程存活已确认 |

---
