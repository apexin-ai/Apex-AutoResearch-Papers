# ops m046 canonical sweep 19828

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_m046_canonical_sweep_19828_20260520T084810_result.json`
- **Structured JSON:** [`9d0b7cb39ebdb8848ee5.json`](../../sessions/9d/9d0b7cb39ebdb8848ee5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总如下：

| exp_dir | PermG (old→new) | TY (old→new) | K≥3 (old→new) | Threshold (old→new) | DiffXcorr (old→new) | 变化? |
|---------|----------------|-------------|---------------|--------------------|--------------------|-------|
| gen_opt13b_wiki_a100_s43_fp32 | 6→6 | 0→**1** | 6→6 | 0→0 | 6→6 | **TY +1** |
| generalize/pythia14b_wiki_a100_s42 | 2→2 | 0→**3** | 1→**3** | 0→0 | 7→7 | **TY +3, K≥3 +2** |
| generalize/pythia14b_wiki_a100_s43 | 6→6 | 4→**3** | 7→**3** | 8→**0** | 8→8 | **TY -1, K≥3 -4, Threshold -8** |
| generalize/pythia1b_c4_a100_s42 | 8→8 | 1→1 | 7→7 | 0→0 | 8→8 | 无变化 |
| generalize/pythia1b_c4_a100_s43 | 8→8 | 2→**4** | 5→**6** | 2→2 | 8→8 | **TY +2, K≥3 +1** |
| scale/14b_a050_s42_fp32 | N/A | N/A | N/A | N/A | N/A | **ERROR: 仅 2 代** |
| ~~opt13b_wiki_a100_s42~~ | — | — | — | — | — | **19828 上不存在** |

**关键变化**：
- **TY Granger** 是主要变化项（D123 `kind="f"` fix 影响 TY 结果）
- pythia14b_s42: TY 从 0→3，推高 K≥3 从 1→3
- pythia14b_s43: TY 从 4→3，且 Threshold 从 8→0（脚本版本差异较大，旧脚本可能使用了不同的 threshold 标准）
- pythia1b_c4_s43: TY 从 2→4，K≥3 从 5→6
- scale/14b_a050_s42_fp32 因只有 2 代数据无法运行分析

---
