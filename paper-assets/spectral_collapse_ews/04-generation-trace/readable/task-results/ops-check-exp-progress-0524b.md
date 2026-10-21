# ops check exp progress 0524b

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-exp-progress-0524b_20260524T053926_result.json`
- **Structured JSON:** [`794820cea2492fde3e8c.json`](../../sessions/79/794820cea2492fde3e8c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

## exp_020 — GPT-2-medium pure collapse
- **进度**: Gen 8/10，Step ~1800/6200
- **已完成**: Gen 0-7（checkpoint 已保存）
- **每代耗时**: ~2h24m（从 checkpoint 时间戳推算）
- **预计剩余**: Gen 8 剩 ~1h15m + Gen 9 ~2h24m + Gen 10 ~2h24m ≈ **~6h**
- GPU 0，26.4GB 显存，100% 利用率

## exp_021 — GPT-2-medium real-data control (r=1.0)
- **进度**: Gen 3/3（最后一代），Step ~4900/6200
- **已完成**: Gen 0-2（checkpoint 已保存）
- **预计剩余**: 训练剩 ~1300 步 + eval ≈ **~30-45min**，之后完成
- GPU 1，29.1GB 显存，100% 利用率

## 服务器状态
- 2× RTX PRO 6000 Blackwell (96GB)，均 100% 满载
- 磁盘 `/root/autodl-tmp/`: 118GB/250GB 已用 (48%)

exp_021 预计今天下午 ~14:15 前完成；exp_020 预计今晚 ~19:30-20:00 完成。

---
