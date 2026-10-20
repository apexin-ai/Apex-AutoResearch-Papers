# paper table3 r025 3seed

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_table3-r025-3seed_20260522T061820_result.json`
- **Structured JSON:** [`6e5d8ef6e128315289ec.json`](../../sessions/6e/6e5d8ef6e128315289ec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

编译成功，11 页（含 references + appendix，符合 8 页正文限制）。

**已完成的修改汇总：**

| 位置 | 旧值 | 新值 |
|------|------|------|
| Table 3 (L180) SLV | 2485.0 | 2488.1 |
| Table 3 (L180) eff_rank | 512.5 | 513.8 |
| Table 3 (L180) PPL | 13.29 | 13.41 |
| Table 3 (L180) D-4 | .357 | .342 |
| §4.4 L142 Gen~10 SLV | $2485.0$, $+5.0\%$ | $2488.1$, $+5.1\%$ |
| §4.4 L145 EMA 幅度 | $-0.6$ vs.\ $-1.7$ | $-0.6$, $-1.7$, $-0.9$ |
| Table 3 caption (L185) | r=0.25 single seed | r=0.25 mean of three seeds (42, 43, 44) |
| §4.4 L162 D-4 | 0.357 | 0.342 |
| Limitations (L5) | r∈{0.2, 0.25, 0.5} single seed | r∈{0.2, 0.5} single seed; r=0.25 three seeds |

**未改动（按要求）：** Abstract L5。

**全文 grep 旧值残留：** 无。`.tex` 文件中 `2485.0`、`512.5`、`13.29`、`.357` 均已清除。

**注意：** L142 的早期 dip 值（$2362.1$、$2363.1$、$-4.6$）和 L143-144 的 EMA/controller 值未更新，因为 Director 只提供了 Gen~10 的 3-seed 统计值，无早期 generation 的 3-seed 数据。如需更新这些值，请提供对应数据。

---
