# ssh re diagnostic cascade

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_re_diagnostic_cascade_20260522T072559_result.json`
- **Structured JSON:** [`1b710c32e70543896674.json`](../../sessions/1b/1b710c32e70543896674.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the summary:

---

## 1. RE Diagnostic Cascade (SciERC RE, N=8, finetuned)

| Metric | Value |
|--------|-------|
| Degeneracy | 0.8% (3/397) |
| LP-F1 ρ (pooled) | 0.1622 (p=3.6e-20) |
| LP-F1 ρ (within-instance) | 0.2243 (n=110) |
| Greedy F1 | 0.0752 |
| MV F1 | 0.0390 (Δ = **-3.62pp**) |
| LP-best F1 | 0.0760 (Δ = **+0.08pp**) |
| Oracle F1 | 0.1541 (Δ = +7.89pp) |
| Zero-F1% | **71.8%** |

## 2. NER vs RE Comparison Table

| Task | Dataset | Degen% | LP-F1 ρ | MV Δ(pp) | LP-best Δ(pp) | Zero-F1% |
|------|---------|--------|---------|----------|---------------|----------|
| NER | SciERC | 13.4 | — | -1.24 | -0.32 | — |
| NER | CoNLL | 56.7 | — | +0.20 | -1.62 | — |
| NER | FewNERD | 8.8 | — | -2.74 | — | — |
| **RE** | **SciERC** | **0.8** | **0.162** | **-3.62** | **+0.08** | **71.8** |

RE 的关键发现：
- **极低 degeneracy**（0.8% vs NER 8.8-56.7%）— RE 样本多样性远高于 NER
- **MV 严重损害**（-3.62pp）— 比所有 NER 数据集都差，说明 RE 的低一致性让 MV 无效
- **LP-best 近乎无效**（+0.08pp）— logprob 基本无法区分 RE 质量
- **71.8% Zero-F1** — 绝大多数 instance 所有 8 个 sample 的 RE F1 都是 0，说明 RE 任务本身极难

## 3. GPU 状态

**autodl-5090** — 4× GPU 全部空闲 (0%, 2MiB)
| GPU | Util | VRAM |
|-----|------|------|
| 0-3 | 0% | 2/32607 MiB |

pretrained 实验目录（`conll_pretrained_n16_seed42`, `scierc_pretrained_n64_seed42`, `conll_pretrained_n64_seed42`）均为空，**没有在跑**，也没有对应的活跃进程。

**autodl-5090-c** — 3 GPU 活跃
| GPU | Util | VRAM |
|-----|------|------|
| 0 | 81% | 30115/32607 MiB |
| 1 | 78% | 30079/32607 MiB |
| 2 | 0% | 0/32607 MiB |
| 3 | 68% | 29785/32607 MiB |

## 4. 实验状态

**仍在运行（autodl-5090-c）**：
- `fewnerd_n32_seed42` — 运行中，output 目录仍为空（tmux 启动于 10:49）
- `fewnerd_pretrained_n16_seed42` — 运行中，output 为空（tmux 启动于 13:31）
- `fewnerd_pretrained_n32_seed42` — 运行中，output 为空（tmux 启动于 12:13）

**未启动（autodl-5090）**：
- `conll_pretrained_n16_seed42` — 空目录，无进程
- `scierc_pretrained_n64_seed42` — 空目录，无进程
- `conll_pretrained_n64_seed42` — 空目录，无进程

autodl-5090 的 3 个 pretrained 实验没有实际启动，GPU 全部空闲。需要排查原因或重新提交。

---
