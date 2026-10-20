# ops westd gsm8k olmo2 status

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd-gsm8k-olmo2-status_20260521T142220_result.json`
- **Structured JSON:** [`2085016399db4226fac0.json`](../../sessions/20/2085016399db4226fac0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GSM8K Results
- **仍在运行**，3 个进程均存活（elapsed ~20min / ~55min）
  - PID 528870 (d000): `Rl` 状态，已运行 19:45
  - PID 529276 (d025): `Rl` 状态，已运行 19:14
  - PID 529683 (d100): `Rl` 状态，已运行 18:43
- 输出目录已创建但为空，尚未写出结果
- 预计还需 ~35min

## OLMo-2 Baseline Status
- 是否有新 eval 在跑：**否**，无 OLMo 相关进程
- 最新 d000_s0 结果：`eval_results.json` 修改时间 **2026-05-20 18:39**（昨天），**未今天重跑**
- 当前 d000_s0 MMLU 准确率：**55.34%**（7771/14042），与 ROADMAP 中 "53.79% 存疑" 不一致——这个 55.34% 可能是 5/20 的重跑结果，已修正了之前的数值
- `exp001/eval_results_v2/olmo2_d000/` 不存在
- GPU 状态：
  - GPU 0/1/2: 91% utilization, 18591 MiB / 97887 MiB（LLaMA-3 eval 占用）
  - GPU 3: 0% utilization, 空闲

---
