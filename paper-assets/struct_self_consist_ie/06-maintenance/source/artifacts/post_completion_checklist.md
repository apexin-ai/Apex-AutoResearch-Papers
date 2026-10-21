# Post-Completion Checklist

## 1. 72B Few-Shot FewNERD（ETA ~01:30 UTC, 2026-05-20）

- [ ] SSH autodl-5090-b 确认实验完成
- [ ] `compute_signals.py --input-dir output/72b_fewshot --dataset fewnerd --model-size 72 --regime fs`
- [ ] `bootstrap_construction.py --input-dir output/72b_fewshot --dataset fewnerd`
- [ ] `format_for_scaling.py --report .../full_signal_report.json --model-size 72 --regime fs`
- [ ] 更新 `72b_fewshot_signal_summary.json` 加入 FewNERD 数据
- [ ] 填入 `zs_vs_fs_comparison_draft.tex` 的 5 个 placeholder
- [ ] 更新 registry metrics
- [ ] 汇报 Director

## 2. 7B FewNERD Pipeline（ETA ~04:30 UTC, 2026-05-20）

Pipeline 自动跑 train→export→inference→signals→construction

- [ ] 确认 pipeline 自动步骤全部完成
- [ ] 手动 `compute_signals.py --input-dir output/qwen25_7b_fewnerd_seed42 --model-size 7 --regime ft`
- [ ] 手动 `compute_signals.py --input-dir output/qwen25_7b_fewnerd_seed123 --model-size 7 --regime ft`
- [ ] 手动 `compute_signals.py --input-dir output/qwen25_7b_fewnerd_seed456 --model-size 7 --regime ft`
- [ ] 手动 `format_for_scaling.py --report .../full_signal_report.json --model-size 7 --regime ft`
- [ ] 填入 `scaling_narrative_A.tex` / `scaling_narrative_B.tex` 的 scaleSevenDegen / Greedy / Constr / LP
- [ ] 更新 `tab:scale_comparison` 或 `tab:scaling_ft` 7B 行
- [ ] 更新 registry
- [ ] 汇报 Director

## 3. 14B FewNERD（ETA ~19:20 UTC, 2026-05-20）

训练完成后需手动 pipeline

- [ ] Export LoRA adapter
- [ ] 3-seed N=8 inference
- [ ] `compute_signals.py` + `bootstrap_construction.py` + `format_for_scaling.py`
- [ ] 填 14B placeholder
- [ ] 更新 registry
- [ ] 汇报 Director

## 4. 32B FewNERD（ETA ~01:40 UTC, 2026-05-21）

训练完成后需手动 pipeline，**这是最后一块拼图**

- [ ] Export LoRA adapter
- [ ] 3-seed N=8 inference
- [ ] `compute_signals.py` + `bootstrap_construction.py` + `format_for_scaling.py`
- [ ] 填 32B placeholder
- [ ] 更新 registry
- [ ] 汇报 Director
- [ ] **定稿决策**：7B/14B/32B/72B 全部就绪后，选择 narrative A（monotonic）或 B（non-monotonic），启用 `fig:scaling_curve`，定稿 §5.5
