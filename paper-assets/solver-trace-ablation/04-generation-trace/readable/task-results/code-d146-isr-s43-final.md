# code d146 isr s43 final

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d146-isr-s43-final_20260520T002826_result.json`
- **Structured JSON:** [`d170234d4e0d9e62416d.json`](../../sessions/d1/d170234d4e0d9e62416d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### 1. isr-s43: **已完成** (500/500)

最终指标 (step 500): `prove_rate=1.000  isr=0.205  reward=1.020  parse_rate=1.0`

完成时间: 2026-05-19 23:55 UTC, 总耗时 ~1h53m

### 2. isr-s43 轨迹 (每 50 步)

| Step | prove_rate | ISR   | reward |
|------|-----------|-------|--------|
| 50   | 0.000     | 0.000 | 0.000  |
| 100  | 0.500     | 0.190 | 0.519  |
| 150  | 0.000     | 0.000 | 0.000  |
| 200  | 0.000     | 0.000 | 0.000  |
| 250  | 0.375     | 0.022 | 0.377  |
| 300  | 0.500     | 0.109 | 0.511  |
| 350  | 1.000     | 0.205 | 1.021  |
| 400  | 0.125     | 0.058 | 0.131  |
| 450  | 1.000     | 0.219 | 1.022  |
| **500** | **1.000** | **0.205** | **1.020** |

Per-step metrics 噪声大（小 batch），单步可在 0.0~1.0 间跳变。整体趋势：前 200 步以 0.0/0.5 为主，250 步后 0.5/1.0 出现频率增高。无法远程计算 running average，但末尾 5 步 (496-500) 中 4 步 prove_rate=0.5、1 步 prove_rate=1.0。

### 3. isr-s44: **运行中** (154/500)

- 进程 PID 639946，99% CPU，配置: `grpo_prooffol_isr_b01.yaml --seed 44`
- 当前 step 154，checkpoint-150 已保存
- 最新 (step 154): prove_rate=0.0, isr=0.0
- ETA: ~(500−154)×13s ≈ **75 分钟**（约 09:45 北京时间）

### 4. GPU

单 GPU 占用 83179 MiB，利用率 91%，仅 isr-s44 训练进程在跑。

---
