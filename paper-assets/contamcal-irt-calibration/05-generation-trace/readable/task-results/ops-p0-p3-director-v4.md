# ops P0 P3 director v4

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_P0-P3-director-v4_20260516T135144_result.json`
- **Structured JSON:** [`67bc86d8c901ef00a99f.json`](../../sessions/67/67bc86d8c901ef00a99f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报如下：

---

**P1 结果**: 
- Kill PID 784230 (3B d000_s123 重复进程) ✓ 已确认 DEAD
- Kill PID 785585 (Llama eval 旧进程) ✓ 已确认 DEAD
- nvidia-smi 确认每卡最多一个进程，无重复

**P0 结果**:
- 无错误脚本进程在运行，无需额外 kill
- 已删除 4 个无效域结果目录
- v4 进程启动成功：PID=789935 (python子进程), 父bash PID=789930
- 日志确认 MCMC 4 chains warmup→sampling 正常启动
- Registry 已更新为 RUNNING

**P2 结果**: Pooled IRT N=20+ 已成功完成，结果：

| Bench | N_mod | N_item | γ̂ | 95% CI | R̂ | ESS | PPP | rawMAE | calMAE | ΔMAE |
|-------|-------|--------|------|--------|------|-----|------|--------|--------|------|
| mmlu | 13 | 300 | 0.5502 | [-0.572, 1.709] | 1.006 | 1564 | 0.227 | 0.0140 | 0.0051 | **0.0089** |
| gsm8k | 21 | 300 | 0.3784 | [-0.100, 0.847] | 1.008 | 1476 | 0.105 | 0.1470 | 0.0119 | **0.1351** |
| arc_challenge | 13 | 300 | 0.8616 | [0.092, 1.630] | 1.007 | 1553 | 0.003 | 0.0324 | 0.0229 | **0.0094** |

注意：arc_challenge PPP=0.003 极低（模型拟合不佳），且用了 4PL+γ 但 N=13 < 16（违反 C008 规则）。gsm8k 校准改善最大（ΔMAE=0.135）。结果存于 `/root/autodl-tmp/exp006/results_pooled_n20`。

**P3 结果**: GPU 状态表

| GPU | 进程 PID | 显存 | 利用率 | 对应实验 |
|-----|---------|------|--------|---------|
| 0 | 780943 | 6902 MiB | 63% | signals 3B d000_s123 (mmlu s4) |
| 1 | 780591 | 1768 MiB | 30% | signals 0.5B-Instruct (mmlu s4) |
| 2 | 790124 | 7814 MiB | 86% | signals 3B d000_s123 (下一信号) |
| 3 | — | 0 MiB | 0% | 空闲 |
| 4 | 785955 | 8304 MiB | 87% | eval Llama-3.2-3B_d000_s42 |
| 5 | 786898 | 3650 MiB | 54% | eval Qwen2.5-1.5B-Instruct |

PID 存活检查：
- 760236 (signals_05B_s123_v2 注册PID): **DEAD** — 实际已被新进程 780591 接替
- 782625 (eval_15B bash wrapper): ALIVE
- 785949 (eval_llama32 bash wrapper): ALIVE  
- 784219 (signals_3B_d000_s123 bash wrapper): ALIVE
- GPU 进程 780943/780591/785955/786898: 全部 ALIVE

---
