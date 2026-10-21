# diagnose phase2 4way eval

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_phase2_4way_eval_20260519T131212_result.json`
- **Structured JSON:** [`12f046b53625edd4e8a4.json`](../../sessions/12/12f046b53625edd4e8a4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果：四路 Eval 已成功完成

### 状态：**已完成** (EXIT_CODE=0)

PID 60024 已退出，tmux 无 session，因为 eval 正常跑完了。所有 8 个 eval 子任务全部完成，结果已写入 `/root/turn_residual_gating/runs/4way_eval/`。

### 结果汇总（dongre GAR 指标）

| 配置 | GAR variant | Mid-turn GAR | GAR Recovery | Avg PPL | NTP Loss |
|------|-------------|-------------|-------------|---------|----------|
| **Base** (无微调) | ours | 0.0107 | -0.15pp | 4.23 | 1.4162 |
| **Base** | dongre | 0.0030 | -0.92pp | 4.23 | 1.4162 |
| **TG v7** (ThreadGate) | ours | 0.4866 | **+47.44pp** | 2.63 | 0.9484 |
| **TG v7** | dongre | 0.0157 | +0.35pp | 2.63 | 0.9484 |
| **UG** (Uniform Gate) | ours | 0.4923 | **+48.01pp** | 2.62 | 0.9433 |
| **UG** | dongre | 0.0130 | +0.08pp | 2.62 | 0.9433 |
| **LoRA-only** | ours | 0.4860 | **+47.39pp** | 2.63 | 0.9482 |
| **LoRA-only** | dongre | 0.0137 | +0.15pp | 2.63 | 0.9482 |

### Checkpoint 可用性
- TG v7 (`phase2_tg_s42_v7/lora/`): 存在
- UG (`phase2_ug_s42/lora/`): 存在
- LoRA-only (`phase2_lora_only_s42/lora/`): 存在

### 服务器状态
- **GPU**: 0% utilization, 0 MiB / 97887 MiB — 完全空闲
- **磁盘**: 根分区 16G/30G (52%), 数据盘 2.6M/250G (几乎空)
- **Eval 输出**: 2.3 MB（8 个 JSON + PNG 文件）

### Registry 不一致
Registry 中查不到 `phase2_4way_eval` 记录（count=0）。任务实际已完成但 registry 状态未更新——可能需要手动将 registry 状态标记为 DONE。

---
