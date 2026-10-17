# Paper Data Integration Audit — 2026-05-16

## ✅ 已集成

1. **Compounding curves (Fig 2)** — 3 条曲线（Llama-spike, Mistral-flat, Qwen-spread）全部到位，数据与最新 sweep 完全一致：
   - Llama: k0=8.09, k256=1519.19 ✅
   - Mistral v2 (bf16_2bitonly): k0=7.04, k256=45.28 ✅
   - Qwen v2: k0=9.81, k256=98.75 ✅
   - `generate_compounding_curves.py` 与 PDF 图表一致

2. **Compounding 讨论 (§3.3)** — `experiments.tex:89-107` 正确引用 `fig_compounding_curves`，数值描述与图表数据吻合

3. **Qwen 3-seed downstream CI** — `experiments.tex:121` 已集成 ±1σ error bars（ARC ±0.4, HS ±0.2, PIQA ±0.2, WG ±1.2）

## ❌ 缺失

1. **Llama 3-seed downstream CI error bars** — `experiments.tex:123` Llama 行只有单值（-0.8, +0.0, -0.1, +0.5），无 ±std
   - **修复**: 获取 `llama_3seed_downstream_ci` 数据后，在 `experiments.tex:123` 为 Llama 行添加 `{\scriptsize$\pm$X.X}` 格式的 error bars；更新 caption (line 115) 提及 "Qwen and Llama values are mean over 3 seeds"

2. **Phi-3-medium-14B Table 1 数据** — `experiments.tex:46-60` Table 1 当前覆盖 7 模型，无 Phi-3-medium 行
   - **修复**: 实验完成后在 `experiments.tex:58`（Pythia 行前）插入 Phi-3-medium 行；同步更新 §3.1 Models 段落 (line 7-16) 和 caption (line 44) 描述
