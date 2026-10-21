# code resubmit a005 a060 check others

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_resubmit_a005_a060_check_others_20260518T232248_result.json`
- **Structured JSON:** [`a96178d4068549002b2f.json`](../../sessions/a9/a96178d4068549002b2f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

cuda:2 和 cuda:3 各占用 2307 MiB，模型正在加载。一切正常。

---

## 报告

### 1. metrics.py 修复状态
- **westd-17855**: 已修复 (lines 208, 211 有 `except np.linalg.LinAlgError`)
- **westd-19828**: 已修复 (lines 206, 211 有 `except np.linalg.LinAlgError`)

### 2. 重提交实验
| 实验 | GPU | PID | tmux session | 输出目录 |
|------|-----|-----|-------------|---------|
| a005 (α=0.05) | cuda:3 | 63878 | a005_fp32_v2 | results/alpha_sweep/a005_s42_fp32_v2 |
| a060 (α=0.60) | cuda:2 | 63952 | a060_fp32_v2 | results/alpha_sweep/a060_s42_fp32_v2 |

Registry 已更新，cron 监控已注册（120s 间隔）。

### 3. 实验状态
| 实验 | 服务器 | 进度 | 状态 |
|------|--------|------|------|
| **Qwen3.5** | westd-17855 cuda:1 | gen训练中 39% (1953/5000 steps), loss ~1.6 | 正常运行 |
| **a010_s43** (bf16) | westd-17855 cuda:5 | gen_7 生成阶段 (7/10代完成) | 正常运行 |
| **SmolLM3 bf16** | westd-19828 cuda:? | gen_3 生成阶段 (2/10代完成) | 正常运行 |
| **SmolLM3 fp32** | westd-19828 cuda:? | gen_1 生成阶段 (0/10代完成) | 正常运行 |

### 4. 其他受影响实验
无。所有当前运行的实验要么已经过了 gen_1 metrics 阶段（a010_s43），要么还在 gen_0/gen_1 训练/生成阶段（Qwen3.5, SmolLM3），metrics.py 已修复，后续 metrics 计算不会再崩。

---
