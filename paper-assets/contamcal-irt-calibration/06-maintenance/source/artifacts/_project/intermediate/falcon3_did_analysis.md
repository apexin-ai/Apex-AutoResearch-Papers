# Falcon3-7B-Base DiD Analysis (Table 3 Format)

**Date**: 2026-05-22
**Status**: BLOCKED — servers inaccessible

## Blockers

DiD 需要 item-level correctness 数据（每道题的对/错），不能从 aggregate accuracy 计算。

- **westd-29999**: SSH auth failed (连续 5 次认证失败)
- **cqa1-21977**: SSH config 中无此 host entry

所需数据文件（均在远程服务器）:
- `correctness_matrix.json`: `/root/autodl-tmp/exp001/eval_results/Falcon3-7B-Base_{d000,d025}_s42_aligned/`
- `contamination_labels_mmlu_d025.json`: `/root/autodl-tmp/exp001/sft_data/`

## 运行方法

服务器恢复后，SSH 到 westd-29999 或 cqa1-21977 执行:

```bash
cd /root/contamcal-irt-calibration
python artifacts/falcon3_did_analysis.py \
    --sft-dir /root/autodl-tmp/exp001/sft_data \
    --eval-dir /root/autodl-tmp/exp001/eval_results \
    --output-dir /root/contamcal-irt-calibration/artifacts/falcon3_did
```

输出:
- `falcon3_did/falcon3_did_results.json` — 完整 DiD 统计 (4 dosages × 2 benchmarks)
- 终端直接输出 Table 3 LaTeX row

## Table 3 参考格式

```
Model          | Treated Δ    | Untreated Δ  | DiD          | Verdict
Gemma-2 9B     | +3.1**       | +2.6***      | +0.5 (ns)    | generalization
OLMo-2 7B      | +1.6 (ns)    | +2.7***      | -1.1 (ns)    | mixed
Phi-4 14.7B    | +0.3 (ns)    | +0.6 (ns)    | -0.3 (ns)    | no-effect
Qwen-14B       | -6.9***      | -7.6***      | +0.7 (ns)    | anti-contam.
Qwen-7B        | -3.8**       | -2.9***      | -0.8 (ns)    | anti-contam.
Falcon3 7B     | [待计算]      | [待计算]      | [待计算]      | [待计算]
```

注: d025 MMLU, n_treated=3540, n_untreated=10502. 10,000 bootstrap, seed=42.

## 预期结果预判

基于 Falcon3 aggregate data:
- d000 → d025 MMLU: +2.46pp (58.77% → 61.23%)
- 其他 Benefit 模型（Gemma-2, OLMo-2）的 DiD 均为 ns
- Falcon3 作为 Benefit 模型，预期 treated Δ ≈ untreated Δ > 0，DiD 接近 0 (ns)
- 最可能的 verdict: **generalization** (如果 both deltas significant) 或 **mixed**

## 计算方法 (与 treated_untreated_analysis.py 完全一致)

1. 加载 d000 和 d025 的 per-item correctness (14,042 binary values for MMLU)
2. 用 contamination labels 分为 treated (3,540) 和 untreated (10,502)
3. treated_delta = mean(dose_treated) - mean(base_treated)
4. untreated_delta = mean(dose_untreated) - mean(base_untreated)
5. DiD = treated_delta - untreated_delta
6. Bootstrap (B=10,000, seed=42) 计算 95% CI 和 p-value
7. Verdict 按 significance 分类

## 脚本

`artifacts/falcon3_did_analysis.py` — 独立可运行，输出 Table 3 行和完整 JSON。
