# ops rename project dir

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_rename-project-dir_20260513T154521_result.json`
- **Structured JSON:** [`db24ba75e767a77ab71d.json`](../../sessions/db/db24ba75e767a77ab71d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

这个部署脚本是给旧服务器 cqa1 的，当前服务器是 westd-39279，不需要修改。

服务器端工作已全部完成。汇总：

**已完成的变更：**

| 操作 | 详情 |
|------|------|
| 目录重命名 | `/root/structfuse-context` → `/root/min_necessary_circuit_css` |
| runs 目录重命名 | `/root/runs/structfuse-context` → `/root/runs/min_necessary_circuit_css` |
| 路径替换（14 个 .py 文件） | 所有 `/root/structfuse-context` → `/root/min_necessary_circuit_css` |

**替换的文件列表：**
- `acdc_topk_sweep.py` (6 处)
- `eval_mean_ablation.py` (3 处)
- `eval_topk_faithfulness.py` (2 处)
- `run_circus_fix.py` (1 处)
- `run_phase_d_only.py` (1 处)
- `e2e_validate.py` (1 处)
- `run_qwen_ioi.py` (1 处)
- `diagnose_ifr_perhead.py` (1 处)
- `diagnose_proportional_binarize.py` (1 处)
- `fix_css067_eval.py` (1 处)
- `run_qwen_ioi_acdc.py` (1 处)
- `run_size_controlled_ioi.py` (2 处)
- `run_bootstrap_ci.py` (1 处)
- `_gen_arith_caches.py` (3 处)

**未修改：** `.log` 文件中的历史输出（不影响运行）、`.git/config`（无旧名引用）。

---
