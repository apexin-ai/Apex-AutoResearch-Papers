# fix bib reviewer warnings

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_bib_reviewer_warnings_20260514T091252_result.json`
- **Structured JSON:** [`f188769cd38bd1336bc9.json`](../../sessions/f1/f188769cd38bd1336bc9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

自查通过。修改汇总：

### Fix 1: 年份修正
| 条目 | 修改 |
|------|------|
| `liu2024scissorhands` | year 2024 → **2023**（匹配 NeurIPS 2023） |
| `lin2024qserve` | year 2024 → **2025**（匹配 MLSys 2025） |

### Fix 2: arXiv 伪 DOI → url（6 条 @inproceedings）
| 条目 | `doi = {10.48550/arXiv.XXXX}` → `url = {https://arxiv.org/abs/XXXX}` |
|------|------|
| `zhang2023h2o` | 2306.14048 |
| `li2024snapkv` | 2404.14469 |
| `ge2024fastgen` | 2310.01801 |
| `xiao2024streamingllm` | 2309.17453 |
| `liu2024scissorhands` | 2305.17118 |
| `yang2024pyramidinfer` | 2405.12532 |

### Fix 3: @misc 补 eprint + archivePrefix（6 条）
`kang2024gear`, `duanmu2024skvq`, `zuo2026ratequant`, `lei2026arkv`, `li2025kvmix`, `zhang2025mixkvq`

### 自查结果
- 所有 year 与 booktitle 年份一致 ✓
- 无 `doi = {10.48550/arXiv.*}` 残留 ✓
- 所有 @misc 均有 eprint + archivePrefix ✓
- 无遗漏 ✓

---
