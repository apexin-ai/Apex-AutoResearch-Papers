# infra disk gpu check

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_disk-gpu-check_20260522T210748_result.json`
- **Structured JSON:** [`b3184a46921338bd9178.json`](../../sessions/b3/b3184a46921338bd9178.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总报告

### westd-16639

**磁盘：**
| 分区 | 容量 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| 根分区 `/` | 30G | 11G | 20G | 35% |
| 数据盘 `/root/autodl-tmp` | 350G | 230G | 121G | 66% |

- multi_seed 结果仅占 **142M**，不是磁盘问题根源
- 模型占大头（~170G）：Qwen2.5-72B-AWQ 39G, Qwen2.5-14B 28G, Mistral-7B 28G, Qwen3-14B 28G, phi-4-reasoning 25G, deepseek-r1-qwen3-8b 16G, LLaMA-8B 15G, deepseek-ai 15G 等

**GPU（4× RTX PRO 6000 Blackwell 96GB）— 全部在用：**
| GPU | 显存占用 | 利用率 | 运行内容 |
|-----|----------|--------|----------|
| 0 | 88/97 GB | 97% | vLLM Qwen2.5-14B (port 8001) → qwen25_pw_seed456 |
| 1 | 88/97 GB | 96% | vLLM LLaMA-8B (port 8006) → llama8b_pw_seed123 |
| 2 | 90/97 GB | 96% | vLLM Mistral-7B (port 8003) → mistral_pw_seed789 |
| 3 | 88/97 GB | 97% | vLLM Qwen2.5-14B (port 8005) → qwen25_pw_seed123 |

**关键进程状态：**
- PID 510987（Mistral PW multi-seed runner）— **存活**，seed789 正在跑
- PID 552333（Qwen PW multi-seed）— **已死**，但已被新进程替代（GPU0 跑 seed456，GPU3 跑 seed123 rerun）
- **与预期不符：cuda:1 和 cuda:3 并非空闲，已被重新部署了 LLaMA-8B 和 Qwen2.5-14B 实验**

---

### westd-14391

**磁盘：**
| 分区 | 容量 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| 根分区 `/` | 30G | 13G | 18G | 41% |
| 数据盘 `/root/autodl-tmp` | 250G | 26G | 225G | 11% |

**GPU（1× RTX PRO 6000 Blackwell 96GB）— 在用：**
| GPU | 显存占用 | 利用率 | 运行内容 |
|-----|----------|--------|----------|
| 0 | 88/97 GB | 100% | vLLM LLaMA-8B (port 8000) → llama8b_pw_seed42 + run_after_folio.sh |

- 项目目录已存在，代码完整
- 有 3 个 ModelScope 下载进程在后台（下载 LLaMA-3.1-8B，可能是重复的）
- 磁盘非常充裕（225G 可用）

---

### 建议

1. **westd-16639 磁盘暂时没问题**（根分区 35%，数据盘 66%），之前的磁盘满可能是临时文件或日志导致的，已恢复。4 张 GPU 全部在跑多种子实验，不需要干预。

2. **westd-14391 不适合转移**——只有 1 张 GPU 且已在用。如果要在这台跑更多实验，需要等当前任务完成。

3. **当前最优策略：不动**。westd-16639 的 4 张 GPU 都在跑 PW 多种子实验，等它们自然完成即可。如果需要清理磁盘腾空间，可以考虑删除不再需要的模型（如 Qwen2.5-72B-AWQ 39G、phi-4-reasoning 25G、Qwen3-14B 28G），能释放 ~92G。

---
