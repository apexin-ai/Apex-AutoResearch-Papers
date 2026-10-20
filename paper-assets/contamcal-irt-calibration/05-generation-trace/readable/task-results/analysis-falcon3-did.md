# analysis falcon3 did

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_falcon3-did_20260522T172610_result.json`
- **Structured JSON:** [`f15ea6dca2fd792bc21d.json`](../../sessions/f1/f15ea6dca2fd792bc21d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出：

1. **`artifacts/falcon3_did_analysis.py`** — 独立 DiD 计算脚本，方法与 `treated_untreated_analysis.py` 完全一致（10,000 bootstrap, seed=42, 同样的 verdict 分类逻辑）

2. **`artifacts/falcon3_did_analysis.md`** — 文档含运行命令、Table 3 格式参考、预期结果预判

**状态: BLOCKED** — DiD 需要 item-level `correctness_matrix.json`（14,042 个 MMLU 题的逐题对/错），无法从 aggregate accuracy 计算。westd-29999 SSH 认证失败，cqa1-21977 不在 SSH config 中。

**恢复后执行：**
```bash
python artifacts/falcon3_did_analysis.py \
    --sft-dir /root/autodl-tmp/exp001/sft_data \
    --eval-dir /root/autodl-tmp/exp001/eval_results
```

脚本会直接输出 Table 3 的 LaTeX 行和完整 JSON。基于 Falcon3 的 Benefit pattern（d025 +2.46pp），预期 DiD 为 ns，verdict 大概率是 generalization。

---
