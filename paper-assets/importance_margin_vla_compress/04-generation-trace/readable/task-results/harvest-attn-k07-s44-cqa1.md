# harvest attn k07 s44 cqa1

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_attn_k07_s44_cqa1_20260528T022729_result.json`
- **Structured JSON:** [`4a1ce3b03ab8d5cd96ea.json`](../../sessions/4a/4a1ce3b03ab8d5cd96ea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇总：

## Attn k=0.75 Long seed44 结果

**SR = 51.6%** (258/500)，运行 164 min。

注意：日志显示实际 keep_ratio=0.75（192/256 tokens），命令行传入 `--keep_ratio 0.7` 但 prune 逻辑 keep 了 192/256=0.75。

### Per-task 明细

| Task | SR |
|------|-----|
| T0 alphabet soup + tomato | 72% |
| T1 cream cheese + butter | 70% |
| T2 stove + moka pot | 78% |
| T3 black bowl → drawer | 28% |
| T4 white mug + left plate | 30% |
| T5 book → back compartment | 48% |
| T6 white mug → plate | 74% |
| T7 alphabet soup + cream | 26% |
| T8 both moka pots → stove | 10% |
| T9 yellow mug → microwave | 80% |

### 3-seed 汇总

| Seed | SR |
|------|------|
| s42 | 53.6% |
| s43 | 53.8% |
| s44 | 51.6% |
| **Mean** | **53.0% ± 1.0pp** |

s44 比前两个 seed 低 ~2pp，方差从 ±0.1pp 扩大到 ±1.0pp，但仍在合理范围内。

---
