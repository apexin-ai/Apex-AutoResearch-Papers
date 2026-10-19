# Handover — 2026-05-16

> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。

## 运行中
| exp_id | 假设 | 状态 | 关键指标 | W&B |
|--------|------|------|---------|-----|
| unixcoder-3strat-s43 | UniXcoder-base s43: 3 strategies (random/embedding/dataflow) × seed 43, patience=2。与 s42 (patience=3) 构成 2-seed 统计，验证 null result 稳定性。Director D064 批准。 | — | — | — |
| m2_full_qwen | Full M2 Qwen: 3 strategies (random/embedding/dataflow) × 3 seeds on full M1 data (~11K train/seed). Statistical validation of pilot signal (embedding > random +2pp). Go/no-go for paper claims per D018. | — | — | — |

## 待处理
- plan_018_bm25: BM25 negative baseline: Dream 审稿三档一致认定缺 BM25 baseline 是论文最大结构性缺陷。Phase 1 (CPU): 对 M2 训练语料建 BM25 索引，挖掘 BM25 hard negatives，生成训练数据。Phase 2 (GPU): 用 BM25 negatives 训练 Qwen + StarCoder 各 1 seed，对比 R@1。（排队等待 GPU）
- plan_015_dynamic: Dynamic negative mining (epoch-level re-mining): 每 epoch 重新用当前 encoder embedding 挖掘 negatives，验证 static mining 是否足够。缩减版：只跑 dynamic_ep × 1 seed (Qwen, s42)，~11h 单卡。若 dynamic ≈ static（预期 <1pp 差异），在 Limitation 段排除 confound。（排队等待 GPU）
- m2_full_starcoder_v3（准备中）
- d062-remaining-eval（准备中）
- plan_005_stratified: Plan 005 分层分析：按 repo size/pool size/query-pos similarity/structural data availability/neg_difficulty quartile 5 维度分层评估 embedding vs random 策略差异，控制 pool_size confound。Claim 2 支撑实验。v2 结果为 ground truth（v1→v2 changelog 见 art_20260514_3008c4）。（准备中）
- unixcoder-3strat-s44: UniXcoder-base s44: 3 strategies (random/embedding/dataflow) × seed 44, patience=2。与 s42/s43 构成 3-seed 统计，确认 encoder-only/small-scale null result。Director D064 批准。（准备中）
- qwen_random_s42_retrain: Qwen random_s42 重训（统一 regime: 2 epoch + early_stopping_patience=2）。原 s42 用 3 epoch + patience=0 导致 pool=50 R@1 异常低（0.2730 vs s43=0.3138/s44=0.3181），不可纳入 cross-seed 统计。重训后可补完 3-seed comparison。Director 批准方案 B。（准备中）

## 近期结论
- **m2_full_qwen_continued** (failed): M2 Qwen continued: 继续 m2_full_qwen 的剩余 runs (random_s44 + embedding×3 + dataflow×3)。原实验 cron 在 s42 退出时自动设为 ANALYZING，但链仍在运行。 ← 基于 m2_full_qwen
- **m2_full_starcoder_resumed** (failed): M2 StarCoder resumed: 继续 m2_full_starcoder 的 8 sequential runs (random×2 + embedding×3 + dataflow×3)。原实验因 cron timeout 标记为 failed，实际 PID 519791 正常运行。 ← 基于 m2_full_starcoder
- **unixcoder-3strat-s42** (negative): UniXcoder-base (125M, encoder-only RoBERTa) 第三 encoder: 3 strategies (random/embedding/dataflow) × seed 42。验证 embedding distance mining 优势是否跨架构泛化（encoder-only vs decoder-only）。batch_size=16, max_seq_length=1024, LoRA, gradient-checkpointing。

## 趋势
成功 12 / 负向 3 / 失败 7 / 共 36

## 下一步
（无活跃 idea，请通过 ideas.md 添加）

## 资源状态
bjb1-42106: 无 GPU 信息

## 告警
- p2b-smoke-test: 已被终止 — unknown
- p2b-smoke2: 已被终止 — unknown
- p2b-smoke3: 已被终止 — unknown
- p2b-smoke4: 已被终止 — unknown
- p2b-smoke5: 已被终止 — unknown
- p2b-smoke6: 已被终止 — unknown
- p2b-smoke7: 已被终止 — unknown
- p2b-smoke8: 已被终止 — unknown
- p2b-all-9runs: 已被终止 — unknown
- mvp_p2b_contrastive_training: 已被终止 — unknown
- mvp_p2b_contrastive_v2: 已被终止 — unknown
- p2b_eval_all: 已被终止 — unknown
- m2_early_pilot: 已被终止 — unknown
- m2_early_pilot_v2: 训练失败 — unknown
- m2_early_pilot_v3: 已被终止 — unknown
- m2_full_starcoder: 训练失败 — unknown
- m1_reextract: 训练失败 — unknown
- m2_full_starcoder_resumed: 训练失败 — unknown
- m2_full_qwen_continued: 训练失败 — unknown
- plan_003_swebench_eval: 训练失败 — unknown
- unixcoder_3strat_s42: 训练失败 — unknown
