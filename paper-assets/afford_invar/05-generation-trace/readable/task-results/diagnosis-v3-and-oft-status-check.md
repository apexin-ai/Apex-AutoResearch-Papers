# diagnosis v3 and oft status check

**afford invar** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_v3-and-oft-status-check_20260520T013716_result.json`
- **Structured JSON:** [`c153549ffebe2d2aff15.json`](../../sessions/c1/c153549ffebe2d2aff15.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 1. phase1_transfer_v3 — PID 139040 存活，正在训练

| 项目 | 状态 |
|------|------|
| PID 139040 | **存活**，已运行 6m13s |
| 当前 step | **~1211 / 20000 (6%)** |
| 速度 | ~3.3 it/s |
| ETA | ~1h35m |
| GPU 0 | 25143 MiB / 97887 MiB, 71% util |

**训练指标（最近）：**
- `L_act`: 0.19 ~ 0.44（正常波动）
- `L_xfr`: **4.174**（从 step 500 起几乎不变，完全平坦）
- `hm_ent`: **9.11**（稳定）
- `L_tot`: 0.60 ~ 0.87

**GRAD MONITOR 趋势（值得注意）：**

| Step | L_transfer | transfer_grad_norm | grad_ratio |
|------|-----------|-------------------|------------|
| 100 | 4.129 | 0.1325 | 0.0064 |
| 300 | 4.174 | 0.1049 | 0.0081 |
| 500 | 4.174 | 0.0070 | 0.0004 |
| 800 | 4.174 | 0.0048 | 0.0004 |
| 1200 | 4.174 | 0.0065 | 0.0004 |

**L_xfr 从 step ~300 开始完全停滞在 4.174，transfer_grad_norm 从 0.13 骤降到 0.005 级别，grad_ratio 从 0.008 降到 0.0004。** Transfer loss 实际上没有在学习。

### 2. v3 checkpoints

只有 `dataset_statistics.json`，尚无模型 checkpoint（还未达到 checkpoint 保存间隔）。

### 3. OFT baseline_v2 — 已成功完成

checkpoint-20000 **完整存在**：
- `action_head--20000_checkpoint.pt` (288MB)
- `lora_adapter/` 目录
- `dataset_statistics.json`, `tokenizer.json` 等配套文件
- 日志确认 `Max step 20000 reached! Stopping training...`

Cron 标记为 failed 是**误判**。

### 4. GPU 状态

| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| 0 | 25143 / 97887 MiB | 71% (v3 在用) |
| 1 | 0 MiB | 0% 空闲 |
| 2 | 0 MiB | 0% 空闲 |
| 3 | 0 MiB | 0% 空闲 |

---
