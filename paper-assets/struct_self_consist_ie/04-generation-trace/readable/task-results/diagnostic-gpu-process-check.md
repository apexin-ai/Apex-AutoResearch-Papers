# diagnostic gpu process check

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnostic_gpu_process_check_20260515T154231_result.json`
- **Structured JSON:** [`eed4e953ca2f80d5217d.json`](../../sessions/ee/eed4e953ca2f80d5217d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 进程排查报告

### 1. GPU 全景 (nvidia-smi)

| GPU | 显存 | 利用率 | 进程 |
|-----|------|--------|------|
| 0 | 2MiB / 32607MiB | 0% | **空闲** |
| 1 | 2MiB / 32607MiB | 0% | **空闲** |
| 2 | 30230MiB / 32607MiB | 81% | PID 199584 (VLLM::EngineCore) |
| 3 | 30280MiB / 32607MiB | 83% | PID 199733 (VLLM::EngineCore) |

### 2. PID 197287 身份确认

**已不存在。** `ps -p 197287` 返回 exit code 1。该进程已自然退出。

### 3. 旧实验状态

| 实验 | PID | 状态 |
|------|-----|------|
| exp_017_llama_conll_n8_t07 | 195927 (cuda:0) | **已结束** |
| exp_lp_scierc_t07 | 196993 (cuda:1) | **已结束** |
| exp_re_scierc_seed123 | 199021 (cuda:2) | **运行中** |
| exp_re_scierc_seed456 | 199161 (cuda:3) | **运行中** |

### 4. GPU 2/3 进程链（已确认合法）

**GPU 2:**
```
PID 199021 (bash wrapper, exp_re_scierc_seed123)
 → PID 199026 (python run_mvp_pilot.py --seed 123)
   → PID 199584 (VLLM::EngineCore, 30220MiB)
```

**GPU 3:**
```
PID 199161 (bash wrapper, exp_re_scierc_seed456)
 → PID 199166 (python run_mvp_pilot.py --seed 456)
   → PID 199733 (VLLM::EngineCore, 30270MiB)
```

两个 vLLM 进程均为实验脚本 `run_mvp_pilot.py` 的子进程，完全合法。

### 5. tmux sessions

```
exp_011_ood_conll_to_scierc      (19:48) — 无 GPU 进程
exp_017_llama_conll_n16_r1024    (18:38) — 无 GPU 进程
exp_017_llama_conll_n16_s456_r1024 (18:38) — 无 GPU 进程
exp_re_scierc_seed123            (23:40) — 活跃, GPU 2
exp_re_scierc_seed456            (23:40) — 活跃, GPU 3
```

原先报告的 `exp_017_llama_conll_n8_t07` 和 `exp_lp_scierc_t07` tmux session 已不存在。

### 6. 结论

**PID 197287 大概率是 exp_lp_scierc_t07 (PID 196993) 在 cuda:1 上的 vLLM 子进程。** 该实验已结束，子进程随之自然退出。不是孤立进程，无需处理。

当前服务器无异常进程。GPU 0/1 空闲可用。

---
