# Gemma-2-9B seed=0 Dose-Response Sweep Analysis

**Date**: 2026-05-20
**Server**: westd-29999 (CUDA_VISIBLE_DEVICES=1)
**Log**: `~/runs/contamcal-irt-calibration/sft_gemma2_s0_sweep.log`

## MMLU 5-shot Accuracy

| Dosage | Accuracy | Correct/Total | Δ from d000 |
|--------|----------|---------------|-------------|
| d000   | 0.6488   | 9111/14042    | —           |
| d005   | 0.6414   | 9007/14042    | -0.74pp     |
| d025   | 0.6491   | 9115/14042    | +0.03pp     |
| d050   | 0.6309   | 8859/14042    | -1.79pp     |
| d100   | **MISSING** | — | — |

**delta_d100**: 无法计算（d100 训练崩溃）

## d100 崩溃详情

- 错误: `RuntimeError: Pin memory thread exited unexpectedly`
- 崩溃位置: step 1618/4159 (39%)
- 结果: lora_adapter 目录为空，eval 跳过
- 脚本误报 `exit code=0`，但实际训练失败

## 训练时间线

| Dosage | Train Start | Train End | Train Duration | Eval Duration |
|--------|------------|-----------|----------------|---------------|
| d000   | May 20 17:47 | May 20 20:14 | ~2h27m | ~12m |
| d005   | May 20 20:26 | May 20 22:55 | ~2h29m | ~11m |
| d025   | May 20 23:06 | May 21 01:41 | ~2h35m | ~11m |
| d050   | May 21 01:52 | May 21 04:35 | ~2h43m | ~11m |
| d100   | May 21 04:46 | May 21 05:55 | ~1h09m (crashed) | skipped |

总耗时: ~12h08m (其中 ~1h09m 浪费在 d100 崩溃)

## Checkpoint 路径

| Dosage | Path | Status |
|--------|------|--------|
| d000 | `/root/autodl-tmp/exp001/checkpoints/gemma-2-9b_d000_s0/lora_adapter/` | ✓ 完整 |
| d005 | `/root/autodl-tmp/exp001/checkpoints/gemma-2-9b_d005_s0/lora_adapter/` | ✓ 完整 |
| d025 | `/root/autodl-tmp/exp001/checkpoints/gemma-2-9b_d025_s0/lora_adapter/` | ✓ 完整 |
| d050 | `/root/autodl-tmp/exp001/checkpoints/gemma-2-9b_d050_s0/lora_adapter/` | ✓ 完整 |
| d100 | `/root/autodl-tmp/exp001/checkpoints/gemma-2-9b_d100_s0/lora_adapter/` | ✗ 空目录 |

Eval 结果: `/root/autodl-tmp/exp001/eval_results_v2/gemma2_d{000,005,025,050}_s0/mmlu_results.json`

## 跨 Seed 对比

| Dosage | s42    | s123   | s0     |
|--------|--------|--------|--------|
| d000   | —      | 0.6584 | 0.6488 |
| d005   | —      | 0.6581 | 0.6414 |
| d025   | —      | 0.6302 | 0.6491 |
| d050   | —      | 0.6674 | 0.6309 |
| d100   | —      | 0.6733 | MISSING |
| delta_d100 | +3.76pp | +1.49pp | N/A |

## 结论

1. **d100 缺失**: 训练因 `Pin memory thread exited unexpectedly` 崩溃，无法计算 delta_d100，无法判断是否复现 Benefit pattern。
2. **d000-d050 趋势**: s0 的 d000-d050 结果呈非单调波动（d005 下降、d025 回升、d050 显著下降），与 s123 的 dip-at-d025 模式不同。
3. **需要重跑 d100**: 建议单独重跑 d100 seed=0 训练 + eval，利用已有 d000-d050 checkpoint。
4. **无 ARC 结果**: 日志中未包含 ARC eval。
