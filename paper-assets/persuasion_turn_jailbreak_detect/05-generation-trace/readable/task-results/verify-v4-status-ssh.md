# verify v4 status ssh

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_v4-status-ssh_20260517T152554_result.json`
- **Structured JSON:** [`9162b1355db8315494e7.json`](../../sessions/91/9162b1355db8315494e7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 当前进程
- **`generate_benign_v4b.py test20` (iter2)** 正在运行（PID 66247，启动于 23:15，CPU 145%）
- 进度：**12/20 完成**（benign_v4b_iter2_test20.jsonl 当前 11 行，第 12 条正在生成）
- 每条对话约 40-100 秒，预计剩余 ~8 条需 6-10 分钟

### V4 Benign 数据文件

| 文件 | 行数 | 大小 |
|------|------|------|
| `benign_v4_test20.jsonl` | 20 | 466 KB |
| `benign_v4b_test20.jsonl` | 20 | 444 KB |
| `benign_v4b_iter2_test20.jsonl` | 11 (生成中) | 226 KB |

- 最新生成的条目：`conv_id=benign_v4b_0011`, register=casual, goal="law enforcement evasion technique study for policy research", 6 turns

### Sanity Check 结果 (`sanity_v4b_results.json`)
- **TF-IDF F1**: 0.887 (std=0.169)
- **Pass**: ❌ `false`
- **Register 分布**: casual=8, personal=4, formal=8
- **Top jailbreak words**: some, you, hey, just, him, someone, but, could, to, if
- **Top benign words**: do, so, how, training, does, our, also, behavioral, ensure, malware

Sanity check 未通过——TF-IDF 仍能以 ~89% F1 区分 jailbreak 和 v4b benign 数据。`iter2` 可能是修复此问题的第二次迭代尝试。

### GPU 使用
| GPU | 利用率 | 显存占用 |
|-----|--------|----------|
| 0 | 88% | 19013 MiB |
| 1 | 0% | 17649 MiB |
| 2 | 0% | 3 MiB |
| 3 | 0% | 3 MiB |

GPU 0 活跃生成中，GPU 1 已加载 target model（Qwen2.5-7B-Instruct）但当前 idle。符合约束 C001（仅使用 cuda:0-3）。

---
