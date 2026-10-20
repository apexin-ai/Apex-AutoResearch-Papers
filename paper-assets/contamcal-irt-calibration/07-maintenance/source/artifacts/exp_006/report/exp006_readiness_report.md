# exp-006 IRT Fitting Pipeline 可用性报告

**日期**: 2026-05-16  
**状态**: **READY** — 所有组件就绪，RRF 完成后可立即启动

---

## 组件状态总览

| 组件 | 状态 | 说明 |
|------|------|------|
| Stan 模型文件 | ✅ Ready | 5 个 .stan 文件 + 已编译二进制 |
| CmdStan | ✅ Ready | v2.38.0 (`/root/.cmdstan/cmdstan-2.38.0`) |
| cmdstanpy | ✅ Ready | 已安装 (`/root/miniconda3/lib/python3.12/site-packages/cmdstanpy/`) |
| IRT fitting 脚本 | ✅ Ready | `run_exp006.py` 端到端 pipeline |
| 7 Baselines | ✅ Ready | B0-B6 全部实现，unified interface |
| 评估框架 | ✅ Ready | 8 metrics + LaTeX table |
| Dry-run 验证 | ✅ Passed | `dryrun_full.json` 含 Stan fitting 结果 |
| 数据格式对接 | ✅ Compatible | RRF → IRT 格式直接兼容 |

---

## 详细检查

### 1. Stan 模型

位置：`/root/contamcal-irt-calibration/stan_models/`

| 文件 | 用途 | 编译状态 |
|------|------|----------|
| `contam_irt_4pl_simple.stan` | 主模型：4PL + γ（默认 prior） | ✅ 已编译 |
| `contam_irt_4pl_simple_wider.stan` | 宽 prior 消融 | ✅ 已编译 |
| `contam_irt_4pl.stan` | 4PL + γ（原始版本） | ✅ 已编译 |
| `contam_irt_2pl_gamma.stan` | 2PL + γ（B2 baseline 用） | ✅ 已编译 |
| `vanilla_4pl.stan` | 标准 4PL（B3 baseline 用） | ✅ 已编译 |

模型参数化：`P(y_ij=1) = c_j + (d_j - c_j) * inv_logit(a_j*(θ_i - b_j) + γ * exposure_ij)`

**关于 per-benchmark γ_k**：Stan 模型使用单一全局 `real gamma`，per-benchmark γ_k 通过 pipeline 对每个 benchmark 独立 fitting 实现（`run_benchmark_fit` per benchmark），等效于 per-benchmark γ_k。

### 2. 7 Baselines

实现文件：`/root/contamcal-irt-calibration/exp006/baselines.py`

| ID | 类名 | 方法 | 需 Stan? |
|----|------|------|----------|
| B0 | `RawBaseline` | Raw accuracy（anchor） | No |
| B1 | `RemoveRescoreBaseline` | 去除高 exposure items 后重评分 | No |
| B2 | `SingleSignal2PLGamma` | 简化 2PL + γ IRT | Yes |
| B3 | `Vanilla4PL` | 标准 4PL（无 γ） | Yes |
| B4 | `LinearRegressionBaseline` | 线性回归 + bootstrap CI | No |
| B5 | `EmperorMitigationBaseline` | exposure-weighted downweighting | No |
| B6 | `DCRFuzzyBaseline` | Xu et al. (EMNLP 2025) | No |

统一接口：`fit(correctness_matrix, exposure_scores) → {calibrated_scores, ci_lower/upper (50/80/95%)}`

### 3. 数据格式兼容性

**RRF 输出**（exp-003）：
- `exposure_aggregated.json`: `{benchmark: [per-item float]}` — 所有 model 的 RRF 均值
- `exposure_scores.json`: `{model_id: {benchmark: {exposure_scores: [...]}}}` — per-model 细粒度

**IRT 输入**（exp-006 `load_exposure_scores`）：
- 接受 flat 格式 `{benchmark: [floats]}` → 直接用 `exposure_aggregated.json`
- 接受 nested 格式 → 需指定 `--tau-model-id`
- 无 exposure 文件时 fallback 到 `tau=1.0`（oracle dosage）

**结论：`exposure_aggregated.json` 可直接作为 `--exposure-file` 传入，零适配。**

`build_exposure_matrix` 构建方式：`exposure[i,j] = dosage[i] * tau[j] / max_dosage`

### 4. Dry-run 验证

已有两份 dry-run 输出：
- `dryrun_full.json`：含 Stan fitting（B2 single_signal_2pl_gamma + B3 vanilla_4pl），5 models × 10 items 合成数据，7 个方法全部输出 calibrated_scores + CI + metrics
- `dryrun_no_stan.json`：跳过 Stan 的 5 baselines 快速测试

Full dry-run 结果确认：Stan MCMC 正常收敛（max_rhat ≈ 1.003），所有 metrics 正常计算。

### 5. 启动命令

```bash
# Dry-run 快速验证
python exp006/run_exp006.py --dry-run --skip-stan --max-items 20 --output-dir /tmp/exp006_test

# 正式运行（RRF 完成后）
python exp006/run_exp006.py \
    --eval-dir /root/autodl-tmp/exp001/eval_results \
    --exposure-file /path/to/exp003/exposure_aggregated.json \
    --output-dir /root/autodl-tmp/exp006/results

# 含 joint fitting 消融
python exp006/run_exp006.py --joint-fit \
    --eval-dir /root/autodl-tmp/exp001/eval_results \
    --exposure-file /path/to/exp003/exposure_aggregated.json \
    --output-dir /root/autodl-tmp/exp006/results
```

---

## 无阻塞项

Pipeline 端到端就绪，无需任何修复或补充。RRF 完成后可立即启动 IRT fitting。
