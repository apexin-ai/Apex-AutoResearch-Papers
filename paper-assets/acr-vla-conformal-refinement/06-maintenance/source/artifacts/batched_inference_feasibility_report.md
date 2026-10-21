# SmolVLA Batched Inference 可行性报告

**日期**: 2026-05-19  
**服务器**: bjb2-40593 (RTX 4090 D, 24GB)

---

## 1. 是否支持 batch > 1？

**YES**

**证据**:
- `SmolVLAWrapper.generate_k_samples()` 中，所有张量操作已经使用 batch 维度 `B`（dim=0）
- `VLAFlowMatching.denoise_step()` 接受 `(B, chunk_size, max_act_dim)` 的 `x_t`，`(B,)` 的 timestep，`(B, seq_len)` 的 `prefix_pad_masks`，完全是 batch-parallel 的
- `SmolVLMWithExpertModel.forward()` 的 attention 计算（包括 self_attn 和 cross_attn 路径）均以 `batch_size` 为第一维运算
- KV cache 结构为 `dict[layer_idx] -> {"key_states": (B, L, H, D), "value_states": (B, L, H, D)}`，batch 维度天然支持

**当前 K sample 循环位置**:
```
smolvla_wrapper.py: SmolVLAWrapper.generate_k_samples()
```
```python
all_samples = []
for _ in range(K):            # ← 这里是 sequential loop
    noise = self.flow.sample_noise((B, chunk_size, max_act_dim), self.device)
    x_t = noise
    for step in range(num_steps):  # 10 denoising steps
        v_t = self.flow.denoise_step(x_t, prefix_pad_masks, past_key_values, time_tensor)
        x_t = x_t + dt * v_t
    all_samples.append(unnorm_action)
return torch.stack(all_samples, dim=1)  # (B, K, chunk_size, 7)
```

K=5 时执行 5 * 10 = 50 次 `denoise_step`。Batched 后变为 10 次。

---

## 2. Flow-matching batch 化可行性

**YES，技术上完全可行**

### 核心分析

SmolVLA 使用 flow-matching（确定性 ODE 积分），不是 DDPM（随机采样）。K 个 sample 的差异仅在于初始噪声 `noise ~ N(0, I)`，ODE 步骤完全相同。

**Denoising 中 KV cache 行为**（关键验证）:

| Layer 类型 | 条件 | `fill_kv_cache=False` 时行为 | Batch 安全? |
|---|---|---|---|
| self_attn (偶数层) | `layer_idx % 2 == 0` | `torch.cat([cached_prefix_kv, suffix_kv])` 创建新张量，不修改原 cache | YES |
| cross_attn (奇数层) | `layer_idx % 2 != 0` | 直接读 `cached_prefix_kv`，expert 的 k/v_proj 投影后 attend | YES |

**关键结论**: KV cache 在 denoising 过程中是只读的（self_attn 层的 `torch.cat` 创建新张量）。同一份 expanded cache 可安全重用 10 个 step。

### Batch 化方案

```python
def generate_k_samples_batched(self, past_key_values, prefix_pad_masks, K=5):
    B = prefix_pad_masks.shape[0]
    
    # 1. 展开 KV cache: B → B*K
    expanded_kv = {}
    for layer_idx, kv in past_key_values.items():
        expanded_kv[layer_idx] = {
            "key_states": kv["key_states"].repeat_interleave(K, dim=0),
            "value_states": kv["value_states"].repeat_interleave(K, dim=0),
        }
    expanded_masks = prefix_pad_masks.repeat_interleave(K, dim=0)
    
    # 2. 一次生成 B*K 个噪声
    noise = self.flow.sample_noise((B * K, chunk_size, max_act_dim), self.device)
    x_t = noise
    
    # 3. 单次 denoising loop（10 steps，不是 K*10）
    for step in range(num_steps):
        time_tensor = torch.full((B * K,), time_val, ...)
        v_t = self.flow.denoise_step(x_t, expanded_masks, expanded_kv, time_tensor)
        x_t = x_t + dt * v_t
    
    # 4. Reshape
    raw_action = x_t[:, :, :FULL_ACTION_DIM]
    unnorm = self._unnormalize_action(raw_action)
    return unnorm.reshape(B, K, chunk_size, FULL_ACTION_DIM)
```

