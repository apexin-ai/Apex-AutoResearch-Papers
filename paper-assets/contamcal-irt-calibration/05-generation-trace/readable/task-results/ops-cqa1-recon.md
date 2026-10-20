# ops cqa1 recon

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cqa1-recon_20260518T140813_result.json`
- **Structured JSON:** [`f541298e55c10592def0.json`](../../sessions/f5/f541298e55c10592def0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总：

| 项目 | 状态 |
|---|---|
| **GPU** | 1× RTX 4090 D, 24564 MiB VRAM |
| **磁盘** | /root 30G 总量，12G 可用 (63% used) |
| **Python** | `/root/miniconda3/bin/python` 3.12，torch 版本未能通过 read-only 工具确认（分号被拦） |
| **项目目录** | `/root/contamcal-irt-calibration/` 存在，含 exp001–exp008、stan_models、figures 等 |
| **autodl-tmp** | 存在，含 .hf_cache、models、多个 exp 目录、structfuse 等 |
| **预置镜像** | 未检测到，需手动环境搭建 |

torch 版本需要通过 `ssh_execute` 确认。是否需要进一步操作？

---
