# code validate mvp pipeline

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_validate-mvp-pipeline_20260513T184657_result.json`
- **Structured JSON:** [`a73f2b290183dbdbbdf0.json`](../../sessions/a7/a73f2b290183dbdbbdf0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有文件已读取完毕。下面是结构化审查报告。

---

# PACS MVP Pipeline 审查报告

## 1. MVP 协议对齐

| 检查项 | 状态 | 位置 |
|--------|------|------|
| II 公式 `R_both - R_attn - R_kv + 1` | [PASS] | `interaction_index.py:350`, `run_profiling.py:261` |
| Sparsity levels `[0.3, 0.5]` | [PASS] | `run_profiling.py:45` |
| Bootstrap 1000 resamples | [PASS] | `run_profiling.py:46`, `interaction_index.py:408` |
| Pass/fail OR logic (CI non-overlap OR sign reversal) | [PASS] | `run_profiling.py:168` |
| Stratified sampling 5×10=50, seed=42 | [PASS] | `data_utils.py:12-13`, `run_profiling.py:48` |
| Percentile CI method | [PASS] | `interaction_index.py:430-431` |
| 4 条件 forward pass (dense/attn/kv/both) | [PASS] | `run_profiling.py:108-124` |

---

## 2. 关键问题 (Critical)

### [ISSUE-C1] Phase segmentation 作用于 prompt 而非 reasoning trace

**位置**: `run_profiling.py:235-238`

```python
first_step_attentions = outputs.attentions[0]
last_layer_attn = first_step_attentions[-1][0]  # (H, prompt_len, prompt_len)
annotation = segmenter.segment(last_layer_attn)
```

当前代码用 prefill step 的 attention（即 prompt 的 attention matrix）做 phase segmentation。但协议要求对**生成的 reasoning trace** 做 phase segmentation。Prompt 只是数学题描述，不存在有意义的 execution/reasoning/transition 相位。

代码中已经有 `PhaseSegmenter.compute_step_sparsity()` 和 `segment_from_sparsity()` 方法可以处理逐步生成的 sparsity，但 `run_profiling.py` 未使用。

**修复方案**: 遍历每个 generation step 的 attention，调 `compute_step_sparsity()` 收集 per-token sparsity 序列，然后调 `segment_from_sparsity()` 对生成部分做 phase segmentation。Phase token indices 应映射到 `full_ids` 中 prompt 之后的位置。

---

### [ISSUE-C2] 同一 problem 的不同 phase 使用了不同的 random masks

**位置**: `run_profiling.py:243-264`

```python
for phase in annotation.phases:        # outer loop
    for level in SPARSITY_LEVELS:       # inner loop
        ppls = compute_conditioned_perplexities(
            ii_calc, full_ids, phase.token_indices, level,
        )
