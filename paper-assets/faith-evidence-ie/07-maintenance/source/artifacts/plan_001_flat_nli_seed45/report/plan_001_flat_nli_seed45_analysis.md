# plan_001_flat_nli_seed45 训练结果分析

## Conclusion: **SUCCESS**

训练正常完成，无 error/crash，EXIT_CODE=0。

## 训练概况

| 项目 | 值 |
|------|-----|
| 模型 | Qwen3-4B + SFT adapter + LoRA RSFT |
| 数据 | 2691 RSFT samples (flat-NLI), CED mean=0.725 |
| Epochs | 3 |
| Total steps | 507 |
| Train runtime | 5938.5s (~1h39m) |
| Train loss (final) | **0.6245** |
| Eval loss (final) | 0.7567 |
| Eval mean_token_accuracy | 0.8299 |

## Task Eval (DocRE F1) 各阶段

| Step | F1 | Ign-F1 | Evi-F1 | EDCR | Preds |
|------|-----|--------|--------|------|-------|
| 169 (epoch ~1) | 0.4522 | 0.4522 | 0.7493 | 0.6309 | 865 |
| 338 (epoch ~2) | 0.4700 | 0.4700 | 0.7538 | 0.6178 | 836 |
| **507 (epoch 3, final)** | **0.4876** | **0.4876** | **0.7927** | **0.6517** | 820 |

F1 逐 epoch 稳步提升，无过拟合迹象。

## Checkpoint

- 路径: `/root/autodl-tmp/rsft_output_flat_nli_s45/`
- adapter_model.safetensors: 529MB
- 中间 checkpoints: 350, 400, 450, 500, 507

## 与同系列对比

| Seed | Rel-F1 (final) | Evi-F1 | 状态 |
|------|----------------|--------|------|
| s42 (eval) | 0.4539 | — | 已完成 eval |
| **s45** | **0.4876** | **0.7927** | ✅ 训练完成，待 eval |
| s44 | — | — | 训练中 |

s45 的 task-eval F1 (0.4876) 高于 s42 eval 的 rel_f1 (0.4539)，但注意 task-eval 仅用 50 docs，正式 eval 用全量 dev set，数值不可直接对比。

## 日志路径
`/root/runs/faith-evidence-ie/plan_001_flat_nli_seed45.log`
