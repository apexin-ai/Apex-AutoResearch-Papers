## Bug Fix: M029 gripper loss double-sigmoid

### File: /root/autodl-tmp/RoboFlamingo/train_libero.py

### Change 1 (L144): Loss function
- Before: `grip_loss = nn.functional.binary_cross_entropy_with_logits(grip_pred, (grip_gt > 0).float())`
- After:  `grip_loss = nn.functional.binary_cross_entropy(grip_pred, (grip_gt > 0).float())`
- Reason: grip_pred already passed through sigmoid in model output; using `_with_logits` applies sigmoid twice

### Change 2 (L148): Loss weight
- Before: `loss = arm_loss + 0.01 * grip_loss`
- After:  `loss = arm_loss + 0.1 * grip_loss`
- Reason: 0.01 weight too small, gripper signal drowned out

### Training restart
- Old PID: 47691 (killed)
- New PID: 53406
- Save dir: /root/autodl-tmp/checkpoints/roboflamingo_libero_c5_v2
- Log: /root/autodl-tmp/importance_margin_vla_compress/logs/train_c5_roboflamingo_v2.log
- GPU: 1 (CUDA_VISIBLE_DEVICES=1)