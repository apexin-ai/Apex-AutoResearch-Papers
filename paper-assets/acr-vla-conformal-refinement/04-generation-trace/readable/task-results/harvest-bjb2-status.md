# harvest bjb2 status

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_bjb2-status_20260526T200050_result.json`
- **Structured JSON:** [`34b5182e532ecffb96f2.json`](../../sessions/34/34b5182e532ecffb96f2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

关键发现：GPU 1 上有**两个相同的 object tau035 实验**在碰撞，还有一个未列出的 tau045 实验在 GPU 2 上。PID 548208（原先碰撞 GPU 0 的进程）已死。

汇总如下：

---

## 实验状态

### 1. pi05-adaptive-long-s42-tau015-bjb2
```
exp_id: pi05-adaptive-long-s42-tau015-bjb2
server: bjb2-28827
status: STILL_RUNNING (6/10 tasks done, task 7 rollout 10/20)
GPU: cuda:4, 11459 MiB, clean — 0 OOM
log_path: /root/runs/acr-vla-conformal-refinement/tau-sweep-long-tau015-s42.log
已完成 tasks:
  alphabet_soup+tomato_sauce: 95%
  cream_cheese+butter: 95%
  stove+moka_pot: 100%
  black_bowl+cabinet: 80%
  white_mug+yellow_mug: 95%
  book+caddy: 80%
预计还需 ~3 小时完成
```

### 2. pi05-adaptive-long-s42-tau035-bjb2
```
exp_id: pi05-adaptive-long-s42-tau035-bjb2
server: bjb2-28827
status: STILL_RUNNING (6/10 tasks done, task 7 rollout 10/20)
GPU: cuda:5, 11459 MiB, clean — 0 OOM
log_path: /root/runs/acr-vla-conformal-refinement/tau-sweep-long-tau035-s42.log
已完成 tasks:
  alphabet_soup+tomato_sauce: 80%
  cream_cheese+butter: 95%
  stove+moka_pot: 100%
  black_bowl+cabinet: 90%
  white_mug+yellow_mug: 95%
  book+caddy: 70%
预计还需 ~3 小时完成
```

### 3. pi05-object-tau015-s42-bjb2 ⚠️ OOM 污染
```
exp_id: pi05-object-tau015-s42-bjb2
server: bjb2-28827
status: STILL_RUNNING (4/10 tasks done, task 5 in progress)
GPU: cuda:0, 10346 MiB
OOM: 23 次 — 碰撞源 PID 548208 已死，OOM 已停止
⚠️ Task 1 (alphabet_soup) SR=0% 完全由 OOM 导致，结果不可信
log_path: /root/acr-vla-conformal-refinement/logs/eval_object_adaptive_pi05_tau015_seed42.log
已完成 tasks:
  alphabet_soup: 0% ❌ (OOM 致假结果)
  cream_cheese: 70% (可能有 ~3 次 OOM 影响)
  salad_dressing: 90%
  bbq_sauce: 75%
```

### 4. pi05-object-tau035-s42-bjb2 ⚠️⚠️ 活跃 GPU 碰撞
```
exp_id: pi05-object-tau035-s42-bjb2
server: bjb2-28827
status: STILL_RUNNING — ⚠️ GPU 1 上有两个相同实验在碰撞！
  PID 548411 (直接启动, 12089 MiB) + PID 549422 (nohup 子进程, 10346 MiB) = 22435 MiB
  两者写同一个 output JSON，结果完全不可信
GPU: cuda:1, 22471 MiB total
OOM: 15 次且仍在持续
log_path: /root/acr-vla-conformal-refinement/logs/eval_object_adaptive_pi05_tau035_seed42.log
已完成 tasks (不可信):
  alphabet_soup: 20%
  cream_cheese: 90%
  salad_dressing: 90%
  bbq_sauce: 85%
```

### 5. eval-k2-tau045-spatial-s42-bjb2 ✅
```
exp_id: eval-k2-tau045-spatial-s42-bjb2
server: bjb2-24035
status: COMPLETED
SR: 78.0% (156/200)
mean_uncertainty: 0.1945, trigger_rate: 8.1%, tau: 0.45
log_path: /root/acr-vla-conformal-refinement/logs/eval-k2-tau045-spatial-s42-bjb2.log
json_path: /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_tau045_k2_s42.json
per_task: between_plate_ramekin 90%, next_to_ramekin 95%, table_center 100%, cookie_box 90%, top_drawer 70%, on_ramekin 0%, next_to_cookie 95%, stove 75%, next_to_plate 80%, wooden_cabinet 85%
```

### 未列出实验 (bjb2-28827)
```
PID 564173, GPU 2 (12674 MiB): object tau=0.45 sweep
status: STILL_RUNNING, elapsed 1h48m
output: logs/eval_object_adaptive_tau045_pi05_seed42.json
```

---

## GPU 空闲情况

| 服务器 | GPU | 显存占用 | 状态 |
|--------|-----|----------|------|
| bjb2-28827 | 0 | 10346 MiB | 占用 (object tau015) |
| bjb2-28827 | 1 | 22435 MiB | 占用 + **碰撞** |
| bjb2-28827 | 2 | 12674 MiB | 占用 (object tau045) |
| bjb2-28827 | **3** | **~0 MiB** | **✅ 可用** |
| bjb2-28827 | 4 | 11459 MiB | 占用 (long tau015) |
| bjb2-28827 | 5 | 11459 MiB | 占用 (long tau035) |
| bjb2-24035 | **0** | **0 MiB** | **✅ 可用** |

---

## 需要决策

1. **Object tau035 碰撞 (GPU 1)**：PID 548411 和 549422 都是 tau035，需要杀掉一个（或都杀掉重跑）。两个进程写同一个 JSON，当前数据不可信。
2. **Object tau015 (GPU 0)**：Task 1 的 0% SR 是 OOM 假结果。后续 task 基本可用但可能有轻微污染。是否接受部分结果还是重跑？
3. **Object tau045 (GPU 2)**：未在任务列表中但正在运行，是否保留？

---
