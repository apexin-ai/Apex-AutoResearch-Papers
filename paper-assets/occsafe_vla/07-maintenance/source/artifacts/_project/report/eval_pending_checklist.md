# Eval Pending Checklist

生成时间: 2026-05-24

## 需要 eval 的实验（checkpoint 已确认存在）
| exp_id | server | checkpoint_path | condition | seed |
|--------|--------|-----------------|-----------|------|
| full_occ_retrain_s0 | westd-34685 | /root/autodl-tmp/checkpoints/full_occ_retrain_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt | Retrain Full OCC (occ_detach=False) for gradient decomposition analysis | 42 |

## checkpoint 不存在或已被清理
| exp_id | expected_path | server | 备注 |
|--------|---------------|--------|------|
| (无) | - | - | - |

## 已有 eval 但 Director 点名检查的
| exp_id | eval_exp_id | CAR | TSR |
|--------|-------------|-----|-----|
| cutoff_15k_s0 | cutoff_15k_s0_eval | 0.804 | 0.912 |
| cutoff_25k_s0 | cutoff_25k_s0_eval | 0.688 | 0.844 |
| cutoff_45k_s0 | cutoff_45k_s0_eval | 0.764 | 0.896 |
| reverse_cutoff_s0 | reverse_cutoff_s0_eval | 0.700 | 0.788 |
| cutoff_s0 | cutoff_s0_eval | 0.768 | 0.912 |
| cutoff_s1 | cutoff_s1_eval | 0.798 | 0.918 |
| detach_ln_s0 | detach_ln_s0_eval | 0.792 | 0.914 |
| detach_ln_s1 | detach_ln_s1_eval | 0.756 | 0.906 |
| detach_ln_s2 | detach_ln_s2_eval | 0.748 | 0.884 |

## 当前正在训练（完成后需要 eval）
| exp_id | server | 状态 |
|--------|--------|------|
| cutoff_45k_s1 | westd-34685 | RUNNING |
| ablation_occ_detach_s0_retrain | westd-10894 | RUNNING |
| full_occ_ln_s2 | westd-10894 | RUNNING |
| full_occ_ln_s1 | westd-10894 | RUNNING |
| reverse_cutoff_s2 | westd-34685 | RUNNING |
| cutoff_25k_s2 | westd-34685 | RUNNING |
| cutoff_15k_s1 | westd-34685 | RUNNING |
| full_occ_ln_s0 | westd-10894 | RUNNING |
