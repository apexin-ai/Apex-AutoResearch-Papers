# setup bjb1 32546 r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_setup_bjb1-32546-r2_20260515T022614_result.json`
- **Structured JSON:** [`38cfdac4c66a345f3e02.json`](../../sessions/38/38cfdac4c66a345f3e02.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## bjb1-32546 Setup

| 项目 | 状态 |
|------|------|
| SSH | OK |
| Python | 3.12.3 (conda) |
| PyTorch | 2.10.0+cu128, CUDA=True |
| GPUs | 6× RTX 4090 (24GB each) |
| Code | synced (`src/` 全部文件) |
| Checkpoints | synced: perdof, obs_only, scalar_unc |
| SmolVLA | available (`/root/autodl-tmp/models/smolvla_libero/`, 865MB) |
| HF cache | synced (smolvla_libero + SmolVLM2) |
| crm_cache_v5 | synced (264MB) |
| LIBERO data | 不需要传输 — BDDL 文件随 libero 包安装 |
| Env vars | 已配置 (HF_HOME, OFFLINE, SSL) |
| Disk | root: 21GB free, data: 218GB free |
| Dry-run | PASS (`evaluate.py --help` OK) |
| Blockers | 无 |
| **Ready for experiments** | **YES** |

传输方式：通过在 bjb1-18228 生成 SSH 密钥并注入 bjb1-32546 的 authorized_keys，实现服务器间直接 scp。所有依赖包、模型权重、checkpoints、cache 均已到位。

---
