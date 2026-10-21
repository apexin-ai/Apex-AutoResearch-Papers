# Memory — nlp_variance_gtheory

## Gated Model 约束 (2026-05-20)
Llama-3.1-8B-Instruct 和 gemma-2-9b-it 是 HF gated models，直接用 repo ID 加载失败。westd-32570 上通过 ModelScope 下载到本地路径（如 `/root/autodl-tmp/.hf_cache/LLM-Research/Meta-Llama-3___1-8B-Instruct`）。exp-001 正式运行需要 model path mapping 或 HF token。

## 双 Metric 设计决策 (2026-05-20, D002)
binary_correct 和 text_exact_match 测量正交维度（Spearman ρ = −0.21, n.s.）。前者衡量评估有效性（item 难度主导），后者衡量可复现性（prompt×item + temperature 主导）。两者必须同时保留——不能互相替代。

## Temperature 对 text_match 的决定性影响 (2026-05-20)
T=0 → text_match=0.247, T=0.5 → text_match=0.019（降 92%），但 binary_correct 几乎不变。这是 G-theory 框架的关键洞察：采样随机性改变文本表述但不改变答案选择。

## FP32 精度效应确认 (2026-05-20)
FP32 的 8.5pp accuracy gap 中 97.4% 是精度效应（非引擎 confound）。BF16-trained model 用 FP32 推理表现更差，可能因为权重从 BF16 加载到 FP32 时的数值行为差异。

## Gemma2 不支持 float16 (2026-05-21)
vLLM 拒绝以 float16 加载 gemma2：`"The model type 'gemma2' does not support float16. Reason: Numerical instability."`。这是架构层面限制，非配置问题。Director 决策 (方案 A 修改版)：cross-model 分析用 bf16+fp32 (2 precisions × 4 models 平衡设计)，fp16 仅用于 Llama/Mistral/Qwen 的 within-model G-study。bf16 vs fp16 差异 <0.1pp (Llama 已证实)，precision 信号集中在 fp32 vs 其他 (10.7pp gap)。

## M006: D-study 公式方向性检查 (2026-05-21)
D-study 公式 `G_ni = σ²τ / (σ²τ + σ²δ × (n_actual / ni))` — 注意是 n_actual/ni 而非 ni/n_actual。G 必须随 n_items 单调递增（items 越多 error 越小）。所有 D-study 代码必须带 monotonicity assertion。

## Cross-model G-study 关键洞察 (2026-05-21, 更新至 8-model)
8-model MMLU BF16: item_id=37.88% [33.12, 42.17], model×item=30.21%, G_item=0.896 [0.874, 0.915]。核心叙事 "item difficulty is model-specific" 在 8-model 下仍成立。

## G_item 计算 Bug 汇总 (2026-05-21, D016 最终确认)
两个独立 bug：(1) gstudy_full.py 用了 ICC 而非 Henderson I G coefficient；(2) FF G-study 代码 residual 除以 1 而非 2304（D016）。统一修复后所有 benchmark G_item 在 0.82-0.90。方差百分比不受影响。

## HellaSwag 3-temp Bug (2026-05-22)
`pd.read_json` 解析 JSON `0.7` 为 float64 带精度误差。修复：`.round(1)` before `.astype(str)`。**所有跨 benchmark 比较必须用 2-temp 数据**。

## 8-model Clean 最终数字 (2026-05-22, Phase 2 完成)

| Benchmark | Format | item_id% | G_item |
|-----------|--------|----------|--------|
| MMLU | MC | 37.88% | 0.896 |
| ARC | MC | 37.88% | 0.892 |
| HellaSwag | MC | 34.27% | 0.872 |
| GSM8K | FF | 16.86% | ~0.86 |
| MATH | FF | 24.03% | 0.888 |

MC mean=36.68%, FF mean=20.45%, diff=16.23pp. Cohen's d=1.73.

## D-study 效率比也是 format-conditional 的 (2026-05-22)
MC ratio ~11×, FF ratio ~21.5×。Bootstrap CI: 所有 ratio 下界 >10.7×。

## D014 叙事验证 (2026-05-22)
Cross-benchmark ρ=0.70 (p=0.188), within-MMLU ρ=0.806 (p=0.005)。Format-conditional 是一级叙事，item heterogeneity 是二级机制。

## Messing (2026) 引用确认 (2026-05-22)
arXiv:2604.11581, Solomon Messing, "Hidden Measurement Error in LLM Pipelines Distorts Annotation, Evaluation, and Benchmarking"。使用 G-theory，judge identity 43.8%, prompt×judge 12.4% — 两个数字都准确。之前因拼写 "Mesting" 误报为幻觉。

## Scale Validation 初步结论 (2026-05-22, Phase 3)
Qwen2.5 within-family 3-point scale validation (MMLU, bf16×2temp, 5-facet Henderson I):
- **3B**: item_id=75.3%, G_item=0.963, accuracy=0.682
- **7B**: item_id=73.4%, G_item=0.956, accuracy=0.742
- **ref (Llama-8B bf16×2t)**: item_id=68.5%, G_item=0.937
- 结论：item dominance 在 3B-7B range 内是 scale-invariant，甚至比 8B 更强
- 7B 对 prompt wording 更敏感（prompt:item=12.2% vs 3B 的 8.8%）
- 72B 待完成（下载中 ~19/140GB）