---

## 3. VRAM 预估

### 模型基础信息

| 项目 | 值 |
|---|---|
| 模型文件 | 907 MB (bf16 safetensors) |
| VLM backbone | SmolVLM2-500M (SmolLM2, hidden=960, 16 layers) |
| Action expert | 0.75x width (hidden=720, 16 layers) |
| Denoising steps | 10 |
| chunk_size | 50 |
| max_action_dim | 32 |

### KV cache 大小估算

VLM: hidden=960, num_kv_heads=5, head_dim=64  
KV cache per layer per sample: `2 * L * 5 * 64 * 2 bytes`（L=prefix length）

保守估计 prefix length L ≈ 800 tokens（1 image ~729 patches + ~48 language + 1 state + padding）:

| 配置 | KV cache 总量 | 额外 activation | 总额外 VRAM |
|---|---|---|---|
| K=1 (当前) | ~16 MB | ~150 MB | baseline |
| K=5 batch | ~80 MB | ~300 MB | **+~215 MB** |
| K=10 batch | ~160 MB | ~500 MB | **+~500 MB** |

### 结论

**RTX 4090 24GB 完全够用。**

当前 nvidia-smi 显示 13.5 GB used（含 LIBERO 环境 + SmolVLA 模型）。即使 K=10 batch，额外 VRAM < 600 MB，总计 ~14 GB，远低于 24 GB 上限。

额外 VRAM 主要来自:
1. KV cache 的 K 倍复制（~64 MB for K=5）
2. Expert denoising 中间激活（suffix attention 的 Q/K/V 矩阵，K 倍）
3. `x_t` 张量从 `(1,50,32)` → `(5,50,32)`（negligible）

---

## 4. 代码改动量

### 需要改的文件

| 文件 | 改动 | 行数 |
|---|---|---|
| `src/smolvla_wrapper.py` | 新增 `generate_k_samples_batched` 方法，或修改现有 `generate_k_samples` | ~25 行 |
| `src/smolvla_wrapper.py` | `get_obs_features_and_samples` 中调用切换 | ~2 行 |
| 总计 | | **~27 行** |

### 不需要改的文件

- `lerobot/policies/smolvla/modeling_smolvla.py` — `denoise_step` 已支持任意 batch size
- `lerobot/policies/smolvla/smolvlm_with_expert.py` — 所有 forward 路径已 batch-parallel
- `src/evaluate.py` — 接口不变（`generate_k_samples` 的输入输出 shape 不变）
- `src/cgs.py` — 在 `generate_k_samples` 之后运行，输入 shape `(K, chunk_size, D)` 不变

### 现成支持？

lerobot 本身没有 "batched multi-sample generation" 的现成 API。但底层代码完全兼容 batch，只需在 wrapper 层做 `repeat_interleave` + reshape。Diffusion Policy (lerobot 中另一个 policy) 也是相同模式，未提供原生 K-sample batch 支持。

---

## 5. 总结

**推荐实现，理由如下：**

| 维度 | 评估 |
|---|---|
| 可行性 | 完全可行，底层代码已天然支持 batch |
| VRAM | K=5 额外 ~215 MB，K=10 额外 ~500 MB，RTX 4090 无压力 |
| 改动量 | ~27 行，仅改 `smolvla_wrapper.py` 一个文件 |
| 预期加速 | K=5 时 denoising 步骤从 50 次 → 10 次 forward pass，预期 **3-4x 加速**（非 5x，因 KV cache expand 和 memory bandwidth overhead） |
| 风险 | 低。不改 lerobot 源码，不改模型权重，不影响数值结果（同噪声 → 同输出） |

**预期 latency 收益**: 当前 K=5 sequential denoising 是推理的主要耗时部分。VLM prefix encoding（最重的单次 forward）已经只做一次。Batch 化后，denoising 部分耗时压缩为 ~1/3-1/4，总推理 latency 下降显著（具体比例取决于 prefix encoding vs denoising 的时间占比）。
