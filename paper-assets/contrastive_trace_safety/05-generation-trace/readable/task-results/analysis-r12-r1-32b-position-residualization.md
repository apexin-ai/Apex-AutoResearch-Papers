# analysis r12 r1 32b position residualization

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r12_r1_32b_position_residualization_20260518T134711_result.json`
- **Structured JSON:** [`cb5a39161330eab141a3.json`](../../sessions/cb/cb5a39161330eab141a3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。D039 表格 R1-32B 行数据：

```
R1-32B Position Residualization (W=1, L63, seed=42):
- Position-only BA: 0.6856
- Original HS BA: 0.7552
- Original Text BA: 0.6011
- Residualized HS BA: 0.5516 (drop: 20.4 pp)
- Residualized Text BA: 0.5324 (drop: 6.9 pp)
- Residualized Gap (HS - Text): 1.9 pp
- Bootstrap p-value: 0.9140
- HB result: fail
```

与 QwQ 的对比：R1-32B 的 HS probe 受 position 影响远大于 QwQ（drop 20.4 pp vs 9.1 pp）。残差化后 HS 与 text 的 gap 仅 1.9 pp（p=0.914），HB 检验 fail，说明 R1-32B 的 HS 优势在去除位置信息后基本消失。

结果已写入远程 `artifacts/r12_r1_32b_position_residualized/results.json` 并注册。

---
