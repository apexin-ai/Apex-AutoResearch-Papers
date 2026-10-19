# ops training status check 20260515

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_training_status_check_20260515_20260514T162453_result.json`
- **Structured JSON:** [`dc0a09103ba2fd77d7a2.json`](../../sessions/dc/dc0a09103ba2fd77d7a2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

### 1. m2_full_qwen (cuda:0) — 运行中
| 项目 | 数据 |
|------|------|
| 进度 | **step 1250 / 2810** (44.5%) |
| 最新 loss | 0.2021 (step 1250) |
| 最新 eval (step 1000) | val_loss=0.4637, R@1=0.5285, R@5=0.9672 |
| 最佳指标 (step 500) | val_loss=0.4476, R@1=0.5357 |
| 状态 | eval@1000 val_loss 未改善 (1/2 patience) |
| 预计剩余 | ~10h（session 创建 19:19，5h 跑了 ~750 步，剩 1560 步） |

### 2. m2_full_starcoder (cuda:1) — s42 即将结束，s43 待启动
| 项目 | 数据 |
|------|------|
| s42 进度 | **step 4000 / 4242** (94.3%)，日志最后输出 loss=0.0636 |
| s42 最佳指标 | val_loss=0.6134 (step 1000), R@1=0.4604 (step 2500) |
| s43 状态 | tmux session `m2_starcoder_s43` 已存在，显示 "Waiting for StarCoder s42 (PID 76627) to finish..." |
| Watcher | `starcoder_s42_watcher` 正常运行，最近一次轮询 00:23 仍报 "still running" |
| 预计 s42 完成 | ~1-2h（剩 242 步），之后 s43 自动启动 |

### 3. m1_reextract_v2 — 运行中
| 项目 | 数据 |
|------|------|
| 总量 | 28276 instances, 82 groups, 4 workers |
| 已启动 groups | **72 / 82** |
| 当前活跃 | fvcore (100/454), conan (100/972), dask (50/329), MONAI (CodeQL 阶段) |
| 已接近完成 | trio (750/753), patsy (750/787) |
| 运行时间 | ~20.5h（03:59 启动） |
| 预计剩余 | ~8-12h（剩余 groups 含 conan 972 例等大 repo，另有 10 groups 未启动） |

### 4. nvidia-smi
| GPU | 型号 | 温度 | 功耗 | VRAM | 利用率 | PID |
|-----|------|------|------|------|--------|-----|
| 0 | RTX PRO 6000 | 68°C | 499W/600W | 50.5G/97.9G | 100% | 337271 (qwen) |
| 1 | RTX PRO 6000 | 75°C | 575W/600W | 55.4G/97.9G | 100% | 76627 (starcoder) |

### 汇总

两张卡满载运行，一切正常。**Qwen s43** 在 44.5%，最佳 R@1=0.5357 出现在 step 500 后有轻微下降趋势，后续 eval 需关注是否回升。**StarCoder s42** 剩 ~242 步即将结束，s43 watcher 就绪会自动接力。**m1_reextract_v2** 已跑完大部分 groups，当前在处理几个大 repo（conan 972 例、fvcore 454 例），预计还需 8-12 小时完成全部 82 groups。

---
