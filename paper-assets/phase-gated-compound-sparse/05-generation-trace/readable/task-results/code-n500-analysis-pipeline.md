# code n500 analysis pipeline

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_n500_analysis_pipeline_20260514T204318_result.json`
- **Structured JSON:** [`cb8d535d556eb8176f3e.json`](../../sessions/cb/cb8d535d556eb8176f3e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 完成

**脚本**：`/root/autodl-tmp/pacs/analyze_n500_unified.py`

**功能**：
| 模块 | 说明 |
|------|------|
| Median II + CI | 每个 condition 的 `ii_low - ii_high` 差值中位数 + 1000 resample percentile bootstrap CI |
| Within-strategy d_z | 同 masking 不同 sparsity 之间的 paired Cohen's d_z（s015↔s020, s020↔s025, s025↔s030, s015↔s030） |
| Dose-response | Spearman ρ + 5000 次 permutation test（sparsity 递增 → II 单调性） |
| 输出 | JSON + 可选 CSV（`--csv`） |

**使用命令**：
```bash
# 全量 n=500（实验全部完成后）
python analyze_n500_unified.py --model all --csv

# 单模型
python analyze_n500_unified.py --model deepseek

# 用 n=50 数据验证
python analyze_n500_unified.py --model all --dry-run --csv
```

**Dry-run 结果**（n=50）：
- DeepSeek imp: 所有 4 个 sparsity 的 median II diff CI 排除 0，dose-response ρ=1.0 (p=0.042)
- Qwen imp: 同上，d_z 从 small (s015→s020) 到 large (s015→s030) 单调递增
- Random 条件：CI 多数跨 0，d_z negligible/small — 符合预期

**当前状态**：n=500 只有 s015 完成，s020~s030 仍在运行。脚本自动跳过缺失条件，实验完成后直接一键执行即可。

---
