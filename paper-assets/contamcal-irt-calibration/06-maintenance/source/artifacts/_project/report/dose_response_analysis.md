# Dose-Response Analysis — Eval Results Summary
**Generated**: 2026-05-14  
**Source**: `/root/autodl-tmp/exp001/eval_results/`

## 1. Completed Eval Results

### Legacy Format (original MC)

| Model | Dosage | Seed | MMLU | GSM8K | ARC-C | HumanEval |
|-------|--------|------|------|-------|-------|-----------|
| 0.5B | d000 | s42 | 0.4049 | 0.3647 | 0.3780 | 0.1098 |
| 0.5B | d000 | s123 | 0.4182 | 0.3404 | 0.3976 | 0.1037 |
| 0.5B | d005 | s42 | 0.2929 | 0.3601 | 0.2858 | 0.0793 |
| 0.5B | d025 | s42 | — | — | — | — |
| 0.5B | d100 | s42 | 0.2322 | 0.3571 | 0.2270 | 0.0854 |
| 1.5B | d000 | s42 | 0.5753 | 0.6368 | 0.7756 | 0.1280 |
| 1.5B | d000 | s123 | 0.5762 | 0.6331 | 0.7662 | 0.1707 |
| 1.5B | d005 | s42 | — | — | — | — |
| 1.5B | d100 | s42 | 0.5933 | 0.6497 | 0.7688 | 0.3049 |
| 3B | d000 | s42 | 0.6337 | **0.1168** ⚠️ | 0.8217 | 0.1159 |
| 3B | d000 | s123 | 0.6362 | **0.1759** ⚠️ | 0.8294 | 0.0854 |
| 3B | d005 | s42 | — | — | — | — |
| 3B | d100 | s42 | — | — | — | — |

### Aligned Format

| Model | Dosage | Seed | Variant | MMLU | GSM8K | ARC-C | HumanEval |
|-------|--------|------|---------|------|-------|-------|-----------|
| 0.5B | d000 | s42 | aligned | 0.3979 | 0.3692 | 0.4693 | 0.1098 |
| 0.5B | d000 | s42 | para_aligned | 0.4428 | 0.2807 | 0.4792 | 0.1154 |

### Raw Baselines (no SFT)

| Model | MMLU | GSM8K | ARC-C | HumanEval | Status |
|-------|------|-------|-------|-----------|--------|
| 0.5B | — | — | — | — | empty dir |
| 1.5B | — | — | — | — | no dir |
| 3B | — | 0.6050 | — | 0.0000 | partial (gsm8k only) |

## 2. Anomalies

- **3B GSM8K 极低**: d000_s42=0.1168, d000_s123=0.1759, 远低于 raw baseline 0.6050。可能是 eval 格式问题（legacy MC 格式对 3B 生成式任务不适配），需要 aligned eval 来修正。
- **1.5B d100 > d000**: d100 在 MMLU/GSM8K/HumanEval 上均高于 d000，但 ARC-C 持平。对 0.5B 则相反（d100 显著下降）。提示污染效果与模型容量交互。
- **3B_raw HumanEval=0.0**: 全部失败，可能是生成格式问题。

## 3. 缺失数据点清单

### 3.1 Legacy Eval 缺失 (3 个)

| Checkpoint | Priority | Note |
|-----------|----------|------|
| 0.5B_d025_s42 | HIGH | dose-response 曲线关键插值点 |
| 1.5B_d005_s42 | HIGH | 中间剂量点 |
| 3B_d005_s42 | HIGH | 中间剂量点 |
| 3B_d100_s42 | HIGH | 高剂量对比 |

### 3.2 Aligned Eval 缺失/进行中 (11+ 个)

| Checkpoint | Status | Note |
|-----------|--------|------|
| 0.5B_d005_s42_aligned | dir exists, empty | 可能在跑或失败 |
| 0.5B_d000_s123_aligned | no dir | 未开始 |
| 0.5B_d025_s42_aligned | no dir | 需先完成 legacy |
| 0.5B_d100_s42_aligned | no dir | 未开始 |
| 1.5B_d000_s42_aligned | dir exists, empty | 可能在跑或失败 |
| 1.5B_d000_s123_aligned | no dir | 未开始 |
| 1.5B_d005_s42_aligned | no dir | 未开始 |
| 1.5B_d100_s42_aligned | no dir | 未开始 |
| 3B_d000_s42_aligned | dir exists, empty | 可能在跑或失败 |
| 3B_d000_s123_aligned | no dir | 未开始 |
| 3B_d005_s42_aligned | no dir | 未开始 |
| 3B_d100_s42_aligned | no dir | 未开始 |

### 3.3 Raw Baselines 缺失

| Model | Status |
|-------|--------|
| 0.5B_raw | dir exists, empty |
| 1.5B_raw | no dir at all |
| 3B_raw | partial (only gsm8k + humaneval) |

## 4. 完成度统计

| 类别 | 已完成 | 总需 | 完成率 |
|------|--------|------|--------|
| Legacy eval | 10/13 | 13 | 77% |
| Aligned eval | 2/13 | 13 | 15% |
| Raw baselines | 0.3/3 | 3 | ~10% |
| **总计** | 12.3/29 | 29 | 42% |

## 5. 0.5B Dose-Response 趋势 (Legacy, 唯一完整序列)

| Dosage | MMLU | GSM8K | ARC-C | HumanEval |
|--------|------|-------|-------|-----------|
| d000 (clean) | 0.405 | 0.365 | 0.378 | 0.110 |
| d005 (5%) | 0.293 ↓27.7% | 0.360 ↓1.3% | 0.286 ↓24.3% | 0.079 ↓28.2% |
| d025 (25%) | — | — | — | — |
| d100 (100%) | 0.232 ↓42.7% | 0.357 ↓2.1% | 0.227 ↓39.9% | 0.085 ↓22.7% |

**初步观察**: MMLU 和 ARC-C 对污染剂量高度敏感（~40% 降幅），GSM8K 几乎无影响（~2% 降幅），HumanEval 中等敏感。这与"MC 格式记忆"假说一致——污染主要破坏选择题能力，生成式任务（GSM8K）相对免疫。
