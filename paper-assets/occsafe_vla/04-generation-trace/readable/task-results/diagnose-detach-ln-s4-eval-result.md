# diagnose detach ln s4 eval result

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_detach_ln_s4_eval-result_20260527T132606_result.json`
- **Structured JSON:** [`61a948146a56efbd6b60.json`](../../sessions/61/61a948146a56efbd6b60.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总：

### westd-34685 状态

**Eval 状态**
| Eval | GPU | 状态 | 进度 |
|------|-----|------|------|
| detach_ln_v2_s1_35_eval | cuda:0 | 运行中 | T0: TSR=0.980 CAR=0.980; T1: TSR=0.980 CAR=0.920; T2: 16% |
| detach_ln_s4_eval | cuda:1 | **已重启** | 原进程在 T0 4% 静默崩溃（日志无错误），已重启并确认过了崩溃点 (T0 8%+) |

**批次② 训练状态**
| 训练 | GPU | PID | 运行时间 | 最新 checkpoint |
|------|-----|-----|---------|----------------|
| ablation_occ_detach_s4 | cuda:2 | 735898 | 13h08m | 40000 (50000 未到) |
| mvp_occ_s4 | cuda:3 | 736253 | 13h08m | 40000 (50000 未到) |

**结论**
- detach_ln_s4_eval 无法提取 CAR/TSR — 之前的运行崩溃了，已重启
- detach_ln_v2_s1_35_eval 仍在运行，预计还需 ~30min 完成剩余 8 个 task
- 批次② 两个训练都还在跑，尚未产出 50000 checkpoint，无法启动新 eval

---
