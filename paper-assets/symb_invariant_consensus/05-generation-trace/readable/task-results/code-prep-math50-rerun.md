# code prep math50 rerun

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep-math50-rerun_20260515T130326_result.json`
- **Structured JSON:** [`472e52f4cc313a34b826.json`](../../sessions/47/472e52f4cc313a34b826.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**参数列表**（`run_full_mvp.py`）：`--mode`, `--k`, `--model`, `--api-base`, `--api-key`, `--math-data`, `--pw-data`, `--output`, `--resume`, `--temperature`, `--max-tokens`, `--no-proofwriter`

**数据集验证**：`math500_subset.json` — 50 题，levels 1-5，6 题 solution 含 Asymptote 图形代码（problem 本身不需要看图，不影响评测）

**脚本**：`/root/symb_invariant_consensus/run_math50_fixed.sh` 已创建，`chmod +x` 就绪。AIME 完成后执行：
```bash
nohup bash /root/symb_invariant_consensus/run_math50_fixed.sh > /tmp/math50_fixed.log 2>&1 &
```

---
