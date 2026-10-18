# investigate pi05 baseline goal strict logs

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_pi05_baseline_goal_strict_logs_20260527T063936_result.json`
- **Structured JSON:** [`567543bae48f2882a158.json`](../../sessions/56/567543bae48f2882a158.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Part 1: eval_pi05_baseline_goal_seed42_strict 判定

**结论：从未实际运行，无可用数据，需要重跑。**

- cqa1-33015 上的日志仅有一行：`Waiting for GPU 0 to be free...`（13:47 CST）
- 脚本 `run_baseline_goal_strict.sh` 正在 `sleep 60` 轮询等待 GPU0 释放
- GPU0 被 `eval_openvla_random_k095_goal_seed42` 占用，预计 ~16:20 CST 完成后 baseline 才能启动
- 启动后 pi05 baseline goal 全10 tasks 预计需 ~3-4h → **完成时间约 20:00-20:30 CST（接近截止线）**

**参考**：非 strict 版本（5月22日 cqa1）跑了 5+ tasks 全为 **0% SR**，高度异常——可能是模型加载/配置问题，而非真实 baseline 表现。

---

## Part 2: 全服务器健康状态

### westd-27271 (2× RTX PRO 6000 Blackwell 98GB)

| GPU | 实验 | 进度 | 利用率 | 速率 | 预估完成 |
|-----|------|------|--------|------|---------|
| 0 | OpenVLA attn k=0.95 goal s42 | T3/10 ep20 | 88% | 2.8 eps/min | ~17:00 |
| 1 | OpenVLA l2norm k=0.85 object s42 | T1/10 ep40 | 73% | 1.9 eps/min | ~18:30 |

### westd-38929 (4× RTX PRO 6000 Blackwell 98GB)

| GPU | 实验 | 进度 | 利用率 | 速率 | 预估完成 |
|-----|------|------|--------|------|---------|
| 0 | OpenVLA random k=0.95 long s42 | T1/10 ep20 | 65% | 1.2 eps/min | ~22:30 |
| 1 | OpenVLA l2norm k=0.95 long s42 | T5/10 ep40 | 78% | 0.7 eps/min | ~20:30 |
| 2 | OpenVLA l2norm k=0.75 long s42 | **异常** | 62% | 0.9 eps/min | 需检查 |
| 3 | OpenVLA attn k=0.95 long s42 | T5/10 ep40 | 68% | 0.7 eps/min | ~20:30 |

**GPU2 异常**：日志末尾有 `EXIT_CODE=124`（超时），但进程 PID 968309 仍在运行（09:41启动，5h CPU时间正常）。可能是旧日志残留 + 新进程写入同一文件。需确认当前进度。

### westd-41074 (4× RTX PRO 6000 Blackwell 98GB)

| GPU | 实验 | 进度 | 利用率 | 速率 | 预估完成 |
|-----|------|------|--------|------|---------|
| 0 | OpenVLA random k=0.95 long s42 | T7/10 | 72% | 0.8 eps/min | ~17:30 |
| 1 | π0.5 random k=0.75 long strict s42 | T3/10 done | 49% | 3.3 eps/min | ~17:00 |
| 2 | **空闲** | - | 0% | - | - |
| 3 | π0.5 attn k=0.85 long strict s42 | T9/10 ep30 | 17% | ~3 eps/min | **~15:00 即将完成** |

### cqa1-33015 (4× RTX 4090D 24GB)

| GPU | 实验 | 进度 | 利用率 | 速率 | 预估完成 |
|-----|------|------|--------|------|---------|
| 0 | OpenVLA random k=0.95 goal s42 | T8/10 ep10 | 23% | 1.4 eps/min | ~16:20 |
| 1 | OpenVLA attn k=0.95 goal s42 | **异常** | 14% | ~1.5 eps/min | 需检查 |
| 2 | π0.5 attn k=0.95 long strict s42 | T6/10 ep30 | 9% | ~7min/task | ~17:30 |
| 3 | OpenVLA attn k=0.5 goal s42 | T6/10 ep10 | 71% | 1.0 eps/min | ~18:30 |

**cqa1 GPU1 异常**：日志显示 `EXIT_CODE=143`（SIGTERM killed），但 PID 11249 仍在运行。可能是旧日志残留，当前进程正常工作中。

---

## 关键异常 & 建议

1. **westd-41074 GPU2 空闲** — 可立即利用
2. **westd-41074 GPU3** — π0.5 attn k=0.85 long strict 即将完成（~15:00），之后 GPU3 也空闲
3. **baseline strict 在 cqa1 等待 GPU0** — 最早 ~16:20 才能开始，完成约 20:00-20:30，非常紧张
4. **westd-38929 GPU0** 的 OpenVLA random k=0.95 long 预计 22:30 才完成——最慢的实验
5. cqa1 GPU1 和 westd-38929 GPU2 的日志异常需要进一步确认进程是否正常产出结果

**建议**：将 baseline strict 转移到 westd-41074 GPU2（立即可用）而非继续等 cqa1 GPU0，可节省 2+ 小时。

---
