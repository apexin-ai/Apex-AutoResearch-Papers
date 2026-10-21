# check openvla attn progress

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_openvla_attn_progress_20260525T001228_result.json`
- **Structured JSON:** [`e0ae1ffced445d88bdf0.json`](../../sessions/e0/e0ae1ffced445d88bdf0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总所有数据：

| 实验 | 服务器 | GPU | 进度 | 速度 | 剩余 | ETA |
|------|--------|-----|------|------|------|-----|
| **OpenVLA Attn k0.85 Goal** | westd-38929 | GPU2 | T6/10, Ep10/50 | 1.4 eps/min | 240 ep | **~2.9h** |
| **OpenVLA Attn k0.85 Spatial** | westd-38929 | GPU3 | T6/10, Ep20/50 | 1.4 eps/min | 230 ep | **~2.7h** |
| **OpenVLA Attn k0.9 Long** | westd-41074 | GPU0 | T2/10, Ep40/50 | 0.8 eps/min | 410 ep | **~8.5h** |
| **OpenVLA Attn k0.85 Long** | westd-41074 | GPU1 | T3/10, Ep30/50 | 0.8 eps/min | 370 ep | **~7.7h** |
| OpenVLA Random k0.9 Goal | westd-38929 | GPU0 | T2/10, Ep40/50 | 1.4 eps/min | 410 ep | **~4.9h** |
| OpenVLA Random k0.9 Spatial | westd-38929 | GPU1 | T2/10, Ep40/50 | 1.4 eps/min | 410 ep | **~4.9h** |
| OpenVLA L2norm k0.9 Goal | westd-27271 | GPU0 | T4/10, Ep10/50 | 2.7 eps/min | 340 ep | **~2.1h** |
| OpenVLA L2norm k0.9 Spatial | westd-27271 | GPU1 | T5/10, Ep10/50 | 3.2 eps/min | 290 ep | **~1.5h** |
| OpenVLA L2norm k0.9 Long | westd-41074 | GPU3 | T1/10, Ep40/50 | 0.8 eps/min | 460 ep | **~9.6h** |

**关键风险：Long Horizon 实验（westd-41074）速度仅 0.8 eps/min，3 个实验都需要 8-10 小时才能完成。** 如果现在是 5/25 下午，它们可能要到 5/26 凌晨甚至上午才能跑完。

其余实验预计 2-5 小时内完成，赶 deadline 没问题。

---
