# debug p0 exposure matrix

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_p0_exposure_matrix_20260514T184603_result.json`
- **Structured JSON:** [`eb458ab48508b4dc8599.json`](../../sessions/eb/eb458ab48508b4dc8599.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

排查完成。以下是完整诊断。

---

## 诊断结果

### 两个 exposure 矩阵的实际值

**Shape**: 两者均为 `(4, 1319)`

**Joint-fit（oracle dosages）**:
| Model | Normalized dosage | Exposure row (constant) |
|---|---|---|
| d000 (clean) | **0.00** | `[0, 0, 0, ..., 0]` |
| d005 | 0.05 | `[0.05, 0.05, ..., 0.05]` |
| d025 | 0.25 | `[0.25, 0.25, ..., 0.25]` |
| d100 | 1.00 | `[1, 1, ..., 1]` |

Stats: min=0, max=1, mean=0.325

**Per-benchmark（signal scores, s1_embedding）**:
| Model | Signal score | Normalized | Exposure row |
|---|---|---|---|
| d000 (clean) | 0.613 | **0.757** | `[0.757, 0.757, ..., 0.757]` |
| d005 | 0.629 | 0.776 | `[0.776, 0.776, ..., 0.776]` |
| d025 | 0.250 *(fallback)* | 0.309 | `[0.309, 0.309, ..., 0.309]` |
| d100 | 0.810 | 1.000 | `[1, 1, ..., 1]` |

Stats: min=0.309, max=1, mean=0.710

**注意**: tau 全为 1.0（未传 `--exposure-file`），所以每行是常数。

### 差异

- Max absolute diff: **0.757**
- Mean absolute diff: **0.385**
- 完全不同。

### 根本原因：两个 bug 叠加

**Bug 1（代码 bug）**: `joint_fit.py` 不支持 `signals_dir`。`run_exp006.py` 调用 `run_joint_fit()` 时没传 `signals_dir`（`run_joint_fit` 也没这个参数），所以 joint-fit 始终用 oracle dosages `[0, 5, 25, 100]`。

代码证据：
- `run_exp006.py:344` — 调用 `run_joint_fit` 无 `signals_dir` 参数
- `joint_fit.py:79` — `build_exposure_matrix(dosages_valid, tau)` 硬编码用 oracle dosage
- `joint_fit.py` 中 grep "signal" 零匹配

**Bug 2（信号质量 bug）**: s1_embedding 信号作为 per-model exposure **完全失效**：
- **d=0（clean model）得到 exposure=0.757** — 应该接近 0
- 排序紊乱：d25 (0.309) < d0 (0.757) < d5 (0.776) < d100 (1.0)，正确应为 d0 < d5 < d25 < d100
- d=25 信号文件缺失，fallback 到 `dosage/100 = 0.25`，与 signal 尺度不一致
- s1_embedding 是 item-level 检测信号，均值化为 model-level dosage proxy 语义不对

**为什么 joint-fit 收敛、per-benchmark 不收敛**: Joint-fit 用 oracle dosage，d=0 exposure 精确为 0，模型有清晰的"无污染基线"，gamma 可识别。Per-benchmark 的 d=0 exposure=0.757，Stan 模型无法区分 clean vs contaminated，gamma 失去可识别性 → Rhat=1.53, ESS=7。

### 建议修复方案

1. **短期修复**: per-benchmark 路径也用 oracle dosage（和 joint-fit 一致），不传 `--signals-dir`。这样两条路径的 exposure 矩阵一致，per-benchmark 应恢复正常收敛。

2. **中期修复**: 如果要用信号做 exposure，需要：
   - 确保 d=0 模型的信号接近 0（当前 s1_embedding 不满足）
   - 信号值与 dosage 单调递增
   - joint_fit.py 也需要同步支持 signals_dir
   - 补全 d=25 缺失的信号文件

3. **长期**: 重新评估哪个 exp-002 信号适合做 model-level dosage proxy。s1_embedding 的 mean 不是好的选择——它反映的是 embedding 相似度，不是污染程度。

---
