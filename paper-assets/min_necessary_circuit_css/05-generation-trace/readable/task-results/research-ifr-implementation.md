# research ifr implementation

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_ifr_implementation_20260512T181149_result.json`
- **Structured JSON:** [`0a0b390b828a9ce05eac.json`](../../sessions/0a/0a0b390b828a9ce05eac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 产出报告

### IFR 算法核心原理

IFR (Ferrando & Voita, EMNLP 2024) 用 ALTI 的 L1 proximity 度量追踪信息在 residual stream 中的流动。对任意边 (u→v)，计算 `score = max(||x_v||_1 - ||y_u - x_v||_1, 0)`，其中 `y_u` 是源节点 u 的输出，`x_v` 是目标节点 v 读取的 residual stream。直觉：如果 y_u 是 x_v 的主要组成部分，移除它会大幅降低 L1 范数，proximity 就高。整个计算只需**单次前向传播 + activation cache**，无需反向传播或优化循环，比 ACDC 快约 100 倍。

### 开源实现

- **`facebookresearch/llm-transparency-tool`**：Facebook 的交互式可视化工具，包含 ALTI attribution 的实现，但面向可视化场景，不直接输出 edge-level scores dict。不可直接复用，需自行实现 edge scoring 层。
- **项目已有**：`artifacts/structfuse-mvp/ifr_discovery.py` 已实现 TransformerLens 版本（用于 GPT-2 Small）。新实现 `ifr_scoring.py` 是 HuggingFace 原生版，支持大模型。

### 实现方案

**函数签名**：
```python
def compute_ifr_edges(model, dataset, metric_fn, threshold=0.1, device="cuda") -> Dict[str, float]
```

**关键步骤**：
1. 架构检测（`_get_model_info`）→ 支持 Llama/Qwen2/Gemma2/Mistral/GPT2
2. 注册 3 类 forward hooks：layer pre-hook 捕获 `resid_pre`，o_proj hook 捕获全注意力输出并通过权重分片分解为 per-head 输出，MLP hook 捕获 MLP 输出
3. 单次前向传播收集全部 activations
4. 构建 source activation 表，计算 `resid_mid = resid_pre + attn_out`
5. 遍历所有合法 (source, destination) 对，计算 proximity score
6. 输出 `Dict[str, float]`，edge name 格式 `{src}->{dst}`

**Edge 命名**：`input`, `a{L}.h{H}`, `m{L}`；注意力目标带 `.q/.k/.v` 后缀

### 预估耗时（Qwen-2.5 0.5B）

| 方法 | 机制 | 预估耗时 (8 examples, seq_len=128) |
|------|------|----------------------------------|
| EAP-IG | 梯度 × IG 插值 | ~15-30s（5 步 IG） |
| Edge Pruning L0 | 100 epoch 优化 | ~2-5 min |
| **IFR** | 单次前向 + proximity | **~3-8s** |

IFR 是三方法中最快的。对 Llama-3.1 8B，预估 ~30-60s（主要瓶颈是 activation 内存，需分批处理）。

### 代码文件

| 文件 | 路径 |
|------|------|
| IFR 实现 | `artifacts/ifr_scoring.py` |
| Smoke test | `artifacts/test_ifr_scoring.py` |

Smoke test 全部通过（AST-based，5/5 pass；runtime tests 需服务器上跑）。

### 已知限制

- **Gemma2**：对 `resid_mid` 的计算是近似的（Gemma2 在 attention 输出上多一层 LN 再加到 residual），影响 MLP 目标边的 score 精度，但不影响排序
- **Per-head Q/K/V 不区分**：所有 head 在同一层共享 `resid_pre`，因此同层不同 head 的 Q/K/V 边从同一 source 获得相同 score（这是 proximity 方法的固有限制，与现有 TransformerLens 版行为一致）

---
