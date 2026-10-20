# ssh f1 scaling law

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_f1-scaling-law_20260520T101432_result.json`
- **Structured JSON:** [`fd682a3f854e1d6f0c59.json`](../../sessions/fd/fd682a3f854e1d6f0c59.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

**F1(N) = a - b·N^(-c) 拟合结果** (所有 R² > 0.999)

| Config | c | c_se | a | b | R² |
|--------|------|------|-------|-------|--------|
| Qwen/SciERC | **0.390** | 0.014 | 0.914 | 0.282 | 0.9999 |
| Qwen/CoNLL | **0.839** | 0.058 | 0.972 | 0.099 | 0.9993 |
| Qwen/FewNERD | **0.612** | 0.023 | 0.957 | 0.251 | 0.9999 |
| LLaMA/SciERC | **0.302** | 0.027 | 0.938 | 0.296 | 0.9998 |
| LLaMA/CoNLL | **0.329** | 0.044 | 0.969 | 0.043 | 0.9994 |
| LLaMA/FewNERD | **0.609** | 0.030 | 0.941 | 0.192 | 0.9999 |

**关键发现：**
- **c_mean = 0.51**, 总体与 Wang et al. 2023 报告的 reasoning tasks (c≈0.5-0.7) 可比
- **SciERC 显著最慢**: c_mean=0.35 (两个模型一致)，说明 complex IE (多类型实体+关系) 的 oracle headroom 增长最缓慢
- **FewNERD 较快**: c_mean=0.61，粗粒度 NER 的 diversity 收益更好
- **Qwen/CoNLL 异常高** (c=0.84)：因为 b=0.099 极小 (headroom 本身就窄)，c 在小 gap 上拟合不够稳定
- **LLaMA/CoNLL 低** (c=0.33, b=0.043)：同理，gap 太小导致 c 不可靠

产出文件保存在 `autodl-5090:/root/autodl-tmp/struct_self_consist_ie/artifacts/f1_scaling/`，已注册 artifact。

---
