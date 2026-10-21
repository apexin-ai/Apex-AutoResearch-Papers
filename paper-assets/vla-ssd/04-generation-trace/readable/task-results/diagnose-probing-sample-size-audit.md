# diagnose probing sample size audit

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_probing_sample_size_audit_20260521T025935_result.json`
- **Structured JSON:** [`4e2310dd9680f0707570.json`](../../sessions/4e/4e2310dd9680f0707570.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。以下是完整结果。

## R² Probing 样本量审计报告

### Part 1: NORA Goal Pipeline

**状态：已崩溃，从未运行。** 日志显示：
```
nora_goal_full_pipeline.py: error: unrecognized arguments: untrained
EXIT_CODE=2
```
PID 525033 已死。`nora_goal/trained/action_r2_probing.json` 存在但**全层 R²=0.0**，来自之前一次失败的运行。

脚本当前配置（已修正，充足）：
- `N_DEMOS = 10`, `N_TIMESTEPS = 50`, 10 tasks → **5000 samples**（500/task，远超 25/task 最低要求）

### Part 2: 已完成实验的 probing 样本量

**服务器上仅找到 2 个 `action_r2_probing.json`**：
- `/results/nora_goal/trained/action_r2_probing.json` — 全层 0.0 ✗
- `/results/tracvla_spatial/trained/action_r2_probing.json` — 全层 0.0 ✗

两者 values 数组长度均为 2，表明来自旧版本脚本（样本严重不足）。

**旧框架有效结果**（本地 artifacts，15 seeds，R² 正常）：
- `openvla_r2_per_layer.json`：OpenVLA-Goal，R² 0.49–0.68 ✓
- `phi3v_r2_per_layer.json`：TracVLA-Spatial，R² 0.45–0.63 ✓

**OpenVLA-Spatial**：无 probing 结果，无 pipeline 脚本。

### Part 3: 所有 Pipeline 脚本配置

| Script | N_DEMOS | N_TIMESTEPS | Tasks | Total Samples |
|--------|---------|-------------|-------|---------------|
| `nora_goal_full_pipeline.py` | 10 | 50 | 10 | 5000 |
| `libero_object_full_pipeline.py` | 10 | 50 | 10 | 5000 |
| `tracvla_spatial_full_pipeline.py` | 10 | 50 | 10 | 5000 |

所有脚本配置均已修正为充足样本量（500/task >> 25/task 要求）。

---

## 汇总表

| Pipeline | demos/task | timesteps/demo | total samples | 状态 |
|----------|-----------|----------------|---------------|------|
| OpenVLA-Goal | ≥50（旧框架） | ≥50 | ≥5000 | **done** ✓ (旧结果 R² 0.49–0.68) |
| OpenVLA-Spatial | — | — | 0 | **无数据**，无 pipeline 脚本 |
| OpenVLA-Object | 10 | 50 | 5000 | **running** ✓ (L0 R²=0.6952) |
| TraceVLA-Spatial | 10 | 50 | 5000 (配置) | **需补跑** (现有结果全 0.0，来自旧版脚本) |
| NORA-Goal | 10 | 50 | 5000 (配置) | **需 kill 重提交** (进程已崩溃) |

## 关键判断

1. **NORA Goal**：进程已崩溃（`unrecognized arguments: untrained`），现有结果无效（全 0.0）。脚本配置已修正（5000 samples），**需要修复参数后重新提交**。不需要 kill（已死），只需修复启动命令。

2. **TraceVLA-Spatial**：旧框架的 probing 结果有效（`phi3v_r2_per_layer.json`，R² 0.45–0.63），但新 pipeline 格式的结果无效（全 0.0）。如果需要新格式结果，需重跑。

3. **OpenVLA-Object**：正常运行中，Phase 2 probing 已开始输出非零 R²。

---
