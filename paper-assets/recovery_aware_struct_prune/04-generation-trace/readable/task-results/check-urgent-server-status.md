# check urgent server status

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_urgent_server_status_20260514T161048_result.json`
- **Structured JSON:** [`cecf95959c4891b21381.json`](../../sessions/ce/cecf95959c4891b21381.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 服务器状态汇报

| 项目 | 状态 |
|------|------|
| **1. 根分区** | 22G 可用 / 30G (29% used) — 正常 |
| **2. autodl-tmp** | **3.8G 可用 / 250G (99% used) — 危险** |
| **3. 模型位置** | 全部在数据盘，根分区 `models/` 目录下是符号链接 → `/root/autodl-tmp/` |
| **4. Base model** | `models/DeepSeek-R1-Distill-Qwen-7B` → `/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B` ✅ 有效（~14.2GB safetensors） |
| **5-6. GPU 进程** | 见下表 |
| **7. results 文件** | 见下方 |
| **8. scores 文件** | `importance_scores.pt` ✅ (17KB) / `cka_scores.pt` ✅ (122KB) |

### GPU 进程

| GPU | PID | 命令 | 显存 | 利用率 | 进度 |
|-----|-----|------|------|--------|------|
| cuda:0 | 206303 | `eval_gsm8k.py --model_path models/pruned_standard_20` | 13003MiB / 97887MiB | 81% | **45/100** (~54s/it, 预计还约50min) |
| cuda:1 | 214454 | `eval_gsm8k.py --model_path models/pruned_rasp_20` | 13003MiB / 97887MiB | 69% | **71/100** (~7s/it, 预计还约3min) |

GPU 1 完成 rasp_20 后会依次自动执行 `standard_25` → `rasp_25`。

### 已有 results 文件

```
cka_scores.pt                          (122KB)
importance_scores.pt                   (17KB)
eval_baseline_7b_quick.json            (87KB)
eval_baseline_7b_quick2.json           (44KB)
eval_baseline_7b_quick_fixed.json      (44KB)
eval_pruned_standard_35.json           (1.3MB)
eval_pruned_standard_35_v3_quick.json  (95KB)
eval_pruned_rasp_35.json               (1.3MB)
eval_pruned_rasp_35_v3_quick.json      (102KB)
debug_extract_results.json             (4.8KB)
analysis/                              (子目录)
```

### 剪枝模型符号链接

- `pruned_standard_20` → `/root/autodl-tmp/pruned_standard_20`
- `pruned_standard_25` → `/root/autodl-tmp/pruned_standard_25`
- `pruned_rasp_20` → `/root/autodl-tmp/pruned_rasp_20`
- `pruned_rasp_25` → `/root/autodl-tmp/pruned_rasp_25`

**⚠️ autodl-tmp 磁盘 99% 满，仅剩 3.8G。** 后续写入（eval 输出、新 checkpoint）可能失败，需要清理空间。

---
