# ops full server diagnostic

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_full-server-diagnostic_20260520T031606_result.json`
- **Structured JSON:** [`15f0c59d7f6e5df3a9a1.json`](../../sessions/15/15f0c59d7f6e5df3a9a1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-29999

| GPU | 利用率 | 显存 | 进程 |
|-----|--------|------|------|
| 0 | 94% | 58.0/97.9 GB | phi-4_d000_s0 (PID 265121) |
| 1 | 86% | 62.3/97.9 GB | Qwen2.5-14B_d100_s123 (PID 246779) |
| 2 | 69% | 66.9/97.9 GB | OLMo-2-7B_d005_s0 (PID 261133) |
| 3 | 69% | 94.9/97.9 GB | gemma-2-9b_d100_s123 (PID 246861) |
| CPU | — | — | IRT fitting MMLU v3 (PID 265452) |

磁盘: `/` 5% (1.4G/30G) | `/root/autodl-tmp` 77% (192G/250G)

### 实验状态

| 实验 | GPU | PID | 进度 | 状态 | ETA |
|------|-----|-----|------|------|-----|
| Qwen2.5-14B_d100_s123 | 1 | 246779 | 1611/4159 (39%) | **running** | ~2h |
| OLMo-2-7B s0 sweep — d000 | 2 | — | 3125/3125 | **completed** | — |
| OLMo-2-7B s0 sweep — d005 | 2 | 261133 | ~140/3125 (4%) | **running** | ~1.5h，之后还有 d025/d050/d100 |
| gemma-2-9b_d100_s123 | 3 | 246861 | 1656/4159 (40%) | **running** | ~2h |
| phi-4 s0 sweep — d000 | 0 | 265121 | 刚启动(~6min) | **running** | ~3h，之后还有 d005/d025/d050/d100 |
| IRT fitting (MMLU, 2PL+γ, ADVI) | CPU | 265452 | 无输出文件 | **running** | 未知（刚启动~6min） |

### 备注
- OLMo-2 sweep 已完成 d000_s0（有 adapter_model.safetensors + train_config.json），正在训练 d005_s0
- phi-4 sweep 刚开始第一个 dosage (d000_s0)，checkpoint 目录为空
- IRT fitting 输出目录和日志均为空，可能仍在 warmup/编译阶段

---

## cqa1-21977

| GPU | 利用率 | 显存 | 进程 |
|-----|--------|------|------|
| 0 | 100% | 21.3/24.6 GB | Qwen2.5-7B_d000_s0 (PID 313418) |

磁盘: `/` 64% (19G/30G) | `/root/autodl-tmp` 72% (121G/169G)

### 实验状态

| 实验 | GPU | PID | 进度 | 状态 | ETA |
|------|-----|-----|------|------|-----|
| Qwen2.5-7B s0 sweep — d000 | 0 | 313418 | 544/3125 (17%) | **running** | ~3h，之后还有 d005/d025/d050/d100 |

### 备注
- cqa1 只有 1 张 4090D (24GB)，全被 Qwen-7B s0 sweep 占满
- 该 sweep 需完成 5 个 dosage (d000→d100)，当前进度仅第 1 个的 17%，全部完成预计 ~15h+

---
