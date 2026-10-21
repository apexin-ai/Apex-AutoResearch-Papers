# code cwm error mode analysis script

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cwm-error-mode-analysis-script_20260514T162722_result.json`
- **Structured JSON:** [`e72f27907a1eb0a8b678.json`](../../sessions/e7/e72f27907a1eb0a8b678.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本运行成功。关键发现：

**CWM v10 (max_new_tokens=64) 的问题根源**：
- **93% unparseable** — 生成的执行 trace 太短（只有 ~251 chars），没有 pass/fail 关键词，全被归为 majority class
- Parseable-only accuracy 仅 28.15%，490 个 parseable 错误全是 false negative (pass→fail)
- 实际分类能力几乎为零，accuracy 69.91% 全靠 majority fallback

**CWM vs CLS 8B 对比**：
- 互补性不错：49% 都对，21% CWM 独对，21% CLS 独对
- CWM 独有错误 2079 个中 97% 是 unparseable（label=fail 的样本被 majority fallback 误判为 pass）

正在跑的两个 eval（max_new_tokens=1024）running acc 57-59%，已到 ~89%，预计 1-2 小时完成。那时用同一脚本分析会更有意义——unparseable 率应该大幅下降，能看到真正的分类错误模式。

脚本位于 `/home/sonny/exec-sim-repair-verifier/analyze_cwm_errors.py`，eval 完成后运行：
```bash
python3 analyze_cwm_errors.py \
  --cwm_results /root/autodl-tmp/results/repo_cwm_seed123_conda_eval/eval_repo_cwm_predictions.jsonl \
  --cls_results /root/autodl-tmp/results/repo_cls_8b_conda_eval/eval_repo_cls_predictions.jsonl \
  --output_dir /root/autodl-tmp/results/repo_cwm_seed123_conda_eval/
```

---
