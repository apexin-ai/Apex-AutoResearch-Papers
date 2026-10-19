# Memory — distill_sparse_swiglu

## Per-layer KL 实验关键发现 (2026-05-21)

### Per-layer KL vs E2E KL downstream gap 分析
- 平均 downstream gap = −2.61pp（6 task mean, excl BoolQ）
- Commonsense (ARC-c/WG/HS) 平均 −3.89pp，HS 最大 drop (−4.88pp)
- Reasoning (MMLU/GSM8K) 平均 −1.87pp
- PIQA 几乎无差异 (−0.23pp)
- PPL gap: +0.24 (9.05 vs 8.81)
- **结论**: per-layer 独立优化丢失跨层 coupling 导致 downstream 一致性下降，commonsense 比 reasoning 更敏感

### BoolQ 3-seed 完整对比 (uniform allocation)
- **E2E KL BoolQ**: s42=75.60%, s123=70.06%, s456=75.54% → Mean=73.73±3.18%
- **Per-layer KL BoolQ**: s42=71.77%, s123=70.46%, s456=51.25% → Mean=64.49±11.49%
- **Gap**: −9.24pp (E2E KL 优势明显)
- **方差对比**: Per-layer KL 方差 3.6× 大于 E2E KL (11.49 vs 3.18 std)
- **结论**: BoolQ 对跨层 coupling 高度敏感，per-layer 独立优化在 NLI 类 task 上不稳定

### Convergence 特征
- 2-seed 均在 ~6000 步收敛（后续改善 <0.1 PPL）
- s123 在 step 8000 出现轻微回弹 (9.16 vs step 6000 的 9.11)，但 step 10000 回到 9.06
- 最终 PPL 跨 seed 高度一致 (9.06 vs 9.06)

### 数据缓存问题
- westd-34887 BoolQ 缓存已通过 embed download 方式部署成功（2026-05-21）
- westd-41718 有完整的 super_glue/boolq 缓存
- **解决方案**: 在 submit_training_job 命令中嵌入 download 步骤（先联网下载,再切 offline 模式 eval）

## Cross-seed Jaccard 分析 (2026-05-22, R18-W7)

### 方法学关键区分
- 论文 46-68% 使用 **per-token activation magnitudes**（per-token abs(dense_act) top-k），不是 weight norms
- 代码确认于 `generate_kl_oracle_masks.py:94-100`：`dense_act.abs().topk(k, dim=-1)`
- 论文明确标注 "computed per-token"（experiments.tex:80）

### 正确参照系（三层对比，非简单 ratio）
- Cross-seed KL Jaccard = 36.3% — **低于 random baseline 10pp** → KL seeds 收敛
- Random baseline (30% sparsity) = 46.2%（计算: 1 - (0.7²)/(2×0.7-0.7²) = 0.462）
- KL-vs-magnitude (30%) = 46% ≈ random → KL 和 magnitude **本质不相关**
- KL-vs-magnitude (50%) = 68% > random 66.7% → 高稀疏度下更强

### 教训
- 用 weight L2 norms 做 magnitude mask（42.8%）与论文用 activation magnitudes（46%）**方法不同**，结果偏低
- Appendix §Cross-Seed Mask Consistency 已含完整数据（cross-seed=0.363, random=0.462），无需重跑
- R18-W7 回应应用 random baseline 做 anchor，而非简单 cross-seed vs KL-vs-mag 的 ratio

## BCE Compensation Data (2026-05-22)

### 50% Sparsity
- **BCE + comp**: PPL = 25.44, exp_id = `bce_comp_staged_s42` (field: `predictor_hard_mask_ppl`)
- **BCE no comp**: PPL = 27.96, exp_id = `bce_comp_staged_s42` (field: `predictor_hard_mask_ppl_no_comp`, same-run ablation: 关闭 comp 路径再 eval)
- **Δ (no_comp − comp) = +2.52 PP** (comp 提升 ~9% per-token PPL)
- **独立验证**: exp_id = `bce_isocompute_v3_s42_eval`, `wikitext2_ppl = 27.97`（独立 BCE-no-comp 50% run，与同 run ablation 一致）
- ⚠️ **稀疏度差异**: BCE+comp model_level_sparsity = 0.558 vs KL baseline 0.498（comp 训练得到稍高 sparsity，对比时需标注）
- 配置: staged training (200 步 BCE warmup + 800 步 joint)，eval_seq_len=2048，wikitext-2

