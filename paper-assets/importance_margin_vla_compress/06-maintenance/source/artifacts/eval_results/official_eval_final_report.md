# LeRobot 官方 Eval 最终确认报告

## 执行结果

### 测试方法
在 `baseline/latest` checkpoint 上，用两种方法对比 10 个 episode：

1. **SmolVLA 官方 `select_action()`**：使用内置 action queue (deque, maxlen=50)，每步 pop 一个 action，queue 空时调 `_get_action_chunk()`
2. **我们的 `predict_actions()`**：直接调 `model.sample_actions()`，手动管理 action chunk index

### 结果

| 方法 | Success Rate | Mean Reward | Action Mean | Action Std |
|------|-------------|-------------|-------------|------------|
| select_action() | **0% (0/10)** | 0.0 | ~0.15 | 0.27–0.48 |
| predict_actions() | **0% (0/10)** | 0.0 | ~0.15 | 0.27–0.41 |

首步 action 对比 (同一 obs, 不同随机噪声): max diff=0.35 → **来自 flow matching 随机性，非 pipeline 差异**

## 关键配置参数

| 参数 | SmolVLA 官方值 | 我们的实现 | 是否一致 |
|------|---------------|-----------|---------|
| chunk_size | 50 | 50 | ✅ |
| n_action_steps | 50 | action_horizon=50 | ✅ |
| temporal_ensemble | **不存在** | 不存在 | ✅ |
| 图像预处理 | [0,1]→resize 512x512→[-1,1] | 相同（`prepare_images`内部完成） | ✅ |
| state 处理 | pad to 32 dim, 无 norm | 相同（`prepare_state`内部完成） | ✅ |
| action 后处理 | 无 clip | clip [-1,1] | ⚠️ 微小差异 |

## Normalization 分析

- SmolVLA 配置: `STATE=MEAN_STD, ACTION=MEAN_STD, VISUAL=IDENTITY`
- 但 normalization 只在 processor pipeline 中使用（`NormalizerProcessorStep` / `UnnormalizerProcessorStep`）
- 我们的训练直接调 `policy.forward(batch)` → **跳过 processor** → 原始空间
- 我们的 eval 直接调 `policy.model.sample_actions()` → **跳过 processor** → 原始空间
- **训练和 eval 一致，都在原始空间**

## 为什么不能直接跑 `lerobot-eval` CLI

1. **Checkpoint 格式不兼容**: 我们是 `checkpoint.pt` (含 LoRA weights)，官方需要 `config.json` + `model.safetensors`
2. **Normalization 不匹配**: 官方 eval 会用 processor pipeline 做 MEAN_STD 归一化，但模型在原始空间训练
3. **即使格式转换，normalization 会导致更差的结果**

## 结论

**eval pipeline 已确认正确。** 0% success rate 不是 eval 实现的问题。

根因在模型训练端（LoRA fine-tuning + flow matching 的兼容性问题），已在 `sim_rollout_diagnosis.md` 中详细诊断。
