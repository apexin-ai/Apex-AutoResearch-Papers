# code m4 compound kernel prototype

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_m4-compound-kernel-prototype_20260513T192452_result.json`
- **Structured JSON:** [`0eb72147689b0067a01a.json`](../../sessions/0e/0eb72147689b0067a01a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

5 个文件全部语法正确。总结写好的内容：

| 文件 | 核心内容 |
|------|---------|
| `__init__.py` | 导出 HeadSelector, HeadMask, KVEvictor, KVMask, CompoundSparseForward, compute_compound_ppl |
| `head_selector.py` | `HeadSelector.compute_importance()` 用 forward hook 捕获 attention output、按 per-head L2 norm 评分；`select()` topk 选 Q heads，自动推导哪些 KV heads 可跳过（GQA 7:1 映射） |
| `kv_evictor.py` | `KVEvictor.compute_kv_importance()` 对 attention weights 沿 batch/head/query 维度求和；`select()` topk 选 KV positions，BOS 永不 evict |
| `compound_forward.py` | `CompoundSparseForward.forward()` 一次 pass 同时应用两种稀疏：KV eviction 折入 attention_mask，head masking 用 output hook 按 Q head 粒度 zero out；`compute_compound_ppl()` 便捷接口 |
| `test_compound.py` | 7 个 smoke test — GQA 分组、head selection、KV eviction、BOS 保护、KV group skip、compound forward shape、masking 有效性 |

与现有 `interaction_index.py` 的关键区别：
- importance-based 选择（非 random）
- GQA 感知（跟踪可跳过的 KV groups）
- 模块化 dataclass 接口（HeadMask / KVMask）
- compound 作为独立模块，可与 II calculator 组合使用

---
