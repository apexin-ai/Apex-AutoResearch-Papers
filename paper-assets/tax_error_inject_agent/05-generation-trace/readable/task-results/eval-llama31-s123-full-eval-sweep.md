# eval llama31 s123 full eval sweep

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_llama31-s123-full-eval-sweep_20260516T142140_result.json`
- **Structured JSON:** [`eb8cf5ca63f51470b4f7.json`](../../sessions/eb/eb8cf5ca63f51470b4f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**当前进展汇总：**

### Step 1-2: 训练状态
| 训练 | 状态 | Checkpoint | Loss |
|------|------|-----------|------|
| vanilla-s123 | ✅ DONE | checkpoint-1635 | 0.400 (final 0.254) |
| taxei-s123 | 🔄 训练中 70% | checkpoint-2258 (2 of 3 epochs) | ~0.27 |
| random-s123 | 🔄 训练中 70% | checkpoint-2258 (2 of 3 epochs) | ~0.27 |

### Step 3: Qwen Random Recovery 结果
| Seed | Recovery Rate |
|------|--------------|
| default | 0.638 |
| s0 | 0.553 |
| s1 | 0.511 |
| s123 | 0.660 |
| s7 | 🔄 运行中 (35/47) |
| s42 | ❌ 未找到 |

### 当前 GPU 分配
| GPU | 进程 | 进度 | ETA |
|-----|-------|------|-----|
| 0 | Qwen random recovery s7 | 35/47 | ~10 min |
| 1 | vanilla-s123 clean eval | 19/47 | ~20 min |
| 2 | taxei-s123 训练 | 2387/3387 | ~35 min |
| 3 | random-s123 训练 | 2387/3387 | ~35 min |

4 分钟后轮询检查 GPU 0 是否空闲，届时启动 vanilla-s123 injected eval。

---
