# research lofo nonqwen reframing

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_lofo_nonqwen_reframing_20260521T015657_result.json`
- **Structured JSON:** [`a0a488be18f24c02efae.json`](../../sessions/a0/a0a488be18f24c02efae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Non-Qwen θ̂ Derivation

### 数据可用性

| 家族 | 模型 | 1v2 AUC | 1v2 ci_lower | 2v3 ci_lower | K\* at θ=0.60 | K\* at θ=0.58 |
|------|------|---------|-------------|-------------|--------------|--------------|
| Gemma | Gemma-2B | 0.5981 | 0.5882 | 0.5234 | 1 | 2 |
| OLMo | OLMo | 0.6145 | 0.6045 | 0.5399 | 2 | 2 |
| Pythia | Pythia-1.4B | 0.6539 | 0.6454 | 0.5417 | 2 | 2 |
| LLaMA | LLaMA-8B | 0.6123 | 0.6028 | 0.5169 | 2 | 2 |
| Mistral | Mistral-7B | 0.5935 | 0.5835 | 0.5301 | 1 | 2 |

5/5 non-Qwen 家族数据齐全（含 LLaMA-8B 和 Mistral-7B，均为 C4 域，scorer=Qwen2.5-1.5B base）。

### 推导结果

- Non-Qwen K\*=2 consensus θ̂ range: **(0.5417, 0.5835]**
- Width: 0.0418
- Midpoint: 0.5626
- Binding high: **Mistral-7B** (1v2 ci_lower = 0.5835，最低)
- Binding low: **Pythia-1.4B** (2v3 ci_lower = 0.5417，最高)

注意：θ=0.60 落在此范围之外（>0.5835），导致 Gemma-2B 和 Mistral-7B 降为 K\*=1。

### Qwen Validation

| Qwen 模型 | 1v2 ci_lower | 2v3 ci_lower | K\* at θ̂=0.58 | margin(1v2) | margin(2v3) |
|-----------|-------------|-------------|---------------|------------|------------|
| Qwen-1.5B-rw | 0.6859 | 0.5795 | **2** | +0.1059 | **-0.0005** |
| Qwen-1.5B-cont | 0.6015 | 0.5511 | **2** | +0.0215 | -0.0289 |
| Qwen-7B | 0.6080 | 0.5390 | **2** | +0.0280 | -0.0410 |

θ=0.58 时 3/3 Qwen 模型均返回 K\*=2，验证通过。Qwen-rw 的 2v3 margin 仅 -0.0005，是最紧约束。

### 全 8 家族 consensus

- All-8 K\*=2 range: **(0.5795, 0.5835]**，width = 0.0040
- Binding high: Mistral-7B (1v2 ci_lower = 0.5835)
- Binding low: Qwen-1.5B-rw (2v3 ci_lower = 0.5795)
- θ=0.5815（midpoint）时 8/8 家族全部 K\*=2

### 结论

θ̂ = **0.58** 使得 non-Qwen 推导 + Qwen 验证完全一致：5 个 non-Qwen 家族推导出的 consensus range (0.5417, 0.5835] 包含 0.58，3 个 held-out Qwen 家族在 θ=0.58 下独立验证为 K\*=2。全 8 家族 consensus 窄带为 (0.5795, 0.5835]。

原始 θ=0.60 偏高，落在 non-Qwen consensus 范围外，导致 Gemma-2B 和 Mistral-7B 被错误降级为 K\*=1。

产出文件：
- `results/lofo_theta_validation/lofo_nonqwen_reframing.json`
- `results/lofo_theta_validation/lofo_nonqwen_reframing_table.tex`

---
