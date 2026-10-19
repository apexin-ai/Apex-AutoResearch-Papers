# infra check bjb1 32546 pi05

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_check-bjb1-32546-pi05_20260521T120056_result.json`
- **Structured JSON:** [`dabbe11b5c26c8c08fe1.json`](../../sessions/da/dabbe11b5c26c8c08fe1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

**GPU 占用（6/6 全部在跑 π0.5 eval r3）**
- GPU0: object-seed42-r3 → task 4/10 (alphabet_soup 85%, cream_cheese 100%, salad_dressing 60%)
- GPU1: object-seed43-r3 → task 3/10
- GPU2: object-seed44-r3 → task 3/10
- GPU3: spatial-seed42-r3 → task 4/10 (95%/90%/100%)
- GPU4: spatial-seed43-r3 → task 3/10
- GPU5: spatial-seed45 (注意：tmux 名无 -r3，应该是 seed44 命名错误) → task 3/10

**实际状态**
- 进程：6 个 `python evaluate.py` 全部 RUNNING（CPU 200%+，已运行 ~10 min）
- 启动时间 19:52，当前 20:02，日志活跃更新（最后写 20:01）
- 已完成 3-4/10 task，速度 ~7-8 rollout/min
- **ETA 修正：约 20-30 min 总耗时，不是 ROADMAP 说的 8h**（GPU 平均利用率低（0-21%），瓶颈在 sim/CPU 不在 GPU）

**先前异常**
- 18:48-18:55 的非 -r3 旧日志显示 `Overall SR: 0.0% (0/200)`——上一次跑挂了，r3 是修复后重跑（registry 显示 PREPARING 是因为状态没更新，实际进程是后启动的）

**磁盘**
- `/root/autodl-tmp`: 40G/250G (16%) ✅
- `/root`: 9.8G/30G (33%) ✅

**结论**：实验正常运行，预计 20:20-20:30 全部完成。建议 ~20 min 后回来收结果。

---
