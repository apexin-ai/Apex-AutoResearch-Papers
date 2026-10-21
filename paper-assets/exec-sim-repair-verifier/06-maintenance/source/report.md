# Handover — 2026-05-23

> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。

## 运行中
（无）

## 待处理
- deepseek-cls-repo-resume: Resume deepseek-cls-repo from checkpoint-2211 after SIGHUP crash at step 3747/6633（已分配 ? GPU:?，等待提交）
- cls14b-func-s42-v2-bf16-eval: CLS 14B bf16 eval should yield higher accuracy than NF4 eval (89.47%), eliminating quantization confound. If bf16 accuracy > 89.47%, the CLS 8B→14B regression is an NF4 artifact; if bf16 ≈ 89.47%, the regression is real.（准备中）
- qwen_cwm_s456_resume2（准备中）
- qwen_cwm_s456_resume（准备中）
- deepseek-cwm-repo-s42-e3-seq4096-eval（准备中）
- exp-downsample-cls-func-v3-eval-v2: Eval downsample CLS (Qwen3-4B, ~8K训练数据) on repo-level test set. 如果 accuracy 接近全量训练的 CLS (83.63%), 则证明 CLS formulation 优势不来自数据量（准备中）
- exp-e-qwen3-3shot-baseline: Qwen3-8B 3-shot few-shot CLS baseline 在 repo-level 表现差于 fine-tuned models，与 DeepSeek 3-shot 一致，证明 fine-tuning 的必要性跨模型成立（准备中）
- D131-cwm-s42-epoch3-seq2048（准备中）
- D133-cwm-s42-e2-seq2048-home-resume（准备中）
- deepseek-cwm-repo-s42-epoch2-eval: Eval CWM s42 epoch 2 checkpoint 解耦过拟合 vs seed 差异：如果 epoch 2 accuracy >> epoch 3 (56.7%)，则 CWM repo-level 在 epoch 3 过拟合（准备中）
- …另有 9 项

## 近期结论
- **cls-downsample-400-s42** (success): CLS function-level trained on ~447 samples (matching TRAJ variant count) should reveal whether TRAJ's lower accuracy (86.30% vs CLS 88.43%) is due to data volume disparity (34×) or formulation difference. If CLS@447 ≈ TRAJ → data volume is main confound; if CLS@447 > TRAJ → formulation effect independent of data volume.
- **deepseek-cwm-repo-s456-train-v2** (success): DeepSeek CWM repo-level s456-v2：第 3 seed，与 s42/s123-v2 对齐（train_unified.py + --train_file swebench_full/swebench_train.jsonl, 70748 行）。组成完整 3-seed coverage (42/123/456)。使用 epoch 3 final checkpoint 评估。 ← 基于 deepseek-cwm-repo-s456-train
- **traj14b-func-s456** (success): TRAJ 14B (seed 456) 补完 Table 2 的 14B TRAJ 行。与 CLS/CWM 14B 对比验证三公式在 14B 的 scaling 趋势。4B→8B TRAJ scaling +2.13pp，14B 应保持或扩大趋势。

## 趋势
成功 149 / 负向 7 / 失败 60 / 共 248

## 下一步
（无活跃 idea，请通过 ideas.md 添加）

## 资源状态
seetacloud-westd-4x5090: 无 GPU 信息

