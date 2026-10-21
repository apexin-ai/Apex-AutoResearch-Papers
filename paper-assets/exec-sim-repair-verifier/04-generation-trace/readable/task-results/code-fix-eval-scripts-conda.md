# code fix eval scripts conda

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-eval-scripts-conda_20260513T230655_result.json`
- **Structured JSON:** [`ff9dc5139f30d308838c.json`](../../sessions/ff/ff9dc5139f30d308838c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

---

### 1. run_eval.sh — 创建并测试通过

- 路径: `/home/sonny/exec-sim-repair-verifier/run_eval.sh`
- 测试输出确认: Python 指向 `/root/miniconda3/bin/python3`, transformers `4.57.6`
- 用法: `./run_eval.sh &lt;gpu_id> &lt;script.py> [args...]`

### 2. Eval 脚本版本确认

| 脚本 | 修改时间 | 状态 |
|------|---------|------|
| `eval_repo_cls.py` | May 14 00:01 | **最终版** — repo-level CLS 评估 |
| `eval_repo_cwm.py` | May 14 01:59 | **最终版** — repo-level CWM 评估 |
| `eval_repo_bootstrap.py` | May 13 17:28 | **当前版** — CLS vs CWM 配对 bootstrap 比较 |
| `eval_verifier.py` | May 12 17:21 | **已标记 DEPRECATED** → `eval_repo_cls.py` |
| `eval_repo_level.py` | May 13 17:28 | **已标记 DEPRECATED** → 拆分为 cls + cwm + bootstrap |
| `eval_cwm_baseline.py` | May 13 00:38 | CWM 生成 baseline，专用工具，保留 |
| 其余 eval_*.py | May 12 | 各有专用功能（majority_voting, pertest_diagnostic, trace_judge, traj_verifier），保留 |

### 3. run_block_corr_pipeline.sh — 已修复

修复内容：
1. **头部加 conda 激活** — `source conda.sh && conda activate base`
2. **GPU 参数化** — `GPU_ID="${1:-2}"`, 用法 `./run_block_corr_pipeline.sh [gpu_id]`
3. **环境打印** — 运行前输出 Python 路径和 transformers 版本
4. **脚本引用确认**:
   - `eval_verifier.py` — 仍存在，pipeline 保留引用（因为参数接口与新版 `eval_repo_cls.py` 不兼容: 不同 data_dir 默认值、`--save_predictions` vs `--pred_output`、无 `--device` 参数）
   - `block_corr_from_predictions.py` — 无新版，当前即最终版

### 4. 修改文件清单

| 文件 | 操作 |
|------|------|
| `run_eval.sh` | 新建 |
| `run_block_corr_pipeline.sh` | 重写（conda 激活 + GPU 参数化） |
| `eval_verifier.py` | 第 2 行加 DEPRECATED 标记 |
| `eval_repo_level.py` | 第 2 行加 DEPRECATED 标记 |

---
