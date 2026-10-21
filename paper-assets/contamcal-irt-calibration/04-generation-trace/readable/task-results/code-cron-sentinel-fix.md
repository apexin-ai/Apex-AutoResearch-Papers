# code cron sentinel fix

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cron-sentinel-fix_20260516T044328_result.json`
- **Structured JSON:** [`c1b55ea05e7585393977.json`](../../sessions/c1/c1b55ea05e7585393977.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All code changes compile and import correctly. Let me now provide the summary.

---

## 变更总结

### 修改的文件

**1. `/home/ubuntu/agent-ml-research/core/tools/cron.py`** — 框架核心
- `register_cron()`: 新增 `done_sentinel` 参数（可选 str），指定远程服务器上的自定义完成标记文件路径
- `poll_cron()`: 在标准 sentinel (`/tmp/agent-ml-exit/{exp_id}.exit`) 缺失且进程已死时，回退检查 `done_sentinel` 文件。如果存在，合成 `_sentinel_exit = 0`，复用全部现有成功处理逻辑（ANALYZING → hooks → delete cron）

**2. `/home/ubuntu/agent-ml-research/core/mcp_server.py`** — MCP 工具暴露层
- `register_cron` MCP tool 新增 `done_sentinel` 参数，透传到核心函数

**3. `artifacts/exp002_signal_pipeline/compute_signals.py` + `exp002/compute_signals.py`** — 信号计算脚本
- 在 `main()` 末尾添加 `(output_dir / ".done").touch()`，使信号计算完成后也写入 `.done` 标记

**4. `config/crons.yaml`** — 活跃 cron 配置
- 4 个 cron 添加了 `done_sentinel` 路径

### 6 个活跃 cron 诊断报告

| # | exp_id | sentinel 状态 | done_sentinel | 风险 |
|---|--------|---------------|---------------|------|
| 1 | `exp_001_eval_3B_d000_s42_a32_batch` | ✅ EXIT trap 正常（PID 676487 运行中） | 已添加 `.done` 备用 | 低 |
| 2 | `exp_001_eval_3B_d005_s42_a32_batch` | ✅ EXIT trap 正常（PID 679180 运行中） | 已添加 `.done` 备用 | 低 |
| 3 | `exp_001_eval_3B_d100_s42_a32_batch` | ❌ 无进程运行，output dir 为空 | 已添加但无实际帮助 | **需重新提交** |
| 4 | `exp_002_signals_3B_d100_s123_v9` | ⚠️ PID 689315 是直接 python 进程，非 tmux wrapper；但其父 tmux 进程有 EXIT trap | 已添加（但当前跑的是旧代码，无 `.done`） | 中 — EXIT trap 应能工作 |
| 5 | `exp_002_signals_05B_s123_v2` | ⚠️ tmux session `exp002_05B_s123_v2` 运行中（log 活跃） | 未添加（批量脚本无单一完成文件） | 低 — tmux check 可检测 |
| 6 | `exp_002_signals_15B_s123_batch` | ✅ EXIT trap 正常（PID 691872 运行中） | 未添加（有 EXIT trap） | 低 |

**关键发现**：`exp_001_eval_3B_d100_s42_a32_batch`（#3）无进程运行且输出为空，需要重新提交。

---
