# code exp 006 d023 code mod sanity

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_006_d023_code_mod_sanity_20260514T174350_result.json`
- **Structured JSON:** [`dcb3b3fcd0b2fcc57bd2.json`](../../sessions/dc/dcb3b3fcd0b2fcc57bd2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Sanity Run 结果摘要

### 代码修改 (4项)

| 修改项 | 状态 | 说明 |
|--------|------|------|
| `--max-items N` | 已完成 | default=None, 独立于 `--dry-run` 工作 |
| `--aligned-only` | 已存在 | 代码已有此功能，无需修改 |
| 删除 ADVI fallback | 不需要 | 代码中无 ADVI 代码 |
| exp-002 signals 替代 oracle dosage | 已完成 | 新增 `--signals-dir` 参数 + `load_exp002_signals()` 函数 |

### GSM8K 300-item Sanity Run

**配置**: 0.5B scale, seed 42, aligned-only, 4 models (d000/d005/d025/d100), 300 items, 4pl_gamma + joint-fit

**总耗时**: 376.6s (~6.3min)

#### Per-benchmark IRT fit (300 items)
| 指标 | 值 |
|------|-----|
| gamma | mean=-3.93, 95%CI=[-5.14, -2.57] |
| ci_excludes_zero | True |
| Rhat | 1.0062 |
| ESS | 503 |
| Divergences | 0 (0.00%) |
| Sampling time | 23.5s |

#### Joint fit (1319 items, 未截断)
| 指标 | 值 |
|------|-----|
| gamma | mean=0.35, 95%CI=[-0.65, 1.40] |
| ci_excludes_zero | False |
| Rhat | 1.0081 |
| ESS | 956 |
| Divergences | 0 (0.00%) |
| Sampling time | 190.9s |

#### 评估指标 (MAE, 越低越好)
| Method | MAE |
|--------|-----|
| B0_raw | 0.019 |
| B1_remove_rescore | 0.019 |
| B5_emperor | 0.019 |
| B4_linear_reg | 0.021 |
| IRT_4pl_gamma | **0.258** |
| B6_dcr_fuzzy | 0.297 |

### 关键问题

1. **Per-benchmark gamma 为负 (-3.93)**：物理上不合理（应为正，表示污染提高分数）。原因：d025 没有 exp-002 signals，fallback 用 oracle dosage/100=0.25，而 d000 的 signal 值为 0.613。这导致 d000 的 exposure 反而高于 d025，破坏了 dose-response 单调性。

2. **exp-002 signals**: `[0.613, 0.629, 0.25, 0.810]` 对应 d000/d005/d025/d100。d025 的 0.25 是 fallback 值。

3. **Joint fit 未受 `--max-items` 限制**：用了全部 1319 items（joint_fit 模块内部未应用 max_items 截断）。但收敛正常，gamma=0.35 不显著。

4. **IRT MAE (0.258) 高于 B0_raw (0.019)**：在这组数据上 IRT 校准反而比不做调整差，因为 gamma 为负导致校准方向错误。

### exp-002 Signal 格式

路径: `/root/autodl-tmp/exp002/signals/{model_dirname}/signals_merged_{benchmark}.json`

格式: JSON array，每个 item 有 `{index, benchmark, s1_embedding, s2_minkpp, s3_constat (null), s4_selfcritique}`。当前实现使用 `s1_embedding` 的 mean 作为 per-model scalar。

**可用的 model-benchmark 组合**: d000/d005/d100 × mmlu/gsm8k/arc_challenge。**d025 缺失**。

---
