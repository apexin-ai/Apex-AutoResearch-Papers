# Handover — 2026-05-22

> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。

## 运行中
（无）

## 待处理
- d158_llama_sft_s42（准备中）
- d154-8b-exec-s42-k4（准备中）
- d154-8b-exec-s42-r2（准备中）
- d154-8b-exec-s42: D154 cross-model: exec-only GRPO on Qwen3-8B/FOLIO seed=42. Tests whether larger model (8B vs 4B) exhibits same Goodhart collapse patterns under exec-only reward. Pilot experiment.（准备中）
- d154-8b-isr-s43: D154 cross-model: ISR β=0.1 GRPO on Qwen3-8B/FOLIO seed=43. Replication of ISR s42 for statistical power at 8B scale.（准备中）
- d154-8b-isr-s42: D154 cross-model: ISR β=0.1 GRPO on Qwen3-8B/FOLIO seed=42. Tests whether ISR-induced Goodhart collapse (TS dominance) persists at 8B scale, or if larger capacity enables genuine reasoning.（准备中）
- d154-8b-exec-s44: D154 cross-model: exec-only GRPO on Qwen3-8B/FOLIO seed=44. Replication of exec s42 for statistical power across model scale.（准备中）
- d154-8b-exec-s43: D154 cross-model: exec-only GRPO on Qwen3-8B/FOLIO seed=43. Replication of exec s42 for statistical power across model scale.（准备中）
- d146-pf-pipeline（准备中）
- d144-llama-isr-s43: D144 cross-model: ISR β=0.1 GRPO on LLaMA-3.2-3B/FOLIO seed=43. Replication of ISR s42 for statistical power.（准备中）
- …另有 22 项

## 近期结论
- **exec-only-s45-1000step-k8** (killed): —
- **exec-only-s45-1000step** (negative): Exec-only GRPO 1000-step K=4 seed 45: testing whether extended training amplifies structural degeneration beyond 500 steps. Config identical to plan001 series (K=4).
- **d154-8b-exec-s42-k8** (negative): 8B K=8 exec-only non-convergence: gradient signal present but insufficient for convergence within 500 steps, resulting in near-zero training reward by step 500 ← 基于 d154-8b-exec-s42-k4v2

## 趋势
成功 73 / 负向 50 / 失败 49 / 共 184
CE_count: 1 →（近 3 次 success）
CI_count: 0 →（近 3 次 success）

## 下一步
（无活跃 idea，请通过 ideas.md 添加）

## 资源状态
westd-39279: 无 GPU 信息

## 告警
- sta-phase1-exec-only: 训练失败 — unknown
- sta-phase1-exec-sta: 训练失败 — unknown
- sta-phase1-exec-only-r2: 训练失败 — unknown
- sta-phase1-exec-sta-r2: 训练失败 — unknown
- sta-phase1-exec-only-r3: 训练失败 — unknown
- sta-phase1-exec-sta-r3: 训练失败 — unknown
- plan001-exec-only-s42: 训练失败 — unknown
- plan001-exec-only-s42-r3: 训练失败 — unknown
- plan001-exec-only-s43: 训练失败 — unknown
- plan013-random-reward-s42: 训练失败 — unknown
- plan013-random-reward-s42-r2: 训练失败 — unknown
- plan001-exec-only-s43-r2: 训练失败 — unknown
- plan013-random-reward-s42-r3: 训练失败 — unknown
- plan001-exec-only-s43-r3: 训练失败 — unknown
- plan006-prolog-exec-s43: 已被终止 — unknown
- plan018-additive-random-b01-s43: 训练失败 — unknown
- plan009-sft-baseline-s42: 已被终止 — unknown
- plan009-sft-baseline-s42-r2: 训练失败 — unknown
- plan009-sft-baseline-s42-r3: 训练失败 — unknown
- plan006-prolog-exec-s43-r2: 训练失败 — unknown
- exp1-isr-b03-s44: 训练失败 — unknown
- exp1-random-b03-s44: 训练失败 — unknown
- exp1-isr-b03-s43-r2: 已被终止 — unknown
- plan015-linear-s42: 已被终止 — unknown
- exp1-isr-b03-s43-r4: 已被终止 — unknown
- exp1-random-b03-s43-r2: 已被终止 — unknown
- exp1-random-b03-s43-r3: 训练失败 — unknown
- plan018-additive-random-b01-s42-1000: 训练失败 — unknown
- exp1-isr-b03-s42-1000: 训练失败 — unknown
- plan009-sft-baseline-s44-1000-r2: 训练失败 — unknown
- plan001-exec-only-s43-1000: 训练失败 — unknown
- plan001-exec-only-s44-1000: 训练失败 — unknown
- sweep-isr-b01-s45: 已被终止 — unknown
- sweep-exec-only-s45: 已被终止 — unknown
- plan018-random-b01-s45-r2: 训练失败 — unknown
- plan018-additive-random-b01-s45-r3: 训练失败 — unknown
- w2-qwen3-8b-exec-pilot: 训练失败 — unknown
- w2-qwen3-8b-isr-pilot: 训练失败 — unknown
- w2-qwen3-8b-exec-pilot-r2: 训练失败 — unknown
- w2-qwen3-8b-isr-pilot-r2: 训练失败 — unknown
- gated-isr-t03-s42: 训练失败 — unknown
- gated-isr-t03-s43: 训练失败 — unknown
- gated-isr-curriculum-t02-s42: 训练失败 — unknown
- gated-isr-curriculum-t02-s43: 训练失败 — unknown
- gated-isr-curriculum-t02-s42-r2: 训练失败 — unknown
- gated-isr-curriculum-t02-s43-r2: 训练失败 — unknown
- exec-retrain-v3-s42: 已被终止 — unknown
- exec-retrain-v3-s43: 已被终止 — unknown
- gated-isr-warmstart-t02-s42: 训练失败 — unknown
- gated-isr-warmstart-t02-s43: 训练失败 — unknown
- exec-only-s43-1000step-r2: 训练失败 — unknown
- exec-only-s43-1000step-r3: 训练失败 — unknown
- exec-only-s43-1000step-r4: 训练失败 — unknown
- exec-only-s43-1000step-r5: 训练失败 — unknown
- exec-only-s43-1000step-r6: 训练失败 — unknown
- d129-1.7b-random-b01-s43: 训练失败 — unknown
- d154-8b-exec-s42-r3: 已被终止 — unknown
- d157-shuffled-isr-s42: 训练失败 — unknown
- d157-shuffled-isr-s42-r2: 训练失败 — unknown
- exec-only-s52-batch2: 训练失败 — unknown
- exec-only-s45-1000step-k8: 已被终止 — unknown
