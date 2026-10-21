# ssh mf4v2 v3 check recompute v2

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_mf4v2_v3_check_recompute_v2_20260521T215005_result.json`
- **Structured JSON:** [`a10aaec380110f705139.json`](../../sessions/a1/a10aaec380110f705139.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Recompute 完成。

## MF4v2 v3 Status

### 完成状态
- s123_v3: **完成** (37648/37648 lines)
- s456_v3: **完成** (37648/37648 lines)

### Recompute 结果

| seed | greedy_f1 | mv_strict_f1 | MV Δ strict (pp) | mv_incl_f1 | MV Δ incl (pp) | degeneracy | α_crit_eff_str | α_crit_eff_incl |
|------|-----------|--------------|-------------------|------------|----------------|------------|----------------|-----------------|
| s123 | 0.7911 | 0.7648 | -2.63 | 0.7844 | -0.67 | 9.3% | 0.6825 | 0.7112 |
| s456 | 0.7910 | 0.7686 | -2.24 | 0.7857 | -0.52 | 8.1% | 0.6793 | 0.7043 |

### 原数据一致性
- 原 3-seed mean: MV Δ = -2.74±0.54pp, degen = 8.8%
- v3 当前 (s123+s456): MV Δ strict = **-2.44pp** (mean), degen = **8.7%**
- 一致: **是** — MV Δ 在原 mean±1σ 范围内 (-2.74±0.54 → [-3.28, -2.20])，degen 8.7% 接近原 8.8%

### pretrained_s42_v2 进度
- 状态: **运行中** (PID 346388, elapsed 3h38m)
- 进度: 87% (263296/301184 prompts)
- 预计剩余: ~30-40 分钟
- samples.jsonl 尚未写入（推测写入在 inference 全部完成后）

---
