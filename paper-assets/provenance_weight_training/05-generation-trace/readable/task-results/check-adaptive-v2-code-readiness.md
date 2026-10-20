# check adaptive v2 code readiness

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_adaptive_v2_code_readiness_20260514T171724_result.json`
- **Structured JSON:** [`4ac7f0bc0538f5c767fe.json`](../../sessions/4a/4ac7f0bc0538f5c767fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结论明确了。

## 代码就绪状态报告

### 1. adaptive_fix vs adaptive_v2 的关系

- **adaptive_fix** = 当前在跑的实验。使用 `--weighting_method adaptive`，核心修正是 `n_min=2`（之前默认是 `batch_size//2`），**无 EMA**。脚本 `run_adaptive_v2_seed42.sh` 实际就是 adaptive_fix 的脚本（注释写的"n_min 修复 (3→2)"）。
- **adaptive_v2**（原始版本） = `scripts/submit_adaptive_v2.sh`，参数为 `--n_min 1 --ema_alpha 0.1 --gradient_checkpointing`。这三组已被 killed。

### 2. 代码当前支持的 adaptive weighting 变体

| 变体 | weighting_method | 参数 | 代码支持？ |
|------|-----------------|------|-----------|
| uniform | `uniform` | 无 | ✅ |
| grid | `grid` | `--grid_b_value` | ✅ |
| adaptive (= adaptive_fix) | `adaptive` | `--tau`, `--n_min` | ✅ |
| adaptive_v2 (带 EMA) | `adaptive` | `--ema_alpha` | ❌ **不支持** |

### 3. 关键缺失

**`--ema_alpha` 和 `--gradient_checkpointing` 参数在当前代码中不存在：**

- `pretrain_weighted.py` 的 argparse 中没有 `ema_alpha` 参数（grep 结果为空）
- `pretrain_weighted.py` 中没有 `gradient_checkpointing` 参数
- `WeightedTrainer.__init__` 没有 EMA 相关字段
- `compute_loss` 中 adaptive 分支直接调 `find_optimal_b(q_scores, tau, n_min)` —— 每个 batch 独立计算 b*，无跨 batch 平滑
- `weighting/alpha_eff.py` 纯数学函数，无任何 EMA 逻辑

### 4. 如果要支持 adaptive_v2（带 EMA），需要的改动

1. **argparse 加参数**：`--ema_alpha`（float, default=0.0 表示不启用）、`--gradient_checkpointing`
2. **WeightedTrainer 加 EMA 状态**：在 `__init__` 中初始化 `self.ema_b = None`，在 `compute_loss` 的 adaptive 分支中：
   ```python
   raw_b = find_optimal_b(q_scores, tau, n_min)
   if self.ema_alpha > 0 and self.ema_b is not None:
       b_val = self.ema_alpha * raw_b + (1 - self.ema_alpha) * self.ema_b
   else:
       b_val = raw_b
   self.ema_b = b_val
   ```
3. **TrainingArguments 加 gradient_checkpointing**：传入 `gradient_checkpointing=args.gradient_checkpointing`
4. **日志增加字段**：记录 `raw_b` 和 `smoothed_b` 方便对比

改动量不大（~30 行），但 `submit_adaptive_v2.sh` 传了 `--ema_alpha 0.1`，当前代码会直接报 `unrecognized arguments` 错误。

---
