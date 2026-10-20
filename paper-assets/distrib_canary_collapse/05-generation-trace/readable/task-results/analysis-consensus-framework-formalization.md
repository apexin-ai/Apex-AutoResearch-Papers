# analysis consensus framework formalization

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_consensus_framework_formalization_20260515T085017_result.json`
- **Structured JSON:** [`98fed58c31810a05f03d.json`](../../sessions/98/98fed58c31810a05f03d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出完成。两个 artifact 已注册：

**`art_20260515_1e9698`** — `consensus_framework.md`
- 数学定义：$R(X,Y;\tau_m,\tau_s) = \mathbb{1}[C(X,Y;\tau_s) \geq \lceil\tau_m \cdot K\rceil]$
- 阈值理由：K-1/K 因 TY 在 T=10 下 power 仅 5-20%；3/4 seed 因 binomial FPR ≈ 4.8×10⁻⁴
- 9 配置 sensitivity grid：从 (3/5,2/4) 的 12 robust 到 (5/5,4/4) 的 3 robust
- Stability：**entropy→d1/d2/d3 和 ece→d1 在全部 9/9 配置下 stable**
- FPR/FNR 表：consensus FPR=0%, FNR=0%（FNR circular 已标注）
- Scheffer et al. 联系：EWS 文献的多指标共识原则，我们从多*指标*扩展到多*方法*
- 6 条 limitations 诚实声明

**`art_20260515_c4694f`** — `consensus_sensitivity_table.json`
- 完整 sig_seeds 矩阵（16 pairs × 5 methods）
- 9 配置 × robust pair 列表 + methods_sig_per_pair
- pair_stability（每对在多少配置下 robust + 原因）
- error_rates + TY power reference

关键数字确认：
- 默认 (4/5, 3/4)：6 robust pairs（entropy→d1/d2/d3, ece→d1/d2/d3）
- token_entropy→distinct 稳定性：**9/9**（预期命中）
- ece→d2/d3：7/9（TY dissenter）
- canary→perplexity：3/9（符合伪回归预期）
- self_bleu/effective_rank：0-2/9（伪回归确认）

---
