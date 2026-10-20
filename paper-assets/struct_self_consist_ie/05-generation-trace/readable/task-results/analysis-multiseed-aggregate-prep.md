# analysis multiseed aggregate prep

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_multiseed_aggregate_prep_20260518T202610_result.json`
- **Structured JSON:** [`4137a08bbdc53796284f.json`](../../sessions/41/4137a08bbdc53796284f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 4 个 GPU 满载运行。以下是完整汇总。

---

## 产出 1: 多种子覆盖汇总表

### Qwen3-8B CoNLL2003 NER (T=1.0, n=16)

| Seed | Greedy F1 | Oracle F1 | Sample F1 | Degen% | Cond ρ(SJ) | Cond AUROC | Verdict |
|------|-----------|-----------|-----------|--------|------------|------------|---------|
| 42   | 0.9075    | 0.9566    | 0.8674    | 7.6%   | 0.4208     | 0.8259     | PASS    |
| 123  | **0.9068**| **0.9633**| **0.8673**| 7.5%   | 0.4238     | 0.8235     | PASS ✓ new |
| 456  | **0.9074**| **0.9549**| **0.8735**| 7.0%   | 0.4482     | 0.8238     | PASS ✓ new |

### Qwen3-8B SciERC NER 温度消融 (n=8)

| T   | Seed | Greedy F1 | Oracle F1 | Degen% | Cond ρ(SJ) | Cond AUROC | Verdict |
|-----|------|-----------|-----------|--------|------------|------------|---------|
| 0.5 | 42   | 0.6647    | 0.7423    | 10.3%  | 0.2781     | 0.5921     | FAIL    |
| 0.5 | 123  | *running* | —         | —      | —          | —          | —       |
| 0.5 | 456  | *running* | —         | —      | —          | —          | —       |
| 0.7 | 42   | 0.6621    | 0.7643    | 11.0%  | 0.3625     | 0.6118     | MARGINAL|
| 0.8 | 42   | 0.6633    | 0.7684    | 11.2%  | 0.3123     | 0.5509     | MARGINAL|
| 0.8 | 123  | *running* | —         | —      | —          | —          | —       |
| 1.0 | 42   | 0.6621    | 0.8150    | 12.4%  | 0.3688     | 0.5851     | PASS    |
| 1.0 | 123  | 0.6621    | 0.8128    | 12.5%  | 0.3757     | 0.5993     | PASS    |
| 1.0 | 456  | 0.6639    | 0.8112    | 12.3%  | 0.3494     | 0.6014     | MARGINAL|
| 1.2 | 42   | 0.6615    | 0.7914    | 13.9%  | 0.3551     | 0.5569     | MARGINAL|
| 1.2 | 123  | **0.6595**| **0.7895**| 14.0%  | 0.2718     | 0.5464     | MARGINAL ✓ new |

### LLaMA3.1-8B CoNLL2003 (T=1.0, n=16)

| Seed | Greedy F1 | Oracle F1 | Sample F1 | Cond ρ(SJ) | Verdict |
|------|-----------|-----------|-----------|------------|---------|
| 42   | 0.9264    | 0.9494    | 0.9219    | 0.4856     | PASS    |
| 123  | 0.9264    | 0.9498    | 0.9218    | 0.4556     | PASS    |
| 456  | 0.9267    | 0.9488    | 0.9215    | 0.4505     | PASS    |

---

## 产出 2: GPU 新任务状态

| GPU | Task | Session | Status |
|-----|------|---------|--------|
| cuda:0 | SciERC T=0.5 s123 | `t05_s123` | Running (~7% done, ~3-4min remaining) |
| cuda:1 | LLaMA FewNERD LoRA train | `llama_fewnerd` | 71% (17476/24708) |
| cuda:2 | SciERC T=0.8 s123 | `t08_s123` | Running (~7% done) |
| cuda:3 | SciERC T=0.5 s456 | `t05_s456` | Running (~7% done) |

---

## 产出 3: LLaMA FewNERD 训练进度

- 进度: **71%** (17476/24708 steps)
- 最新 checkpoint: `checkpoint-17000`
- 预计剩余: ~3h16m
- GPU: cuda:1, 30888 MiB, 87-100% utilization

---
