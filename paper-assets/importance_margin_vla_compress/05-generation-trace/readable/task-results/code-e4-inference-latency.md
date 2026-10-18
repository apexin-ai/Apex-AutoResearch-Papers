# code e4 inference latency

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_e4_inference_latency_20260523T054910_result.json`
- **Structured JSON:** [`cfe23fff41369dbefae2.json`](../../sessions/cf/cfe23fff41369dbefae2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本语法正确，已写入远程服务器。

---

## 设计思路

**目标**：测量 4 个 VLA 模型在不同 vision token 保留比例下的推理延迟和峰值 GPU 显存。

### 架构

每个模型有独立的 `benchmark_*()` 函数，负责加载模型、构建 dummy batch、安装/移除剪枝、测量延迟。模型按序执行（每个测完后释放 GPU），避免 OOM。

### 剪枝方法

统一使用 **L2-norm pruning**（training-free），保留 L2 范数最大的 top-k tokens：

| 模型 | 剪枝注入点 | 机制 |
|------|-----------|------|
| SmolVLA | `connector` forward hook | hook 每次调用剪枝一个摄像头的 64 tokens |
| Pi0.5 | monkey-patch `embed_prefix` | 每个图像 slot 的 256 tokens 独立剪枝 |
| X-VLA | monkey-patch `vlm._encode_image` | Florence2 输出特征按 L2 norm 剪枝 |
| OpenVLA | `projector` forward hook | SigLIP+DINOv2 投影后剪枝 |

### Vision Token 数量

| 模型 | 每图 | 图像数 | 总计 |
|------|------|--------|------|
| SmolVLA | 64 | 2 | 128 |
| Pi0.5 | 256 | 3 slots | 768 |
| X-VLA | 运行时检测 | 2 | N×2 |
| OpenVLA | 运行时检测 | 1 | N |

### 时间测量

- `torch.cuda.synchronize()` 确保 GPU 操作完成
- `time.perf_counter()` 高精度计时
- 10 次 warmup + 100 次正式测量
- 输出 mean/std/median/p95 延迟 + 峰值显存

### 使用方式

```bash
# SmolVLA + Pi0.5 + X-VLA（共享 LeRobot 环境）
python measure_inference_latency.py --models smolvla pi05 xvla --gpu 0

# OpenVLA 需单独运行（transformers 版本冲突）
python measure_inference_latency.py --models openvla --gpu 0
```

输出 CSV 采用追加模式，分开运行的结果会合并到同一个 `eval_results/inference_latency_all_models.csv`。

---
