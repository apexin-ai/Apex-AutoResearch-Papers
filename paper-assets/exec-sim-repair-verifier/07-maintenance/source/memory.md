# Memory — exec-sim-repair-verifier

## 竞品实验参考
（见 literature_map.yaml）

## 经验教训

### timeout 级联杀进程 (M026, 2026-05-20)
`kill <timeout_PID>` 会 SIGTERM 整个进程组，包括子进程（训练进程）。解决方案：用 nohup 启动训练，不用 timeout wrapper。

### ssh_execute 内置 timeout (2026-05-20)
ssh_execute 工具本身有超时限制。长时间训练不能用 ssh_execute 直接跑，必须用 submit_training_job 或 nohup 后台化。

### train_unified.py 数据 bug (2026-05-20)
`--task cwm` 默认加载 function-level 数据 (cwm_train.jsonl)，不是 repo-level。必须显式传 `--train_file swebench_full/swebench_train.jsonl`。

### CWM eval 耗时 (M024, 2026-05-20)
Qwen CWM eval (seq8192, batch=1): ~20h。DeepSeek (seq4096, batch=4): ~13h。不是 1h。

### CLS 对过拟合天然鲁棒 (2026-05-21)
CLS eval_loss 涨 123% 但 accuracy 仅 -0.1pp。CWM 则 epoch 2→3 accuracy 下降 5.36pp。Classification formulation 对 overfitting 比 generation formulation 更鲁棒。

### CWM eval seq_length 不一致教训 (2026-05-24)
Table 2 Qwen3-8B CWM 66.48±1.15 的三个 seed 全部 seq8192，内部一致。s42 来源为 cwm8b-ckpt400-test-eval-v3（ckpt-400, seq8192, 65.18%）。后续 ckpt6100 reeval 误用 seq4096、ckpt300 reeval 误用 seq2048，均与 Table 2 参数不匹配，不可混合。**跑 eval 前必须核查与已有数据的 seq_length/checkpoint 一致性**。

## Rebuttal 素材

### Checkpoint sensitivity（2026-05-21）
28 个 val/test checkpoint sweep 数据已存在 registry。Reviewer 问 checkpoint selection sensitivity 时可快速出图。数据支撑 "<1pp checkpoint selection noise"。

### CWM 过拟合 + early stopping 无法救（2026-05-21）
DS s123 1-epoch: 75.45% (unparseable 66.4%) vs s42 3-epoch: 61.49%。即使 oracle early stopping，CWM 仍 ~7pp below CLS 且 66% unparseable。等 s123-v3 / s456-v2 3-epoch 数据确认 within-seed 趋势后可用。

## 模型版本验证记录
（首次使用某模型时记录已验证的版本）

## 数据一致性修正记录 (2026-05-21)
- Qwen CLS s42: 85.34 → 84.48 (source: cls8b-s42-resume-ckpt3600-test-v2)
- Qwen TRAJ s42: 72.92 → 70.83 (source: qwen3-8b-traj-repo-s42-best-eval, D159)
- DeepSeek CLS s123 = 74.93: known_outlier (NaN eval_loss)
- 影响范围：compute_supplementary_stats.py, integrate_cwm_results.py, plot_figure2_v2.py 已全部修正
