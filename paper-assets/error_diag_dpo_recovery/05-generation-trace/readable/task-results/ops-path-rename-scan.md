# ops path rename scan

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_path-rename-scan_20260513T152827_result.json`
- **Structured JSON:** [`99103f75d21c8948092b.json`](../../sessions/99/99103f75d21c8948092b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 产出汇总

### 1. 目录确认
- ~~旧目录~~ `/root/autodl-tmp/rl-active-probe-fl` → 已重命名为 `/root/autodl-tmp/error_diag_dpo_recovery`（执行时发现旧目录仍在，已完成重命名）

### 2. 修改文件清单

| 文件 | 行号 | 原文 | 替换后 |
|------|------|------|--------|
| `src/test_icl_14b.py` | 34 | `ETO_ROOT = "/root/autodl-tmp/rl-active-probe-fl/eto_repo"` | `ETO_ROOT = "/root/autodl-tmp/error_diag_dpo_recovery/eto_repo"` |
| `src/collect_trajectories.py` | 39 | `ETO_ROOT = "/root/autodl-tmp/rl-active-probe-fl/eto_repo"` | `ETO_ROOT = "/root/autodl-tmp/error_diag_dpo_recovery/eto_repo"` |
| `scripts/run_v6_pipeline.sh` | 14 | `PROJECT=/root/autodl-tmp/rl-active-probe-fl` | `PROJECT=/root/autodl-tmp/error_diag_dpo_recovery` |
| `scripts/cap_v9_at_300.sh` | 3-5, 8 | 4 处 `/root/autodl-tmp/rl-active-probe-fl/...` | 全部替换为 `/root/autodl-tmp/error_diag_dpo_recovery/...` |

### 3. 未修改的文件
- `logs/cap_v9.log` — 历史日志，记录已完成的操作，修改无意义
- `src/__pycache__/*.pyc` — 编译缓存，已清除整个 `__pycache__` 目录

### 4. 最终验证
三条 grep 在代码/配置文件中均零匹配，`__pycache__` 已清除。

### 5. 注意事项
- `rl_active_probe_fl`（下划线形式）在代码中未出现，无需处理
- wandb 项目名为 `etadn-dpo`，不含旧名
- 无 `setup.py` / `pyproject.toml` 等包管理文件引用旧名

---
