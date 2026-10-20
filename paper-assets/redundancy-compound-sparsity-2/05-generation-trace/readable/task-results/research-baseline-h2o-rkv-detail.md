# research baseline h2o rkv detail

**redundancy compound sparsity 2** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_baseline_h2o_rkv_detail_20260512T153115_result.json`
- **Structured JSON:** [`014674f681b658750883.json`](../../sessions/01/014674f681b658750883.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个子任务全部完成。汇总：

### 子任务 1: Baseline 调研

**H2O**: 官方仓库 [lenscloth/KVCache](https://github.com/lenscloth/KVCache)。kvpress 中无 `H2OPress`，等价物是 `ObservedAttentionPress`。budget 直接对应绝对 token 数。Qwen2 无兼容性问题。

**R-KV**: 仓库 [Zefan-Cai/R-KV](https://github.com/Zefan-Cai/R-KV)，已 clone 到 `/root/carc/r_kv_baseline/`。通过 `replace_qwen2()` monkeypatch 支持 DeepSeek-R1-Distill-Qwen-14B。核心公式 `score = attn * 0.07 - redundancy * 0.93`，重 redundancy 惩罚。O(B²) 来自 `cal_similarity()` 的 pairwise cosine（`k_norm @ k_norm.T`）。

**SkipKV/FASA**: 均无公开代码。

### 子任务 2: kvpress 兼容性

- kvpress v0.5.3，37 个 Press 类
- `Qwen2ForCausalLM` 在 SUPPORTED_MODELS 中
- 自定义 Press 通过继承 `ScorerPress` 实现 `score()` 方法即可
- EMA eviction 可封装为 `CARCEMAPress(ScorerPress)`，但需适配 per-step → one-shot 语义差异

### 子任务 3: eval_framework.py

- 已部署到 `/root/carc/eval_framework.py`
- `--help` 和 `--dry-run` 均通过
- 支持 15 种 strategy（6 CARC + 9 kvpress）× 4 dataset × 任意 budget ratio
- 输出 JSON，含 PPL / accuracy / timing metadata

---
