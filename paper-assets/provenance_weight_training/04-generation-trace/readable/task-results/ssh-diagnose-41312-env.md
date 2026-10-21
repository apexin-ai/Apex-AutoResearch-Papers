# ssh diagnose 41312 env

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_diagnose_41312_env_20260517T183107_result.json`
- **Structured JSON:** [`ffcf397f3ba170a3019e.json`](../../sessions/ff/ffcf397f3ba170a3019e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有信息已收集完毕。

---

## 诊断报告：westd-41312

### 结论：**不能启动新实验，4 张 GPU 全部在跑**

---

### 1. GPU 状态：全部占满

| GPU | 显存占用 | 利用率 | 运行实验 |
|-----|---------|--------|---------|
| 0 | 46539/97887 MiB | 100% | qwen06b_uniform_seed42 |
| 1 | 75023/97887 MiB | 76% | ess_only_seed456 |
| 2 | 75023/97887 MiB | 100% | ess_only_seed123 |
| 3 | 46539/97887 MiB | 100% | random_reweight_seed456 |

### 2. Python 环境：正常
- Python: `/root/miniconda3/bin/python` 3.12.3
- transformers: **4.57.6**（有 tokenizer 弃用问题）

### 3. tokenizer bug：**已修复**
`pretrain_weighted.py` 第 101-105 行有兼容性处理，第 420 行已使用 `processing_class=tokenizer`。这不是之前失败的根因。

### 4. 之前失败的 grid_b0_3_seed456：**实际已成功完成**
日志末尾显示 `Training complete. Model saved to output/models/grid_b0_3_seed456/final`，EXIT_CODE=0。并非失败。

### 5. 磁盘空间：充足
- `/root/` = 30G，已用 9.3G，剩余 21G (31%)

### 6. 模型/数据文件：存在
- Qwen3-0.6B 模型文件完整
- scored_data.jsonl 974MB 存在

### 7. grid_b 相关脚本
- `run_grid_b0_1_seed42.sh`
- `run_grid_b0_2_seed42.sh`
- `run_grid_b0_3_seed456.sh`
- `run_grid_b_low_seed42.sh`
- `submit_grid_b_seed456.sh`

### 8. 当前 4 个活跃实验
1. **ess_only_seed123** — GPU 2，已跑 ~3h
2. **ess_only_seed456** — GPU 1，已跑 ~3h
3. **random_reweight_seed456** — GPU 3，启动于 02:14（~17min）
4. **qwen06b_uniform_seed42** — GPU 0，启动于 02:17（~14min）

---

### 总结
- **环境健康**，transformers tokenizer bug 已修复，磁盘充足，模型/数据就位
- **无法启动新实验**：4 张 GPU 全部被现有训练占满
- 需等当前实验完成（ess_only 两个接近完成，约 epoch 0.26/200M tokens；uniform 和 random_reweight 刚启动）
- grid_b0_3_seed456 之前标记为"被 kill"但日志显示已正常完成

---
