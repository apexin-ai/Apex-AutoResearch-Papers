# code perturbation eval update

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_perturbation-eval-update_20260516T203524_result.json`
- **Structured JSON:** [`b09846c72c444b19f321.json`](../../sessions/b0/b09846c72c444b19f321.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

## 结果

### 1. 现有代码完整性
- 原有 4 种扰动中，`gaussian_noise` 和 `color_jitter` 直接匹配需求
- `spatial_jitter`（平移+旋转）≠ 任务要求的 "random crop + resize"
- `sensor_noise`（Poisson噪声）≠ 任务要求的 "sensor dropout（像素置零）"

### 2. 新增/修改内容

**`scripts/perturbation_wrapper.py`** — 新增：
- `random_crop_resize()`：按 border_frac 裁剪边界，cv2 resize 回原尺寸
- `sensor_dropout()`：按 rate 将随机像素置零

**`scripts/eval_acib_perturbed.py`** — 完全重写，新增：
- `--scoring_alpha` (default=0.3)
- `--disable_scoring`
- `--conditioning_mode`
- 个别扰动 flags：`--noise_std`、`--jitter_strength`、`--crop_border`、`--dropout_rate`
- 支持多扰动同时生效（MultiPerturbedWrapper）
- `patch_make_policy` 正确传递 scoring/conditioning 参数

**`scripts/run_perturbation_eval.sh`** — 新建运行脚本

### 3. scoring_alpha 兼容性
已确认：`patch_make_policy` 接收并设置 `scoring_alpha`、`disable_scoring`、`conditioning_mode_override`，逻辑与 `eval_acib.py` 一致。

### 4. Dry-run
`--help` 输出正确，所有 6 种扰动函数通过 shape/dtype 验证。

---
