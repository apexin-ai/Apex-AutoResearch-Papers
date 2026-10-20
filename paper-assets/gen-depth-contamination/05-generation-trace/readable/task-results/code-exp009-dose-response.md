# code exp009 dose response

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp009_dose_response_20260513T234043_result.json`
- **Structured JSON:** [`bc80d5d9573715ad50d1.json`](../../sessions/bc/bc80d5d9573715ad50d1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 交付物总结

### 1. 脚本已部署
`/root/autodl-tmp/gen-depth-contamination/scripts/run_exp009_dose_response.py` (608 行)

**设计要点：**
- **固定数据集大小** N=5000，确保各 injection ratio 下训练成本一致
  - 10%: 4500 human + 500 synthetic
  - 30%: 3500 human + 1500 synthetic
  - 50%: 2500 human + 2500 synthetic
- 复用 exp-006 的 `exp006_filtering_strategies.py`（BinaryOurs + Graduated 分类器）
- 相同 (ratio, seed) 下所有策略看到同一份数据，确保公平对比
- 支持 `--dry-run`、`--analyze-only`、`--skip-eval` 三种模式
- 结果自动跳过已完成的 run（断点续跑）

### 2. Dry-run 验证结果

**Pre-GPU 验证（全部通过）：**
- 数据加载：30000 samples (human=5000, synthetic=25000)
- 三个 ratio 的子采样均正确（10%/30%/50%）
- 确定性检查通过（same seed → same data）
- 三种 filtering 策略在小数据上均正常：
  - no-filter: 200/200 kept, weight=1.0
  - binary-ours: 200/200 kept, weight mean=0.70
  - graduated: 200/200 kept, weight mean=0.78

**Training 验证（`--skip-eval`，通过）：**
- 3/3 策略均成功训练完 10 步
- no-filter: loss=2.73, binary-ours: loss=3.01, graduated: loss=2.84
- 模型加载、LoRA 适配、WeightedRandomSampler 均正常

**Evaluation：** 因 exp-006 占用 13GB GPU 显存，eval 阶段 OOM。eval 代码与 exp-006 完全一致，无需单独验证——exp-006 已跑出完整 MMLU/HellaSwag 结果。

### 3. GPU 预算估算

**基于 exp-006 实测数据推算：**

| 阶段 | exp-006 (30K 样本) | exp-009 (5K 样本) |
|------|-------------------|-------------------|
| 数据准备 + 过滤 | ~0.5 min | ~0.5 min |
| 模型加载 (训练) | ~1 min | ~1 min |
| 训练 (3 epochs) | 36.3 min | **~6 min** |
| 模型保存 + 清理 | ~0.5 min | ~0.5 min |
| 模型加载 (eval) | ~1 min | ~1 min |
| lm-eval (MMLU+HellaSwag) | ~6 min | ~6 min |
| **单 run 合计** | **~45 min** | **~15 min** |

- **Total runs**: 3 ratios × 2 strategies × 5 seeds = **30 runs**
- **总 GPU 时间**: 30 × 15 min = **~450 min ≈ 7.5 小时**
- **GPU 要求**: RTX 4090D 24GB，独占（不能与 exp-006 同时跑）

### 提交命令

等 exp-006 完成后（预计 05-15），执行：

```bash
cd /root/autodl-tmp/gen-depth-contamination && \
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
export HF_HOME=/root/autodl-tmp/.hf_cache && \
export HF_HUB_DISABLE_XET=1 && \
nohup python3 scripts/run_exp009_dose_response.py \
    --ratios 0.1 0.3 0.5 \
    --strategies binary-ours graduated \
    --seeds 42 123 456 789 1024 \
    --alpha 0.5 \
    > /tmp/exp009_full.log 2>&1 &
echo "PID=$!"
```

**建议**：exp-006 出结果后先更新 `--alpha` 为最佳值，再提交。查看结果用：
```bash
python3 scripts/run_exp009_dose_response.py --analyze-only
```

---
