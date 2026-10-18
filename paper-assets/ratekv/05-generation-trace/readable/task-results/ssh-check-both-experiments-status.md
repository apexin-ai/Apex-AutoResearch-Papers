# ssh check both experiments status

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_both_experiments_status_20260516T023201_result.json`
- **Structured JSON:** [`589d4ca4fd0a9d43cb67.json`](../../sessions/58/589d4ca4fd0a9d43cb67.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
GPU 状态：
  GPU 0: RTX PRO 6000 Blackwell, 23179 MiB, 100%  ← InternLM2 运行中
  GPU 1: RTX PRO 6000 Blackwell, 3 MiB, 0%        ← 空闲

InternLM2 profiling:
  进程状态：运行中 (PID 389862)
  进度：176/256 heads (68.8%), elapsed 39.8min, ETA ~18min
  当前位置：Layer 21, Head 7

Phi-3-medium MCKP:
  进程状态：已完成 ✓
  Profiling: 400/400 heads, 149.0min
  concentration = 0.1742, 分类 = Flat (< 0.50)
  t1/t5 = 0.1806 / 0.7700 = 0.234

  PPL 结果：
    bf16:               5.6359
    uniform-4bit:       5.7987  (Δ +0.163)
    constrained MCKP:   5.8149  (Δ +0.179)
    unconstrained MCKP: 6.0730  (Δ +0.437)
    greedy:             6.0730  (Δ +0.437)

  constrained vs uniform: -0.016 (constrained 略差于 uniform)
  bit分布 (constrained): 388×4bit, 8×2bit, 4×8bit

  产出文件：
    /root/ratekv/artifacts/phi3_medium_profiles_hires.json
    /root/ratekv/artifacts/phi3_medium_constrained_results.json
    /root/ratekv/artifacts/phi3_medium_hires_bf16_2bitonly_results.json
```

Phi-3-medium 的 Flat profile 符合预期——concentration 仅 0.17，敏感度分散，constrained MCKP 无法优于 uniform，反而略差 0.016。InternLM2 预计约 18 分钟后完成。

---