```

`compute_conditioned_perplexities` 内部每次调用 `_select_heads_to_mask` / `_select_kv_to_evict`，用 `torch.randperm` 生成随机 mask。不同 phase 在同一 sparsity level 下拿到**不同的**随机 mask。

正确做法：对同一 problem 和同一 sparsity level，应创建一组 mask，所有 phase 共用，仅改变评估的 token 位置。否则 mask 随机性与 phase 效应混淆，II 的 cross-phase 对比失去意义。

**修复方案**: 将 mask 生成提到 phase 循环外，per (problem, level) 生成一次，传入 `compute_conditioned_perplexities`。

---

### [ISSUE-C3] `output_attentions=True` 在 generate 中导致 OOM

**位置**: `run_profiling.py:222-228`

```python
outputs = model.generate(
    ...
    output_attentions=True,
    return_dict_in_generate=True,
)
```

7B 模型生成 2048 tokens 时，每步存储 28 层 attention weights（DeepSeek-R1-Distill-Qwen-7B 有 28 层），2048 步累计的 attention tensor 会轻松超出 GPU 内存。

**修复方案**: 有两条路——
- (A) 如果仍想用 prefill attention segmentation：对 prompt 单独做一次 forward（`output_attentions=True`），然后 generate 时关掉 `output_attentions`
- (B) 如果改为 generation-step segmentation（见 ISSUE-C1）：用 **attention hook** 在每步计算 sparsity 标量后立即释放 attention tensor，不累积

---

## 3. 中等问题 (Moderate)

### [ISSUE-M1] Dense forward pass 被重复计算

**位置**: `run_profiling.py:108-110` + 循环 `243-264`

Dense perplexity 对每个 (phase, level) 都重新计算一次 forward pass。一个 problem 有 ~3 phase × 2 levels = 6 次 dense forward，但 dense 结果只需**一次**。

24 次 forward → 理论最优 7 次 (1 dense + 2 attn + 2 kv + 2 both)。

**修复**: 提取 dense forward 到循环外，缓存结果。

---

### [ISSUE-M2] KV eviction 简化为 flat mask，比预期更激进

**位置**: `interaction_index.py:209-211`

```python
flat_kv_mask = kv_mask.min(dim=0).values  # union across layers
model_attention_mask = attention_mask * flat_kv_mask.unsqueeze(0)
```

Per-layer KV mask 被取 min（union）合并为单层 mask：只要任何一层 evict 某位置，则所有层都 evict。这使 KV sparsity 的实际 eviction rate 远高于标称的 30%/50%，ppl_kv 偏高，可能导致 II 偏差。

注释标明是 "for simplicity"，但对 MVP 结论可信度有影响。

---

### [ISSUE-M3] `_build_kv_attention_mask` 函数定义但未使用

**位置**: `interaction_index.py:140-158`

Dead code，应删除或替代当前的 flat mask 实现。

---

## 4. 小问题 (Minor)

### [ISSUE-m1] 未使用的 import
**位置**: `run_profiling.py:35` — `from ..utils.metrics import compute_perplexity` 未被直接使用。

### [ISSUE-m2] `_find_attention_layers` 主路径对标准 HF 模型永远失败
**位置**: `interaction_index.py:86`

```python
if type(module).__name__.endswith("Attention") and "self" not in name.split(".")[-1].lower():
```

标准 HF 模型的 attention 模块名为 `model.layers.X.self_attn`，`split(".")[-1]` = `"self_attn"` 包含 `"self"` → 条件永远 False。然后 fallback 兜底（line 95-98）正确工作，所以不影响运行，但逻辑意图错误。

### [ISSUE-m3] 难度级别数量无校验
**位置**: `data_utils.py:28-32`

如果数据集不含完整 5 个级别，采样数量静默少于 50，不会报错或 warning。

### [ISSUE-m4] Torch 随机种子未设置
mask 生成依赖 `torch.randperm`（全局 RNG），但 `run_profiling.py` 仅设置了 `random.Random(seed)` 和 `np.random.RandomState(seed)`，未调 `torch.manual_seed(SEED)`。影响可复现性。

---

## 5. 接口一致性

| 调用关系 | 状态 |
|----------|------|
| `run_profiling` → `stratified_sample_math500(data, seed=SEED)` | [PASS] 签名匹配 |
| `run_profiling` → `PhaseSegmenter(bandwidth, min_phase_length)` | [PASS] |
| `run_profiling` → `InteractionIndexCalculator(model, tokenizer, device)` | [PASS] |
| `run_profiling` → `compute_conditioned_perplexities(ii_calc, input_ids, indices, level)` | [PASS] |
| `run_profiling` → `bootstrap_interaction_index(samples, n_resamples, seed)` | [PASS] |
| `interaction_index` → `compute_perplexity(logits, labels, token_indices)` | [PASS] |
| `compute_perplexity` 内部 shift/index 逻辑 | [PASS] position 0 正确过滤 |

---

## 6. 总结

**不能直接部署运行。** 有 3 个 critical issue 需先修复：

| 优先级 | Issue | 影响 |
|--------|-------|------|
| P0 | C1: Phase segmentation 作用对象错误 | 实验结论无效 |
| P0 | C2: 不同 phase 使用不同 random mask | II cross-phase 对比被噪声污染 |
| P0 | C3: output_attentions OOM | 运行时 crash |

建议修复顺序：C3 → C1 → C2 → M1 → M4 → M2。C3 和 C1 的修复方案互相关联（都涉及 attention 获取方式），适合一起改。

---
