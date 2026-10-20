# code reference fixes

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_reference_fixes_20260514T192902_result.json`
- **Structured JSON:** [`51834aff282dc8d46949.json`](../../sessions/51/51834aff282dc8d46949.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

编译通过，无 undefined citation 错误。

## 修改摘要

### references.bib
| # | 问题 | 修改 |
|---|------|------|
| 1 | DOI 错误 | 已为正确值，无需修改 |
| 2 | DeepSeek-R1 标题 | 更新为 Nature 官方标题 "DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning" |
| 3 | DeepSeek-R1 author | 保留 `{DeepSeek-AI}`（>10人团队论文，可接受） |
| 4 | 5个 orphan 条目 | 删除 `compression-ordering-2025`, `mustafar-neurips2025`, `obcache-2025`, `pagedeviction-eacl2026`, `raas-acl2025` |
| 5 | PyramidKV 发表状态 | 更新为 `@inproceedings`，venue = COLM 2025（Spotlight），year 改为 2025 |
| 6 | 3篇缺失引用 | 新增 `physics-kvcache-2026`（arXiv 2603.01426）、`hies-2025`（arXiv 2510.13832）、`rkv-neurips2025`（NeurIPS 2025） |
| 7 | DOI 格式一致性 | 仅 deepseek-r1-2025 有 DOI，格式已正确，无需修改 |

### related_work.tex
- **KV cache eviction 段落**：在 greedy-bias 引用后新增一句引用 HIES（importance score collapse 证据）
- **Phase-aware inference 段落**：在 sparse-frontier 引用后新增两句，分别引用 Physics of KV Cache Compression（单轴 phase transition）和 R-KV（reasoning-specific cache compression）

bib 条目总数：31 → 29（删5 + 加3），tex 中引用数：26 → 29。编译无错误。

---
