# research pi0 pi05 libero feasibility

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_pi0-pi05-libero-feasibility_20260521T005149_result.json`
- **Structured JSON:** [`5e81de378b9aecb6e691.json`](../../sessions/5e/5e81de378b9aecb6e691.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## π0 / π0.5 LIBERO 调研报告

### 模型信息
- **HF Repo (π0)**: `lerobot/pi0_libero_base` / `lerobot/pi0_libero_finetuned`
- **HF Repo (π0.5)**: `lerobot/pi05_libero_base` / `lerobot/pi05_libero_finetuned`
- **官方代码**: `github.com/Physical-Intelligence/openpi`
- **参数量**: π0 ≈ 3.3B（PaliGemma 3B VLM + 0.315B action expert）；π0.5 ≈ 3.6B（结构略不同，用 adaptive RMSNorm 注入 timestep）
- **VRAM 需求**: FP16 推理约 ~7-8GB，bf16 LoRA 微调在 4090 上峰值 ~16GB（batch=16）。**4090 24GB 推理完全没问题。**
- **推理框架**: 两条路径——(1) HuggingFace LeRobot 集成，(2) Physical Intelligence 官方 openpi

### LIBERO 兼容性
- **Fine-tune 数据**: 标准 LIBERO（libero_spatial, libero_object, libero_goal, libero_10），与我们使用的一致
- **Action space**: **7D**（3D eef position + 3D rotation + 1D gripper），与我们的 SmolVLA/OpenVLA 完全一致
- **Action chunking**: chunk_size 由 config 决定，n_action_steps=10
- **Observation 要求**: agentview_image + robot0_eye_in_hand_image（双摄像头），8D proprioception（eef_pos + axisangle + gripper_qpos）——与我们现有的 SmolVLA wrapper 接口一致
- **图像预处理**: openpi 版本会旋转 180°；LeRobot 版本有自己的 pipeline

### 已知问题
- **复现率低于报告值**: GitHub issue [#2114](https://github.com/huggingface/lerobot/issues/2114) 和 [#952](https://github.com/huggingface/lerobot/issues/952) 报告 finetuned 模型实测成功率比 leaderboard 低 10-20%
  - pi0_libero_finetuned 实测: spatial 69%, object 72%, goal 83%, long 35%, 均值 64.75%
  - pi05_libero_finetuned 实测: spatial 77%, object 66%, goal 89%, long 55%, 均值 71.75%
- issue [#2533](https://github.com/huggingface/lerobot/issues/2533) 报告 pi05_libero_base 零成功率

### Action Diversity (CRM 兼容性)
- **多次采样可行性**: **可行。** Flow matching 推理从随机高斯噪声出发，通过 10 步 ODE 积分去噪。不同的 noise seed → 不同的 action trajectory。这与我们 SmolVLA wrapper 中 `generate_k_samples` 的机制完全相同。
- **采样方式**: 每次调用 `sample_noise()` 生成不同初始噪声，经过 denoise loop 得到不同 action chunk。我们现有代码已经实现了这个模式（见 `smolvla_wrapper_fixed.py:233-253`）。
- **KV cache 复用**: 与 SmolVLA 类似，可以先 encode prefix（图像+语言+状态），缓存 KV，然后多次采样 action——计算高效。
- **结论**: π0/π0.5 与 CRM 方法完全兼容，K-sample 生成无障碍。

### 环境依赖
- **方式 1 (LeRobot)**: `pip install lerobot && pip install -e ".[libero]"`
- **方式 2 (openpi)**: `git clone https://github.com/Physical-Intelligence/openpi && pip install -e .`
- **预估下载大小**: 模型权重 ~6-7GB（bf16 3.3-3.6B 参数）

### 服务器适配
- **4090 24GB**: ✅ 可以，推理约 7-8GB VRAM，K=10 采样有足够余量
- **当前服务器 bjb2-40593**: 可直接使用

### 适配工作量

**需要改动的部分：**
1. **新建 `pi0_wrapper.py`**（~200 行）——参照现有 `smolvla_wrapper_fixed.py` 的接口设计：
   - `preprocess_obs()`: 图像预处理差异（π0 用 PaliGemma processor，需 180° 旋转）
   - `encode_prefix()`: VLM 前向 + KV cache
   - `generate_k_samples()`: flow matching 去噪循环
   - `get_obs_features_and_samples()`: 端到端接口
   - normalizer stats 加载方式不同（openpi vs lerobot 格式）

2. **修改 `evaluate.py`**（~50 行）——添加 `--pi0` / `--pi05` flag，类似现有 `--openvla` 的 patch 模式

3. **CRM 模型兼容**——obs_features 维度变化：SmolVLA 是 960D，π0 的 PaliGemma hidden size 是 2048D。CRM 输入层需要适配或重新训练。

**关键风险：**
- obs_features 维度不同（960 vs 2048），CRM 不能直接迁移，需要重新训练 CRM head
- LIBERO 复现率问题尚未解决（社区 issue 仍 open），可能需要调试

**预估时间：4-6 小时**
- wrapper 编写+调试: 2-3h
- evaluate.py 集成: 1h
- CRM 适配（如需）: 1-2h

Sources:
- [lerobot/pi0_libero_base](https://huggingface.co/lerobot/pi0_libero_base)
- [lerobot/pi05_libero_base](https://huggingface.co/lerobot/pi05_libero_base)
- [lerobot/pi0_libero_finetuned](https://huggingface.co/lerobot/pi0_libero_finetuned)
- [lerobot/pi05_libero_finetuned](https://huggingface.co/lerobot/pi05_libero_finetuned)
- [Physical-Intelligence/openpi](https://github.com/Physical-Intelligence/openpi)
- [openpi libero_policy.py](https://github.com/Physical-Intelligence/openpi/blob/main/src/openpi/policies/libero_policy.py)
- [Issue #2114: Fine-tuned models fail to replicate success rates](https://github.com/huggingface/lerobot/issues/2114)
- [Issue #2533: pi05_libero_base zero success rate](https://github.com/huggingface/lerobot/issues/2533)
- [HuggingFace blog: π0 and π0-FAST](https://huggingface.co/blog/pi0)
- [LeRobot LIBERO docs](https://huggingface.co/docs/lerobot/libero)
- [Flow Matching Explained](https://federicosarrocco.com/blog/flow-matching)

---
