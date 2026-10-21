# code fix k2 mean evaluate

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-k2-mean-evaluate_20260523T065032_result.json`
- **Structured JSON:** [`95adf7f39556ac1cdd3e.json`](../../sessions/95/95adf7f39556ac1cdd3e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两台服务器修改一致，`args.K = 10` 强制覆盖已删除，仅保留 `args.K = 1`（single 模式）。

---

**报告：**

1. **Diff**：
   ```diff
    if args.mode == "vla_only":
        if args.baseline_mode == "single":
            args.K = 1
   -    elif args.baseline_mode == "mean":
   -        args.K = 10
    if args.output_file is None:
   ```

2. **`--K` argparse 默认值**：`default=10`（第 76 行），所以不指定 `--K` 时 mean baseline 仍用 K=10，指定 `--K 2` 则用 2。

3. **验证**：两台服务器 `grep -n "args.K"` 输出一致，仅第 813 行保留 `args.K = 1`（single 模式），无 `args.K = 10` 强制覆盖。

4. **同步状态**：bjb1-32546 和 bjb2-28827 均已完成相同修改。

---
