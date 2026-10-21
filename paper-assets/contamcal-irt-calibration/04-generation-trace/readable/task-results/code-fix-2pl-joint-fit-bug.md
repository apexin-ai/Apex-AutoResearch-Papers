# code fix 2pl joint fit bug

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-2pl-joint-fit-bug_20260515T074435_result.json`
- **Structured JSON:** [`560528354b7391383bd0.json`](../../sessions/56/560528354b7391383bd0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证通过。

**修改汇总：**

`joint_fit.py`:
- **L34**: 新增 `STAN_MODELS` 到 `from run_irt_calibration import` 列表
- **L38**: 删除硬编码 `STAN_MODEL = ".../contam_irt_4pl_simple.stan"`
- **L131**: `run_joint_fit()` 签名新增 `model_type="4pl_gamma"` 参数（默认值保持向后兼容）
- **L163**: `STAN_MODEL` → `STAN_MODELS[model_type]`
- **L206**: `"model_type": "4pl_gamma_joint"` → `f"{model_type}_joint"`

`run_exp006.py`:
- **L528**: `run_joint_fit()` 调用新增 `model_type=args.model_type`

**dry-run 验证结果：**
- `model_type` 参数存在于 `run_joint_fit` 签名中 ✓
- 默认值为 `"4pl_gamma"` ✓
- `contam_irt_2pl_gamma.stan` 文件存在 ✓

---
