# audit number consistency

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_number_consistency_20260527T233920_result.json`
- **Structured JSON:** [`630c3c0a220a6997c917.json`](../../sessions/63/630c3c0a220a6997c917.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have all the data needed. Here's the full cross-check report.

---

## 数字一致性核对报告

### 一致通过的数字

| 数字 | 位置一致性 | 验证 |
|------|-----------|------|
| LoRA-only CAR 54.83% ± 2.25% | 主表 + 正文 + appendix per-task 表 | (57+52.5+55)/3=54.833, σ=2.255 ✓ |
| Per-seed s0=57, s1=52.5, s2=55 | 主表 ↔ appendix per-task 表 | ✓ |
| λ=0.005 CAR 54.5% ± 2.29% | 主表 + appendix | (57+54+52.5)/3=54.5, σ=2.291 ✓ |
| λ=0.01 CAR 56.33% ± 1.61% | 主表 + appendix | (57+57.5+54.5)/3=56.333, σ=1.607 ✓ |
| λ=0.1 CAR 58.25% ± 0.35% (2 seeds) | 主表 + 正文 + figure caption | (58+58.5)/2=58.25, σ=0.354 ✓ |
| Baseline CAR 26.8±1.6, TSR 74.7±1.5 | 主表 + 正文引用 | ✓ |
| Null distribution μ=54.67, σ=2.04 | 正文 + appendix | {57,52.5,55,57,54,52.5} → μ=54.667, σ=2.041 ✓ |
| p ≈ 0.071 (two-tailed) | abstract + 主表 caption + 正文 + fig caption + discussion | 全部一致 ✓ |
| p = 0.036 (one-tailed) | claim3 脚注 + appendix | ✓ |
| "within 0.33 pp" | 正文 | 54.83 − 54.5 = 0.33 ✓ |
| "~28 percentage points" | 正文 + abstract + discussion | 54.83 − 26.8 = 28.03 ✓ |
| "~3.6 pp" effect size | 正文 | 58.25 − 54.67 = 3.58 ✓ |
| "within 0.3σ" (stepwise) | 正文 + appendix | (55.3−54.67)/2.04 = 0.31 ✓ |
| Phase 2 ablation CAR=57.5% (s2) | 正文 + 脚注 "single seed" | ✓ |
| λ=0.1 标注 "2 seeds"/"two of three seeds" | 主表 + 脚注 + 正文 + fig caption | 全部正确标注 ✓ |
| SSR/TSR 0.51–0.57 (LoRA fine-tuned) | claim3 + discussion + appendix | appendix 表: 0.515–0.573 ✓ |
| All per-task table internal arithmetic | appendix | 逐项验证全部正确 ✓ |

### 不一致项

#### 1. **SSR/TSR baseline: 0.33 (正文) vs 0.39 (appendix)** — 严重

- **claim3.tex:30** — "SSR/TSR ratio increases from **0.33** (baseline) to 0.51--0.57"
- **discussion.tex** — "SSR/TSR increases from **0.33** to 0.51--0.57"
- **appendix SSR 表** — Pi0.5 baseline: TSR=71.5, SSR=28.0, SSR/TSR=**0.392**
- **appendix 正文** — "Pi0.5 baseline achieves SSR/TSR = **0.39**"

appendix 内部一致 (28.0/71.5 = 0.3916 ≈ 0.39)，但正文写的是 0.33。**应将正文的 0.33 改为 0.39**，或如果 0.33 来自 3-seed baseline 数据（不同于 appendix 的 single-evaluation），需要补充 3-seed SSR 数据。

#### 2. **SSR 表 LoRA-only TSR 值全为 51.5** — 严重

appendix SSR/TSR 表中 LoRA-only 三个 seed 的 TSR 全部是 **51.5%**：
```
LoRA-only  s0  51.5  29.5  0.573
LoRA-only  s1  51.5  27.0  0.524
LoRA-only  s2  51.5  26.5  0.515
```

但主表 (tab:avoidance_source) 显示 LoRA-only TSR = **49.7 ± 3.2**。如果三个 seed 全是 51.5，则 mean=51.5, std=0，与 49.7±3.2 矛盾。三个 seed TSR 恰好相同极不可能，疑为占位符或 copy-paste 错误。**需要填入真实的 per-seed TSR 值**，并相应修正 SSR 和 SSR/TSR。

#### 3. **Threshold 表 LoRA s0 dfCAR = 56.5 vs per-task CAR = 57.0** — 轻微

- appendix threshold 表: LoRA s0 = 56.5 (在所有 τ_d)
- appendix per-task 表: LoRA s0 = 57.0 (from (74+66+68+20)/4 = 57.0)
- 表文说 "no episodes exhibit sub-threshold displacement"，所以 dfCAR 应等于 CAR

差 0.5 pp (1 episode out of 200)。此外 **LoRA s2 缺失**（SDF005/SDF01 各有 3 seed，LoRA 只有 2 个）。需核实数据源并补全。

#### 4. **TSR 降幅 "21–25 pp" 和 "49.7–54.0%" 未包含 λ=0.1** — 建议修正

claim3.tex: "Fine-tuning degrades TSR by ~21–25 pp (74.7% → 49.7–54.0%)"。但 λ=0.1 的 TSR=48.0%，对应降幅 26.7 pp，超出 "21–25" 范围。如果句子意在覆盖所有 fine-tuned 条件，应改为 "~21–27 pp (74.7% → 48.0–54.0%)"；否则应注明 "at λ ≤ 0.01"。

### 旧值残留扫描

| 旧值 | 扫描结果 |
|------|---------|
| 0.039 | **未发现**，全部文件无匹配 ✓ |
| 0.025 | 仅出现在 appendix SDF computation 的 σ₁=0.025（合法使用） ✓ |
| z=1.76 / z = 1.76 | 仅出现在 appendix permutation test 作为新计算 (58.25−54.67)/2.04=1.76，非旧值残留 ✓ |

### 总结

- **需立即修正**：#1 SSR/TSR baseline 0.33→0.39（claim3 + discussion 两处）；#2 SSR 表 LoRA TSR 全为 51.5 需替换为真实值
- **需核实**：#3 threshold 表 LoRA s0 差 0.5 pp + 缺 s2
- **建议修正**：#4 TSR 降幅范围

---
