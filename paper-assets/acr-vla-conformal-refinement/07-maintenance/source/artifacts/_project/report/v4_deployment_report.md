# V4 Deployment Report (2026-05-13)

## Step 1: GPU 清空
- Kill PID 62654/62930/63075/63218 → nvidia-smi 输出为空，4 GPU 全部清空 ✅

## Step 2: Wrapper 部署验证
- 修复版 `smolvla_wrapper_fixed.py` → 服务器 `src/smolvla_wrapper.py`
- 行数: 281 ✅ (预期 ~282)
- flip count: 2 ✅
- resize_with_pad count: 3 ✅
- _unnormalize_action count: 2 ✅

## Step 3: evaluate.py 状态 → 需修复 → 已修复
发现两个 bug 并已修补：
1. `get_eef_state` 只返回 6D（缺 gripper_qpos） → 改为 `get_robot_state` 返回 8D（eef_pos + axisangle + gripper_qpos）
2. 调用 wrapper 时 kwarg 名 `eef_state=` → 改为 `robot_state=`
- 修复后验证: get_robot_state=4处, gripper_qpos=4处, eef_state=0处 ✅
- HF_HUB_OFFLINE=1 已设置 (line 30) ✅

## Step 4: train_crm.py cache_dir
- `--cache_dir` 有效参数 (line 56-57)，默认 `/root/autodl-tmp/crm_cache/` ✅
- 旧 cache `/root/autodl-tmp/crm_cache/spatial/` 已清除 ✅

## Step 5: 最小验证
- Import SmolVLAWrapper, split_action 成功 ✅
- split_action(7D) → 6D + 1D 正确 ✅

## Step 6: 实验提交

| exp_id | PID | GPU | 说明 |
|--------|-----|-----|------|
| eval-spatial-v4-full | 69379 | cuda:0 | vla_only, spatial, 10 rollouts |
| precompute-v4-shard0 | 69647 | cuda:1 | spatial+object, shard 0/3 |
| precompute-v4-shard1 | 69793 | cuda:2 | spatial+object, shard 1/3 |
| precompute-v4-shard2 | 69937 | cuda:3 | spatial+object, shard 2/3 |

## 已知限制
- precompute 管道中 `ee_states` 仅 6D（缺 gripper_qpos），wrapper 的 `_normalize_state` 会自动 pad 到 max_state_dim。不影响 CRM 训练信号（obs_features 主要由图像驱动）。
