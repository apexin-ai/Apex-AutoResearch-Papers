# analysis cross alpha prep

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cross_alpha_prep_20260515T121153_result.json`
- **Structured JSON:** [`f23340e375666a9544b4.json`](../../sessions/f2/f23340e375666a9544b4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4-point dry-run 成功，输出已保存。下面是完整就绪状态报告。

---

## 就绪状态报告

### 脚本状态：**Ready，无需修改**

`cross_alpha_analysis_v4.py` 自动发现机制完全动态——glob `results/alpha_sweep/a*_s42`，自动加 MVP 作为 α=1.0。a075_s42 的 `all_metrics.json` 生成后会被自动识别。

**唯一风险**：自动发现模式下，a075_s42 目录已存在但无 `all_metrics.json` 时脚本会崩溃（`FileNotFoundError`）。解决方案：用 `--alpha-dirs` 显式指定，或等 a075 完全结束。

### 数据完整性

| α 点 | 路径 | all_metrics.json | generations | 状态 |
|------|------|-----------------|-------------|------|
| 0.00 | alpha_sweep/a000_s42 | ✓ | 11 (gen 0-10) | 完成 |
| 0.25 | alpha_sweep/a025_s42 | ✓ | 11 (gen 0-10) | 完成 |
| 0.50 | alpha_sweep/a050_s42 | ✓ | 11 (gen 0-10) | 完成 |
| 0.75 | alpha_sweep/a075_s42 | ✗ | gen_8 进行中 | **运行中** |
| 1.00 | mvp/rep_42..45 | ✓ (4 seeds) | 11 (gen 0-10) | 完成 |

a075_s42 已到 gen_8/10，预计 ~1-2h 内完成（不是任务描述说的 3-4h）。

### 4-point dry-run 结果验证

执行成功（7.8s），关键结论与之前一致：
- **FDR**: 10/32 raw-sig → **1/32 FDR-sig**（ECE→d1 在 α=1.0，p_fdr=0.0192）
- **非单调 dose-response 确认**：d1 drift α=0.25 (-40.3%) > α=0.50 (-37.3%) > α=1.0 (-28.3%)
- **Consensus**: α=0.0 → 0/16 robust, α=0.25 → 1/16, α=0.50 → 0/16, α=1.0 → 6/16 robust
- **6 个 regime-dependent pairs** 全是 canary→downstream 方向（entropy/ece → d1/d2/d3），仅在 α=1.0 robust
- 输出已保存为 `cross_alpha_v5.json` + `cross_alpha_v5_report.md`

### a075 数据到位后的精确执行命令

**自动发现（推荐，等 a075 完全结束后）：**
```bash
cd /root/autodl-tmp/distrib_canary_collapse
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
python cross_alpha_analysis_v4.py --version 6
```

**显式指定（更安全）：**
```bash
python cross_alpha_analysis_v4.py --alpha-dirs a000_s42 a025_s42 a050_s42 a075_s42 mvp --version 6
```

---
