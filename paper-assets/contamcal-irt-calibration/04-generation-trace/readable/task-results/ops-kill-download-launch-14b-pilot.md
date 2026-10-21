# ops kill download launch 14b pilot

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-download-launch-14b-pilot_20260518T130433_result.json`
- **Structured JSON:** [`0f64d386d04106cfd661.json`](../../sessions/0f/0f64d386d04106cfd661.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

| 项目 | 结果 |
|---|---|
| kill 28638 | 成功终止 |
| 14B 模型完整性 | 8 个 safetensors, 28GB, config.json 存在 |
| 新训练 PID | **28900** (cuda:2, CUDA_VISIBLE_DEVICES=2) |
| LoRA 配置 | r=16, alpha=32 (符合规范) |
| cuda:2 显存 | 559MiB（tokenize 阶段，完成后会增长到 ~30-40GB） |

**全卡状态：**
| GPU | 显存 | Util | 进程 |
|---|---|---|---|
| cuda:0 | 69647/97887 MiB | 89% | PID 23304 |
| cuda:1 | 17713/97887 MiB | 91% | PID 25326 |
| cuda:2 | 559/97887 MiB | 0% | PID 28900 (14B pilot, tokenizing) |
| cuda:3 | 0/97887 MiB | 100% | 无进程（util 100% 可能是刚结束的任务残留） |

训练正在 tokenize 50K 样本（当前 ~40%），完成后开始正式训练，显存会大幅增长。

---
