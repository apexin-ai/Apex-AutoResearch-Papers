# code qwen adapt pipeline

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_qwen_adapt_pipeline_20260512T183338_result.json`
- **Structured JSON:** [`b7dd3f4f6489fb0271f5.json`](../../sessions/b7/b7dd3f4f6489fb0271f5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个文件都通过语法检查。下面是汇报。

---

## 1. Qwen-2.5 0.5B 节点命名映射

| Canonical | HuggingFace module path | 备注 |
|-----------|------------------------|------|
| `input` | `model.embed_tokens` | |
| `a{L}.h{H}` | `model.layers.{L}.self_attn.o_proj` | 需 per-head 分解 (slice `[H*64:(H+1)*64]`) |
| `a{L}.h{H}.q` | `model.layers.{L}.self_attn.q_proj` | head H slice, 14 heads × 64 dim |
| `a{L}.h{H}.k` | `model.layers.{L}.self_attn.k_proj` | GQA: 2 KV heads, `H//7` 映射到 KV group |
| `a{L}.h{H}.v` | `model.layers.{L}.self_attn.v_proj` | 同上 |
| `m{L}` | `model.layers.{L}.mlp` | gate_proj + up_proj + down_proj (SwiGLU) |
| `logits` | `lm_head` | |
| `resid_pre.{L}` | `model.layers.{L}` (forward_pre_hook) | 残差流入口 |

**架构参数**: 24L × 14H (2 KV heads, GQA 7:1), d=896, head_dim=64, intermediate=4864, vocab=151936

**EAP-IG hook 注册点**: forward + backward hooks on `model.embed_tokens`, `model.layers.{i}` (pre-hook), `model.layers.{i}.self_attn.o_proj`, `model.layers.{i}.mlp`

**Edge Pruning 适配**: 需要 HF-native masked forward pass。与 GPT-2 的主要区别是 GQA — K/V 的 edge mask 需在同一 KV group 内的 7 个 query head 间共享。

## 2. Pipeline 配置方案

`run_circus.py` 支持 dict / JSON / YAML 配置：

```python
config = {
    "model": "Qwen/Qwen2.5-0.5B",       # 或 "gpt2-small"
    "task": "ioi",
    "methods": ["eap_ig", "edge_pruning", "ifr"],
    "K": 3,
    "num_samples": 50,
    "binarize": {
        "eap_ig":       {"strategy": "topn", "n": 200},
        "edge_pruning": {"strategy": "threshold", "value": 0.5},
        "ifr":          {"strategy": "topn", "n": 200},
    },
    "css_threshold": 0.67,
    "device": "cuda",
    "cache_dir": "./cache",     # 缓存绑定 CANONICAL_VERSION="v2"
    "output_dir": "./results",
}
```

Pipeline 流程: 加载模型(ModelAdapter) → 加载 dataset → 逐方法计算 edge scores (带缓存) → 二值化 → CSS → CIRCUS → cross-tabulation → JSON 输出。

ModelAdapter 自动路由：GPT-2 → TransformerLens, 其他 → HuggingFace。IFR 的 HF 实现已完成（`ifr_scoring.py`），EAP-IG 和 Edge Pruning 的 HF 后端留有接口 stub + hook 注册点文档。

## 3. K=3 checkpoint 预估耗时 (Qwen-2.5 0.5B / IOI)

| 方法 | 预估耗时 | 依据 |
|------|---------|------|
| EAP-IG | 15-30s | 5步 IG, 每步 1 forward+backward (~0.5B params) |
| Edge Pruning | 2-5 min | 100 epochs L0 优化, 每 epoch 1 masked forward |
| IFR | 3-8s | 单次 forward + proximity 计算 |
| CSS + CIRCUS | <1s | 纯 set 运算 |
| **总计** | **~2.5-6 min** | |

对比：ACDC on GPT-2 Small ~2.5h (32,491 edges)。Qwen-2.5 有 ~179,388 edges (5.5×)，ACDC 不可行，IFR 替代后总耗时降到分钟级。

## 4. 代码文件路径

| 文件 | 路径 |
|------|------|
| Model Adapter | `artifacts/model_adapter.py` |
| Pipeline 入口 | `artifacts/run_circus.py` |
| IFR (HF native) | `artifacts/ifr_scoring.py` (已有) |
| MVP 方法 (TL) | `artifacts/structfuse-mvp/{circuit_discovery,edge_pruning_l0,ifr_discovery}.py` (已有) |

---
