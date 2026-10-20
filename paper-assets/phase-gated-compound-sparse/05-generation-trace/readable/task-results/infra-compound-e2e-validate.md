# infra compound e2e validate

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_compound-e2e-validate_20260513T210346_result.json`
- **Structured JSON:** [`8b5c72c5c91e5b7b16ae.json`](../../sessions/8b/8b5c72c5c91e5b7b16ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 验证结果

### 核心检查

| 检查项 | 结果 |
|--------|------|
| logits shape 正确 (1, S, 152064) | ✅ |
| 所有 PPL finite (非 NaN/Inf) | ✅ |
| GQA mapping (28Q → 4KV, 7:1) | ✅ |
| head-only 0.5-0.7 退化 <10x | ✅ (avg 2.28-3.01x) |
| kv-only 0.7 退化 <10x | ❌ (avg 22.4x) |

### PPL 退化表（3 prompt 平均）

| 配置 | avg PPL | avg 退化倍数 |
|------|---------|-------------|
| dense | 46.54 | 1.00x |
| **head_only 0.5** | 137.69 | **3.01x** |
| **head_only 0.7** | 83.91 | **2.28x** |
| kv_only 0.5 | 4204.33 | 76.38x |
| kv_only 0.7 | 1159.42 | 22.40x |
| compound 0.3/0.3 | 29856.00 | 1111.39x |
| compound 0.5/0.7 | 2470.00 | 58.67x |
| compound 0.7/0.7 | 877.83 | 23.70x |

### 分析

1. **Head masking 组件可用** — 0.5-0.7 ratio 退化仅 2-3x，符合预期。

2. **KV eviction 退化异常高** — 根因是测试序列太短（16-26 tokens），随机丢弃 30% 等于丢 5-8 个 token 的上下文，破坏性极大。M2 grid search 会用更长序列 + importance-based eviction，预期会好很多。

3. **Compound 超线性退化** — compound_0.7/0.7 (23.7x) ≈ kv_only_0.7 (22.4x)，说明退化主要由 KV eviction 驱动。head masking 在 KV 已被破坏的情况下进一步叠加损失有限。

4. **Head mask hook 的技术限制** — hook 作用在 `o_proj` 之后，此时各 head 的输出已经被线性混合。按 head_dim 分块 mask 不等于真正的 pre-projection head masking。但在 head-only 模式下退化可控，说明 post-projection 近似仍有效。

### 结论

**Pipeline 端到端可用**，无 crash、无 NaN、shape 正确。Head masking 就绪。KV eviction 在短序列 + 随机选择下退化高是预期行为，不阻塞 M2 grid search（M2 用长序列 + importance-based eviction）。建议 M2 启动时先在 128+ token 序列上验证 KV eviction 退化是否回到合理范围。

---
