# diagnose exp018 and gpu status

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp018_and_gpu_status_20260516T152953_result.json`
- **Structured JSON:** [`63e36194db21a8c3718a.json`](../../sessions/63/63e36194db21a8c3718a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集。汇总如下：

---

## 服务器诊断汇总 — cqa1-22115

### GPU 状态

| GPU | 型号 | 温度 | 功耗 | 显存占用 | 利用率 | 进程 |
|-----|------|------|------|---------|--------|------|
| 0 | RTX 4090 D | 31°C | 20W/425W | **0 MiB** | 0% | 无 (空闲) |
| 1 | RTX 4090 D | 31°C | 28W/425W | **0 MiB** | 0% | 无 (空闲) |
| 2 | RTX 4090 D | 52°C | 232W/425W | **5003 MiB** | 32% | PID 48295 (exp-024) |
| 3 | RTX 4090 D | 31°C | 23W/425W | **3601→4020 MiB** | 0% | PID 53023 (exp-022, 新进程) |

### 磁盘
`/root/autodl-tmp/`: **76G / 250G (31%)** — 充足

---

### exp-018 LLaMA-8B — **正常完成，进程已退出**

**死因：不是 crash，是正常结束。** 日志末尾 `23:27:38 [INFO] Pipeline complete.`

产出完整：
- `data/exp_018_llama8b/`: depth_0~5.jsonl (6个文件) + features.csv
- `results/exp_018_llama8b/`: summary.txt, pairwise_auc.json, jsd.json, ordinal_results.json, feature_importance.json

关键结果：
- **K\* = 2** (AUC > 0.60 的最大深度)
- AUC: 0→1=0.9225, 1→2=0.6123, 2→3=0.5274, 3→4=0.5169, 4→5=0.5162
- Ordinal MAE=1.3146, Accuracy=0.3269

没有 tmux session `exp_018_llama8b_depth`（已消失，进程完成后自行退出）。GPU 0 已释放。

---

### exp-022 cross-scorer — **运行中，进度 4/12**

tmux session `exp022` 存在。刚完成第 3 对 (qwen_base × pythia)，正在启动第 4 对 (qwen_base × olmo)。

当前阶段：[4/12] gen=qwen_base scorer=olmo → Step 4 Feature Extraction，depth_0 的 5000 条文本做 Surprisal 计算，进度 217/625 (~35%)。

GPU 3 上新进程 PID 53023 (4020 MiB)，替代了之前的 PID 52128。

**预估**：12 对组合，已完成 3 对，当前第 4 对进行中。按每对 ~30-40 分钟算，剩余约 4-6 小时完成。

---

### exp-024 arXiv domain — **运行中，Feature Extraction 阶段**

tmux session `exp_024_arxiv` 存在。PID 48295 活跃，运行 44 分钟。

已完成所有生成（depth_0~5.jsonl 全部就绪，每个 2200 docs），当前在 Step 4 Feature Extraction，depth_0 的 Surprisal 提取后进入 VocabDiv 计算。

GPU 2 上占用 5003 MiB，利用率 32%。

**预估**：Feature extraction + classification 阶段，大约还需 15-30 分钟完成。

---

### 总结

| 实验 | 状态 | GPU | 结论 |
|------|------|-----|------|
| exp-018 | **完成** | GPU 0 (已释放) | 正常结束，K\*=2，产出完整 |
| exp-022 | **运行中** 4/12 | GPU 3 | 预计还需 4-6h |
| exp-024 | **运行中** feat extraction | GPU 2 | 预计还需 15-30min |
| — | 空闲 | GPU 0, GPU 1 | 可用于新任务 |

---
