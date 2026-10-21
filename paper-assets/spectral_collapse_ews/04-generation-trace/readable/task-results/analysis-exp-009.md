# analysis exp 009

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_009_20260519T161544_result.json`
- **Structured JSON:** [`54e7c068ef97d029bd45.json`](../../sessions/54/54e7c068ef97d029bd45.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp_009 分析完成，registry 已更新为 DONE。

## 核心结论

**log_det dip 梯度确认 r_crit ∈ (0.25, 0.3]**：
| r | Dip Δ | Dip Gen | 模式 |
|---|-------|---------|------|
| 0.20 | −8.37 | Gen 2 | dip-then-recovery |
| 0.25 | −4.55 | Gen 1 | dip-then-recovery (浅) |
| 0.30 | −0.55 | — | 无 dip，单调上升 |

**关键发现**：
1. r=0.25 的 dip 仍可测（−4.55），但 controller Δ_t = −0.0019 刚好 < τ=0.002，确认 **Type II boundary case**（controller silence at threshold edge）
2. 终态 r=0.25 vs r=0.3 几乎无差异（ppl 13.29 vs 13.38, d4 0.36 vs 0.34），区别仅在早期 spectral dynamics
3. σ₁ 单调下降 1943→703 (−64%)，谱持续扁平化但无 collapse
4. Checkpoints: `gen_0` ~ `gen_10` 完整存于 `/root/autodl-tmp/spectral_collapse_ews/checkpoints_phase1/fixed_mix_r025_seed42/`

产出已注册为 `art_20260519_1fc711`。

---
