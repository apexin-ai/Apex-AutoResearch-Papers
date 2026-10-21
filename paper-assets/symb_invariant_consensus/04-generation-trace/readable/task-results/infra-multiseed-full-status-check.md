# infra multiseed full status check

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_multiseed-full-status-check_20260522T090537_result.json`
- **Structured JSON:** [`0826c4fd83c8506b5ee9.json`](../../sessions/08/0826c4fd83c8506b5ee9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态

| GPU | 型号 | Util | 显存 |
|-----|------|------|------|
| 0 | RTX PRO 6000 Blackwell | 97% | 90159/97887 MiB |
| 1 | RTX PRO 6000 Blackwell | 97% | 90161/97887 MiB |
| 2 | RTX PRO 6000 Blackwell | 0% | 90213/97887 MiB |
| 3 | RTX PRO 6000 Blackwell | 0% | 90197/97887 MiB |

GPU 2/3 模型已加载（90GB）但瞬时采样 0% util，日志显示 Mistral 仍在活跃推理。

## Guard Script
- Guard PID 555317: **运行中**，监视 seed789 intermediates，当前 48/204
- PID 510872 (cuda:1 master): **仍存活**，guard 尚未触发 kill

## Qwen2.5 × FOLIO (cuda:1)

| seed | 进度 | SC | SICA | Δ | 状态 |
|------|------|----|------|---|------|
| 123 | 204/204 | 74.51% | 73.04% | -1.47pp | ✅ |
| 456 | 204/204 | 74.02% | 74.02% | +0.00pp | ✅ |
| 789 | 48/204 | — | — | — | ⏳ ~24% |

## Mistral × PW (cuda:2)

| seed | 进度 | SC | SICA | Δ | 状态 |
|------|------|----|------|---|------|
| 42 | 600/600 | 40.00% | 36.67% | -3.33pp | ✅ |
| 123 | 78/600 | 43.59%* | 47.44%* | +3.85pp* | ⏳ ~13% |
| 456 | — | — | — | — | 未开始 |
| 789 | — | — | — | — | 未开始 |

## Qwen2.5 × PW (cuda:0)

| seed | 进度 | SC | SICA | Δ | 状态 |
|------|------|----|------|---|------|
| 123 | 80/600 | 76.25%* | 75.00%* | -1.25pp* | ⏳ ~13% |
| 456 | — | — | — | — | 未开始 |
| 789 | — | — | — | — | 未开始 |

*\* 标记为部分结果，非最终值*

所有运行中实验日志截至 17:07 CST 均有活跃推理请求，进程正常。

---
