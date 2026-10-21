# ops deploy e3 e4 cqa1

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_deploy_e3_e4_cqa1_20260523T070853_result.json`
- **Structured JSON:** [`3357fb12cc98132fd84e.json`](../../sessions/33/3357fb12cc98132fd84e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 0&1 已进入 LIBERO 仿真，GPU 2&3 模型加载中。

## 部署状态总结

### cqa1-33015 (4×4090D)

| GPU | 实验 | PID | 状态 | 显存 | 预计时间 |
|-----|------|-----|------|------|----------|
| 0 | Pi0.5 l2norm k=0.50 libero_object | 304615 | 运行中（episode 进行中） | 10.2 GB | ~2-4h |
| 1 | Pi0.5 random k=0.50 libero_object | 304879 | 运行中（episode 进行中） | 10.2 GB | ~2-4h |
| 2 | Pi0.5 l2norm k=0.70 libero_object | 305122 | 加载中 | 加载中 | ~2-4h |
| 3 | Pi0.5 random k=0.70 libero_object | 305386 | 加载中 | 加载中 | ~2-4h |

### 已完成

**E3 (Token Cosine Similarity) — Pi0.5 完成：**
- π0.5: CV=0.055, **Mean CosSim=0.9545**, std=0.0174, 512 tokens × 2048D
- 验证假设：低 CV → 高 token 同质性（cosine sim ≈ 0.95）
- 产出：`artifacts/token_cosine_similarity_stats.json` + heatmap PDF/PNG

**E4 (Inference Latency) — 之前已完成：**
- Baseline 128tok: 164.33ms, M=32: 154.78ms (1.06x), M=64: 156.16ms (1.05x)
- 产出：`eval_results/inference_latency_comparison.json`

### 无法运行

- **E3 SmolVLA**: 服务器无法访问 HuggingFace，SmolVLM2-500M 未缓存
- **E3 OpenVLA**: `openvla-repo` 依赖不在此服务器
- **E3 X-VLA/OFT/Pi0**: 模型不在此服务器

### Table 2 gap 填充

4 个 Pi0.5 pruning eval 填充 libero_object 上的缺口（之前只有 k=0.90 一个数据点）。完成后新增 k=0.50 和 k=0.70 的 l2norm+random 对比。

---
