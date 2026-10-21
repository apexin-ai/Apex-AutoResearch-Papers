# infra status and push v2

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_status_and_push_v2_20260521T194953_result.json`
- **Structured JSON:** [`d37ac082294e8f5c4325.json`](../../sessions/d3/d37ac082294e8f5c4325.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

COMET 已开始 back-translation，长时间运行中（qwen: 798 条, llama: 1096 条）。

---

```
[状态]
GPU 0: 空闲 (0 MiB)
GPU 1: COMET qwen 验证中 (16GB, back-translating 798 × 4 fields)
GPU 2: COMET llama 验证中 (16GB, back-translating 1096 × 4 fields)
GPU 3: 空闲 (0 MiB) — ZH 翻译 v2 已完成

Qwen EN activations: ✅ [966, 36, 4096]
Qwen ZH activations: ✅ [1116, 36, 4096]
Qwen ZH translate v2: ✅ train 798 / test 168
COMET model: ✅ 已就绪 (wmt22-comet-da)

[已启动]
- comet_qwen_v5 (GPU 1): back-translation + COMET scoring for qwen3
- comet_llama_v5 (GPU 2): back-translation + COMET scoring for llama31
  预计 30-60 分钟

[探针结果 — Qwen3-8B, 全 4 方向]
EN→EN: 75.00% (layer 24), binomial p<1e-6, permutation p=0.000
ZH→ZH: 63.03% (layer 21), binomial p=3.5e-5, permutation p=0.000
EN→ZH: 63.45% (layer 22), binomial p=2.0e-5, permutation p=0.000
ZH→EN: 62.50% (layer 19), binomial p=7.4e-4, permutation p=0.010

Gate: PASS — 全部 4 方向均显著高于 chance (50%)，
跨语言迁移成立 (EN→ZH/ZH→EN 均 p<0.05)
```

关键发现：
- 同语言探针 (EN→EN 75%, ZH→ZH 63%) 均强于跨语言 (EN→ZH 63.5%, ZH→EN 62.5%)
- EN 侧信号更强（75% vs 63%），可能反映 Qwen3 英文训练数据优势
- 最佳层集中在 19-24 层（中上层），符合知识编码在中间层的假设
- 跨语言迁移虽显著但弱于同语言，暗示 partial language-specific encoding

---
