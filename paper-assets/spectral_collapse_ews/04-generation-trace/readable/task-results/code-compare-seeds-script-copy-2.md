# code compare seeds script

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_compare_seeds_script_20260519T124538_result.json`
- **Structured JSON:** [`9aa67bb8fae86ce19ba3.json`](../../sessions/9a/9aa67bb8fae86ce19ba3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。

**输出结果摘要：**

- `scripts/compare_seeds.py` — 脚本已创建，支持任意数量 seed 文件
- 双 seed 测试：seed42 (11 gens) + seed43 (3 gens)，seed43 缺失的 gen 3-10 正确显示 `n/a`
- Phase boundaries：两个 seed 的 decompression peak 一致在 gen 2；seed42 onset=gen 3, collapse_confirmation=gen 4 (ppl_growth=21.9%, threshold=0.2)；seed43 数据不足无法检测 onset/collapse
- LaTeX 表：gen 0-2 有 mean±std（跨两个 seed），gen 3-10 仅 seed42 值（std 省略）

**已下载到本地 `results/`：**
- `phase0_results.json` (seed42, 11 gens)
- `phase1_pure_collapse_seed43_results.json` (seed43, 3 gens)

---