## 告警
- trace-then-judge: 训练失败 — unknown
- repo-level-cls: 训练失败 — unknown
- repo-level-cwm: 训练失败 — unknown
- repo-level-cls-v2: 训练失败 — unknown
- repo-level-cwm-v2: 训练失败 — unknown
- repo-level-cls-v3: 训练失败 — unknown
- repo-level-cwm-v3: 训练失败 — unknown
- repo-level-cls-home: 训练失败 — unknown
- repo-level-cwm-v4: 已被终止 — unknown
- repo-level-cwm-v5: 训练失败 — unknown
- repo-level-cwm-v6: 训练失败 — unknown
- repo-level-cwm-v7: 训练失败 — unknown
- repo-level-cwm-v8: 训练失败 — unknown
- repo-level-cwm-v9: 训练失败 — unknown
- repo-level-cls-seed123: 已被终止 — unknown
- repo-level-cwm-seed123: 已被终止 — unknown
- repo-level-cwm-v11: 已被终止 — unknown
- repo-level-cls-8b: 已被终止 — unknown
- repo-level-cwm-v12: 已被终止 — unknown
- repo-level-cwm-seed123-conda: 已被终止 — unknown
- repo-level-cwm-8b-conda: 训练失败 — unknown
- repo-level-cls-8b-seed123-conda: 训练失败 — unknown
- repo-level-cwm-8b-conda-v2: 训练失败 — unknown
- repo-level-cls-8b-seed123-conda-v2: 训练失败 — unknown
- repo-level-cwm-8b-conda-v3: 训练失败 — unknown
- repo-level-cwm-8b-conda-v4: 训练失败 — unknown
- cls8b-ckpt3000-test-eval: 已被终止 — unknown
- cls8b-ckpt3000-test-v2: 已被终止 — unknown
- cls8b-seed123-ckpt3000-val-eval: 已被终止 — unknown
- repo-level-cls-8b-s42-ckpt200-val: 已被终止 — unknown
- cls4b-v5-val5120-sweep-home: 训练失败 — unknown
- cls4b-v5-ckpt4400-val5120-eval: 已被终止 — unknown
- cls4b-v5-ckpt4400-val5120-eval-v2: 已被终止 — unknown
- cls8b-s42-ckpt1600-val8192-eval: 训练失败 — unknown
- cls4b-v5-val-sweep-ckpt4400: 已被终止 — unknown
- cls8b-s42-ckpt1200-val8192: 训练失败 — unknown
- cls8b-s42-ckpt1200-val8192-v2: 训练失败 — unknown
- cls8b-seed123-ckpt3000-test8192-eval-v2: 训练失败 — unknown
- cls4b-seed123-ckpt800-test5120-eval: 训练失败 — unknown
- cls8b-seed123-ckpt6200-test8192-eval: 训练失败 — unknown
- cls8b-seed123-ckpt6400-test8192-eval: 训练失败 — unknown
- cls8b-s42-ckpt200-val8192-eval: 训练失败 — unknown
- cls4b-v5-ckpt4000-test5120-eval: 训练失败 — unknown
- cwm8b-ckpt400-test-eval: 训练失败 — unknown
- cwm-rank32-ablation: 已被终止 — unknown
- cwm-4b-rank32-ablation: 已被终止 — unknown
- cwm-rank64-ablation: 已被终止 — unknown
- cwm-4b-rank64-ablation: 已被终止 — unknown
- s42-extended-val-sweep: 训练失败 — unknown
- cls8b-s42-extended-val-sweep: 已被终止 — unknown
- cls8b-s42-resume-val-sweep: 训练失败 — unknown
- s42-extended-val-sweep-v2: 训练失败 — unknown
- cls8b-s42-resume-val-sweep-seq8192: 已被终止 — unknown
- cls8b-s42-resume-val-sweep-seq4096: 已被终止 — unknown
- cls8b-s42-resume-val-sweep-gpu1: 训练失败 — unknown
- cls8b-s42-resume-ckpt1000-test-mutation: 训练失败 — unknown
- cls8b-s42-ckpt1000-test-mutation: 已被终止 — unknown
- repo-level-cwm-8b-conda-v6: 已被终止 — unknown
- cwm8b-ckpt400-test-eval-v2: 已被终止 — unknown
- cwm8b-ckpt400-test-eval-v3: 已被终止 — unknown
- cwm8b-ckpt400-test-eval-shard3: 训练失败 — unknown
- deepseek-cls-repo: 训练失败 — unknown
- deepseek-traj-func-s123: 已被终止 — unknown
- deepseek-cls-repo-v2: 训练失败 — unknown
- deepseek-cls-repo-v3: 训练失败 — unknown
- deepseek-cls-repo-v4: 训练失败 — unknown
- qwen3-8b-traj-repo-s42: 训练失败 — unknown
- D133-cwm-s42-e2-seq2048-home: 训练失败 — unknown
- deepseek-cls-repo-v5-ckpt4210-eval: 训练失败 — unknown
- exp-downsample-cls-func: 训练失败 — unknown
- exp-downsample-cls-func-v2: 训练失败 — unknown
- cls8b-repo-s456-train: 训练失败 — unknown
- deepseek-cls-repo-s456-train: 已被终止 — unknown
- qwen3-8b-cwm-repo-s123-train: 训练失败 — unknown
- cls8b-repo-s456-train-v2: 训练失败 — unknown
- deepseek-cls-repo-s456-train-v2: 训练失败 — unknown
- deepseek-cls-repo-s456-train-v3: 训练失败 — unknown
- qwen3-8b-cwm-repo-s456-train: 已被终止 — unknown
- cls8b-repo-s456-eval: 训练失败 — unknown
- deepseek-cls-repo-s456-eval: 训练失败 — unknown
- qwen3-8b-cwm-repo-s123-train-v2: 已被终止 — unknown
- deepseek-cwm-repo-s123-train: 训练失败 — unknown
- deepseek-cwm-repo-s456-train: 已被终止 — unknown
- qwen3-8b-cwm-repo-s123-train-v3: 训练失败 — unknown
- qwen3-8b-cwm-repo-s456-train-v2: 训练失败 — unknown
- qwen3-8b-cwm-repo-s456-train-v3: 训练失败 — unknown
- deepseek-cwm-repo-s123-eval: 训练失败 — unknown
- deepseek-cwm-repo-s123-train-v2: 训练失败 — unknown
- deepseek-cwm-repo-s123-train-v3: 训练失败 — unknown
- deepseek-cwm-repo-s456-e2-eval: 已被终止 — unknown
- cls14b-func-s42: 已被终止 — unknown
- 14b-baseline-0shot-3shot: 训练失败 — unknown
