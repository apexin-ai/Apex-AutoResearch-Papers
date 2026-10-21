# Memory — gen-depth-fingerprint

## tail_decay 一致性修复 (2026-05-20, CRITICAL)
- 原始 6 gen (extract_features.py) 使用 log-prob slope: `np.polyfit(ranks[100:1000], sorted_avg_log_probs[100:1000], 1)[0]`
- 新增 3 gen (llama/mistral_filter_and_extract.py) 错误使用了 NLL proportion: `np.mean(nll_arr > percentile_90_threshold)`
- 修复: Llama/Mistral 已在 05-16 由 fix_tail_decay_and_eval.py 修复; Gemma 在 05-20 重新提取
- 验证: 全 9 gen tail_decay 均值 [-0.0024, -0.0022]，std ~0.0002，完全一致
- **教训**: 新 generator 加入时必须验证 feature extraction pipeline 与原始 pipeline 完全一致

## 9-gen LOGO 扩展结果 (2026-05-20, exp_057)
- 42,015 行数据，9 generators
- 9-gen 3-class F1=0.751, binary F1=0.666; 8-gen baseline 0.770; Δ=-0.019
- Generator 难度排序: pythia-1b (0.857) > qwen3-0.6b (0.819) > ... > qwen3-8b (0.696) > gemma-2-2b (0.628) > mistral-7b (0.605)
- Gemma-2-2B gen-1 几乎不可分（F1=0.036）——可能是模型架构/tokenizer 差异导致
- **结论**: scale 增加使分类更困难但不消灭信号; Gemma/Mistral 是泛化最差的两个 generator

## DDR 因果性分析 (2026-05-20, exp_058)
- **Permutation importance**: drifting 组均值 0.158 vs stationary 组 0.030（5.3x），hapax_ratio 最强 (0.235)，tail_decay 最弱 (0.014)
- **Granger causality**: 6/7 特征显著（panel N=29095, lag=1）；entropy_min 唯一不显著（pooled p=0.538, Fisher p=0.375）；最大 ΔR²=entropy_std 0.031；方向: hapax_ratio/ttr 随 depth 递增，entropy 系列递减
- **Intervention**: 所有 7 特征干预后 F1 下降 0.6–2.0pp；entropy_max 最大（2.0pp），entropy_min 最小（0.6pp）
- **结论**: hypothesis 成立（success）——DDR 特征对 depth 有因果预测力，超越相关性
- **注意**: entropy_min 是最弱特征（Granger 不显著、permutation 最低），但仍有干预效果；T=5 限制导致只能用 lag=1

## TOST Bootstrap (2026-05-20, exp_059)
- n=1000 bootstrap iterations, margin d=0.2
- 3 个 stationary 特征 (entropy_max/min, tail_decay) 100% rejection rate
- entropy_std 0% rejection (对照, intermediate)
- **结论**: TOST 等价性结论完全稳健

## 独立种子控制实验 (2026-05-18)
- exp_051: 完全不共享种子的 cross-generator 评估 F1=0.680，与 shared-seed LOGO 0.694 差 -1.4pp
- 两方向: Pythia→OLMo 0.695, OLMo→Pythia 0.666
- 与 seed demeaning (F1=0.701) 形成收敛证据：depth signal 非 topic artifact
- 0.680 略低于 LOGO 合理：独立种子 = strict cross-generator transfer，比 LOGO 更严格

## 温度曲线关键约束 (2026-05-17)
- autodl-5090 容器只有 1 张可见 GPU（非 4 张），所有 GPU 实验必须串行
- top_p 必须固定为 0.9（与主实验一致），不同温度下不能改 top_p

## 模型版本确认 (2026-05-17)
- Qwen3 系列: Qwen/Qwen3-0.6B, Qwen/Qwen3-1.7B, Qwen/Qwen3-8B（HuggingFace 上可用）
- 主实验用 8 个 base model generators: Pythia-1B, Pythia-2.8B, OLMo-2-1B, Qwen3-0.6B, Qwen3-1.7B, Qwen3-8B, Llama-3.2-3B, Mistral-7B

## Downstream utility 负面结果 (2026-05-16)
- plan-004-v2: depth-aware curation 不优于随机抽样（all > size_matched > depth01 ≈ binary_filtered >> depth0_only）
- 已 reframe 为 diagnostic-not-curative（D009 决策）
- 跨 seed 方差极小 (<0.002)，结论稳健

## 竞品实验参考
- 暂无直接竞品（depth classification 是新任务）
- 最近的 baseline: FastDetectGPT, Binoculars, LD-Score（均为 binary detection，非 depth）
