End-to-End DeBERTa DCOL Code (plan_008 预研，bonus)

文件:
- src/dcol_dataset.py (239行): 多model/strategy数据加载，19维特征log1p预处理，正确的3-way stratified split，ContrastiveBatchSampler
- src/dcol_trainer.py (526行): DCOLModel (DeBERTa + BatchNorm feature projector + ordinal contrastive head)，strategy-aware learnable margins，multi-margin contrastive ordinal loss + CE
- src/dcol_eval.py (293行): pairwise AUC，per-model/per-strategy分组评估，confusion matrix可视化，RF baseline对比
- scripts/run_dcol_training.sh (141行): 端到端pipeline

关键调试经验:
1. 特征值极端(var_ppl~1e11) → log1p变换 + BatchNorm1d
2. fp16 overflow → 移除GradScaler，autocast forward + fp32 loss
3. AdamW eps=1e-8 在 DeBERTa multi-group optimizer 下产生 NaN → 改为 eps=1e-6

DeBERTa-v3-large 已下载到 /root/autodl-tmp/models/deberta-v3-large/ (828M, 434M params)