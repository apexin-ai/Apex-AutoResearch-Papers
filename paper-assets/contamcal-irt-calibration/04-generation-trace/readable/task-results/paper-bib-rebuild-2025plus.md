# paper bib rebuild 2025plus

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_bib_rebuild_2025plus_20260517T051927_result.json`
- **Structured JSON:** [`f66833e3431cf7eaea03.json`](../../sessions/f6/f66833e3431cf7eaea03.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已生成。验证结果汇总：

| Key | 状态 | 问题 |
|-----|------|------|
| `chang2025benchmarking` | VERIFIED | 年份实为 2024，venue 是 ACM TIST（非 EMNLP 2025） |
| `duan2025minkpp` | REPLACED | 作者全部捏造，实际是 Zhang et al. ICLR 2025（与现有 `zhang_2024_minkpp` 重复） |
| `habba_2025_growing_pains` | VERIFIED | 作者列表全错，年份实为 2026，arXiv 2604.12843 |
| `li_2025_dcr` | NOT_FOUND | 完全幻觉，不存在该论文。真正 DCR 是 Xu et al. EMNLP 2025（已有 `xu_2025_dcr`） |
| `luettgau_2025_hibayes` | VERIFIED | 作者全错（原写 Polo 等人），实际是 UK AI Safety Institute 团队，arXiv 2505.05602 |
| `polo2026growing` | REPLACED | 与 `habba_2025_growing_pains` 是同一篇，Polo 非该文作者 |
| `xu2025emperor` | VERIFIED | 作者全错，实为 Sun Yifan 等，ICML 2025，arXiv 2503.16402 |
| `wust2025selfcritique` | REPLACED | 确认幻觉，替换为 Tao et al. arXiv 2510.09259 |
| `kadavath_2022_self_eval` | NEW | 已添加，arXiv 2207.05221 |

需要决策：
- `duan2025minkpp` 与已有 `zhang_2024_minkpp` 重复，tex 中是否统一改用后者？
- `li_2025_dcr` 是幻觉，引用上下文需要改用 `xu_2025_dcr` 还是 Li Yucheng 2024 的 contamination report？
- `polo2026growing` 与 `habba_2025_growing_pains` 同一论文，需合并 key。

---
