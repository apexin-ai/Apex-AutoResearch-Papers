# code exp003 rrf prep

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp003-rrf-prep_20260516T021040_result.json`
- **Structured JSON:** [`7c2408e9936659d8e474.json`](../../sessions/7c/7c2408e9936659d8e474.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研完成。以下是汇总报告。

---

## 1. d000_s42 Symlink 状态：**不需要修复**

- Symlink 已存在：`Qwen2.5-3B_d000_a32_s42 -> Qwen2.5-3B_d000_s42`（创建于 May 16 09:10）
- `Qwen2.5-3B_d000_s42/lora_adapter/adapter_config.json` 确认 `lora_alpha: 32` ✓
- Eval results 目录中也已有 `Qwen2.5-3B_d000_s42_a32_aligned` 条目

## 2. RRF 代码现状：**存在，需修改**

`/root/contamcal-irt-calibration/exp003/` 包含 3 个文件：

| 文件 | 功能 |
|------|------|
| `rrf_aggregation.py` | 主 RRF 聚合（k=60，rank fusion，min-max 归一化到[0,1]） |
| `ablations.py` | 5 种消融对比（rank avg、single signal、calibrated weighted、FP injection、degraded 2-signal） |
| `evaluate_rrf.py` | 评估 pipeline（AUC-ROC、AP、precision@k、ROC/分布/鲁棒性图） |

**需修改的问题**：
- `SIGNAL_KEYS` 仍包含 `s3_constat`，需按 D098 决策删除，只保留 `s1_embedding`, `s2_minkpp`, `s4_selfcritique`
- `ablations.py` 的 `degraded_2signal()` 使用 `s3_constat + s4_selfcritique`，需要更新或移除
- `detect_available_signals()` 动态检测的机制意味着缺失 s3 文件时不会报错，但常量定义仍不一致

## 3. Signals 完成度矩阵

### 0.5B + 1.5B（seed=42）：全部完成 ✅

| Model | Dosage | mmlu | gsm8k | arc_challenge |
|-------|--------|------|-------|---------------|
| 0.5B | d000 | s1✓ s2✓ s4✓ | s1✓ s2✓ s4✓ | s1✓ s2✓ s4✓ |
| 0.5B | d005 | s1✓ s2✓ s4✓ | s1✓ s2✓ s4✓ | s1✓ s2✓ s4✓ |
| 0.5B | d025 | s1✓ s2✓ s4✓ | s1✓ s2✓ s4✓ | s1✓ s2✓ s4✓ |
| 0.5B | d100 | s1✓ s2✓ s4✓ | s1✓ s2✓ s4✓ | s1✓ s2✓ s4✓ |
| 1.5B | d000 | s1✓ s2✓ s4✓ | s1✓ s2✓ s4✓ | s1✓ s2✓ s4✓ |
| 1.5B | d005 | s1✓ s2✓ s4✓ | s1✓ s2✓ s4✓ | s1✓ s2✓ s4✓ |
| 1.5B | d025 | s1✓ s2✓ s4✓ | s1✓ s2✓ s4✓ | s1✓ s2✓ s4✓ |
| 1.5B | d100 | s1✓ s2✓ s4✓ | s1✓ s2✓ s4✓ | s1✓ s2✓ s4✓ |

### 3B（seed=42）：大量缺失

| Model dir | mmlu | gsm8k | arc_challenge | 状态 |
|-----------|------|-------|---------------|------|
| d000_v2_s42 | s1✓ s2✓ s3✓ | s1✓ s2✓ s3✓ | s1✓ s2✓ s3✓ | **缺 s4**，且有废弃的 s3 |
| d000_s42 | **无信号目录** | — | — | D076 重训版本，尚未计算信号 |
| d005_s42 | s1✓ s2✓ | s1✓ s2✓ | s1✓ s2✓ s4✓ | **mmlu/gsm8k 缺 s4** |
| d025_s42 | s4✓ | — | — | **极度不完整**（仅 s4_mmlu） |
| d025_v3_s42 | s1✓ s2✓ | s1✓ s2✓ | s1✓ s2✓ | **全部缺 s4** |
| d100_s42 | s1✓ s2✓ | s1✓ s2✓ s4✓ | s1✓ s2✓ s4✓ | **mmlu 缺 s4** |

### 3B（seed=123）：部分完成

| Model dir | mmlu | gsm8k | arc_challenge | 状态 |
|-----------|------|-------|---------------|------|
| d005_s123 | s1✓ s2✓ s4✓ | s1✓ s2✓ s4✓ | s1✓ s2✓ s4✓ | **完整** ✅ |
| d025_s123 | s1✓ s2✓ (s4 chunked) | s1✓ s2✓ s4✓ | s1✓ s2✓ s4✓ | **mmlu s4 未合并**（7 chunks 待 merge） |
| d100_a32_s123 | s1✓ s2✓ | — | — | **仅 mmlu 的 s1+s2**，极不完整 |

## 4. RRF 聚合的 Blockers

1. **3B s42 系列信号严重不完整**：d000_s42（D076 重训版）完全没有信号目录；d005/d025/d025_v3/d100 各有不同程度的 s4 缺失。这与 D076 重训流水线尚在进行中一致。
2. **d000_v2_s42 仅有 s3（已废弃信号），无 s4**：无法用于 RRF 融合。
3. **d025_s123 的 s4_mmlu 在 chunks 中未合并**：需要运行 merge 脚本。
4. **d100_a32_s123 几乎是空的**：仅 2 个文件。
5. **RRF 代码需更新**：从 SIGNAL_KEYS 中移除 s3_constat 以匹配 D098 决策。
6. **命名不一致**：信号目录中同时存在 `d000_v2_s42`（旧）和应该使用的 `d000_s42`（D076 新），RRF 需要明确用哪个。

**结论**：0.5B 和 1.5B 可以立即跑 RRF 聚合。3B 系列需等 D076 信号计算流水线完成后才能跑。

---
