# prep cross alpha 5pt script

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_cross-alpha-5pt-script_20260515T120307_result.json`
- **Structured JSON:** [`80f6769c1869e6ab455f.json`](../../sessions/80/80f6769c1869e6ab455f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部检查完成，汇总如下：

## 检查结果

### 1. 脚本状态
`cross_alpha_analysis_v4.py` — 34714 bytes, 最后更新 2026-05-15 17:16 ✅

### 2. 数据完整性

| α 点 | all_metrics.json | 状态 |
|------|-----------------|------|
| a000_s42 (α=0.0) | ✅ | 完整 |
| a025_s42 (α=0.25) | ✅ | 完整 |
| a050_s42 (α=0.5) | ✅ | 完整 |
| a075_s42 (α=0.75) | ❌ | **未完成** |
| MVP (α=1.0) | ✅ 4 seeds (rep_42..45) | 完整 |

### 3. a075 进度
- 9 个 generation 目录 (gen_0..gen_8)
- 8/9 有 `metrics.json` (gen_0..gen_7 完成)
- **gen_8 目录为空** — 正在运行或待运行
- 训练日志显示 padding warnings（仍在推理阶段）
- 阻塞项：gen_8 完成后还需生成 `all_metrics.json`

### 4. Dry-run 结果
Import 成功 ✅。Auto-discovery 正确识别全部 5 个 α 点（含 a075）。注意：a075 虽然被 discover 了，但因缺少 `all_metrics.json`，实际运行时会在加载阶段失败。

### 5. 最终执行命令
a075 数据就绪后执行：
```bash
cd /root/autodl-tmp/distrib_canary_collapse && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python cross_alpha_analysis_v4.py --n-perms 5000 --consensus-n-perms 1000 --update-registry
```

**结论**：脚本就绪，4/5 α 点数据完整，唯一阻塞是 a075_s42 的 gen_8 + all_metrics 聚合。

---
