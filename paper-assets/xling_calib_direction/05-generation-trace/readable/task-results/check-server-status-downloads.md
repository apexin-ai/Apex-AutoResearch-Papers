# check server status downloads

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_server_status_downloads_20260521T013130_result.json`
- **Structured JSON:** [`40e53bfbbd06af60db98.json`](../../sessions/40/40e53bfbbd06af60db98.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`save_project_file` 只支持白名单文件，无法写 `artifacts/server_status_check.md`，已将内容写入 `memory.md`。

## 检查结果

### 模型下载

| 模型 | 状态 | 进度 | 详情 |
|------|------|------|------|
| **Llama4-Scout-W4A16** | ⚠️ 已停止 | 7/14 shards (~33GB/66GB) | 无活跃进程，5个 .incomplete 文件，可续传 |
| **Qwen3-235B-A22B-GPTQ-Int4** | ❌ 已删除 | 0/32 (目录被清理) | 进程死亡后目录消失，需完全重启 |

**两个下载都需要重启。** Qwen3 损失更严重——之前下了 40GB 的 7/32 shards，现在目录整个没了。

### 磁盘
350G 中已用 131G，剩余 220G (38%)。两个模型都下完需要额外 ~155G，空间足够。

### Procrustes Sensitivity 实验
**已完成。** 两个 CSV 结果文件：
- `linproj_procrustes_sensitivity.csv` (31KB) — Procrustes 对齐，layers {0,4,8,12} × 5 语言 × 7 种 n_pairs
- `linproj_sensitivity.csv` (23KB) — Mean-shift 投影，同配置 + n_pairs=14042 全量

关键趋势：Procrustes 在 AUROC 上普遍正向（尤其 layer 8 hi 语言 delta +0.14），但 ECE 表现语言依赖性强（sw 始终恶化）。Mean-shift 类似模式。

---
