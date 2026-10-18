# code 340m eval script fix

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_340m-eval-script-fix_20260521T222448_result.json`
- **Structured JSON:** [`b21e575403bc2337cc00.json`](../../sessions/b2/b21e575403bc2337cc00.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。汇报如下：

---

### 1. 模型路径

模型在 `/root/entrainment_gated_ft/models/`（两个目录都有，脚本使用项目目录）。15 个模型全部确认存在：

| Arch | pure | h24-1 | h12-1 | h6-1 | h3-1 |
|------|------|-------|-------|------|------|
| GDN | `*-pure-baseline` | `*-New-hybrid-24-1` | `*-hybrid-12-1` | `*-hybrid-6-1` | `*-hybrid-3-1` |
| RetNet | `*-pure` | `*-hybrid-24-1` | `*-hybrid-12-1` | `*-hybrid-6-1` | `*-hybrid-3-1` |
| HGRN2 | `*-pure-baseline` | `*-hybrid-24-1` | `*-hybrid-12-1` | `*-hybrid-6-1` | `*-hybrid-3-1` |

### 2. 脚本位置

`/root/entrainment_gated_ft/run_340m_multi_eval.sh`

- 15 个模型，associative array 映射 SHORT_NAME → 目录名
- 固定遍历顺序：GDN 5 → RetNet 5 → HGRN2 5
- 跳过逻辑：`output_dir/samples/` 下 ≥3 个 `.jsonl` 文件则跳过
- `--log_samples` 已加
- `--device cuda:0`
- 每个模型前后打印时间戳

### 3. 验证结果

| 检查项 | 结果 |
|--------|------|
| `bash -n` 语法检查 | SYNTAX_OK |
| `run_lmeval_clean.py --help` | 确认支持 `--model_path`, `--tasks`, `--output_dir`, `--batch_size`, `--device`, `--log_samples` |
| 3 个 pure 模型 config.json | 全部存在 |

脚本就绪，可直接用 `nohup bash /root/entrainment_gated_ft/run_340m_multi_eval.sh > /tmp/eval_340m_multi.log 2>&1 &` 启动。

---
