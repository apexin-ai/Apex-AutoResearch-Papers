# fix heatmap 3seed p0 v2

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_heatmap_3seed_p0_v2_20260514T213423_result.json`
- **Structured JSON:** [`1b0c7b7642c54f69037e.json`](../../sessions/1b/1b0c7b7642c54f69037e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

现在有了所有对比数据。输出验证结果。

```
=== 热力图数据来源验证 ===

Row 0 (SciERC NER Qwen):
  Full:  source=3-seed mean (seed42/123/456) from all_signals_report.json
         SJ=0.412 FK=0.260 EM=0.329 VC=0.422 LP=0.234
  Cond:  source=3-seed mean (seed42/123/456) from all_signals_report.json
         SJ=0.365 FK=0.176 EM=0.408 VC=0.346 LP=0.166

Row 1 (CoNLL NER Qwen):
  Full:  source=n16_5signal_results.json (single seed)
  Cond:  source=n16_5signal_results.json (single seed)

Row 2 (CoNLL NER LLaMA):
  Full:  source=3-seed mean from llama_conll summary
  Cond:  source=3-seed mean from llama_conll summary

Row 3 (SciERC RE Qwen):
  Full:  source=2-seed mean (seed42/123) from exp_015_v2
         SJ=0.285 FK=0.294 EM=0.154 VC=0.378 LP=0.297
  Cond:  source=2-seed mean (seed42/123) from re_all_signals_report.json
         SJ=0.318 FK=0.148 EM=0.485 VC=0.345 LP=0.002
```

```
=== 新旧 conditional ρ 对比 ===

NER conditional (Row 0):
旧源: exp_015_unified (单 seed, 合成 fallback)
新源: 3-seed mean from all_signals_report.json

| Signal   | Old (unified) | New (3-seed) |    Δ   |
|----------|---------------|--------------|--------|
| SJ       |   0.4120      |   0.3646     | -0.047 |
| FK       |   0.3060      |   0.1761     | -0.130 |
| EM       |   0.3427      |   0.4082     | +0.065 |
| VotConf  |   0.4497      |   0.3461     | -0.104 |
| LogProb  |   0.1627      |   0.1665     | +0.004 |

RE conditional (Row 3):
旧源: exp_015_unified (单 seed, 合成 fallback)
新源: 2-seed mean from re_all_signals_report.json

| Signal   | Old (unified) | New (2-seed) |    Δ   |
|----------|---------------|--------------|--------|
| SJ       |   0.3683      |   0.3183     | -0.050 |
| FK       |   0.3168      |   0.1478     | -0.169 |
| EM       |   0.3607      |   0.4846     | +0.124 |
| VotConf  |   0.4630      |   0.3452     | -0.118 |
| LogProb  |   0.1457      |   0.0018     | -0.144 |
```

关键发现：
- FK 和 VotConf 的旧 conditional 值显著偏高（合成数据高估）
- EM 在真实数据中表现更好（旧值低估）
- RE LogProb conditional 接近 0（旧值 0.146 完全是合成的）
- NER full 从 2-seed 切换到 3-seed，变化很小（seed456 略拉低 SJ/FK）

所有 SciERC 行现在均来自真实测量值，无近似/fallback/ratio estimate。本地脚本和服务器脚本已同步，3 个 PNG 已拉回 `artifacts/figures/`。

---
