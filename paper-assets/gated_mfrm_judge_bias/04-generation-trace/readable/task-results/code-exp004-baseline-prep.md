# code exp004 baseline prep

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp004_baseline_prep_20260522T163502_result.json`
- **Structured JSON:** [`fbd79ca4455fc536c9ee.json`](../../sessions/fb/fbd79ca4455fc536c9ee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部通过。nanmean 的 warning 是合成数据稀疏导致的，正常数据不会触发。

---

## 产出总结

### 1. Baseline 调研

| # | 方法 | 论文 | 代码 | 核心算法 |
|---|------|------|------|----------|
| 4 | **CyclicJudge** | Zhu et al., arXiv:2603.01865 | 无公开代码 | 方差分解 (scenario/generation/judge/residual) → round-robin 分配 judge 到 item，每 judge 只评一次/cycle，消除系统性偏差 |
| 5 | **CyclicJudge+discard** | 4 的变体 | — | CyclicJudge + 丢弃 exposure > threshold 的 item |
| 6 | **DCR Factor** | Xu et al., EMNLP 2025 ([ACL Anthology](https://aclanthology.org/2025.emnlp-main.1173/)) | [github.com/chengxuphd/dcr](https://github.com/chengxuphd/dcr) | 4 级污染信号 (semantic/information/data/label) → Mamdani fuzzy inference → DCR factor ∈ [0,1] 折扣 raw accuracy |
| 7 | **UDA** | AAAI 2026 ([arXiv:2508.09724](https://arxiv.org/abs/2508.09724)) | anonymous.4open.science/r/62AB93CD-23B4 | 学习 per-judge K-factor 缩放 → 最小化跨 judge Elo 轨迹离散度 → 共识 rating；简化版用 scipy.optimize 替代原文 neural net |
| 8 | **Preference Leakage** | Li et al., ICLR 2026 ([arXiv:2502.01534](https://arxiv.org/abs/2502.01534)) | [github.com/David-Li0406/Preference-Leakage](https://github.com/David-Li0406/Preference-Leakage) | 计算 PLS(judge_i, judge_j) = judge 偏好泄露分数 → 从 raw score 减去 per-(judge,model) preference deviation 再聚合 |

### 2. exp-004 代码

- `/root/gated_mfrm_judge_bias/exp004/baselines.py` — 5 个 baseline 实现 (cyclic_judge, cyclic_judge_discard, dcr_factor, uda, pref_leakage)
- `/root/gated_mfrm_judge_bias/exp004/run_exp004.py` — 主入口，含完整评估 pipeline

运行命令（exp-003 完成后）:
```bash
cd /root/gated_mfrm_judge_bias/exp004
/root/miniconda3/bin/python3 run_exp004.py \
  --judgment-dir /root/gated_mfrm_judge_bias/exp001/results \
  --exposure-csv /root/gated_mfrm_judge_bias/exp002/results/exposure_scores.csv \
  --exp003-dir /root/gated_mfrm_judge_bias/exp003/output \
  --output-dir /root/gated_mfrm_judge_bias/exp004/results
```

如果 exp-003 output 不存在，加 `--skip-exp003` 会自动从头跑 4 个 MCMC 方法。

### 3. Dry-run

所有 import 和合成数据测试通过。

---
