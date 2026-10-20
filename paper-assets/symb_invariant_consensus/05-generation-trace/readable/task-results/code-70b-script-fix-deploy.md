# code 70b script fix deploy

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_70b-script-fix-deploy_20260518T065432_result.json`
- **Structured JSON:** [`4f72ce7392756b6f9076.json`](../../sessions/4f/4f72ce7392756b6f9076.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。结果汇总：

**脚本已部署到 westd-25068:**
- `/root/symb_invariant_consensus/scripts/run_exp024_llama70b.sh` (chmod +x, syntax OK)
- `/root/symb_invariant_consensus/scripts/run_exp025_qwen72b.sh` (chmod +x, syntax OK)

**exp024 修正项已确认：**
1. K=10 → **K=12** (line 33)
2. tensor-parallel-size=2 → **tensor-parallel-size=4** (line 81)，GPU 检查阈值也从 2 → 4
3. 注释更新为 **westd-25068, 4×GPU**

**项目代码未部署：** `/root/symb_invariant_consensus/` 目前只有 `scripts/` 目录。运行脚本前需要先将完整项目代码（sica/、baselines/、utils/、data/、run_full_mvp.py 等）同步到服务器。

**额外注意：** 脚本中调用的 `run_full_mvp.py` 使用了 `--temperature`、`--max-tokens`、`--seed`、`--folio-data`、`--save-intermediates` 等参数，这些在当前本地的 `run_full_mvp.py` 中尚未实现。部署项目代码时需要确保 `run_full_mvp.py` 已更新支持这些参数。

---
