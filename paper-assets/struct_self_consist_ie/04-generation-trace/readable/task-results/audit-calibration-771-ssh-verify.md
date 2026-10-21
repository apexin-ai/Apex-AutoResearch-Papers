# audit calibration 771 ssh verify

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_calibration-771-ssh-verify_20260519T184510_result.json`
- **Structured JSON:** [`5c295c6af113604452a5.json`](../../sessions/5c/5c295c6af113604452a5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查完成。以下是完整的来源链和发现的问题。

---

## .771 来源链

| 环节 | 值 |
|------|------|
| **结果文件** | `output/calibration_baseline_results.json`, key `"Few-NERD"` |
| **生成脚本** | `scripts/calibration_baseline.py` |
| **数据源** | `output/exp_027_fewnerd_n16/samples.jsonl` (5000 行) |
| **5K 来源** | 4 个 shard × 1250 = 5000，**前 5000 个测试实例**（顺序截取，非随机抽样） |
| **Checkpoint** | `checkpoints/qwen3-8b-fewnerd-exp021-merged` (3-epoch LoRA merged) |
| **N / T** | N=16, T=1.0 |
| **评估** | **非 gold-filtered**，span-based F1 (text, type, start, end) |
| **Seed** | 单次运行，无多 seed 平均 |
| **精确值** | `greedy_f1 = 0.7711562403689257` |

## 发现的问题

### 1. Caption N=8 与实际 N=16 不符
`calibration_baseline_results.json` 中三个数据集的 `n_samples_per_instance`:
- SciERC: **8** (正确)
- CoNLL: **16** (caption 说 N=8，错误)
- Few-NERD: **16** (caption 说 N=8，错误)

N 不影响 greedy F1，但**影响 LP selection F1**。表中 Raw LP .785 和 MF-Platt .778 是在 N=16 候选中选择的结果，不能标注为 N=8。

### 2. Gold-filtering 不一致
- **.771** = 非 gold-filtered（全部 5000 实例，空 gold 实例的 F1=1.0 被计入）
- **.748** (tab:fewnerd 主表) = gold-filtered（32,565 / 37,648 实例）

Caption 说"full-set greedy is .748"暗示差异仅因样本量，但实际上是 gold-filtering 不同。验算：5K 中 4351 个 gold-filtered 实例的 greedy F1 ≈ 0.748（与 exp_027 results.json 吻合），剩余 649 个 gold-empty 实例的 mean F1 ≈ 0.925，拉高了整体均值。

### 3. 单 seed，非 3-seed 均值
主表 (tab:fewnerd) 是 3-seed mean，calibration table 是单次运行。

### 4. 顺序截取而非随机抽样
run.log 显示 shard_0 加载 `[index 0:1250]`，直接取 FewNERD 测试集前 5000 条，无 shuffle、无 random seed。

### 建议修复
Caption 应改为类似：`Few-NERD evaluated on the first 5K test instances (non-gold-filtered greedy .771; gold-filtered .748, matching Table~\ref{tab:fewnerd}). CoNLL and Few-NERD use $N{=}16$; SciERC uses $N{=}8$.`

---
