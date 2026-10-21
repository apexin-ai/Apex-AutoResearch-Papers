# code westd16980 disk audit

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_westd16980_disk_audit_20260518T105505_result.json`
- **Structured JSON:** [`525729262b64231bffd1.json`](../../sessions/52/525729262b64231bffd1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have everything needed. Here's the full report.

---

## 磁盘总览

| 分区 | 总量 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| `/` (系统盘) | 30G | 27G | 3.7G | **88%** |
| `/root/autodl-tmp` (数据盘) | 250G | 132G | 119G | 53% |

**系统盘紧张（仅剩 3.7G），数据盘有余量。**

系统盘主要占用：
- `/root/miniconda3/` — 12G
- `/root/schema_semantic_constrained_ie/` — 5.2G（其中 checkpoints 4.7G, outputs 347M）
- `/root/carc/` — 663M（其他项目代码+数据）
- `/root/.cache/` — 496M（HF datasets 457M, pip 23M, HF hub 17M）
- `/root/turn-hier-kv-compress/` — 2.1M
- `/root/runs/` — 22M（tensorboard/其他项目 runs）

---

## 清理建议表

### A. 系统盘 — 高优先级（释放系统盘空间）

| 文件/目录 | 大小 | 分类 | 建议 | 原因 |
|-----------|------|------|------|------|
| `/root/schema_semantic_constrained_ie/checkpoints/` (4个 LoRA adapter) | **4.7G** | LoRA adapters | **可清理** | merged 版本已在 autodl-tmp/checkpoints/ 下（共 61G），这些是合并前的原始 adapter，可从 merged 版恢复或重新训练 |
| `/root/.cache/huggingface/datasets/` | **457M** | HF datasets 缓存 | **可清理** | 自动缓存，按需重新下载 |
| `/root/carc/` | **663M** | 其他项目 (CARC KV eviction) | **可清理** | 非当前项目，若不再需要可删 |
| `/root/.cache/pip/` | **23M** | pip 缓存 | **可清理** | `pip cache purge` 即可 |
| `/root/runs/` | **22M** | tensorboard runs | **可清理** | 含 3 个项目的旧 runs |
| `/root/turn-hier-kv-compress/` | **2.1M** | 其他项目 | **可清理** | 非当前项目 |

**系统盘可释放：~5.9G（使系统盘从 88% 降至 ~68%）**

### B. outputs/ 文件分类（347M，系统盘）

| 文件 | 大小 | 分类 | 建议 | 原因 |
|------|------|------|------|------|
| `ee_*_v3*.jsonl`, `ee_*_posthoc.jsonl`, `ee_*_cf_voted.jsonl` | ~35M | v3 / WikiEvents EE 最终结果 | **保留** | 论文需要 |
| `wikievents_*_constrained_full.jsonl`, `wikievents_*_unconstrained_full.jsonl` | ~27M | WikiEvents 最终结果 | **保留** | 论文需要 |
| `w5_*`, `w8_*`, `w9_*` (LoRA/FT 评估) | ~85M | LoRA/FT 实验结果 | **保留** | 论文 Table 数据 |
| `docred_*`, `phase2_scierc_*`, `scierc_full_s1_consensus_v2.jsonl` | ~45M | 主实验 ablation 数据 | **保留** | grammar_only/unconstrained/semantic_only 均为 ablation |
| `stability_seed*.jsonl` (3 files) | ~3.9M | 稳定性实验 | **保留** | 论文稳定性分析 |
| `scierc_qwen_beam_*.jsonl`, `beam_search_scierc_*.jsonl` | ~3.9M | beam search 实验 | **保留** | 论文实验 |
| `wikievents_*_backup.jsonl` (2 files) | **9.6M** | 备份文件 | **可清理** | 被后续完整版替代 |
| `wikievents_*.jsonl.bak_before16k` (2 files) | **10.9M** | 备份文件 | **可清理** | 被 16k max_tokens 版替代 |
| `raw_outputs_*.jsonl` (3 files) | ~23M | 早期原始输出 | **可能可清理** | v1 阶段产物，已被后续实验替代 |
| `test_*.jsonl` (4 files, ~2.2K each) | ~9K | 测试文件 | **可清理** | dryrun/test 文件 |
| `dryrun_*.jsonl`, `dryrun_prompt_sens_full.jsonl` | ~几K | dryrun 文件 | **可清理** | 空文件或调试产物 |
| `*.log` (多个) | ~几十K | 日志 | **可清理** | 调试日志 |
| `dry_run_violations.json`, `violation_report*.json` (多个) | ~几十K | 违规报告 | **可清理** | 调试产物 |
| `w1_cf_fallback_*.jsonl` (2 files) | ~2.8M | 旧版 cf_fallback 试验 | **可能可清理** | 早期版本，若论文不引用可删 |
| `posthoc_docred.jsonl`, `posthoc_report*.json` | ~9.1M | 早期 posthoc 结果 | **可能可清理** | 若已被 w8/w9 posthoc 替代 |

### C. 数据盘 — autodl-tmp（132G / 250G）

| 文件/目录 | 大小 | 分类 | 建议 | 原因 |
|-----------|------|------|------|------|
| `autodl-tmp/models/LLM-Research/` (Meta-Llama-3.1-8B-Instruct, 两份) | **15G** | 基座模型（重复） | **可能可清理** | 含两个目录名指向同一模型，确认是否重复 |
| `autodl-tmp/models/Qwen3-8B-ms/` | 16G | 基座模型 | **保留** | 实验在用 |
| `autodl-tmp/models/Mistral-7B-Instruct-v0.3-ms/` | 14G | 基座模型 | **保留** | 实验在用 |
| `autodl-tmp/models/._____temp/` | **85M** | 临时/残留 | **可清理** | 下载临时文件 |
| `autodl-tmp/checkpoints/` (4 merged LoRA) | 61G | Merged 模型 | **保留** | LoRA eval 需要 |
| `autodl-tmp/checkpoints/qwen_lora_docred/` | **0** | 空目录 | **可清理** | 空的 |
| `autodl-tmp/carc/models/` (DeepSeek-R1-Distill-Qwen-14B) | **28G** | 其他项目模型 | **可清理** | CARC 项目模型，非当前项目 |

---

## 汇总

| 优先级 | 可释放空间 | 来源 |
|--------|-----------|------|
| **系统盘高优** | ~5.9G | checkpoints/(4.7G) + HF datasets 缓存(457M) + carc/(663M) + pip cache(23M) + runs(22M) |
| **系统盘低优** | ~46M | outputs/ 中备份/test/dryrun/log 文件 |
| **数据盘高优** | ~28G | autodl-tmp/carc/models/ (其他项目 DeepSeek 14B) |
| **数据盘低优** | ~85M | autodl-tmp/models/._____temp/ + 空目录 |

**建议优先清理系统盘 checkpoints/（4.7G）和 HF datasets 缓存（457M），可立即将系统盘使用率从 88% 降至 ~70%。** 数据盘如果不再需要 CARC 项目，删除 DeepSeek 14B 可再释放 28G。

---
