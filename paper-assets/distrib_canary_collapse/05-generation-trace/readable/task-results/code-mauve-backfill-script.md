# code mauve backfill script

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mauve-backfill-script_20260523T172558_result.json`
- **Structured JSON:** [`8e8438cea83a46a770a5.json`](../../sessions/8e/8e8438cea83a46a770a5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

**脚本** `scripts/backfill_mauve.py` 已写入本地和远程 westd-17855。

**Dry-run 结果：**
- `t15_a050_s43_fp32_14b`：13 个 gen (gen_0–gen_12) mauve 为 null 需补算，gen_13 无 metrics.json
- `t15_a060_s43_fp32_14b`：0 个需补算，所有 gen 正确跳过

**HF_HOME 环境变量检查：**
- PID 749427 (t15_a060_s43)：已设置 `HF_HOME=/root/autodl-tmp/.hf_cache`
- PID 796624 (t10_a045_s44)：**未设置** — 确认了 mauve 缺失的根因

验证结果写入 `artifacts/_project/mauve_backfill_dryrun_20260523.md`。

---
