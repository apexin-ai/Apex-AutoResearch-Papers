# Handover — 2026-05-25

> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。

## 运行中
（无 — 4 GPU 全部空闲）

## D&R 阈值扫描结果（完整）
| 阈值 | 数据保留 | holdout_ppl | owt_ppl | wiki_ppl | seeds |
|------|---------|-------------|---------|----------|-------|
| q>0.3 | 31.5% | 17.25 | — | — | 3 (prior) |
| q>0.5 | 41.4% | 17.291 | 18.02 | 15.06 | 1 (ckpt-5500) |
| q>0.7 | 50.0% | 17.32 | 18.04 | 15.11 | 3 |
| Uniform | 100% | 17.694 | — | — | baseline |
| Adaptive b* | 100% | 17.674 | — | — | baseline |

## 近期结论
- **q07 三 seed 完成** (success): holdout=17.32±0.00, owt=18.04±0.01, wiki=15.11±0.01 — 方差极小
- **q05 ckpt-5500** (success): holdout=17.291, owt=18.02, wiki=15.06（final model 因 optimizer corruption 废弃）
- **所有 D&R 阈值均显著优于 Uniform (17.694) 和 Adaptive b* (17.674)**

## 趋势
成功 175 / 负向 14 / 失败 42 / 共 254

## 下一步
- Paper Agent 可用完整 D&R 数据更新论文
- 4 GPU 空闲待命

## 资源状态
westd-41312: cuda:0/1/2/3 全部空闲

## 告警
- detector_modernbert: 已被终止 — unknown
- diagnostic_contamination100: 已被终止 — unknown
- adaptive_v2_seed42: 已被终止 — unknown
- adaptive_v2_seed123: 已被终止 — unknown
- adaptive_v2_seed456: 已被终止 — unknown
- grid_b_low_seed42: 训练失败 — unknown
- tau_0.6_seed42: 已被终止 — unknown
- bs8_seed42: 训练失败 — unknown
- bs8_nmin2_seed42: 训练失败 — unknown
- contamination_60_seed42: 训练失败 — unknown
- grid_b_low_seed42_r2: 训练失败 — unknown
- grid_b_low_seed42_r3: 训练失败 — unknown
- grid_b_low_serial_seed42: 已被终止 — unknown
- tau_05_nmin2_seed42: 已被终止 — unknown
- tau_06_nmin2_seed42: 已被终止 — unknown
- tau_07_nmin2_seed42: 已被终止 — unknown
- tau_09_nmin2_seed42: 已被终止 — unknown
- tau_095_nmin2_seed42: 已被终止 — unknown
- nmin5_seed42: 已被终止 — unknown
- batchsize16_nmin8_seed42: 训练失败 — unknown
- threshold_q07_seed42: 训练失败 — unknown
- random_reweight_seed42: 训练失败 — unknown
- rho02_adaptive_tau09_seed42: 训练失败 — unknown
- batch_adaptive_tau_rho06_seed42: 训练失败 — unknown
- bs8_auto_nmin_seed42: 训练失败 — unknown
- grid_b0_3_seed123: 训练失败 — unknown
- grid_b0_3_seed456: 已被终止 — unknown
- bs8_auto_nmin_r2: 训练失败 — unknown
- batch_adaptive_tau_rho06_r2: 训练失败 — unknown
- rho02_adaptive_tau09_r2: 训练失败 — unknown
- batchsize16_nmin8_r2: 已被终止 — unknown
- random_reweight_seed123_r2: 训练失败 — unknown
- bs8_auto_nmin_r3: 训练失败 — unknown
- batch_adaptive_tau_rho06_r3: 训练失败 — unknown
- rho02_adaptive_tau09_r3: 训练失败 — unknown
- random_reweight_seed123_r3: 训练失败 — unknown
- rho02_adaptive_tau09_r4: 训练失败 — unknown
- random_reweight_seed123_r4: 训练失败 — unknown
- uniform_1_7b_seed42: 训练失败 — unknown
- detect_remove_q07_seed42_r2: 已被终止 — unknown
- detect_remove_q03_seed42: 已被终止 — unknown
- tau07_downstream_eval: 训练失败 — unknown
- rho06_tau07_seed42: 训练失败 — unknown
- rho06_tau07_seed123: 已被终止 — unknown
- rho06_tau07_seed456: 已被终止 — unknown
- uniform_1_7b_seed42_v3: 已被终止 — unknown
- adaptive_1_7b_seed42_v3: 已被终止 — unknown
- uniform_1_7b_seed42_v4: 训练失败 — unknown
- adaptive_1_7b_seed42_v4: 训练失败 — unknown
- adaptive_tau08_scratch_seed42: 训练失败 — unknown
- gpt2_adaptive_seed123: 训练失败 — unknown
- gpt2_adaptive_seed456: 训练失败 — unknown
- adaptive_tau08_scratch_seed42_v2: 训练失败 — unknown
- gpt2_adaptive_seed123_v2: 训练失败 — unknown
- ngram_adaptive_seed456: 训练失败 — unknown
- dr_epoch_matched_indep_lr_seed42: 训练失败 — unknown
- bs16_adaptive_tau07_seed123: 训练失败 — unknown
- detect_remove_q05_v2_seed123: 训练失败 — unknown
- dr_epoch_matched_seed123: 训练失败 — unknown
- rho03_adaptive_seed456: 训练失败 — unknown
- bs8_nmin4_adaptive_seed123: 训练失败 — unknown
- bs8_nmin4_uniform_seed123: 训练失败 — unknown
- bs8_nmin4_adaptive_seed456: 已被终止 — unknown
- bs8_nmin4_uniform_seed456: 已被终止 — unknown
- p0_batchsize_16: 训练失败 — unknown
