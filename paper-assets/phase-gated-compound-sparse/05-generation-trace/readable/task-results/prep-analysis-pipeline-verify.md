# prep analysis pipeline verify

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_analysis_pipeline_verify_20260515T044019_result.json`
- **Structured JSON:** [`e9c389ef9443c4021dfe.json`](../../sessions/e9/e9c389ef9443c4021dfe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## n=500 分析 Pipeline 就绪状态简报

### 1. 分析脚本 — OK (有 bug)
`analyze_n500_unified.py` 存在，结构完整（median II + bootstrap CI, mid-phase null rate, Cohen's d_z, permutation monotonicity, Bonferroni）。但 **LaTeX 输出有 KeyError**：`latex_output()` 在处理 random masking 条件时崩溃于 `c["median_ii_diff_ci"]`（见 `n500_preliminary.log` 中的 traceback）。JSON/CSV 输出不受影响。

### 2. 依赖 — OK
- Python 3.12 (miniconda3)
- scipy ✓, numpy ✓, pandas ✓ （均在 `/root/miniconda3/lib/python3.12/site-packages/`）

### 3. n500 数据完整性 — **12/16 完成，4 个 s030 缺失**

| 条件 | ds_imp | ds_rand | qw_imp | qw_rand |
|------|--------|---------|--------|---------|
| s015 | ✅ | ✅ | ✅ | ✅ |
| s020 | ✅ | ✅ | ✅ | ✅ |
| s025 | ✅ (22MB, 11:19) | ✅ | ✅ | ✅ (19MB, 10:01) |
| s030 | ❌ 空目录 | ❌ 空目录 | ❌ 空目录 | ❌ 空目录 |

### 4. 实验进度
- `completion_check.log` 有自动轮询（每 10min），最新记录 **12:39:54**：`DeepSeek 6/8, Qwen 6/8`
- s025 最晚完成时间 11:19，之后 s030 目录已创建但无数据写入 — **s030 实验可能正在运行或卡住**
- 已有部分分析输出：`n500_unified.json`/`.csv` (10:08，仅含 s015/s020 数据)

### 5. 潜在问题

1. **s030 × 4 条件数据缺失** — 全部空目录，距 s025 完成已过 ~1.5h，需确认实验是否还在跑
2. **LaTeX 输出 bug** — `analyze_n500_unified.py:442` `latex_output()` 对 random 条件缺少 `median_ii_diff_ci` 键，需修复后才能生成完整 LaTeX 表格
3. **无法确认进程状态** — `screen -ls` 受 ssh_read_only 限制无法执行，建议用 ssh_execute 检查 `screen -ls` 或 `ps aux | grep profil`

---
