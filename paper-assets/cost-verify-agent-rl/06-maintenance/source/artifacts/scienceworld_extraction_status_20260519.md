# ScienceWorld 数据提取状态报告

**日期:** 2026-05-19  
**服务器:** westd-47453

## 进程状态

| PID | 脚本 | 状态 | 运行时间 | CPU |
|-----|------|------|----------|-----|
| 19201 | `extract_scienceworld_sft_partial.py` | Running | 2h20m | 40% |
| 51279 | `extract_scienceworld_sft_optimized.py` | Running | 1h47m | 41% |

两个进程均在处理 task 16/25（`inclined-plane-friction-named-surfaces`，最大任务：692 train + 346 val 变体）。

**⚠️ 写入冲突：** 两个脚本都以 `open('w')` 模式写入同一组 `*_partial.jsonl` 文件，导致少量数据损坏（train 1 行、val 2 行无效 JSON）。

## 输出文件

| 文件 | 大小 | 行数 | 有效行 | 错误行 | 状态 |
|------|------|------|--------|--------|------|
| `scienceworld_sft_train.jsonl` | 335MB | 3592 | 3592 | 0 | ✅ 完整 |
| `scienceworld_sft_val.jsonl` | 159MB | 1796 | 1796 | 0 | ✅ 完整 |
| `scienceworld_sft_train_partial.jsonl` | 117MB | 1362 | 1361 | 1 | ⏳ 进行中（有损坏） |
| `scienceworld_sft_val_partial.jsonl` | 45MB | 650 | 648 | 2 | ⏳ 进行中（有损坏） |
| `expert_sft_train.jsonl` | 12MB | 2460 | 2460 | 0 | ✅ 完整（非 ScienceWorld） |

路径前缀：`/root/autodl-tmp/expert_sft/`

## 数据统计（完整文件 scienceworld_sft_*.jsonl）

- **覆盖任务：30/30** 全部 ScienceWorld 任务
- **总条目：5388**（train 3592 + val 1796）
- **成功轨迹（score=100）：4538**（train 2994 + val 1544）
- 成功率：train 83.3%, val 85.9%
- 格式：ChatML messages + metadata（task, variation, final_score, num_steps, success）
- 每条数据包含完整多轮对话轨迹（system → user/assistant 交替），带 `<think>` reasoning 和 `<answer>` action

## 是否可用于 SFT

**可以。** `scienceworld_sft_train.jsonl` 和 `scienceworld_sft_val.jsonl` 已完整可用：
- 筛选 `metadata.success == true` 即得 2994 条 train + 1544 条 val 成功轨迹
- 数据格式已是 chat messages 格式，可直接用于 SFT
- 两个仍在跑的进程**可以 kill**——它们是冗余的（只覆盖前 25 个任务的 score=100 子集），且输出文件有写入冲突损坏

## 建议

1. **Kill 两个进程**（PID 19201, 51279），它们在做无用功
2. 直接使用已完成的 `scienceworld_sft_train.jsonl` / `scienceworld_sft_val.jsonl`，过滤 `success=true`
3. 删除有损坏的 `*_partial.jsonl` 文件
