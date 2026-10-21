# π0.5 Server-Client 架构可行性报告

## 1. π0.5 推理接口分析

### 模型结构
- PaliGemma 2B (VLM) + Gemma 300M (action expert) = **3.6B 参数**
- Flow matching 推理：每次生成需 **10 步 denoise**
- **Chunk-based**：一次推理生成 50 步 action chunk，open-loop 回放（即每 50 个 env step 才调用一次模型）

### 内部状态
- `_action_queue`：per-instance deque，缓存 50 步 action chunk → **需要 per-client 隔离**
- KV cache：每次 `encode_prefix` 重新计算，无跨时间步状态 → **无状态，server 友好**
- `denoise_step` 内部 deep-copy KV cache → 每次推理独立

### K-sample 生成
- 当前实现：K 个 sample **串行循环**生成（K=10 → 100 次 denoise_step 调用）
- 底层 PI05Pytorch 支持 batch_size 维度 → **可改为 batch 并行**（100 次 → 10 次 batched 调用）

## 2. 显存分析

| 项目 | 数值 |
|------|------|
| GPU 型号 | RTX 4090 (24 GB) × 6 |
| 模型权重 (bf16) | ~7 GB |
| 运行时显存 (含 KV cache + activations) | **~13 GB / instance** |
| 剩余显存 | ~11 GB |
| MuJoCo EGL 渲染 | <100 MB（可忽略） |

当前：3 张 4090 各加载一个 PI05 实例，各跑 1 个 eval（3 个 benchmark/seed 并行）。

## 3. 方案对比

| 方案 | 可行性 | 复杂度 | 说明 |
|------|--------|--------|------|
| **A: vLLM / TGI** | ❌ 不可行 | — | PI05 是自定义 flow-matching policy，非标准 LLM，vLLM 不支持 |
| **B: CUDA MPS** | ⚠️ 有限 | 低 | 多进程共享 GPU，但无法做 request batching，且 MPS 在 4090 上稳定性一般 |
| **C: torch.mp 共享模型** | ⚠️ 复杂 | 高 | CUDA tensor 跨进程共享脆弱，调试困难 |
| **D: FastAPI Server** | ✅ 推荐 | **4-6h** | 最直接，per-client 状态管理简单 |

## 4. 推荐方案：FastAPI Server

### Server 端
```
Pi05Server (单 GPU)
├── Pi05Wrapper (单实例，~13GB VRAM)
├── per-client action queues: dict[client_id, deque]
└── FastAPI endpoints:
    POST /predict     → (image, task, state, K, client_id) → action
    POST /reset       → (client_id) → 清空 action queue
    POST /features    → (image, task, state, K) → obs_features + samples
```

### Client 端
```python
# evaluate.py 改动极小：替换 wrapper.predict_action() 为 HTTP 调用
def predict_action_remote(obs, task_name, robot_state, client_id):
    resp = requests.post(f"http://localhost:8000/predict", json={
        "agentview_rgb": encode_image(obs["agentview_image"]),
        "task_name": task_name,
        "robot_state": robot_state.tolist(),
        "client_id": client_id,
    })
    return np.array(resp.json()["action"])
```

### LIBERO 环境
- MuJoCo OffScreenRenderEnv 依赖 **EGL GPU 渲染**（`MUJOCO_EGL_DEVICE_ID`）
- 渲染显存极小（<100MB），多个 env 可共享同一张 GPU
- Client 进程设 `MUJOCO_EGL_DEVICE_ID=1`（或其他空闲 GPU），与 model server GPU 分开

## 5. 预期收益

### GPU 节省

| 配置 | GPU 数 | 说明 |
|------|--------|------|
| 当前 | **6 GPU** | bjb1 × 3 + bjb2 × 3，各加载独立 PI05 |
| Server 模式 | **2 GPU** | 1 × model server + 1 × EGL 渲染（多 env 共享） |
| 激进模式 | **1 GPU** | model + 渲染共享同一 GPU（13GB model + <1GB 渲染 = 14GB < 24GB） |

### 吞吐量分析

**关键洞察：chunk_size=50 大幅降低了 server 的价值。**

- 300 步 rollout 中只有 **~6 次模型推理**，其余时间模型空闲
- 单次 eval (K=1, 10 tasks × 20 rollouts) 总耗时 ~105 分钟
- 估算：每次推理 ~200-400ms（K=1），env step ~15ms/step
- GPU 利用率：推理时间占比 < 10%，90%+ 时间花在 env stepping

因此，单 GPU server 完全能承载 3-6 个并发 eval client，因为请求天然稀疏。

### K-sample 批量优化（bonus）

独立于 server 架构的额外优化：将 K 个 sample 的串行循环改为 batch 并行。

- 现状：K=10 → 100 次 `denoise_step`（串行）
- 优化：stack K 个 noise 到 batch 维度 → 10 次 batched `denoise_step`
- 预期加速：推理部分 **3-5×**（受限于 KV cache tiling 开销）
- 显存代价：KV cache × K，约 13GB → 15-18GB（K=10 在 24GB 4090 上可能偏紧）

## 6. 风险与 Showstopper

| 风险 | 严重度 | 缓解措施 |
|------|--------|----------|
| EGL 渲染必须用 GPU | 中 | 多 env 共享一张 GPU 渲染，显存开销极小 |
| 图片序列化开销 | 低 | 256×256 RGB 图片 ~192KB，localhost 传输 <1ms |
| 多 client batching 显存溢出 | 中 | 限制并发 batch size；或不做 batching，串行处理（反正请求稀疏） |
| action queue 状态管理 | 低 | per-client dict，reset 时清空即可 |
| **chunk replay 语义**（关键） | **高** | PI05 的 50 步 open-loop chunk 意味着 client 必须在本地缓存 action queue，否则每步都调 server 会破坏 chunk replay 语义。两种策略：(1) server 维护 queue，client 每步调用；(2) server 返回整个 chunk，client 本地 replay。推荐 (2)，减少网络调用。 |

### Showstopper 检查
**无 showstopper。** 方案技术上完全可行。主要权衡是 chunk_size=50 已经让 GPU 利用率很低，server 化的收益主要是省 GPU 数量（从 6 → 1-2），而非提升吞吐。

## 7. 实施建议

1. **Phase 1（2-3h）**：写 `pi05_server.py`，FastAPI 包装 Pi05Wrapper，暴露 `/predict_chunk` 和 `/reset` 端点
2. **Phase 2（1-2h）**：改 `evaluate.py`，增加 `--remote_server` 参数，支持 HTTP client 模式
3. **Phase 3（1h）**：测试 + 部署脚本（server 启动、多 client 并行启动）
4. **Phase 4（bonus, 2-3h）**：K-sample batch 优化（独立 PR，不依赖 server）

总工期：**4-6 小时**（Phase 1-3），可选 +2-3 小时（Phase 4）。
