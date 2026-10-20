# ops check 14b progress all

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-14b-progress-all_20260522T132424_result.json`
- **Structured JSON:** [`f1da6b24198a2113c8a4.json`](../../sessions/f1/f1da6b24198a2113c8a4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据收集完毕，汇总如下：

## 1.4B 实验进度总览（截至 ~21:26 CST）

| exp_id | 服务器 | GPU | 已完成/总 gen | 训练中 | 每 gen 耗时 | 预计剩余 | 预计完成 | 状态 |
|--------|--------|-----|--------------|--------|------------|---------|---------|------|
| **t10_a050** | 19828 | cuda:1 | **6/10** | gen_6 | ~65 min | **~4.3h** | ~01:45 | 运行中 |
| **t10_a075** | 17855 | cuda:2 | **5/10** | gen_5 | ~61 min | **~4.8h** | ~02:15 | 运行中 |
| **t10_a060** | 17855 | cuda:3 | **5/10** | gen_5 | ~61 min | **~4.8h** | ~02:15 | 运行中 |
| t10_a045 | 17855 | cuda:4 | **0/10** | gen_0 | ~61 min | **~9.9h** | ~07:20 | 刚启动 |
| t15_a060 | 17855 | cuda:0 | **4/15** | gen_4 | ~61 min | **~10.9h** | ~08:20 | 运行中 |
| t15_a050 | 17855 | cuda:1 | **4/15** | gen_4 | ~61 min | **~10.9h** | ~08:20 | 运行中 |
| t15_a045 | 17855 | cuda:5 | **2/15** | gen_2 | ~61 min | **~12.9h** | ~10:20 | 运行中 |
| t15_a075 | 19828 | cuda:0 | **1/15** | gen_1 | ~65 min | **~15.1h** | ~12:32 | 运行中 |

## 重点

- **最快完成（T=10 系列）**：t10_a050、t10_a075、t10_a060 三个实验预计今晚 01:45-02:15 完成
- **已完成**：无
- **异常**：
  - **t10_a045 晚启动**：21:06 才从 gen_0 开始（其他 17855 实验已跑到 gen_4-5），比同 target=10 的兄弟实验落后 ~5h
  - 17855 上 6 个实验在 21:08 附近**全部重启过**（ps 显示 START=21:08，带 `--start_gen` 从 checkpoint 恢复）。有 wget 进程正在下载 pythia-1.4b-deduped safetensors，说明之前可能模型文件缺失导致了重启
  - 19828 两个实验正常运行，无重启痕迹

GPU 利用率全部正常：17855 六卡 85-90%（11.2GB/卡），19828 两卡 83-84%。

---
