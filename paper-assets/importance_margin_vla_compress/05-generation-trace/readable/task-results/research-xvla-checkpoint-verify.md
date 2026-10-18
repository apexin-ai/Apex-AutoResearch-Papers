# research xvla checkpoint verify

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_xvla-checkpoint-verify_20260520T092657_result.json`
- **Structured JSON:** [`05d3b2c342db4823a261.json`](../../sessions/05/05d3b2c342db4823a261.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。以下是完整结论：

---

## 1. Checkpoint 来源：确认是 LIBERO fine-tuned

`2toINF/X-VLA-Libero`（即服务器上 `/root/autodl-tmp/X-VLA-Libero/`）是 LIBERO fine-tuned checkpoint，论文声称 98.1% SR。`lerobot/xvla-libero` 是 LeRobot 框架的封装版本（93% SR）。两者都是 fine-tuned 而非通用预训练。

**0% SR 不是预期的，是 eval pipeline 有 bug。**

## 2. Token 数量（50）：实际是正确的

从 `modeling_florence2.py` 的 `_encode_image` 代码分析：
- DaViT 224×224 → patch stride [4,2,2,2] → 7×7 = 49 spatial tokens  
- `image_feature_source: ["spatial_avg_pool", "temporal_avg_pool"]` → 1 (spatial avg) + 49 (temporal avg) = **50 tokens**
- config 中 `max_pos_embeddings: 50` 也印证了这一点
- 50 tokens 是 X-VLA 正确的 vision token 数量，不是 bug

## 3. max_steps = 800：与官方一致

lerobot 官方 eval 命令使用 `episode_length=800`。X-VLA action chunk = 30，800 steps ≈ 27 次 forward pass。**不需要修改。**

## 4. 导致 0% SR 的 eval pipeline 问题

所有 episode 跑满 800 步后 FAIL，说明模型在输出 action 但从未完成任务。按可能性排序：

### 4a. 最可能：应使用 lerobot 官方 eval 而非自定义脚本
当前脚本从零手写了整个 eval pipeline（image preprocessing → model inference → action decoding → env step），任何一环出错就会导致完全失败。应先用 lerobot 的原生 eval 验证 checkpoint 是否能正常工作：
```bash
lerobot-eval --policy.path=lerobot/xvla-libero --env.type=libero --eval.batch_size=1 --eval.n_episodes=20
```

### 4b. Action normalization 缺失
X-VLA 训练时可能对 position/rotation 做了 normalization（mean/std 或 min/max）。`action_space.postprocess()` 只对 gripper 做了 sigmoid，position/rotation 直接输出。如果训练数据用了 normalized absolute actions，模型输出的 raw values 直接喂给 controller 会导致 action 完全错误。

### 4c. Image flip 可能错误
```python
# 当前：双向 flip (180° 旋转)
img = np.flip(np.flip(img, 0), 1).copy()
```
agentview 做了垂直+水平 flip。如果训练数据只做了垂直 flip（或不 flip），模型看到的场景是镜像的。

### 4d. `strict=False` 在 model loading 中
`model.load_state_dict(state_dict, strict=False)` 会静默忽略 key 不匹配，可能导致某些权重没有加载。应该先用 `strict=True` 验证所有 key 是否匹配。

### 4e. 其他小问题
- Proprio 的 gripper 值硬编码为 0.0（不过 `preprocess` 会 zero-out gripper，所以影响不大）
- Closed-loop proprio 用 predicted action 而非 env state 更新前 9 维（这是 X-VLA 的设计，不一定是 bug）

## 5. 建议修复步骤

1. **先用 lerobot 官方 eval** 验证 checkpoint 本身是否工作正常
2. 如果 lerobot eval 能跑出 90%+ SR，说明自定义脚本有 bug → 对比 lerobot 的 action 解码和 image 预处理
3. 如果 lerobot eval 也是 0%，检查 checkpoint 是否完整下载、环境依赖版本是否匹配
4. 将 `strict=False` 改为 `strict=True` 排除权重加载问题

Sources:
- [lerobot/xvla-libero Model Card](https://huggingface.co/lerobot/xvla-libero)
- [lerobot/xvla-base](https://huggingface.co/lerobot/xvla-base)
- [X-VLA Official Repo](https://github.com/2toinf/X-VLA)
- [X-VLA Absolute Actions in LIBERO (Issue #15)](https://github.com/2toinf/X-VLA/issues/15)
- [X-VLA Action Conversion (Issue #2)](https://github.com/2toinf/X-VLA/issues/2)
- [LeRobot X-VLA Documentation](https://huggingface.co/docs/lerobot/xvla)

---
