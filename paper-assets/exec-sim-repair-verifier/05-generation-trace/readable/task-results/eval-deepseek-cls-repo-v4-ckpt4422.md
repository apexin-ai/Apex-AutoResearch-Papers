# eval deepseek cls repo v4 ckpt4422

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_deepseek-cls-repo-v4-ckpt4422_20260517T161113_result.json`
- **Structured JSON:** [`564e4cf57b01f4a2ed73.json`](../../sessions/56/564e4cf57b01f4a2ed73.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三项任务全部完成。汇报：

---

## 任务 1: cls-repo-v4 eval ✅ 已启动

- tmux session: `cls-repo-v4-eval`
- GPU 0: 26947 MiB 占用，推理中
- 进度: 80/9784, running_acc = **75.0%**（早期，不稳定）
- checkpoint: `/root/autodl-tmp/checkpoints_deepseek_cls_repo_v4/checkpoint-4422`
- 注: 无 conda 环境，用系统 python3 直接运行

## 任务 2: cls-repo-s123 最终结果 ✅ 已完成

| 指标 | 值 |
|------|-----|
| **Accuracy** | **82.62%** |
| Majority baseline | 72.96% |
| Gap vs majority | +9.67pp |
| F1 macro | 71.35% |
| F1 (fail) | 53.37% (P=97.3%, R=36.77%) |
| F1 (pass) | 89.32% (P=80.95%, R=99.62%) |
| Unparseable | 2796/9784 (28.6%) |
| Checkpoint | `/root/autodl-tmp/checkpoints_deepseek_cls_repo_s123/best` |
| Test instances | 9784 |

## 任务 3: cwm-repo s42 eval 进度

- 44/9784 (~0.4%)，running_acc = **75.0%**
- 速度: ~13s/sample（batch_size=1, max_seq_length=8192）
- 预计完成: ~35 小时
- GPU 1: PID 660618, 16483 MiB

---
