# diag exp 068 gpu check

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_exp-068-gpu-check_20260519T120032_result.json`
- **Structured JSON:** [`9cc732cde80498ef2940.json`](../../sessions/9c/9cc732cde80498ef2940.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

### exp-068 状态

**正在运行**，位于 **westd-16639 GPU 1**。
- 模型：Qwen3-14B，vLLM port 8001
- 进度：**87/200** (43.5%)
- ETA：约 63 分钟（日志显示 114 remaining samples）
- 最后活跃时间：20:00:52（实时写入中）
- registry 标记 RUNNING 是正确的，`get_project_resource_usage` 未显示是因为它可能没追踪到 westd-16639 上的进程。

---

### GPU 全景表

#### westd-25068（4× RTX PRO 6000 Blackwell）— 全部满载

| GPU | vLLM 模型 | Port | 实验 | 进度 |
|-----|-----------|------|------|------|
| 0 | Qwen2.5-7B-Instruct | 8010 | exp-065 | 333/600 (55.5%) |
| 1 | Mistral-7B-Instruct-v0.3 | 8001 | exp-069 | 25/200 (12.5%) |
| 2 | Qwen2.5-7B-Instruct | 8002 | exp-070 | 14/200 (7%) |
| 3 | gemma-3-27b-it | 8003 | exp-062 | 101/204 (49.5%) |

#### westd-16639（4× RTX PRO 6000 Blackwell）

| GPU | vLLM 模型 | Port | 实验 | 进度 |
|-----|-----------|------|------|------|
| 0 | Meta-Llama-3.1-8B-Instruct | 8005 | **孤儿进程**（exp069 dry-run 残留，无 runner 使用） | N/A |
| 1 | Qwen3-14B | 8001 | **exp-068** | 87/200 (43.5%) |
| 2 | deepseek-r1-0528-qwen3-8b | 8002 | exp-064 | 69/204 (33.8%) |
| 3 | Meta-Llama-3.1-8B-Instruct | 8003 | exp-048 | 448/600 (74.7%) |

注：exp-048 有 context length 400 错误（8192 token 上限被触发），但仍在跑。

---

### 空闲 GPU

**无完全空闲 GPU。** 但 westd-16639 GPU 0 上有一个孤儿 vLLM 进程（PID 148803, port 8005），是 exp-069 dry-run 残留，没有实验 runner 在使用它。杀掉后 GPU 0 即可释放。

---
