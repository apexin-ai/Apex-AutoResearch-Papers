# ops progress check all servers

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_progress-check-all-servers_20260515T194926_result.json`
- **Structured JSON:** [`755735c3e5c90dee838b.json`](../../sessions/75/755735c3e5c90dee838b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 17 个实验 registry 已更新。汇总如下：

## 进度总览（2026-05-16 03:55 UTC）

**全部 17 个进程存活，无异常。**

### bjb2-40593 (1 GPU)
| 实验 | GPU | 进度 | 备注 |
|------|------|------|------|
| eval-mag-obsonly-norm003-b2 | cuda:0 | **7/10** | spatial sweep, 累计 SR: 31/70 (44.3%). 预计 ~2h 完成 |

已完成 task SR: between_plate 90%, next_to_ramekin 100%, table_center 0%, cookie_box 30%, top_drawer 10%, on_ramekin 0%, next_to_cookie 80%

### bjb1-18228 (4 GPUs)
| 实验 | GPU | 进度 | 部分 SR |
|------|------|------|---------|
| eval-obs-only-object-seed43 | cuda:2 | **6/10** | soup 0%, cheese 10%, salad 10%, bbq 30%, ketchup 0%, tomato 0% |
| eval-argmin-object-seed43 | cuda:3 | **6/10** | soup 0%, cheese 0%, salad 20%, bbq 20%, ketchup 10%, tomato 10% |
| eval-perdof-object-seed43 | cuda:1 | **4/10** | soup 0%, cheese 0%, salad 20%, bbq 30%. 当前: ketchup rollout 5/10 |
| eval-acr-object-v4-default-r2 | cuda:0 | **1/10** | soup 0%. 刚启动 1.5h |

### bjb1-32546 (6 GPUs)
| 实验 | GPU | 进度 | 部分 SR |
|------|------|------|---------|
| eval-vla-mean-object-seed43 | cuda:1 | **3/10** | soup 0%, cheese 0%, salad 20% |
| eval-scalar-object-seed43 | cuda:2 | **2/10** | soup 0%, cheese 0%. 当前: salad rollout 5/10 |
| eval-mag-obsonly-norm003-object | cuda:0 | **2/10** | soup 0%, cheese 20% |
| eval-obs-only-object-norm02-seed43-r2 | cuda:3 | **0/10** | 刚启动 51min, task 1 rollout 5/10 |
| eval-acr-object-obs-only-default | cuda:4 | **1/10** | soup 0%. 当前: cheese rollout 5/10 |
| eval-mag-perdof-norm02-object | cuda:5 | **2/10** | soup 0%, cheese 10%. **已确认存活** |

### bjb2-28827 (6 GPUs) — GPU 映射已确认
| 实验 | GPU | 进度 | 部分 SR |
|------|------|------|---------|
| eval-mag-perdof-norm003-object | **cuda:0** | **1/10** | soup 0%. 当前: cheese rollout 5/10 |
| eval-mag-perdof-norm005-object | **cuda:1** | **1/10** | soup 0%. 当前: cheese rollout 5/10 |
| eval-mag-obsonly-norm03-object | **cuda:5** | **2/10** | soup 0%, cheese 0% |
| eval-mag-obsonly-norm005-object | **cuda:4** | **2/10** | soup 0%, cheese 0% |
| eval-mag-perdof-norm03-object-r3 | **cuda:2** | **0/10** | 刚启动, 模型已加载 |
| eval-mag-perdof-norm02-seed43-object-r3 | **cuda:3** | **0/10** | 刚启动, 模型已加载 |

### 关键发现
1. **GPU 映射确认**: bjb2-28827 上 eval-mag-obsonly-norm03-object → cuda:5, eval-mag-obsonly-norm005-object → cuda:4
2. **eval-mag-perdof-norm02-object** (bjb1-32546:cuda:5) 确认存活且正常推进 (2/10 done)，之前误报已纠正
3. **seed=43 进度**: obs-only 和 argmin 领先 (6/10)，perdof 落后 (4/10)。预计 obs-only/argmin ~4h 完成，perdof ~6h
4. **bjb2-28827 进度偏慢**: 多数实验仅 1-2/10，3 个刚启动。全部完成预计 ~10-12h
5. **早期趋势**: object benchmark 各方法前几个 task 的 SR 普遍很低 (0-30%)，与 seed=42 趋势一致

---
