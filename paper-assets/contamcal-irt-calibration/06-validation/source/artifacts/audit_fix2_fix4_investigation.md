# Audit Investigation: Fix-2 and Fix-4

## Fix-2: Cohen's d

### d = −1.98 at d100 — VERIFIED ✓

- **源文件路径**: `/root/contamcal-irt-calibration/exp008/exp008_v4_output/exp008_v4_results.json`
- **计算脚本**: `/root/contamcal-irt-calibration/exp008/signal_survival_v4.py`
- **原始信号数据**: `/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_{d000,d100}_s42/`
- **源文件值**: S2_MinKPP cross_model_d100_vs_d000 cohens_d，三 benchmark 均值：
  - MMLU: −1.2203
  - GSM8K: −2.6660
  - ARC: −2.0480
  - **Mean: −1.9781 ≈ −1.98**
- **论文值**: −1.98 (introduction.tex:20, results.tex:123)
- **一致**: Yes
- **注意**: 审计此前只找到 MMLU 单一值 −1.2203，误判为不匹配。实际上 −1.98 是三 benchmark 均值。
- **建议**: 保留，但论文中应注明 "mean across three benchmarks" 以便溯源。

### |d| > 1.4 at d005 — PARTIALLY FALSE ⚠️

- **源文件**: 无持久化 JSON（exp008_v4 仅对 d005 计算 within-model AUC，不计算 cross-model Cohen's d）
- **复现计算** (来自 worker_analysis_cohens-d-source-trace_20260522): paired d005 vs d000 for S2_MinKPP:
  - MMLU: −1.386 → |d| = 1.386 (**< 1.4 ❌**)
  - GSM8K: −1.816 → |d| = 1.816 (> 1.4 ✓)
  - ARC: −1.962 → |d| = 1.962 (> 1.4 ✓)
  - Mean: |d| = 1.721 (> 1.4 ✓)
- **论文值**:
  - introduction.tex:20: "|d| > 1.4 across benchmarks at d005" — **MMLU 不满足** (1.386 < 1.4)
  - results.tex:123: "|d| > 1.4 at d005" — 如果指均值则正确，但含义模糊
- **一致**: 部分。均值满足，但 "across benchmarks" 措辞暗示每个 benchmark 都满足，MMLU 差 0.014。
- **建议**:
  - 方案 A: 改为 "|d| > 1.2 across benchmarks" (MMLU |d|=1.39 满足)
  - 方案 B: 改为 "|d| > 1.4 on GSM8K and ARC; |d| = 1.39 on MMLU"
  - 方案 C: 删除 "across benchmarks"，仅写 "|d| > 1.4 at d005"（保持均值层面正确）

---

## Fix-4: Qwen-7B GSM8K

### 计算口径

| Seed | d000 | d100 | Δ |
|------|------|------|---|
| s0 | 73.31% | 81.20% | +7.89pp |
| s42 | 70.58% | 81.65% | +11.07pp |
| s123 | — | — | +9.18pp |
| **mean(s42, s123)** | — | — | **+10.13pp ≈ +10.1pp** |

数据来源：
- s0: `/root/autodl-tmp/exp001/eval_results_v2/qwen7b_d{000,100}_s0/gsm8k_results.json` (cqa1 确认)
- s42: cqa1 eval results（由 `data_audit_table1.md` 记录）
- s123: `data_audit_table1.md` 记录

### "+10.1pp" 已不在当前论文中

原始审计针对的是旧版论文。`data_audit_table1.md` 已验证 +10.1pp = mean(s42=11.07, s123=9.18) = 10.13pp ✓。

### 当前论文值: +11.1pp — 存在不一致 ⚠️

当前 `tab:gsm8k_transfer` (appendix.tex:60):
```
Qwen-7B & −1.8pp & +11.1pp & ±0.9 & Reversal
```

- **+11.1pp** 是 s42 单种子值 (11.07 rounded)，不再是 mean(s42,s123)=10.1pp
- **Range ±0.9** 仍然是旧的 half-range = (11.07−9.18)/2 = ±0.95，这是基于 mean=10.1 的计算
- **不一致**: 如果报告 s42 值 (+11.1)，Range ±0.9 没有意义（不含 s123=+9.18）；如果报告 mean，值应为 +10.1
- 同表其他行（Qwen-14B +13.1pp, OLMo-2 +2.1pp）仍使用 mean(s42,s123)，只有 Qwen-7B 改了

### results.tex 文本问题 ⚠️

results.tex:57: "Volume effects are ruled out: d005 (+1.5% data) yields +11.1pp for Qwen-7B"

这句话暗示 d005 的 GSM8K delta 是 +11.1pp，但实际 d005 delta:
- s42: 70.58 → 76.95 = **+6.37pp** (≠ 11.1)
- s0: 73.31 → 78.32 = **+5.01pp**

+11.1pp 是 d100 值，不是 d005。句子歧义：作者可能想表达 "仅 1.5% 数据就产生大效应（d100 达 +11.1pp）"，但文法上读作 "d005 产出 +11.1pp"。

### 建议

1. **tab:gsm8k_transfer**: 恢复为 mean(s42,s123)=+10.1pp + Range ±0.9（与同表其他行统一口径），或改为 +11.1pp (s42) 并删除 Range（改为单种子标注）
2. **results.tex:57**: 改为 "Volume effects are ruled out: d005 (+1.5\% data) already yields +6.4pp for Qwen-7B, over half the d100 transfer (+11.1pp)"
3. **introduction.tex:14**: "+13pp" 指 Qwen-14B，正确无误
