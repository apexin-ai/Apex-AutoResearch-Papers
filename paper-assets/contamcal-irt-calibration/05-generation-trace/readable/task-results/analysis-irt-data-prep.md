# analysis irt data prep

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_irt-data-prep_20260519T185034_result.json`
- **Structured JSON:** [`4cce654cb734ae78762d.json`](../../sessions/4c/4cce654cb734ae78762d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据收集完毕，汇报如下：

---

## 1. 25/25 seed=42 数据完整性

**westd-29999: 25/25 全部完整 ✓**

| 模型 | d000 | d005 | d025 | d050 | d100 |
|------|------|------|------|------|------|
| phi4 | ✓ | ✓ | ✓ | ✓ | ✓ |
| qwen14b | ✓ | ✓ | ✓ | ✓ | ✓ |
| qwen7b | ✓ | ✓ | ✓ | ✓ | ✓ |
| gemma2 | ✓ | ✓ | ✓ | ✓ | ✓ |
| olmo2 | ✓ | ✓ | ✓ | ✓ | ✓ |

每个目录都有 correctness_matrix.json + item_responses.json + eval_results.json + .done。evaluate.py md5 = `001a9bc23f808c47d25ef9eaeecb81f1`（37591 bytes）— 与 reference hash 一致。

---

## 2. IRT 输入格式 vs 当前数据格式的 GAP

**2PL+γ Stan 模型需要**：
- `y[N_models, N_items]`: 二值响应矩阵 (int 0/1)
- `exposure[N_models, N_items]`: 连续曝光矩阵

**现有数据**：
- `correctness_matrix.json` 格式：`{"mmlu": [bool, bool, ...], "arc_challenge": [bool, bool, ...]}`
- `eval_results.json` 格式：嵌套 `benchmarks.{bench}.per_item[].correct`

**GAP**：

| 问题 | 详情 |
|------|------|
| **目录命名不兼容** | westd 用短名 `phi4_d000`，exp006 代码的 DOSAGE_PATTERN 期望 `{Model}_d{NNN}_s{NN}` 格式（如 `Qwen2.5-7B_d000_s42`），正则匹配失败 |
| **无曝光分数文件** | westd 上不存在 RRF 聚合的 exposure 文件；exp002 信号仅有 Qwen2.5-7B 的，其余 4 个模型家族无信号数据 |
| **格式转换** | correctness_matrix.json 是 per-dir 的 `{bench: [bool]}` 格式，需汇聚成 `(J=25, I) numpy` 矩阵 |

**可行捷径**：用 oracle exposure（ground-truth dosage 作为曝光强度：`exposure[i,j] = dosage_i * 1.0`），无需信号计算。`exp001/fit_irt_dose_response.py` 已能读短名目录构建 response matrix，只需在此基础上加 gamma 项或直接构建 numpy 矩阵喂 Stan。

---

## 3. M025 旧版 evaluate.py 影响范围

**westd-29999: 不受影响 ✓**
- evaluate.py md5 hash 一致，所有 25 个 seed=42 eval 在 May 19 运行，版本正确

**cqa1-21977: 5 个 s123 eval 受影响，3 个尚未补跑**

| 目录 | 状态 | 说明 |
|------|------|------|
| qwen7b_d000_s123 | ✓ 已补跑 | eval_meta 确认 md5 正确 |
| qwen7b_d005_s123 | ✓ 已补跑 | eval_meta 确认 md5 正确 |
| qwen7b_d025_s123 | ✗ **空目录** | eval 失败或未完成 |
| qwen7b_d050_s123 | ✗ **未补跑** | 仅有 old 备份 |
| qwen7b_d100_s123 | ✗ **未补跑** | 仅有 old 备份 |

旧版备份在 `*_old_20260520` 目录中保留。

---

## 4. 下一步

1. **补跑 cqa1 eval**：qwen7b_d{025,050,100}_s123 需要用新版 evaluate.py 重跑（先 SCP 同步脚本，验证 md5）
2. **数据格式转换**：写脚本从 25 个 `correctness_matrix.json` 构建 `(25, I)` numpy response matrix + oracle exposure matrix（`exposure[i,j] = dosage_i/100`）
3. **2PL+γ fitting**：可直接用现有 Stan 模型 `contam_irt_2pl_gamma.stan`，通过 `run_irt_calibration.py --response-matrix --exposure-matrix` 模式运行（绕过目录命名不兼容问题）
4. **RRF exposure**（如需）：需对 phi4/qwen14b/gemma2/olmo2 的 25-5=20 个模型-dosage 组合运行 `compute_signals`，GPU-intensive

---
