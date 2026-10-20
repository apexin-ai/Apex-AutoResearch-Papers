# ops westd full status v2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd-full-status-v2_20260520T033412_result.json`
- **Structured JSON:** [`ae6f0d40b3778e175c90.json`](../../sessions/ae/ae6f0d40b3778e175c90.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

| 服务器 | GPU | 实验 | PID | Registry状态 | 实际状态 | 进度 | 当前dosage | ETA(当前) |
|--------|-----|------|-----|-------------|---------|------|-----------|-----------|
| westd | cuda:0 | Phi-4 s0 sweep | 265121 | running | **still_running** | 547/3125 (17%) | d000_s0 | ~1h44m |
| westd | cuda:1 | Qwen-14B d100 s123 | 246779 | ~~failed~~ | **still_running** | 1982/4159 (48%) | d100_s123 | ~1h54m |
| westd | cuda:2 | OLMo-2 s0 sweep | 261133 | ~~failed~~ | **still_running** | ~800/3125 (26%) | d005_s0 | ~2h41m |
| westd | cuda:3 | Gemma-2 d100 s123 | 246861 | ~~failed~~ | **still_running** | 2034/4159 (49%) | d100_s123 | ~1h36m |
| westd | CPU | IRT 2PL+γ fitting | 268172 | running | **actually_dead** | — | — | — |
| cqa1 | cuda:0 | Qwen-7B s0 sweep | 313418 | running | **still_running** | 800/3125 (26%) | d000_s0 | ~2h40m |

### 关键发现

1. **Registry 误标的 3 个实验全部存活**：Qwen-14B/OLMo-2/Gemma-2 的 PID 均在，GPU 负载 67-96%，训练正常推进。Registry 需修正为 running。

2. **OLMo-2 s0 sweep 进度**：d000_s0 已完成（checkpoint 含 adapter_config.json），当前训练 d005_s0 (26%)。剩余 d025/d050/d100 未开始。总剩余约 ~8h。

3. **Phi-4 s0 sweep 进度**：仍在第一个 dosage d000_s0 (17%)。lora_adapter 目录为空（尚未保存 checkpoint）。总剩余约 ~10h（含后续 4 个 dosage）。

4. **IRT fitting 已死**：PID 268172 不存在，`irt_results_v3/` 目录为空，无任何输出。需要排查原因并重新提交。

5. **Qwen-7B s0 sweep (cqa1)**：正常运行，d000_s0 at 26%。4090D 上速度 ~4.1s/it，总剩余约 ~17h（含后续 4 个 dosage）。

6. **磁盘状态**：westd 数据盘 77% (59GB free)，cqa1 数据盘 72% (49GB free)，均充足。

---
