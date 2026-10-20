# code collect phase table script

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_collect_phase_table_script_20260522T080906_result.json`
- **Structured JSON:** [`57afe35d2151c1d4fb14.json`](../../sessions/57/57afe35d2151c1d4fb14.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部通过。脚本位于 `scripts/collect_phase_table_stats.py`，用法：

```bash
python scripts/collect_phase_table_stats.py --ratio 0.3 --seeds 42 43 44
python scripts/collect_phase_table_stats.py --ratio 0.0 --seeds 42 43 44
python scripts/collect_phase_table_stats.py --ratio 0.25 --seeds 42 43 44
python scripts/collect_phase_table_stats.py --ratio 0.5 --seeds 42
```

注意：
- seed 44 的 r=0.3 只有 5 代数据（Gen 0–4），脚本会 WARNING 并 fallback 到最大可用代，会拉低平均值
- `--gen N` 可以指定目标代（默认 10）
- 文件命名映射：r=0.0 用 `phase0_results.json`（seed42）/ `phase1_pure_collapse_seed{N}`，r=0.5 用 `phase1_fixed_mix_seed{N}`（无 ratio tag）

---
