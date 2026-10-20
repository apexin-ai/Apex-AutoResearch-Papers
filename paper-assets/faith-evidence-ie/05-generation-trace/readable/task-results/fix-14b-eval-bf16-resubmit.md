# fix 14b eval bf16 resubmit

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_14b_eval_bf16_resubmit_20260519T085020_result.json`
- **Structured JSON:** [`6e4f94514c06faa496b2.json`](../../sessions/6e/6e4f94514c06faa496b2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 eval 正常运行，无 OOM：

| 实验 | exp_id | PID (python) | GPU | 显存占用 |
|---|---|---|---|---|
| 14B SFT eval | `plan017_14b_sft_eval_r2` | 633119 | cuda:1 | 30760 MiB / 32607 MiB |
| 14B no-evidence eval | `plan017_14b_sft_no_evidence_eval_r2` | 633203 | cuda:2 | 30866 MiB / 32607 MiB |

**汇报：**

- **脚本修改**：两个脚本均已 `--quantize` → `--no-quantize`，`--batch_size 4` → `--batch_size 2`
- **PID**：SFT eval = 633106 (tmux) / 633119 (python)，no-evidence eval = 633190 (tmux) / 633203 (python)
- **GPU 显存**：cuda:1 30760 MiB，cuda:2 30866 MiB（总 32607 MiB，headroom ~1.8GB）
- **OOM**：未发生，batch_size=2 下 14B bf16 单卡可行，但余量极小
- **Cron 监控**：两个实验均已注册

---
