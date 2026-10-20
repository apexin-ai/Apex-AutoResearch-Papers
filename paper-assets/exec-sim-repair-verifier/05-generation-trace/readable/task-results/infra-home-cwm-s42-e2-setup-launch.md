# infra home cwm s42 e2 setup launch

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_home-cwm-s42-e2-setup-launch_20260518T144853_result.json`
- **Structured JSON:** [`459a744f30e5c75c20f7.json`](../../sessions/45/459a744f30e5c75c20f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 启动成功。汇总：

| 项目 | 状态 |
|------|------|
| Home GPU | RTX 5090, 15535MiB/32607MiB, 87% util |
| eval_repo_cwm.py | md5 一致 (04a6907...) |
| Checkpoint | 6 文件, adapter_model.safetensors 67MB |
| adapter_config.json | `base_model_name_or_path` → `deepseek-ai/deepseek-coder-6.7b-instruct` |
| 数据 | swebench_test.jsonl, 9784 条 |
| PID | 4141145 |
| tmux session | `cwm-s42-e2-home` |
| 参数确认 | `max_seq_length=2048`, family=deepseek, stop tokens=[32021, 32014] |
| 首行 log | 3/9784, running_acc=33.3%, ~8s/sample |

预估总时间 ~22h（9784 samples × ~8s）。

---
