# code exp006 baselines scaffold

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp006-baselines-scaffold_20260514T075102_result.json`
- **Structured JSON:** [`7b51df67d4d20fa432de.json`](../../sessions/7b/7b51df67d4d20fa432de.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研完成。以下是报告。

---

## exp-006 代码框架调研报告

### 1. 目录/代码现状

exp006 目录已存在且代码框架基本完整：

| 文件 | 用途 | 状态 |
|------|------|------|
| `baselines.py` | 7 个 baseline 统一实现（~500 行） | **完成**，含 B0-B6 全部 |
| `run_irt_calibration.py` | IRT 4PL+γ MCMC 拟合 | **完成**，支持 matrix 和 eval-dir 两种输入模式 |
| `evaluate_calibration.py` | 5 指标评估 + LaTeX 表格 | **完成**，含 bootstrap CI |
| `run_exp006.py` | 端到端 pipeline（加载数据→IRT→baselines→评估） | **完成**，支持 dry-run |
| `run_all_baselines.py` | 独立 baseline 运行器 + 合成数据测试 | **完成** |
| `_baselines_v1/` | 早期版本（每 baseline 一个文件），已被 `baselines.py` 取代 | 归档 |
| `dryrun_full.json` | 合成数据 dry-run 输出（含 Stan baselines） | 有结果 |
| `dryrun_no_stan.json` | 合成数据 dry-run 输出（跳过 Stan） | 有结果 |

### 2. Stan 模型文件

位于 `/root/contamcal-irt-calibration/stan_models/`，共 4 个：

| 文件 | 模型 | 用途 |
|------|------|------|
| `contam_irt_4pl_simple.stan` | 4PL+γ（无测量误差） | **主模型**，c/d 限 (0.001,0.999) |
| `contam_irt_4pl.stan` | 4PL+γ（c/d 限 (0,1)） | 主模型变体 |
| `contam_irt_2pl_gamma.stan` | 2PL+γ（无 c/d） | B2 baseline |
| `vanilla_4pl.stan` | 4PL 无 γ | B3 baseline |

所有模型都包含 `generated quantities` 块：calibrated_score（exposure=0 反事实）和 log_lik（LOO-CV）。

### 3. 可复用资源

- **exp001 eval 数据**：`/root/autodl-tmp/exp001/eval_results/` 下有 Qwen2.5-0.5B/1.5B/3B 多个 dosage 变体（d000/d005/d100），含 paraphrase 版本
- **exp002 信号计算**：`compute_signals.py`、`signal_embedding.py`、`signal_minkpp.py`、`signal_selfcritique.py`、`aggregate_rrf.py` — exposure 信号计算管线
- **MVP simulation 目录不存在**（`artifacts/mvp_simulation/` 404）
- **env_setup.sh**：conda 环境配置已就绪
- **CmdStanPy**：已安装，CmdStan 2.38.0 位于 `/root/.cmdstan/cmdstan-2.38.0`

### 4. Baseline 实现难度评估

**已完成（可直接运行）**：

| Baseline | 实现方式 | 复杂度 |
|----------|----------|--------|
| B0 Raw | Wilson CI | 极简 |
| B1 Remove-rescore | 75th-pctl 阈值 + bootstrap | 简单 |
| B2 2PL+γ | CmdStanPy NUTS | 中等（Stan 已有） |
| B3 Vanilla 4PL | CmdStanPy NUTS | 中等（Stan 已有） |
| B4 Linear regression | OLS + bootstrap CI | 简单 |

**需注意的实现**：

| Baseline | 当前实现 | 潜在问题 |
|----------|----------|----------|
| B5 Emperor's | exposure-weighted downweighting，模拟 rephrasing（`has_real_paraphrases=false`） | 无真实 paraphrase 数据时退化为 exposure 加权；exp001 有 `_para` 变体可用 |
| B6 DCR fuzzy | 4 档模糊推理（low/medium/high/very_high），Mamdani defuzzification | 实现完整，但 membership function 参数需与 Xu et al. 原文对齐验证 |

### 5. 代码架构评估

当前架构清晰合理：

```
exp006/
├── baselines.py              # 统一 BaselineMethod 接口，ALL_BASELINES 注册表
├── run_irt_calibration.py    # IRT 拟合核心（load_matrix → build_exposure_matrix → run_benchmark_fit）
├── evaluate_calibration.py   # 5 指标 + LaTeX/text 表格
├── run_exp006.py             # E2E pipeline orchestrator
└── run_all_baselines.py      # 独立 baseline 测试器
```

**统一接口**：`BaselineMethod.fit(y, exposure) → dict{calibrated_scores, ci_lower/upper (50/80/95)}`，所有 baseline 和 IRT 输出格式一致，直接对接 `evaluate_method()`。

**两种运行模式**：
1. **Direct matrix**：`--response-matrix` + `--exposure-matrix`（单 benchmark）
2. **Eval-dir**：自动从 exp001 目录加载（多 benchmark 批量）

### 6. 跑通前的待办

1. **CmdStanPy 编译验证**：Stan 模型尚未编译（需首次 `model.compile()`），预计 1-2 分钟
2. **exposure-file 路径**：`run_exp006.py` 需要 `--exposure-file`（exp002/003 输出的 per-benchmark per-item tau JSON），需确认该文件是否已生成
3. **ground truth 定义**：当前用 dosage=0 模型的 raw accuracy 作为 clean score 参考，逻辑合理
4. **B5 paraphrase 数据**：exp001 有 `_para` 变体（`Qwen2.5-0.5B_d000_s42_para`），可接入 Emperor's baseline 做真实 rephrasing 对比

---
