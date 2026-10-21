# paper experiments gen7 sync

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_experiments_gen7_sync_20260517T114113_result.json`
- **Structured JSON:** [`9347b4cd4aa2e755cd86.json`](../../sessions/93/9347b4cd4aa2e755cd86.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部修改完成，无遗漏。`Gen~5` 仅出现在中间位置（表头列名、per-gen 增量序列的中间步、sigma_1 中间值），均为正确引用。

**修改汇总（14 处）：**

| # | 行号 | 修改内容 |
|---|------|----------|
| 1 | 147 | 段落标题 `Gen~3→5` → `Gen~3→7` |
| 2 | 148 | `through Generation~5` → `~7` |
| 3 | 148 | eff rank 列表扩展到 Gen 7，累计下降 `-3.5%` → `-6.5%` |
| 4 | 148 | log-vol 列表扩展到 Gen 7，累计下降 `-4.0%` → `-6.7%` |
| 5 | 148 | per-gen rank 下降率追加 Gen 5→6 (`-1.3%`)、Gen 6→7 (`-1.9%`) |
| 6 | 153 | σ₁ 从 `741.0 at Generation~5` 扩展为 `741.0 (Gen~5), 758.4 (Gen~6), 791.3 (Gen~7)` |
| 7 | 159 | 正文引用 `Generations~0--5` → `0--7` |
| 8 | 161 | 表格 caption `Generations~0--5` → `0--7` |
| 9 | 180 | `through Generation~5` → `~7` |
| 10 | 180 | ppl `24.59 at Gen~5, 116%` → `38.89 at Gen~7, 242%` |
| 11 | 180 | ppl 增量序列追加 `6.32 (Gen~5→6), 7.97 (Gen~6→7)` |
| 12 | 180 | distinct-4 `0.4630 (-26.0%)` → `0.4474 (-28.5%)` |
| 13 | 182 | HellaSwag `0.3439 (Gen~5), 16.7%, 11.7%` → `0.3187 (Gen~7), 22.8%, 18.2%` |
| 14 | 184 | train loss `1.047 (Gen~5), 116%` → `1.015 (Gen~7), 242%` |

表格（item 6）HellaSwag Gen 6-7 列已有正确数值 0.3311/0.3187，无需修改。

---
