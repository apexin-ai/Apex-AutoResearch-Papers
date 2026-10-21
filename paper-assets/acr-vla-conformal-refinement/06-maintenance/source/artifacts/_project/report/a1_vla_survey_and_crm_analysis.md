# A1 VLA 调研与 CRM 集成分析报告

## 1. 模型概况

| 属性 | 值 |
|------|-----|
| 论文 | A1: A Fully Transparent Open-Source, Adaptive and Efficient Truncated VLA (arXiv:2604.05672) |
| GitHub | https://github.com/ATeam-Research/A1 |
| LLM backbone | Qwen2-7B (d_model=3584, n_layers=28, n_heads=28) |
| Vision backbone | ViT-L-14-336 (OpenAI CLIP, image_emb_dim=1024) |
| Action head | FlowMatchingActionHead (Qwen2-based, dim=1024, 28 layers, 8 heads) |
| 总参数量 | ~7.5B (LLM) + ~0.3B (ViT) + ~1B (FM head) ≈ 8.8B |
| Checkpoint 格式 | 单个 model.pt (~20GB, fp32/mixed) |
| HuggingFace | spatialtemporal-ai/a1-libero |

## 2. Action 机制

| 属性 | 值 |
|------|-----|
| Action dim | 32 (multi-robot padding, eval 时截取 :7) |
| 实际 LIBERO action | 7 (3D pos + 3D rot axis-angle + 1D gripper) |
| Action chunk | 10 steps |
| Open-loop steps | 8 |
| Flow-matching inference steps | 10 (Euler integration) |
| **Stochastic** | **Yes** — Beta(1.5,1) timestep sampling + flow-matching noise |
| Normalization | BOUNDS_Q99 |

## 3. 官方 LIBERO Benchmark（论文 Table 1）

| Suite | A1 SR% | π0.5 | π0 | SmolVLA | OpenVLA |
|-------|--------|------|-----|---------|---------|
| Spatial | 97.4% | — | — | — | — |
| Object | **99.8%** | — | — | — | — |
| Goal | 97.6% | — | — | — | — |
| Long | 91.4% | — | — | — | — |
| **Avg** | **96.6%** | 96.9% | 94.2% | 88.8% | 76.5% |

- LIBERO-Plus (zero-shot transfer): 75.3%
- 早停 + 热启动: 96.4% avg, 10.5s latency (72.3% latency reduction)

## 4. CRM 集成可行性分析

### 4.1 Feature 提取方案

**提取位置**: `AffordVLA.extract_action_hidden_states()`
- 输入: LLM last_hidden_state (B, seq_len, 3584)
- 定位 `<ACT_START>` / `<ACT_END>` 特殊 token
- 输出: action hidden states (B, num_action_tokens, **3584**)
  - num_action_tokens = num_actions_chunk × action_dim = 10 × 32 = 320

**CRM feature**: mean pool over action tokens → (B, **3584**)

### 4.2 与现有模型的对比

| 模型 | Feature dim | Action dim | Chunk | Stochastic |
|------|-----------|------------|-------|------------|
| SmolVLA | 960 | 7 | 8 | Yes (flow) |
| OpenVLA | 4096 | 7 | 1 | No |
| π0.5 | 2048 | 7 | 10 | Yes (flow) |
| **A1** | **3584** | **7 (from 32)** | **10** | **Yes (flow)** |

### 4.3 集成工作量

| 任务 | 工作量 | 说明 |
|------|--------|------|
| Feature 提取 hook | 低 | 类似 SmolVLA，hook predict_actions 获取 last_hidden_state |
| CRM 适配 | 低 | 仅需修改 feature_dim=3584 |
| Calibration 数据收集 | 中 | 需要跑 ~200 calibration episodes |
| Action dim 处理 | 低 | 截取前 7 维，与现有 LIBERO 流程一致 |
| **总预估** | **1-2 天** | 大部分代码可复用 SmolVLA CRM 集成 |

### 4.4 风险与注意事项

1. **Object suite (99.8%) 改进空间极小** — CRM 主要应关注 Long (91.4%) 和 Goal (97.6%)
2. **GPU 显存**：模型 ~20GB，RTX 4090 24GB 可能需要 bf16 推理
3. **推理延迟**：flow-matching 10 steps + Qwen2 expert (28 layers) = 较慢，需测量
4. **action_dim=32**：虽然 eval 时截取前 7 维，CRM 的 conformal set 计算需要确认是在 32-dim 还是 7-dim 空间

## 5. 服务器环境

| 项目 | 值 |
|------|-----|
| 服务器 | bjb2-40593 |
| GPU | NVIDIA RTX 4090 D (24GB) |
| Conda env | /root/autodl-tmp/envs/a1 (Python 3.10) |
| PyTorch | 2.6.0+cu124 |
| 代码 | /root/autodl-tmp/A1 |
| Checkpoint | /root/autodl-tmp/models/a1_libero (下载中) |
| 所有 eval 依赖 | 已安装验证通过 |

## 6. 待完成

- [ ] Checkpoint 下载完成后跑 Object + Spatial baseline eval (seed=42, 20 trials/task)
- [ ] 验证 baseline 结果与论文数据的一致性
- [ ] 测量推理延迟
