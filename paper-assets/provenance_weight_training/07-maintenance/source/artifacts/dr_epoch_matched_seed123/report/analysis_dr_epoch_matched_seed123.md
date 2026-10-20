## dr_epoch_matched_seed123 最终指标

- holdout_ppl: **未评估** (eval 未运行)
- holdout_loss: **未评估**
- owt_ppl: **未评估**
- wiki_ppl: **未评估**
- train_loss_final: 2.831
- total_steps: 2533/2533 (完成)
- checkpoint_path: `/root/autodl-tmp/provenance_weight_training/output/models/dr_epoch_matched_seed123/final`
- checkpoints: checkpoint-2000, checkpoint-2500, checkpoint-2533

## detect_remove_q05_v2_seed123 最终指标

- holdout_ppl: 17.366
- holdout_loss: 2.854
- owt_ppl: **未评估** (OOD eval 未运行)
- wiki_ppl: **未评估** (OOD eval 未运行)
- train_loss_final: 2.760
- total_steps: 24414/24414 (完成, 200M tokens, batch_size=4, seq_len=2048)
- checkpoint_path: `/root/autodl-tmp/provenance_weight_training/output/models/detect_remove_q05_v2_seed123/final`
- checkpoints: checkpoint-23500, checkpoint-24000, checkpoint-24414

## Epoch Confound 分析

### Seed42 参考数据
| 实验 | holdout_ppl | holdout_loss | owt_ppl | wiki_ppl |
|------|-------------|--------------|---------|----------|
| dr_epoch_matched_indep_lr_v2_seed42 | 17.651 | 2.871 | 18.261 | 15.194 |
| detect_remove_q05_v2_seed42 | 17.285 | 2.850 | 18.014 | 15.053 |

- Seed42 gap (full - epoch_matched): 17.285 - 17.651 = **-0.366** (full 更好)

### Seed123 初步数据
| 实验 | holdout_ppl | holdout_loss |
|------|-------------|--------------|
| dr_epoch_matched_seed123 | 未评估 | 未评估 |
| detect_remove_q05_v2_seed123 | 17.366 | 2.854 |

- Seed123 gap: **无法计算** (dr_epoch_matched_seed123 缺少 eval)

### 一致性判断
无法完成对比，需要先运行以下 eval：
1. **dr_epoch_matched_seed123**: holdout + OOD (owt, wiki) eval
2. **detect_remove_q05_v2_seed123**: OOD (owt, wiki) eval

### 备注
- detect_remove_q05_v2_seed123 的 holdout_ppl=17.366 vs seed42 的 17.285，差异 +0.081，seed 间变异在合理范围内
- dr_epoch_matched_seed123 的 train_loss=2.831 vs seed42 的 2.871(holdout_loss)，趋势相近
- uniform_epoch_matched_indep_lr_seed42 另有一组 eval 数据（holdout_ppl=18.06, owt_ppl=18.65, wiki_ppl=15.51），注意这是不同实验配置
