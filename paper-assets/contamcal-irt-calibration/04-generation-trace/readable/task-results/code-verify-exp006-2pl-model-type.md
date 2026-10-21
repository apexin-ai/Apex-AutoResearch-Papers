# code verify exp006 2pl model type

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_verify-exp006-2pl-model-type_20260515T070919_result.json`
- **Structured JSON:** [`6f0e0b302c33f7b29b5c.json`](../../sessions/6f/6f0e0b302c33f7b29b5c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 分析报告：exp006-s1only-gsm8k-2pl 的 model_type 传递链

### 1. model_type 传递链

```
argparse (--model-type 2pl_gamma)
  → args.model_type = "2pl_gamma"
    → run_pipeline(args)
      → per-benchmark fit: run_benchmark_fit(..., model_type=args.model_type)  ✅ 正确传递
      → joint fit: run_joint_fit(...)  ❌ 未传递 model_type
```

**关键发现：`run_joint_fit()` 函数签名中根本没有 `model_type` 参数。**

### 2. Bug 定位：两处硬编码

| 位置 | 文件 | 行号 | 硬编码内容 |
|------|------|------|------------|
| Stan 模型路径 | `joint_fit.py` | L38 | `STAN_MODEL = ".../contam_irt_4pl_simple.stan"` |
| JSON 输出标签 | `joint_fit.py` | 结果 dict | `"model_type": "4pl_gamma_joint"` |

**调用侧**（`run_exp006.py` L524-538）也未传入 `model_type`：
```python
joint_result = run_joint_fit(
    args.eval_dir, args.exposure_file, str(joint_dir),
    benchmarks=args.benchmarks,
    exclude_rules=D018_EXCLUDE_RULES,
    chains=args.chains, warmup=args.warmup, samples=args.samples,
    ...  # 无 model_type 参数
)
```

而 per-benchmark 路径的 `run_irt_calibration.py` 正确使用了 `STAN_MODELS` 字典映射：
```python
STAN_MODELS = {
    "4pl_gamma": ".../contam_irt_4pl_simple.stan",
    "2pl_gamma": ".../contam_irt_2pl_gamma.stan",   # ← 2PL 对应的 Stan 文件
    "vanilla_4pl": ".../vanilla_4pl.stan",
    "4pl_gamma_wider": ".../contam_irt_4pl_simple_wider.stan",
}
```

### 3. 结论

**确认是代码 bug（硬编码覆盖），不是 JSON 记录错误。**

`joint_fit.py` 独立于 `run_irt_calibration.py` 的 `STAN_MODELS` 映射体系，无论命令行传入 `--model-type 2pl_gamma` 还是其他值，joint fit 路径始终：
- 调用 `contam_irt_4pl_simple.stan`（4PL 模型）
- 输出 `"model_type": "4pl_gamma_joint"`

因此 **exp006-s1only-gsm8k-2pl 的 joint fit 实际运行的是 4PL 模型，不是 2PL。**

### 4. 与 exp006-pooled-s1only-gsm8k-v2 对比

| 实验 | 目录 | joint_fit model_type | gamma mean | gamma 95%CI |
|------|------|---------------------|------------|-------------|
| s1only-gsm8k-2pl | `results_pooled_05B_15B_gsm8k_s1only_2pl` | `4pl_gamma_joint` | 0.1352 | [-0.6639, 0.9628] |
| pooled-s1only-gsm8k (v1) | `results_pooled_s1only_gsm8k` | `4pl_gamma_joint` | 0.1202 | [-0.7367, 0.9647] |

两者都是 4PL joint fit，模型配置相同（8 models, 1319 items, gsm8k only），仅采样配置不同（2pl 用 16000 draws vs v1 用 4000 draws）。**2pl 实验本质上是 v1 的高采样量重跑，并非 2PL 消融。**

### 5. 需要修改的代码位置

1. **`joint_fit.py` L38**：删除 `STAN_MODEL` 硬编码，改为接受 `model_type` 参数并从 `STAN_MODELS` 字典查找
2. **`joint_fit.py` `run_joint_fit()` 函数签名**（L130）：增加 `model_type="4pl_gamma"` 参数
3. **`joint_fit.py` 结果 dict**：`"model_type"` 字段改为动态值（如 `f"{model_type}_joint"`）
4. **`run_exp006.py` L524**：调用 `run_joint_fit` 时传入 `model_type=args.model_type`

### 6. 实验 Metrics 确认

- gamma = 0.1352, 95% CI = [-0.6639, 0.9628], ci_excludes_zero = false ✅ 与 JSON 一致

---
