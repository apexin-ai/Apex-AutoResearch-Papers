# code d146 exec s43 completion

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d146-exec-s43-completion_20260519T181447_result.json`
- **Structured JSON:** [`17a73f3e58836741f4c6.json`](../../sessions/17/17a73f3e58836741f4c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## D146 exec-s43 完成报告

### 1. exec-s43 最终指标 (step 500)

| 指标 | 值 |
|------|-----|
| reward | 1.000 |
| prove_rate | 1.000 |
| isr_mean | 0.2048 |
| parse_rate | 1.000 |

### 2. prove_rate 全程分布

| | s43 | s42 |
|--|-----|-----|
| prove_rate=0.0 | 156 steps (31.2%) | 84 steps (16.8%) |
| prove_rate=0.5 | 193 steps (38.6%) | 51 steps (10.2%) |
| prove_rate=1.0 | 75 steps (15.0%) | 314 steps (62.8%) |
| **mean** | **0.4143** | **0.7280** |
| **final 50 mean** | **0.5500** | **0.9975** |

final 50 breakdown:
- s43: 0.0×7, 0.5×23, 1.0×11 — 持续震荡
- s42: 0.0×0, 0.5×0, 1.0×49 — 完全收敛

### 3. ISR 对比

| | s43 | s42 |
|--|-----|-----|
| mean | 0.1068 | 0.0628 |
| max | 0.4295 | 0.5000 |
| final 50 | 0.1190 | 0.0658 |

### 4. Cross-seed 差异分析

**s43 与 s42 差异显著：**
- s42 早期收敛，final 50 prove_rate 近乎完美 (0.998)；s43 始终未收敛，final 50 仅 0.55，仍有 14% 步数 prove_rate=0
- s43 ISR 约为 s42 的 1.8 倍（0.119 vs 0.066 final 50），说明 s43 模型在 prove 成功时生成了更多非必要推理步骤
- s43 的震荡 pattern 与 s42 的稳定收敛形成鲜明对比——seed 对 exec-only 训练稳定性影响很大

### 5. exec-s44 状态

已自动启动，当前 step 75/500。GPU 占用 83GB/98GB，utilization 88%。

---
