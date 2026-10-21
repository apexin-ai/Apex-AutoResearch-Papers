# Memory — turn_residual_gating

## 服务器环境
- westd-20861: RTX PRO 6000 Blackwell 98GB, conda base 环境
- Qwen 模型路径: /root/.cache/modelscope/Qwen/Qwen2___5-7B-Instruct
- Llama-3 模型路径: /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-8B-Instruct/（safetensors, ~16GB, vocab_size=128256）
- 数据路径: /root/turn_residual_gating/data/ultrachat_8k (8000 samples)
- Python 激活: source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

## D048 SS eval 结论 (2026-05-22)
- D048 s42 eval (bootstrap CI): SS AR GAR=0.3833 [0.3692, 0.3934], TF GAR=0.5025, gap=1.31×
- 对比旧 v8b eval: s42 gap 从 1.57× 修正为 1.31×（D048 protocol 更严谨），s123 之前为 1.20×
- SS+steering 双路互补: SS baseline 0.38 + β=5 → 0.67 (CI [0.64, 0.69])，PPL 代价从 1.35→1.81
- SS 不影响 AR PPL (1.35 = base)，但 TF PPL 从 4.34 降至 2.78（训练改善）
- N=5 conv AR eval 的 CI 已经足够 tight (range ~0.02)，效果大小远超统计噪声

## Multi-seed 结论 (C7, 2026-05-22)
- v7 TG: s123 完全复现 s42（gap 30.6× vs 32×, TF GAR 0.505 vs 0.504, AR GAR 0.017 vs 0.016）
- v8b SS: s123 优于 s42（gap 1.20× vs 1.57×, modelgen GAR 0.418 vs 0.318）— SS mitigation 跨 seed 稳健
- 训练 metrics 高度一致：loss/gate profile 差异在噪声范围内
- Gate profile 层选择性：s42 最低 L3/L4, s123 最低 L1/L5 — 具体层不同但浅层抑制 pattern 一致

## Llama 跨模型结论 (C5, 2026-05-22)
- TF: TG 0.484 vs LoRA-only 0.481 (Δ=0.6%) → gating 零增量 confirmed
- AR (N=20 median): TG 0.0179 vs LoRA-only 0.0184 (Δ<0.1pp) → 零增量 confirmed
- AR mean 不可靠（CoV>100%, spikes 拉高），论文用 median 报告
- Base TF 0.017, Base AR 0.010 → gap 1.6× (control pass)
- TG/LO gap ratio ~11-27×（mean/median），exposure bias 跨模型确认
- Li et al. 2024 (COLM) 是 direct-competitor：bib 已有 (li2024measuring) 但论文未 cite，需在 Related Work 讨论

## 关键约束与教训
- M020: 禁止将 AR nGAR 与 TF raw GAR 对比（TF nGAR=11.88 不是 0.484）
- M021: 训练完成后必须先 eval 再启动下一个训练（v8b s123 因跳过 eval 延迟 10h）
- M022: 日志 step 是 microsteps（per-epoch 0-7999），optimizer_steps = microsteps / grad_accum(8)。汇报进度一律用 optimizer steps (X/3000)
- 论文绝不能使用 "normalization artifact" 叙事（Director 明令）
- Cron 回调不可靠（连续 5+ 次丢失）——超过预期完成时间 30min 应主动 spawn Worker 检查
- AR eval 中 GAR-ours mean 被 spikes 严重拉高（CoV>100%），必须用 median 报告
- v7 s123 checkpoint: runs/phase2_tg_s123_v7/epoch_2/
- v8b s123 checkpoint: checkpoints/tg_v8b_ss_s123/epoch_2/
- s42 目录名: tg_v8b_ss_fixed_s42（不是 tg_v8b_ss）
- D048 SS s42 checkpoint: runs/d048_ss_s42/epoch_2, eval results: results/d048_ss_s42/

## 论文数字修正记录 (2026-05-22)
- N=5 steering 残留引用已替换为 N=50 数据（abstract/intro/conclusion/discussion）
- Gap ratio 统一：精确值用 32×, 概述用 >30×, 范围 20-33× 或 12.5-33×
- plan_018 重复条目已清理
- levy2025lost / ko2024found 第一作者错误已修复 (commit 2e58ab1)
- literature_map 从空白填充 5 篇（含 Li et al. 2024 direct-competitor）
