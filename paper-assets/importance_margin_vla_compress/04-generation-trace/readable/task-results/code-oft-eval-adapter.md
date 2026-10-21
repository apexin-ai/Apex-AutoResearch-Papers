# code oft eval adapter

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_oft-eval-adapter_20260521T012139_result.json`
- **Structured JSON:** [`fd813ba72f18abfb281d.json`](../../sessions/fd/fd813ba72f18abfb281d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有任务完成。总结：

---

### 1. OFT Vision Connector 架构

**确认 3-layer MLP**（fused DinoSigLIP backbone）：

| Layer | In → Out | Activation |
|-------|----------|------------|
| fc1 | vision_dim (1792) → 4×vision_dim (7168) | GELU |
| fc2 | 7168 → llm_dim (4096) | GELU |
| fc3 | 4096 → 4096 | — |

代码位置：`modeling_prismatic.py` 的 `PrismaticProjector` 类，`use_fused_vision_backbone=True` 分支。

### 2. eval_oft_libero.py

已部署到 `westd-38929:/root/autodl-tmp/importance_margin_vla_compress/eval_oft_libero.py`（617 行），dry-run `--help` 通过。

关键设计：
- **自己实现 OFT 推理流程**：checkpoint 的 `predict_action` 是 base OpenVLA（discrete tokens），OFT 的 L1 regression 需要直接调用 `vision_backbone → projector → language_model → action_head`
- **Pruning 注入点**：monkey-patch `model.projector.forward`，在投影后按 L2 norm / random 剪裁 vision tokens
- **双图处理**：分别通过 backbone 处理 agentview 和 wrist 的 pixel_values，拼接 patches 后统一投影
- **L1RegressionActionHead / ProprioProjector**：内联定义，state_dict key 与 OFT repo 完全对齐

### 3. 依赖

无需额外安装。已有 transformers、torch、timm、libero。

### 4. Checkpoint 下载状态

| Suite | 状态 | 路径 |
|-------|------|------|
| object | ✅ 已有 (23GB) | `/root/autodl-tmp/openvla-oft-libero-object/` |
| spatial | 下载中 (PID 306031) | `/root/autodl-tmp/openvla-oft-libero-spatial/` |
| goal | 下载中 (PID 305443) | `/root/autodl-tmp/openvla-oft-libero-goal/` |
| 10 | 未启动 | 磁盘仅剩 65GB，spatial+goal 占 ~46GB，10 需等释放空间 |

### 5. 注意事项

- **所有 GPU 被占用**，未执行任何 GPU 操作
- checkpoint 的 `modeling_prismatic.py` 有被修改过的痕迹（`.bak` 文件），但 `predict_action` 仍是 base 版本
- `openvla-oft-git` 目录只有 3.4MB（仅 config），不是完整 checkpoint

---
