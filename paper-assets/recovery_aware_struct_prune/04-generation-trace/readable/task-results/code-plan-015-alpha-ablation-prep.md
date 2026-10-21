# code plan 015 alpha ablation prep

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_015_alpha_ablation_prep_20260515T033556_result.json`
- **Structured JSON:** [`3e861d04b5184c23ceb6.json`](../../sessions/3e/3e861d04b5184c23ceb6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

代码已就绪。有一个磁盘空间风险需要注意：每个 pruned model 约 12GB，4 个新 α 值需要 ~48GB，但数据盘只剩 29GB。

## 产出报告

### 代码结构
| 文件 | 作用 |
|------|------|
| `src/prune.py` | 剪枝主逻辑，已支持 `--alpha` 参数（line 166），直接在 scoring 公式中使用 |
| `src/rasp_scoring.py` | RASP 评分：`S(h) = I(h) * (1-F(h))^alpha`，独立工具 |
| `src/eval_gsm8k.py` | GSM8K 评估，支持 `--max_samples` 控制样本数 |
| `src/run_alpha_ablation.sh` | **主脚本（仅 prune + eval）** α ∈ {0, 0.5, 1, 2, 4} |
| `scripts/run_alpha_ablation.sh` | 全流程版（prune → SFT → GRPO → eval）同步更新 |

### α 参数注入
**不需要改 prune.py**。`--alpha` 已原生支持，scoring 直接在 prune.py:202 计算：
```python
attn_scores[k] = attn_importance[k].float() * (1.0 - attn_overlap[k].float()).pow(args.alpha)
```

### CKA 分数
**已缓存**：`results/cka_scores.pt`（122KB），28 层 × 4 attn groups + 28 MLP groups。α sweep 只重新计算 scoring，不需重跑 CKA。

### 运行命令
```bash
# GRPO 完成后执行（仅 prune + GSM8K eval，无 SFT/GRPO）
CUDA_VISIBLE_DEVICES=0,1 bash src/run_alpha_ablation.sh

# 如果想快速验证（N=100 而非全量 1319），手动加 --max_samples 100
```

α=1.0 结果自动通过 symlink 复用 `/root/autodl-tmp/pruned_rasp_20`。

### 预估 GPU 时间
- 剪枝：每个 α ~2-3 min（加载模型 + 重排 + 剪枝 + 保存），4 个新 α 用 2 GPU 并行 ≈ **6 min**
- Eval：每个 α ~25-30 min（GSM8K full 1319 samples），5 个 α 用 2 GPU 并行 ≈ **75 min**
- **总计 ~80 min**

### ⚠️ 磁盘空间风险
数据盘剩余 29GB，每个 pruned model 12GB，4 个新 α 需要 ~48GB。**需要先清理旧文件**（如 `pruned_standard_20`、`pruned_standard_25`、`pruned_rasp_25` 等不再需要的模型），或改为顺序执行：prune → eval → 删除 pruned model → 下一个 α。

---
