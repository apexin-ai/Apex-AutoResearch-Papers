# ops westb registry consistency check

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westb_registry_consistency_check_20260519T020802_result.json`
- **Structured JSON:** [`ab8314c52e9bdbc2142b.json`](../../sessions/ab/ab8314c52e9bdbc2142b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### eval_gsm8k_sft_rasp_20_1p5b (cuda:0, PID 845212)
| 项目 | 值 |
|------|------|
| PID 状态 | **存活** |
| 进度 | **1102/1319** (83.5%) |
| 当前 accuracy | 0.2764 (27.64%) @ 1100 samples |
| EOS rate | 94.27%, avg_len=374 |
| 已运行 | ~2h24m (07:44 启动) |
| 预估剩余 | ~20-30 min (217 samples remaining, ~2-3s/it + 偶发长生成 spike) |

### eval_gsm8k_sft_standard_20_1p5b (cuda:1, PID 842784)
| 项目 | 值 |
|------|------|
| PID 状态 | **存活** |
| 进度 | **972/1319** (73.7%) |
| 当前 accuracy | 0.2295 (22.95%) @ 950 samples |
| EOS rate | 90.63%, avg_len=509 |
| 已运行 | ~3h04m (07:02 启动) |
| 预估剩余 | ~40-60 min (347 samples remaining, 频繁出现 30-47s spike) |

### GPU 状态
| GPU | 利用率 | 显存使用 |
|-----|--------|----------|
| cuda:0 | 45% | 6,579 / 97,887 MiB |
| cuda:1 | 99% | 6,537 / 97,887 MiB |

### 要点
- 两个实验均正常运行，结果文件尚未生成
- RASP 模型 (27.64%) 领先 Standard 模型 (22.95%) 约 4.7 个百分点
- Standard 实验速度明显慢于 RASP（avg_len 更长 509 vs 374，且 spike 更频繁），虽然先启动 42 分钟但进度反而落后
- cuda:1 利用率 99% 符合 Standard 实验正在密集生成的状态

---
