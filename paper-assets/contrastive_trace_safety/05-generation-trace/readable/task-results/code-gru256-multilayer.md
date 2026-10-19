# code gru256 multilayer

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gru256_multilayer_20260516T194158_result.json`
- **Structured JSON:** [`046c63488d0dde0dec2c.json`](../../sessions/04/046c63488d0dde0dec2c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。

## 结果汇总

| Method | Acc | Crossing% | Lead Mean | Lead Med | Pos Lead |
|---|---|---|---|---|---|
| **GRU single L14** | 0.8386 | 72.1% | +3.5 | 0.0 | 13/31 |
| **GRU multi 7L** | **0.8094** | **76.7%** | **+4.7** | 0.0 | 13/33 |
| LR single L14 | 0.8172 | 46.5% | -2.0 | -2.0 | 6/20 |
| LR multi 7L | 0.8060 | 39.5% | +1.1 | 0.0 | 6/17 |

## Pass/Fail 判断：**PASS — STRONG SIGNAL**

- **Best GRU** (multi-7L): lead = **+4.7 步**
- **Best LR** (multi-7L): lead = +1.1 步
- **Delta = 3.7 步 > 3 阈值** → 序列建模确认有效
- GRU crossing rate (72-77%) 远高于 LR (40-47%)，检出能力大幅提升
- Multi-layer GRU 略优于 single-layer (4.7 vs 3.5 lead)，聚合分布式信号有帮助
- 两个 GRU 都在 epoch 11 early stop，训练快速收敛

Checkpoints 已保存至 `artifacts/diagnostics/gru256_single_l14.pt` 和 `gru256_multi_7l.pt`。Registry 已更新为 DONE/success。

---
