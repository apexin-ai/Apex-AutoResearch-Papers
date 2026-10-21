# code westd val sweep prep

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_westd-val-sweep-prep_20260514T061513_result.json`
- **Structured JSON:** [`ef8337b757814af3ba9c.json`](../../sessions/ef/ef8337b757814af3ba9c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪。汇总：

**已完成的修改：**
- `eval_repo_cls.py` 添加了 `--split {val,test}` 参数（默认 test，向后兼容），数据路径自动切换为 `swebench_{split}.jsonl`，输出 JSON 包含 `split` 字段

**Dry-run 验证通过：**
- `--split val` 正确加载 9335 个 val 实例（pass: 7083, fail: 2252）

**可用 Checkpoints（全部确认存在）：**

| 模型 | Base | Checkpoints |
|------|------|------------|
| 8B | Qwen3-8B | checkpoint-{200,400,600} |
| v5-conda | Qwen3-4B | checkpoint-{200,400,600} |

**Sweep 脚本：** `/home/sonny/exec-sim-repair-verifier/run_westd_val_sweep.sh`
- 用法：`bash run_westd_val_sweep.sh &lt;gpu_id>`
- 依次跑 6 个 checkpoint 的 val eval，结果输出到 `val_eval_results_westd/`

---
