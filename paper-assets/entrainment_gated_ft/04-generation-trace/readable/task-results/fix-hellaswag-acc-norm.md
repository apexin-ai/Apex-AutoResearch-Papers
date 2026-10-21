# fix hellaswag acc norm

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_hellaswag-acc-norm_20260521T101458_result.json`
- **Structured JSON:** [`ad6e36835fe4d6a1f6c4.json`](../../sessions/ad/ad6e36835fe4d6a1f6c4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。以下是新旧值对比汇报。

---

## 修复汇报：HellaSwag acc → acc_norm

### 修改的脚本
| 脚本 | 修改位置 | 改动 |
|------|---------|------|
| `analyze_boolq_hellaswag.py` | L31-32 `load_accs()` | `d["acc"]` → `d["acc_norm"]` (仅 hellaswag) |
| `analyze_confidence_margin_mc.py` | L101-103 分类逻辑 | `ps["acc"]`/`hs["acc"]` → `ps[acc_field]`/`hs[acc_field]` |

### 核心指标对比：mean_acc (convergence_sigma)

| Config | GDN old→new | RetNet old→new | HGRN2 old→new | σ old→new |
|--------|-------------|----------------|---------------|-----------|
| pure | 0.4641→**0.6076** | 0.4421→**0.5798** | 0.4563→**0.5990** | 0.0091→0.0117 |
| h24-1 | 0.4600→**0.5974** | 0.4446→**0.5824** | 0.4579→**0.6020** | 0.0068→0.0084 |
| h12-1 | 0.4627→**0.6101** | 0.4475→**0.5882** | 0.4635→**0.6066** | 0.0073→0.0096 |
| h6-1 | 0.4633→**0.6056** | 0.4520→**0.5849** | 0.4607→**0.6062** | 0.0048→0.0099 |
| h3-1 | 0.4584→**0.6032** | 0.4454→**0.5777** | 0.4600→**0.6040** | 0.0065→0.0122 |

**差异 ~14pp**，与预期一致。

### Spearman ρ_convergence

| | 旧 (acc) | 新 (acc_norm) |
|--|---------|--------------|
| ρ | **-0.8** | **0.4** |
| p_exact | 0.1333 | 0.5167 |

方向反转且不显著——acc_norm 下 σ 不再随 attention ratio 递减。

### Ambiguity α

| Config | 旧 α | 新 α |
|--------|------|------|
| pure | 0.1006 | **0.1482** |
| h24-1 | 0.1031 | **0.1505** |
| h12-1 | 0.1003 | **0.1482** |
| h6-1 | 0.0908 | **0.1463** |
| h3-1 | 0.0962 | **0.1505** |
| mean | 0.0982 | **0.1487** |
| range | 0.0123 | **0.0042** |

α 升高 ~5pp（更多样本在 acc_norm 下产生 disagreement），但 within-benchmark variation 更小（0.004 < 0.03），α 稳定性更强。

### Confidence Margin (HellaSwag 部分)

| Arch | C1 (hurt vs stayed-right) | | C2 (helped vs stayed-wrong) | |
|------|---|----|---|----|
| | 旧 d / p | 新 d / p | 旧 d / p | 新 d / p |
| GDN | 0.0899 / 0.109 | **0.0092 / 0.999** | -0.5175 / 1.3e-20 | **-0.1657 / 6.1e-4** |
| RetNet | 0.2064 / 1.5e-3 | **-0.035 / 0.453** | -0.4818 / 2.5e-17 | **-0.1322 / 0.014** |
| HGRN2 | 0.2807 / 2.5e-5 | **-0.0622 / 0.274** | -0.5145 / 6.3e-18 | **-0.1638 / 1.4e-3** |

**C1**：acc_norm 下 hurt vs stayed-right 差异消失（3/3 不显著），假说不成立。
**C2**：helped 仍然 margin 更低（3/3 p<0.05），但 effect size 大幅缩小（d 从 ~0.5 降到 ~0.15）。RetNet/HGRN2 的 C1 方向甚至反转（`hypothesis_supported: false`）。

### 更新的 Artifacts（4 个）
1. `hellaswag_per_example.json` — art_20260521_db901c
2. `hellaswag_jaccard_analysis.json` — art_20260521_8cde16
3. `hellaswag_alpha_by_ratio.json` — art_20260521_672592
4. `cross_benchmark_confidence_margin.json` — art_20260521_e8bcdb

---
