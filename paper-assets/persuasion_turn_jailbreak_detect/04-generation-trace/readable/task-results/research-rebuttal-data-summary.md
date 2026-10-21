# research rebuttal data summary

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_rebuttal_data_summary_20260522T213017_result.json`
- **Structured JSON:** [`475bc14baf432ae8e8af.json`](../../sessions/47/475bc14baf432ae8e8af.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已写入 `/root/jailbreak_detect/rebuttal_data_summary.md`（203 行），覆盖 5 个板块：

1. **exp63 FP/FN** — 9-class vs MLM 的 F1/FPR/P/R + 144/46 样本错误分解
2. **exp54 causal probe** — top-3 SVD 投影保留完美 OOD 检测 (F1=1.0)，MLM full-768 仅 0.636；附 exp57 IID-only SVD 补充（无数据泄漏）
3. **exp50 layerwise** — 13 层 Fisher ratio 完整表，peak 在 layer 10（9-class=10.92 vs vanilla=0.73）
4. **WildChat/OASST2 adaptation** — FPR 随 N 下降曲线 + multi-seed 验证（WC n=10 FPR=0，OASST2 n=25 FPR=0.010±0.005）
5. **Per-seed variance** — 3-seed/5-seed/10-seed 的 DD/AA OOD F1 mean±std，含 TOST 等价检验结果

---
