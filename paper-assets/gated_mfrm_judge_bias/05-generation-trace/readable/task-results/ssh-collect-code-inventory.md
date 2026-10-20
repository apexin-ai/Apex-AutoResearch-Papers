# ssh collect code inventory

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_collect_code_inventory_20260523T124822_result.json`
- **Structured JSON:** [`153880110d8623794d25.json`](../../sessions/15/153880110d8623794d25.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**⚠️ 发现硬编码密钥！** `exp001/judge_interface.py:343` 和 `exp001/generate_responses.py:24` 中有硬编码的 proxy key `tum_XXB3sZILRCg8...`。打包前需要处理。

---

## 汇总结果

### 1. 文件清单

#### autodl-8gpu (93 files, 123K tar.gz)

| 目录 | 文件 |
|------|------|
| **baselines/** | `cyclic_judge.py`, `dcr_adapter.py`, `dcr_baseline.py`, `pref_leakage.py`, `test_dcr.py`, `test_pref_leakage.py`, `dcr_factor/` (8 files) |
| **exp001/** | `collect.py`, `collect_pointwise.py`, `data_loader.py`, `generate_responses.py`, `generate_vllm_batch.py`, `generate_vllm_online.py`, `judge_interface.py`, `run_small_models.sh`, `run_remaining.sh`, 11 yaml configs, `data/download_benchmarks.py`, `prompts/` (2 files) |
| **exp002/** | `composite.py`, `run_exp002.py`, `validation.py`, `sources/` (3 files + `__init__.py`) |
| **exp003/** | `data_loader.py`, `evaluation.py`, `models.py`, `run_exp003.py`, `analyze_003b.py`, `generate_ppc.py`, `bootstrap_delta_tau.py`, `compute_waic_loo.py` |
| **exp004/** | `baselines.py`, `run_exp004.py` |
| **exp005/** | `run_exp005.py` |
| **exp006/** | `run_exp006.py`, `analyze_exp006.py` |
| **exp008/** | `run_exp008.py`, `generate_diagnostics.py` |
| **exp009/** | `run_exp009.py` |
| **exp012/** | `run_exp012.py` |
| **exp014-019/** | 各一个 `run_exp0XX.py` |
| **exp_w7_ablation/** | `run_ablation.py`, `analyze_w7.py` |
| **lib/** | `__init__.py`, `murphy_topel.py`, `priors.py`, `rope_test.py` |
| **mvp/** | `bias_scatter.py`, `data_gen.py`, `evaluate.py`, `models.py`, `models_v3.py`, `run_diagnosis.py`, `run_mvp.py`, `run_mvp_002.py`, `run_mvp_003.py` |
| **scripts/** | `waic_loo_comparison.py` |

#### rtx6000-4x (独有文件，88K tar.gz)

与 autodl-8gpu 共有大部分文件，**独有**：
- `exp003/models_horseshoe.py` — G-MFRM Horseshoe prior 变体
- `exp013/run_exp013.py` — weight sensitivity analysis
- `figures/paper/gen_fig1.py` — Fig 1 概念图生成
- `mvp/collect_fig2_data.py` — Fig 2 数据收集
- `exp001/config_llama_arena_a.yaml`, `config_llama_arena_b.yaml`

**autodl-8gpu 独有**（rtx6000-4x 没有）：
- `exp005/`, `exp006/`, `exp008/`, `exp014-019/`, `scripts/`, `artifacts/`

### 2. 敏感信息扫描

| 文件 | 问题 | 严重性 |
|------|------|--------|
| `exp001/judge_interface.py:343` | 硬编码 `_PROXY_KEY = "tum_XXB3s..."` | **高** |
| `exp001/generate_responses.py:24` | 硬编码 `PROXY_KEY = "tum_XXB3s..."` | **高** |
| `exp001/judge_interface.py` 多处 | `api_key` 参数引用（从环境变量读取，安全） | 低 |

### 3. 顶层目录结构

```
gated_mfrm_judge_bias/
├── baselines/          # Baseline 方法 (PLS, DCR, CyclicJudge)
├── data/               # 数据目录
├── exp001/             # Judge 评测数据收集 (pairwise/pointwise)
├── exp002/             # Exposure estimation (logprob, ref-anchoring, cross-model)
├── exp003/             # G-MFRM fitting (JAX/NumPyro MCMC)
├── exp004/             # Baseline comparison
├── exp005-019/         # 后续实验 (仅 autodl-8gpu)
├── exp_w7_ablation/    # W7 ablation study
├── exp013/             # Weight sensitivity (仅 rtx6000-4x)
├── figures/            # 论文图表生成 (仅 rtx6000-4x)
├── lib/                # 共享库 (Murphy-Topel, priors, ROPE)
├── mvp/                # MVP 原型 (simulation + fitting)
├── scripts/            # 工具脚本 (仅 autodl-8gpu)
└── artifacts/          # 产出 (仅 autodl-8gpu)
```

### 4. Tar 包状态

| 服务器 | 路径 | 大小 | 状态 |
|--------|------|------|------|
| autodl-8gpu | `/tmp/code_autodl.tar.gz` | 123K | ✓ 创建成功 |
| rtx6000-4x | `/tmp/code_rtx.tar.gz` | 88K | ✓ 创建成功 |

### 5. 关键文件概要

- **exp003/run_exp003.py** — G-MFRM 主 fitting 脚本，JAX/NumPyro NUTS 采样，支持 GPU
- **exp003/models.py** — 4 种 fitting 方法：raw_average / mfrm_only / sequential / joint_gmfrm；模型公式 `logit(P) = θ_n - b_i - d_j + c_n·e_i`
- **exp001/collect.py** — Judge 评测数据收集，支持 pairwise/pointwise、位置交换、增量恢复、并发限流
- **baselines/pref_leakage.py** — Preference Leakage Score 基线实现 (ICLR 2026)
- **exp002/sources/logprober.py** — Min-K% Prob 记忆化检测
- **exp003/models_horseshoe.py** (rtx6000-4x) — Regularized Horseshoe prior 变体的 G-MFRM

**打包前建议**：将 `judge_interface.py` 和 `generate_responses.py` 中的硬编码 proxy key 替换为环境变量引用后再分发。

---
