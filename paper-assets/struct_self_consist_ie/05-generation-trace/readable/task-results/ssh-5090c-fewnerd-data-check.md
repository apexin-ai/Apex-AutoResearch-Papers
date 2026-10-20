# ssh 5090c fewnerd data check

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_5090c_fewnerd_data_check_20260521T143623_result.json`
- **Structured JSON:** [`bebdc58ae4539eb3b874.json`](../../sessions/be/bebdc58ae4539eb3b874.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

### 1. FewNERD MF4v2 数据

**不存在。** 服务器上唯一名含 `mf4v2` 的目录是 **CoNLL** 的：
- `/root/autodl-tmp/struct_self_consist_ie/output/conll_mf4v2_seed42/` — CoNLL MF4v2 结果（samples.jsonl 57MB, report.json, 时间戳 May 21 18:27）

FewNERD 没有对应的 MF4v2 output 目录。

FewNERD 现有 samples.jsonl（均非 MF4v2）：
| 路径 | 说明 |
|------|------|
| `output/exp_fewnerd_seed789/` | seed 789 |
| `output/exp_tlow_fewnerd_t05_s42/` | temp=0.5, seed 42 |
| `output/fewnerd_7b_n16_seed42/` | 7B, n=16, seed 42 |
| `output/fewnerd_n16_seed456_v2/` | n=16, seed 456 v2 |

### 2. GPU 状态（4× RTX 5090 32GB）

| GPU | 利用率 | 显存占用 | 状态 |
|-----|--------|---------|------|
| GPU 0 | 84% | 30131/32607 MiB | 运行 `exp_fewnerd_n16_s123`（Qwen3-8B-merged, n=16, seed 123） |
| GPU 1 | 0% | 0 MiB | **空闲** |
| GPU 2 | 0% | 0 MiB | **空闲** |
| GPU 3 | 85% | 30889/32607 MiB | 运行 `e2_pretrained_fewnerd_s123`（Qwen2.5-7B, n=8, seed 123） |

---
