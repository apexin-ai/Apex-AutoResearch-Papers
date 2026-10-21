# diagnose westd status check

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_westd-status-check_20260519T143333_result.json`
- **Structured JSON:** [`9d5ef410b0d0c331c64b.json`](../../sessions/9d/9d5ef410b0d0c331c64b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-47453 状态汇总

### GPU（4× RTX PRO 6000 96GB）
**全部空闲。** 0MiB 显存占用，0% 利用率，无 GPU 进程。

### 活跃进程
两个 ScienceWorld SFT 数据提取脚本正在 **CPU 上** 运行：

| PID | 脚本 | CPU% | 启动时间 |
|-----|------|------|----------|
| 19201 | `extract_scienceworld_sft_partial.py` | 39.9% | 19:56 |
| 51279 | `extract_scienceworld_sft_optimized.py` | 41.5% | 20:30 |

两者各带一个 Java 进程（ScienceWorld 的 Py4J gateway），分别占 ~2.6GB 和 ~2.1GB 内存。

### ScienceWorld SFT 数据提取进展
- **已生成文件**：
  - `scienceworld_sft_train.jsonl` — 3,592 条（335MB），20:53 生成
  - `scienceworld_sft_val.jsonl` — 1,796 条
  - `scienceworld_sft_train_partial.jsonl` — 1,602 条
  - `scienceworld_sft_val_partial.jsonl` — 844 条
- **任务覆盖**：30 个任务类型中大部分已完成。`mendelian-genetics-known-plant` 和 `mendelian-genetics-unknown-plant` 成功率为 0，已被脚本 skip。少数任务有部分 variation 失败（如 `freeze` 12/14、`grow-fruit` 54/62、`inclined-plane-*` 系列部分缺失）。
- `extract_scienceworld_sft_optimized.py`（优化版）进展到 21/25 个任务，仍在运行。

### 8B SFT 训练脚本
`scripts/sft_train_8b.py`（5月19日 14:39 更新）已就绪：
- 模型：Qwen3-8B（`/root/autodl-tmp/models/Qwen3-8B`，已下载）
- 策略：FSDP full_shard + gradient_checkpointing，bf16
- **无 CPU offload 配置**（grep 无匹配）
- 默认数据路径指向 `expert_sft_train.jsonl`（ALFWorld），需改为 ScienceWorld 数据路径

### 磁盘
| 挂载点 | 大小 | 已用 | 可用 | 使用率 |
|--------|------|------|------|--------|
| `/`（根） | 30G | 14G | 17G | 46% |
| `/dev/sda2`（数据盘） | 879G | 21G | 813G | 3% |

充裕，无风险。

### 代码变动
`/root/cost-verify-agent-rl` 下无最近 6 小时内修改的 `.py` 文件。`sft_train_8b.py` 最后修改于 14:39（~8h 前），当时只是基础 FSDP 配置，未涉及 CPU offload 改动。

### 关键结论
1. **4 块 GPU 完全空闲**，可立即启动训练
2. ScienceWorld SFT 数据提取仍在运行（optimized 版 21/25 tasks），完整数据已有 3,592 train + 1,796 val 条
3. `sft_train_8b.py` **不含 CPU offload** 逻辑——当前用纯 FSDP full_shard，8B 模型在 4×96GB 上无需 offload
4. 数据路径需要从 ALFWorld 默认值切换到 ScienceWorld jsonl

---
