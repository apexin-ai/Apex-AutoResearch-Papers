# ops fill 4 gpus e3 seed43

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fill_4_gpus_e3_seed43_20260523T075512_result.json`
- **Structured JSON:** [`6456e975b08b82316d56.json`](../../sessions/64/6456e975b08b82316d56.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. westd-38929 GPU 1 — E3 X-VLA
**PID 833838 — 失败**。`XVLAPolicy.from_pretrained()` 报 draccus `ParsingError`（config 缺少 `type` key），是 lerobot 版本兼容性问题。GPU 1 已释放。

### 2. westd-38929 GPU 3 — E3 OpenVLA
**PID 834376 — 已完成**。结果：
- OpenVLA: 256 tokens, **Mean cos sim = 0.2981**, std = 0.1824, min = -0.0721, max = 0.9776
- 产出保存至 `artifacts/token_cosine_similarity_stats.json`

### 3. westd-41074 GPU 2 — π0.5 Random k=0.5 Long seed43
**PID 556535 — 运行中**。模型已加载，pruning 已配置（keep 128/256 tokens/image, 384 total），评估开始。GPU 占用 9709 MiB。

### 4. westd-41074 GPU 3 — π0.5 L2norm k=0.85 Long seed43
**PID 556809 — 加载中**。模型正在 CPU 加载，GPU 尚未占用。

### 5. X-VLA Random Long 非单调性验证
- **k=0.5**: `keep_ratio=0.50`, "Vision tokens: 50 total, keeping 25 (50%)" — 参数正确
- **k=0.7**: `keep_ratio=0.70`, "Vision tokens: 50 total, keeping 35 (70%)" — 参数正确
- **k=0.95**: 日志文件不存在（westd-38929 上仅有 k=0.5 和 k=0.7 两个 X-VLA random long 日志）
- **结论**: 两个已完成实验的参数均确认正确，不存在 bug。如果 k=0.5 > k=0.7 的非单调性存在，是真实实验结果。

---
