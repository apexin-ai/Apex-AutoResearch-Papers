# ssh check gpu status

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_gpu_status_20260514T185550_result.json`
- **Structured JSON:** [`b45678d764d8587be112.json`](../../sessions/b4/b45678d764d8587be112.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇总

### GPU 使用情况
| GPU | 状态 | 显存 | 利用率 |
|-----|------|------|--------|
| cuda:0 | **空闲** | 2MiB / 32607MiB | 0% |
| cuda:1 | **运行中** | 29916MiB / 32607MiB | 79% |
| cuda:2 | 空闲 | 2MiB / 32607MiB | 0% |
| cuda:3 | 空闲 | 2MiB / 32607MiB | 0% |

---

### exp_002_conll_n16 (Qwen CoNLL N=16) — **已完成**

- 进程已结束，cuda:0 已释放
- 输出文件:
  - `output/exp_002_conll_n16/report.json` (1.8K)
  - `output/exp_002_conll_n16/samples.jsonl` (17M)
  - `output/exp_002_conll_n16.log` (400K)

**关键 metrics:**
| 指标 | 值 |
|------|-----|
| Verdict | **PASS** |
| Greedy F1 | 0.9075 |
| Oracle F1 | 0.9566 |
| Oracle headroom | +0.0492 |
| Fleiss' κ (mean) | 0.7160 |
| Soft Jaccard (mean) | 0.8770 |
| ρ(κ, F1) full / cond | +0.3928 / +0.3494 |
| ρ(SJ, F1) full / cond | +0.4496 / +0.4208 |
| Structural > Surface | **YES** (Δ=+0.0568) |
| Logprob AUROC full / cond | 0.7531 / 0.8259 |
| 样本数 | 3453 instances, N=16 |

---

### exp_007_llama_n16 (LLaMA SciERC N=16) — **运行中**

- PID 104278, 启动于 02:52, 运行约 4 分钟
- VLLM EngineCore PID 104554 在 cuda:1, 占用 29906MiB
- 进度: **~66% (5824/8816)**, 预计还需约 1-2 分钟
- 吞吐: ~5200 tok/s input, ~4350 tok/s output
- 已有部分输出:
  - `output/exp_007_llama_n16/report.json` (1.7K)
  - `output/exp_007_llama_n16/samples.jsonl` (6.5M)

---

### checkpoints/ — 无新产出

最新是 `llama3.1-8b-conll2003-merged` (May 15 01:33), 之前已存在。

---
