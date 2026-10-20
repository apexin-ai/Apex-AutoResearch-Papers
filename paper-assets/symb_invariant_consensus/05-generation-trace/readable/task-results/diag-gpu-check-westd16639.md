# diag gpu check westd16639

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_gpu-check-westd16639_20260519T043257_result.json`
- **Structured JSON:** [`27cfddda39010e7a46ce.json`](../../sessions/27/27cfddda39010e7a46ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-16639 GPU 状态

| GPU | 预期实验 | 实际实验 | PID | 进度 | ETA | 备注 |
|-----|---------|---------|-----|------|-----|------|
| cuda:0 | exp-039 Qwen2.5-14B | **exp-032** Qwen2.5-14B-Instruct PW-600 | 6584 (vLLM) / 7244 (run) | **590/600** | ~12 min | 即将完成 |
| cuda:1 | exp-040 Qwen3 | **exp-033** Qwen3-14B PW-600 (non-thinking) | 7589 (vLLM) / 8432 (run) | **375/600** | ~390 min (~6.5h) | 正常运行，avg 103.6s/prob |
| cuda:2 | exp-028b resume | **exp-028b** Qwen3-14B thinking FOLIO remaining 38 | 91144 (vLLM) / 92739 (run) | **9/38** | ~83 min (~1.4h) | 正常运行，avg 165.2s/prob |
| cuda:3 | exp-048 LLaMA-8B | **exp-048** LLaMA-3.1-8B-Instruct PW-600 | 76474 (vLLM) / 77064 (run) | **104/600** | ~640 min (~10.7h) | **有 context length 溢出错误** |

**磁盘**: 30G 总量，13G 已用，18G 可用 (44%) — 充足

**vLLM 进程**: 4 个，分别在 port 8000/8001/8002/8003，全部活跃

**tmux sessions**: exp032, exp033, exp028b_vllm, exp028b_run, exp048_vllm, exp048_run (共 6 个)

---

### 关键发现

1. **cuda:0/cuda:1 实验名不匹配预期**: 实际跑的是 exp-032/exp-033，不是 exp-039/exp-040。模型相同（Qwen2.5-14B / Qwen3-14B），任务相同（PW-600），但实验编号不同。

2. **exp-048 (cuda:3) 有 context length 溢出问题**: LLaMA-8B max-model-len=8192，当 input prompt >= 4097 tokens 时，加上 max-tokens=4096 会超限。日志显示 retry 2/2 后仍 400 Bad Request，这些题会失败跳过。按当前速度还需约 10.7 小时。

3. **exp-032 (cuda:0) 即将完成**: 仅剩 11 题，约 12 分钟后完成。**cuda:0 即将空闲，需安排下一个实验。**

4. **4 GPU 全部满载运行**，GPU-Util 97-100%，无空转。

---
