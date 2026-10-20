# fix server path rename

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_server_path_rename_20260513T154145_result.json`
- **Structured JSON:** [`756cabb51a4f2f7c2bdd.json`](../../sessions/75/756cabb51a4f2f7c2bdd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`update_registry` 工具不可用，无法执行 checkpoint_path 更新。如需更新，请通过其他方式处理。

---

## 完成报告

### 1. 重命名的目录
| 旧路径 | 新路径 |
|--------|--------|
| `/root/phase-gated-compound-sparse` | `/root/div_cal_verify` |
| `/root/autodl-tmp/phase-gated-compound-sparse` | `/root/autodl-tmp/div_cal_verify` |
| `/root/runs/phase-gated-compound-sparse` | `/root/runs/div_cal_verify` |

### 2. 修复的 symlink
- `results -> /root/autodl-tmp/div_cal_verify/results/`（原指向旧路径）

### 3. 修改过的文件（sed 替换 `phase-gated-compound-sparse` → `div_cal_verify`）
- `run_all_methods.sh`
- `run_phase1.sh`
- `run_phase1b.sh`
- `run_phase2.sh`
- `run_phase3_medium.sh`
- `run_ext_seed123.sh`
- `run_seed123_remaining.sh`
- `run_random50.sh`
- `analyze_phase2.py`
- `prepare_plot_data.py`

### 4. 无需修改
- `env.sh` — 不含旧路径
- `autodl-tmp/div_cal_verify/` 下的文件 — 无旧路径引用

### 5. 无法修改的历史产物
- `~/runs/div_cal_verify/` 下的 `.log` 文件内容中可能包含旧路径的打印输出（历史日志，不影响运行）
- 已完成的 wandb runs 中记录的路径无法修改

### 6. 验证结果
- grep 搜索残留引用：**0 处** ✓
- 所有 `.sh` 脚本可执行权限完好 ✓
- `data_gpt2/` 数据完整 ✓
- `results_phase2/` 结果完整 ✓
- symlink 指向正确 ✓

---
