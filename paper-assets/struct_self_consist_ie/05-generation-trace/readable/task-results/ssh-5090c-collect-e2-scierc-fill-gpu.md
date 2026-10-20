# ssh 5090c collect e2 scierc fill gpu

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_5090c_collect_e2_scierc_fill_gpu_20260521T143841_result.json`
- **Structured JSON:** [`97ffd2a85349e7d1232b.json`](../../sessions/97/97ffd2a85349e7d1232b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇总如下：

---

## 1. e2_pretrained_scierc 三种子完整对比

| Metric | s42 | s123 | s456 |
|--------|-----|------|------|
| greedy_f1 | 0.2418 | 0.2396 | 0.2403 |
| oracle_f1 | — | 0.3867 | 0.3875 |
| oracle_headroom | — | 0.1471 | 0.1472 |
| rho_FK_full | — | 0.1974 | 0.2340 |
| rho_SJ_full | — | 0.1808 | 0.2151 |
| rho_FK_cond | — | 0.2221 | 0.1958 |
| **rho_SJ_cond** | **0.1987** | **0.2250** | **0.2187** |
| logprob_rho_full | — | 0.048 (n.s.) | 0.065 (n.s.) |
| logprob_rho_cond | — | 0.2261 | 0.2002 |
| structural_beats_surface | — | false | false |
| sample_f1_pct_zero | — | 45.96% | 45.53% |
| **verdict** | **FAIL** | **FAIL** | **FAIL** |

**结论：三种子高度一致，全部 FAIL。** 预训练 Qwen2.5-7B-Instruct 在 SciERC 上 greedy_f1 仅 ~0.24，~46% 样本 F1=0，SC 信号极弱（rho_SJ_cond ~0.20-0.22），logprob 在 full 条件下甚至不显著。模型未经微调在 SciERC 上能力不足，无法产生有意义的 SC 信号。

---

## 2. 5090-c 可用模型

`checkpoints/` 目录：

| 模型 | 类型 |
|------|------|
| qwen3-8b-fewnerd-exp021-merged | Qwen3-8B FewNERD finetuned |
| qwen3-8b-conll2003-merged | Qwen3-8B CoNLL finetuned |
| qwen3-8b-scierc-merged-v2 | Qwen3-8B SciERC finetuned |
| qwen25-7b-fewnerd-merged | Qwen2.5-7B FewNERD finetuned |
| qwen25-14b-fewnerd-merged-ckpt36000 | Qwen2.5-14B FewNERD ckpt36000 |
| qwen25-14b-fewnerd-merged-final | Qwen2.5-14B FewNERD final |
| llama3.1-8b-scierc-lora | LLaMA3.1-8B SciERC LoRA |

**Qwen3-8B-FewNERD finetuned 模型已在 5090-c 上可用**（`qwen3-8b-fewnerd-exp021-merged`）。

`/root/autodl-tmp/models/` 不存在。

---

## 3. cuda:1/2 利用建议

当前 5090-c 状态：cuda:0 被 `fewnerd_n16_s123` 占用（RUNNING），cuda:1/2 空闲。

可选方案（按优先级）：
1. **FewNERD N=16 多种子补充**（s456）— 如果 N=16 scaling 实验需要第三种子
2. **SciERC finetuned N=16 scaling** — 用 `qwen3-8b-scierc-merged-v2` 跑 SciERC N=16（与 FewNERD N=16 对称）
3. **MF4v2 pipeline** — Qwen3-8B-FewNERD 模型已就位，可直接启动 MF4v2 相关实验
4. **CoNLL N=16 补充种子** — 用 `qwen3-8b-conll2003-merged` 补 CoNLL 多种子

取决于当前 roadmap 的优先级，需要你决定。

---
