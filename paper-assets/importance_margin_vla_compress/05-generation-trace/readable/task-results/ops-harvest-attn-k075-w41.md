# ops harvest attn k075 w41

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_harvest-attn-k075-w41_20260527T151634_result.json`
- **Structured JSON:** [`d29353d7fe766bd74c44.json`](../../sessions/d2/d29353d7fe766bd74c44.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

## 结果汇总

**π0.5 Attention k=0.75 Long strict seed42 (westd-41074)**

| Task | Description | SR |
|------|------------|-----|
| T0 | put both the alphabet soup and the tomato... | 68% |
| T1 | put both the cream cheese box and the butter... | 70% |
| T2 | turn on the stove and put the moka pot... | 64% |
| T3 | put the black bowl in the bottom drawer | 30% |
| T4 | put the white mug on the left plate... | 36% |
| T5 | pick up the book and place it in the back... | 38% |
| T6 | put the white mug on the plate... | 74% |
| T7 | put both the alphabet soup and the cream... | 24% |
| T8 | put both moka pots on the stove | 12% |
| T9 | put the yellow and white mug in the microwave | 82% |

**avg SR = 49.8%** | 249/500 episodes | 169.4 min

对比参考：Attn k=0.85 strict = 50.0%，Attn k=0.75 lenient = 51.8%。k=0.75 strict 49.8% 与 k=0.85 strict 几乎持平，说明 attention pruning 在 75%-85% keep ratio 范围内 strict 评估下性能稳定。

---
