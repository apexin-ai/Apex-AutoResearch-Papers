# code exp008 signal survival

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp008_signal_survival_20260514T040430_result.json`
- **Structured JSON:** [`5758b961232e1b672cc1.json`](../../sessions/57/5758b961232e1b672cc1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部通过。创建的文件和验证结果：

**文件（`/root/contamcal-irt-calibration/exp008/`）：**

| 文件 | 用途 |
|------|------|
| `signal_survival_analysis.py` | 核心分析：Cohen's d、Spearman ρ、AUROC、Wilcoxon 检验 |
| `run_signal_survival.py` | 端到端执行：加载 signal JSON → 分析 → 报告 |
| `plot_survival.py` | 可视化：AUC 对比柱状图 + signal decay 散点图 |

**dry-run 结果（`--dry-run --max-items 10`）：**
- 4/4 signals 正常计算，summary table 输出正确
- `survival_report.json` (1.9KB)、`survival_auc_comparison.pdf` (16KB)、`signal_decay_scatter.pdf` (23KB) 均已生成
- 无报错，无 GPU 依赖

**实际使用时的命令：**
```bash
python run_signal_survival.py \
  --sft-signals-dir /path/to/sft_signals/ \
  --rl-signals-dir /path/to/rl_signals/ \
  --labels-file /path/to/labels.json \
  --output-dir /root/contamcal-irt-calibration/outputs/exp008/
```

---
