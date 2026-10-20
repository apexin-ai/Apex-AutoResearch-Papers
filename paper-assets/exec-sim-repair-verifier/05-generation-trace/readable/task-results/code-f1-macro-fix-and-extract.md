# code f1 macro fix and extract

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_f1-macro-fix-and-extract_20260516T162319_result.json`
- **Structured JSON:** [`2dd084027bbdeaa3c92f.json`](../../sessions/2d/2dd084027bbdeaa3c92f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

### Part 1: Eval 脚本修改

| 脚本 | 状态 |
|------|------|
| `eval_repo_verifier.py` | ✅ 新增 `f1_macro` 到 results dict（L250）、`compute_subset_metrics`（L89/L104）、print 输出（L271） |
| `eval_traj_verifier.py` | ✅ 新增 `f1_macro` 到 results dict（L232）、print 输出（L263） |
| `eval_repo_cls.py` | ✅ 已有 `f1_macro`（L268） |
| `eval_repo_cwm.py` | ✅ 已有 `f1_macro`（L281） |
| `eval_unified.py` | 不存在，跳过 |

### Part 2: F1-macro 回溯提取

79/164 个实验有可计算的 f1_macro，已输出到 `artifacts/f1_macro_summary.json`。

数据来源分布：
- `direct:f1_macro` — 45 个
- `avg(pass_f1, fail_f1)` — 21 个
- `avg(resolved_f1, unresolved_f1)` — 7 个
- `direct:test_f1_macro` / `eval_test_f1_macro` — 6 个

85 个实验缺少 F1 数据（多为训练类/调试类实验，无 eval metrics）。

### Part 3: Git commit

服务器 `/home/sonny/exec-sim-repair-verifier/` 无 `.git` 目录，无法在服务器上 commit。修改已直接应用在服务器文件上。如需 git 管理，需要先在服务器上 `git init` 或从本地推送。

---