### 30% Sparsity
- **BCE + comp**: ⚠️ **数据不存在** — registry 中所有 30% BCE 实验均为 no-comp（hypothesis 字段明示 "no compensation"）
- **BCE no comp (uniform allocation)**:
  - exp_id = `bce_30_s42_uniform_eval`, PPL = 15.7069 (allocation=uniform)
  - exp_id = `bce_iso_v3_s42_30pct_uniform_eval`, PPL = 14.947
  - exp_id = `bce_iso_v3_s123_30pct_uniform_eval`, PPL = 15.2051
  - exp_id = `bce_iso_v3_s456_30pct_uniform_eval`, PPL = 15.1102
- **BCE no comp (global_topk allocation)**:
  - exp_id = `bce_30pct_s42_eval`, wikitext2_ppl = 11.2445（training_sparsity_native=0.042，Lagrangian 失败，TEAL 外部强制 30%）
- **Δ at 30%**: 不可计算（缺 BCE+comp 30% 实验）

### 对比 KL+comp（同样 staged，30% sparsity）— 仅作参考非任务要求
- `kl_comp_30pct_s42_ppl`: wikitext2_ppl = 8.9768
- `kl_comp_30pct_s123_ppl`: wikitext2_ppl = 8.9768
- 提示: 若要补 30% BCE+comp 数据，可对照 KL+comp 30% 同 spec 复跑

### 来源注释
所有数字来自 `registry.yaml`，每个数字附 exp_id 追溯：
- 50% comp 提升: `bce_comp_staged_s42` (metrics.predictor_hard_mask_ppl / .._no_comp)
- 50% 独立 no-comp 验证: `bce_isocompute_v3_s42_eval` (metrics.wikitext2_ppl)
- 30% no-comp uniform: `bce_30_s42_uniform_eval`, `bce_iso_v3_s{42,123,456}_30pct_uniform_eval`
- 30% no-comp global_topk: `bce_30pct_s42_eval`

## kl50_global_s123_downstream_v2 诊断 (2026-05-22)

### 结论：Cron 误报，实验实际已成功完成

**错误报告**: "process dead 5× with no sentinel/W&B — auto-resolved as failed"

**实际状态**: 实验正常完成，结果已保存至 `/root/distill_sparse_swiglu/results/benchmark/kl50_global_s123_downstream_v2/results.json`

**结果**:
- ARC-c: acc=0.3567, acc_norm=0.3916
- WinoGrande: acc=0.6401
- MMLU: acc=0.2908
- GSM8K: exact_match=0.0341

**误报原因**: 实验以 `WANDB_MODE=disabled` 运行，cron 监控依赖 W&B metrics 或 PID 存活检测。进程正常退出后 PID 消失，cron 连续 5 次检测到 "process dead" 且无 W&B 数据可回退验证，自动判定失败。

**前序实验 `kl50_global_s123_reeval`**: 最初在 westd-41718 上因 CLI 参数不匹配失败（`--predictor_path` vs `--checkpoint`，`--allocation global` vs `--sparsity_mode teal_global`），retry 后成功。结果: PPL=11.72, ARC-c=0.3635, WG=0.6109, MMLU=0.2834, GSM8K=0.0258。

**建议**: Registry 中 `kl50_global_s123_downstream_v2` 状态需从 `conclusion: failed` 更新为 `conclusion: success`，metrics 已在 results.json 中。

## 竞品实验参考
（见 literature_map.yaml）

## 经验教训
- Registry 状态机不允许跳级转换，必须依次走 PREPARING→PENDING→QUEUED→ALLOCATED→RUNNING→ANALYZING→DONE
- submit_training_job 命令必须用 bash -c "..." 包裹（tmux 用 sh 不支持 source）
- 离线模式下 eval 前必须确认目标服务器上的 HF datasets 缓存齐全
- GPU 编号从 0 开始（框架自动映射 CUDA_VISIBLE_DEVICES）
- 状态机走完需要在 RUNNING 步提供完整 spec，hypothesis 需 ≥20 chars 且 mechanistic
- BoolQ 缓存缺失时，可将 download 步骤嵌入 eval 命令
- Magnitude mask 有两种：weight norms（静态）vs activation magnitudes（per-token dynamic）。论文用后者。
- WANDB_MODE=disabled 的实验会导致 cron PID/W&B 监控误报失败——需在日志中写 sentinel 文件或检查 results.json 是否存在

## 硬规则 (2026-05-23, M049/D107)
- **本项目所有训练/eval命令必须加 `WANDB_MODE=disabled`**——项目未配置 W&B API key，不加会导致启动即崩溃（K=16 v1 argparse + v2 wandb key 连续两次失败教训）
- K=8 成功命令未显式加此参数但因环境变量碰巧无 wandb 包而幸免，不可依赖
