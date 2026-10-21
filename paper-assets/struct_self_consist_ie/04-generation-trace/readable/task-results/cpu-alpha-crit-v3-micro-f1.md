# cpu alpha crit v3 micro f1

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_cpu_alpha_crit_v3_micro_f1_20260521T094702_result.json`
- **Structured JSON:** [`246fe926f9a4d5cb2d94.json`](../../sessions/24/246fe926f9a4d5cb2d94.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总输出：

---

## 1. MF4v2 micro_f1 原始数据

| 实验 | n | greedy_f1 | mv_f1 | oracle_f1 | degen | Δ_SC (pp) |
|------|---|-----------|-------|-----------|-------|-----------|
| fewnerd_s42 | 32565 | 0.7909 | 0.7781 | 0.8802 | 9.1% | −1.28 |
| fewnerd_s123 | 32565 | 0.7909 | 0.7844 | 0.8897 | 9.2% | −0.64 |
| fewnerd_s456 | 32565 | 0.7916 | 0.7857 | 0.8855 | 8.1% | −0.58 |
| conll_s123 | 2756 | 0.9129 | 0.9157 | 0.9543 | 60.4% | +0.28 |
| conll_s456 | 2756 | 0.9118 | 0.9122 | 0.9500 | 60.2% | +0.04 |
| scierc_s42 | 529 | 0.6663 | 0.6657 | 0.7839 | 13.4% | −0.06 |
| scierc_s123 | 529 | 0.6663 | 0.6689 | 0.7789 | 11.0% | +0.26 |
| scierc_s456 | 529 | 0.6663 | 0.6687 | 0.7795 | 12.1% | +0.24 |

> CoNLL seed42 MF4v2 未执行，仅 2-seed。

## 2. 重算后 α_crit 表（multi-seed mean±σ）

| Dataset | greedy | mv | oracle | Δ_SC (pp) | α_crit | δ | α_crit_eff |
|---------|--------|------|--------|-----------|--------|------|------------|
| FewNERD | 0.7911 | 0.7828 | 0.8851 | **−0.83±0.38** | 0.643 | 8.8% | 0.705 |
| CoNLL | 0.9124 | 0.9140 | 0.9522 | **+0.16±0.17** | 0.842 | 60.3% | 2.121 |
| SciERC | 0.6663 | 0.6678 | 0.7808 | **+0.15±0.18** | 0.501 | 12.2% | 0.571 |

## 3. 论文中受影响位置

tex 文件中**无直接引用旧的 -9.21/-1.37/-3.03 数值**。这些数值仅存在于：
- `artifacts/d220_correction_notes.md`（已更新为 v3）
- `artifacts/alpha_crit_table.md`（已更新为 v3）
- `artifacts/manifest.yaml` 中旧版描述（历史记录，无需修改）
- `decisions.yaml`, `mistakes.yaml`, `ROADMAP.md` — 决策/错误日志（历史记录）

论文 tex 中 `theory.tex:19` 有 `−3.09pp at N=8` 和 `−0.87pp` 等数值，但这些是 θ=2/N sweep 数据（不同实验），不是 α_crit 表数据。

## 4. 新旧数值对比

| Dataset | v2 Δ (macro, 错误) | v3 Δ (micro, 正确) | 变化 |
|---------|-------|-------|------|
| FewNERD | −9.21pp | −0.83pp | 11× smaller, same sign |
| CoNLL | −1.37pp | +0.16pp | **Sign flip** |
| SciERC | −3.03pp | +0.15pp | **Sign flip** |

核心结论修正：~~"SC universally fails"~~ → **"MV ≈ greedy (|Δ| < 1pp)"**。SC 既不显著改善也不显著恶化，bottleneck 是 alignment 不足，非 aggregation 本身。

---
