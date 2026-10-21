# cpu llama d005 d000 rrf

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_cpu_llama_d005_d000_rrf_20260516T223842_result.json`
- **Structured JSON:** [`6d6388982a807e868a51.json`](../../sessions/6d/6d6388982a807e868a51.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Signals 完整性
| Dosage | MMLU | ARC | GSM8K |
|--------|------|-----|-------|
| d000 | ✓ | ✓ | ✓ |
| d005 | ✓ | ✓ | ✓ |
| d025 | ✗ | ✓ | ✓ |
| d100 | ✗ | ✓ | ✗ |

## RRF 结果
| Dosage | 状态 | 输出路径 |
|--------|------|----------|
| d000 | **完成** | `/root/autodl-tmp/exp003/rrf/Llama-3.2-3B_d000_s42/` (MMLU 14042, ARC 1172, GSM8K 1319 items) |
| d005 | **完成** | `/root/autodl-tmp/exp003/rrf/Llama-3.2-3B_d005_s42/` (MMLU 14042, ARC 1172, GSM8K 1319 items) |
| d025 | 跳过 | 缺 MMLU signals |
| d100 | 跳过 | 仅有 ARC，缺 MMLU + GSM8K |

## Cross-family IRT Pool 就绪模型数

现有池 (`rrf_full_n_latest`): **N = 25** (Qwen 0.5B/1.5B/3B 全系列 + Instruct baseline)

新增就绪: **+2** (Llama-3.2-3B d000, d005)

合并后: **N = 27** (首次引入 Llama family，实现 cross-family pooling)

待补齐: d025 需要 MMLU signals，d100 需要 MMLU + GSM8K signals。

---
