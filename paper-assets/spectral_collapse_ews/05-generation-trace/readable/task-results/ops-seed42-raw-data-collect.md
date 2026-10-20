# ops seed42 raw data collect

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_seed42-raw-data-collect_20260521T115051_result.json`
- **Structured JSON:** [`fd1cfa664d97f4402654.json`](../../sessions/fd/fd1cfa664d97f4402654.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 3 seeds 原始数据已获取。计算 3-seed 统计。

```
=== TABLE 1 DATA (3-seed mean) ===
Gen 0:  eff_rank=417.55  SLV=2366.68  PPL=9.55   HeSw=.413  D-4=.738  σ₁=1942.8
Gen 2:  eff_rank=496.17  SLV=2467.98  PPL=13.56  HeSw=.380  D-4=.505  σ₁=718.7
Gen 5:  eff_rank=479.77  SLV=2365.99  PPL=24.50  HeSw=.341  D-4=.412  σ₁=749.2
Gen 7:  eff_rank=464.10  SLV=2293.24  PPL=37.82  HeSw=.319  D-4=.375  σ₁=788.4
Gen 10: eff_rank=438.05  SLV=2181.35  PPL=70.99  HeSw=.296  D-4=.324  σ₁=874.6

=== TABLE 1 GEN 10 S.D. ===
eff_rank ±4.8  SLV ±28.3  PPL ±5.6  HeSw ±.006  D-4 ±.150  σ₁ ±44.2

=== TABLE 3 r=0 ROW (Gen 10 3-seed mean) ===
SLV=2181.4  eff_rank=438.1  PPL=70.99  D-4=.324

=== PHASE III STAT ===
Per-gen eff_rank decline: 1.78 ± 0.22 %/gen (3-seed)
  seed42: 1.54 %/gen
  seed43: 1.80 %/gen
  seed44: 1.99 %/gen

=== SEED42 RAW DATA (for reference) ===
gen0:  eff_rank=417.55, log_det=2366.68, ppl=9.554,  d4=0.7414, sigma1=1942.82
gen1:  eff_rank=491.77, log_det=2464.76, ppl=11.383, d4=0.6256, sigma1=803.96
gen2:  eff_rank=496.44, log_det=2469.93, ppl=13.581, d4=0.5154, sigma1=712.03
gen3:  eff_rank=493.31, log_det=2440.57, ppl=16.246, d4=0.4900, sigma1=700.68
gen4:  eff_rank=485.67, log_det=2405.05, ppl=19.804, d4=0.4679, sigma1=729.59
gen5:  eff_rank=479.21, log_det=2370.17, ppl=24.593, d4=0.4630, sigma1=741.02
gen6:  eff_rank=473.00, log_det=2335.17, ppl=30.914, d4=0.4655, sigma1=758.40
gen7:  eff_rank=464.20, log_det=2304.19, ppl=38.889, d4=0.4474, sigma1=791.28
gen8:  eff_rank=456.76, log_det=2252.12, ppl=49.290, d4=0.4401, sigma1=797.66
gen9:  eff_rank=448.45, log_det=2207.57, ppl=63.325, d4=0.4262, sigma1=814.13
gen10: eff_rank=442.46, log_det=2178.95, ppl=76.781, d4=0.4259, sigma1=825.72

gen4-10 eff_rank: [485.67, 479.21, 473.00, 464.20, 456.76, 448.45, 442.46]
```

**计算方法备注**：std 使用 sample std (n-1=2)。Phase III 对每 seed 取 gen5→10 六步的逐代下降百分比均值，再对 3 seeds 求 grand mean ± s.d.。

---
