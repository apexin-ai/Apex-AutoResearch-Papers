# analysis n475 recalc

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_n475_recalc_20260515T081534_result.json`
- **Structured JSON:** [`cb6bd3db3a6b05e8a2fd.json`](../../sessions/cb/cb6bd3db3a6b05e8a2fd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**修复内容：**
- 创建 `analyze_n500_v2.py`，筛选逻辑：D = ii_low − ii_high 只要求 low+high 有效（不要求 mid），Qwen n=475（原 registry 记录的 n=274 是错误的 complete-case）
- `extract_diffs_paired` 函数确保跨条件配对时也只用 low+high 都有效的问题
- Bonferroni 校正因子从 20 增到 48（新增 cross-model Mann-Whitney U 8 项检验）

**输出文件（`/root/autodl-tmp/pacs/analysis_output/`）：**
- `n500_unified_final.csv` — 16 条件 + within d_z + imp vs rand + cross-model + effect ratio
- `n500_unified_final.json` — 完整结构化 JSON
- `n500_full_statistics.md` — 人可读 markdown 报告

**关键变化 vs 旧版：**
- Qwen n: 274 → 475
- DS rand s025/s030: 旧版 bonf_p ≈ 0.03（显著），新版 bonf_p ≈ 0.07（因 48 tests 校正后不再显著）
- Qwen 所有 imp 条件保持 *** 显著，结论不变
- Registry `c2_qw_n500_r3` 已更新 metrics/notes

---
