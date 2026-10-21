# ops eval progress pipeline check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval_progress_pipeline_check_20260514T041112_result.json`
- **Structured JSON:** [`85bc6af96a2b36edd16a.json`](../../sessions/85/85bc6af96a2b36edd16a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 实验进度

| exp_id | GPU | progress | 剩余时间估算 | ETA (UTC) | 异常 |
|--------|-----|----------|-------------|-----------|------|
| sft_d100_15B_v2 | cuda:0 | 2669/4159 (64%) | ~4h30m | ~16:30 | 无（GPU util 采样0%为正常波动） |
| eval_05B_d005 | cuda:1 | GSM8K 1085/1319 (82%) + HumanEval待跑 | ~2h | ~14:00 | HF连接超时已恢复 |
| eval_3B_d000_s42 | cuda:1 | GSM8K 1177/1319 (89%) + HumanEval待跑 | ~2h30m | ~14:30 | bitsandbytes警告（非致命） |
| eval_05B_d000_s42_v5 | cuda:2 | GSM8K 649/1319 (49%) + HumanEval待跑 | ~4h | ~16:00 | 无 |
| eval_05B_d100_v5 | cuda:2 | GSM8K 654/1319 (50%) + HumanEval待跑 | ~4h | ~16:00 | 无 |
| eval_3B_d000_s123 | cuda:3 | **HumanEval 109/164 (66%) — 最后一个benchmark** | ~27m | **~12:30** | 无 |
| eval_15B_d000_s123 | cuda:5 | **HumanEval 86/164 (52%) — 最后一个benchmark** | ~34m | **~12:35** | 无 |
| sft_d005_15B | cuda:4 | 537/3177 (17%) | ~8h | ~20:00 | 无，lr warmup阶段 |

注：所有 eval 进程有 bitsandbytes `libnvJitLink.so.13` 加载错误，但不影响推理，是非致命警告。

## 代码就绪

- **exp-002**: ❌ 部分缺失 — 仅 `aggregate_rrf.py` 存在于 `/root/contamcal-irt-calibration/exp002/`，`extract_signals.py` 和 `run_exp002.sh` 不存在
- **exp-006**: ❌ `run_exp006.sh` 服务器上未找到

## GPU 健康

| GPU | mem_used/total | util% | 进程 |
|-----|---------------|-------|------|
| 0 | 10055/24564 MiB (41%) | 0%* | PID 251924 (sft_d100_15B_v2) |
| 1 | 12620/24564 MiB (51%) | 52% | PID 249294 (3B_d000_s42) + PID 255322 (05B_d005) |
| 2 | 7330/24564 MiB (30%) | 49% | PID 266521 (05B_d000_s42_v5) + PID 266790 (05B_d100_v5) |
| 3 | 13493/24564 MiB (55%) | 12% | PID 242591 (3B_d000_s123) |
| 4 | 18547/24564 MiB (75%) | 7% | PID 271921 (sft_d005_15B) |
| 5 | 10365/24564 MiB (42%) | 16% | PID 250610 (15B_d000_s123) |

*GPU 0 util 0% 是采样瞬间值，SFT 训练在 forward/backward 间有空隙，属正常。

**即将完成**: eval_3B_d000_s123 和 eval_15B_d000_s123 预计 30 分钟内完成。cuda:1 双进程共享无 OOM 风险（12.6/24.6 GB）。cuda:2 同理（7.3/24.6 GB）。

---
