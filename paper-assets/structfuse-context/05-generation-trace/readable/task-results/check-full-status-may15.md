# check full status may15

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_full-status-may15_20260514T235634_result.json`
- **Structured JSON:** [`f216b546e1815b5288b4.json`](../../sessions/f2/f216b546e1815b5288b4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕，汇总如下。

---

## 1. m1_reextract_v2

**状态**：运行中，4 workers 并行处理，已持续 ~28 小时

**关键数据**：
- 总计 28,276 instances / 82 repos
- 预估总耗时 ~60h（4 workers），目前约 28h
- 当前活跃的 4 个 repo（最新进度）：
  - `sqlfluff/sqlfluff`: 850/1,272
  - `conan-io/conan`: 650/972
  - `pydicom/pydicom`: 300/1,315
  - `Project-MONAI/MONAI`: 刚开始处理
- 已出现 ~70 个 unique repo 有 "processed" 记录，82 个 repo 全部已启动
- `all.jsonl` 当前 44,173 行（已有数据）
- `m1_reextract_v2_output/` 下无 JSON 文件（产出写入 `full_m1_data/`）

**问题/风险**：当前处理的几个 repo 都是大 repo（1000+ instances），剩余时间可能还需 10-15h。

---

## 2. M2 Qwen 训练链 (cuda:0, PID 337267)

**状态**：运行中，已运行 12h33m，当前在链中 **第 2/9 个 run: `random_s44`**

**关键数据**：
| Run | 状态 | Best R@1 | Best val_loss |
|-----|------|----------|---------------|
| [1/9] random_s43 | ✅ 完成 | 0.5501 | 0.5434 |
| [2/9] random_s44 | 🔄 Epoch 2, step 1500/2810 (~53%) | 0.6009 | 0.4252 |

- random_s44 当前 metrics（eval@1000）: val_loss=0.4695, R@1=0.5638（未超 @500 的 best）
- 之前独立跑的 random_s42 也已完成: R@1=0.5503, val_loss=0.5456
- GPU 0: 99% utilization, 51.5GB/95.6GB VRAM

**问题/风险**：random_s44 的 eval@1000 出现 val_loss regression（0.4695 vs best 0.4252），patience 1/2。如果 eval@1500 继续不 improve，会 early stop。链中还剩 7 个 run。

---

## 3. M2 StarCoder 训练链 (cuda:1, PID 519791)

**状态**：运行中，已运行 5h54m，当前在 **`random_s43`（resume 后重跑）**

**关键数据**：
| Run | 状态 | Best R@1 | Best val_loss |
|-----|------|----------|---------------|
| random_s42 | ✅ 完成 | ~0.455 | ~0.664（过拟合） |
| random_s43 | 🔄 Epoch 1, step 1050/2810 (~37%) | 0.4780 | 0.5279 |

- eval@500: val_loss=0.5279, R@1=0.4708
- eval@1000: val_loss=0.5430（not improved 1/2）, R@1=0.4780（improved, saved best）
- GPU 1: 100% utilization, 52.7GB/95.6GB VRAM

**问题/风险**：
1. 之前的 s43 训练进程被 OOM Killed（日志中有明确 `Killed` 信号），之后通过 `run_m2_full_starcoder_resume.sh` 重启
2. random_s42 严重过拟合（val_loss 0.664），StarCoder 整体 R@1 (~0.47) 明显低于 Qwen (~0.55-0.60)
3. val_loss 已 not improved 1/2，如果下次 eval 继续 degrade 会触发 early stopping

---

## 4. BM25 Phase 2 Watcher

**状态**：两个 watcher 均在运行

| tmux session | 监控目标 | 状态 |
|-------------|---------|------|
| `bm25_qwen_watcher` | Qwen PID 337267 | 等待中 |
| `bm25_starcoder_watcher` | StarCoder PID 519791 | 等待中 |

- 还有 `qwen_s42_watcher` 和 `m2_qwen_s43`（历史 session）
- 两个 watcher pane 内容仅显示 "Watching XXX chain PID ..." 后空白，正在 sleep 轮询

**问题/风险**：watcher 逻辑只从 tmux capture-pane 看不到具体脚本内容，无法确认触发条件是否正确。建议后续确认 watcher 脚本检测的是整个链完成还是单个 run 完成。

---
