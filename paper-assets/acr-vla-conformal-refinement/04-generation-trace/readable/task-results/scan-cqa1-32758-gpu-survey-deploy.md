# scan cqa1 32758 gpu survey deploy

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_scan_cqa1-32758-gpu-survey-deploy_20260523T231914_result.json`
- **Structured JSON:** [`0a1b762c01f35902c75a.json`](../../sessions/0a/0a1b762c01f35902c75a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 使用状态汇总

### cqa1-32758（6× RTX 4090 D）— 全部占满

| GPU | 内存占用 | PID | 实验 |
|-----|---------|-----|------|
| 0 | 3046/24564 MiB | 456787 | `goal` / `vla_only` / K2 mean / **seed 45** |
| 1 | 3275/24564 MiB | 456947 | `spatial` / `vla_only` / **seed 45** |
| 2 | 4949/24564 MiB | 512632 | `object` / `vla_only` / K2 mean / **seed 45** |
| 3 | 2810/24564 MiB | 457405 | `spatial` / `crm_obs_only` / norm 0.05 / K10 / **seed 45** |
| 4 | 4337/24564 MiB | 502821 | `spatial` / `adaptive_conformal_crm` / norm 0.2 / tau 0.25 / K2 / **seed 45** |
| 5 | 2776/24564 MiB | 457485 | `spatial` / `reconvla` / K10 / **seed 45** |

### bjb1-32546（6× RTX 4090）— 全部占满

| GPU | 内存占用 | PID | 实验 |
|-----|---------|-----|------|
| 0 | 6191/24564 MiB | 188432 | `spatial` / `vla_only` / K2 mean / **seed 46** |
| 1 | 2303/24564 MiB | 103128 | `long` / `vla_only` / **seed 45** |
| 2 | 2309/24564 MiB | 103397 | `long` / `adaptive_conformal_crm` / norm 0.2 / tau 0.25 / K2 / **seed 45** |
| 3 | 2403/24564 MiB | 103675 | `long` / `crm_obs_only` / norm 0.05 / K10 / **seed 45** |
| 4 | 2365/24564 MiB | 103942 | `long` / `reconvla` / K10 / **seed 45** |
| 5 | 4278/24564 MiB | 172434 | `object` / `reconvla` / K10 / **seed 45** |

### 结论

**两台服务器 12 个 GPU 全部在跑 4th-seed (seed 45) 扩展实验**，无空闲 GPU。bjb1-32546 的 GPU 0 还在跑 seed 46 的 spatial k2mean。所有实验内存占用较低（2.3-6.2 GB / 24.6 GB），但 GPU utilization 13-35%，属于 rollout evaluation 的正常水平。

---
