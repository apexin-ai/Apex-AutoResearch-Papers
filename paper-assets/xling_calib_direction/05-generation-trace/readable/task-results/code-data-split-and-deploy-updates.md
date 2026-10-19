# code data split and deploy updates

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_data_split_and_deploy_updates_20260520T221347_result.json`
- **Structured JSON:** [`c4e5be1e02d13f174165.json`](../../sessions/c4/c4e5be1e02d13f174165.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两项任务完成。

### 任务 A: 代码修改

修改的文件：`extract_activations_large.py`

| 行号 | 修改内容 |
|------|----------|
| 42-44 | `--languages` 默认值扩展为 20 语言 |
| 57-60 | 新增 `--split_ratio` 和 `--split_seed` 参数 |
| 264-287 | `save_layer_data()` 增加 `train_indices`/`eval_indices` 参数，支持分别保存 train/eval 文件 |
| 331-333 | `main()` 中初始化 `split_train_indices`/`split_eval_indices = None` |
| 340 | 循环改为 `enumerate(args.languages)` |
| 354-368 | 第一个语言时基于 subject 做 stratified split，保存 `split_indices.pt`，后续语言复用同一组 indices |
| 409-410, 414-415 | `save_layer_data` 调用传入 split indices |
| 420-422 | 打印输出适配 train/eval 文件名 |

关键设计：split 在第一个语言时计算一次，所有语言复用相同 indices（因为 GlobalMMLU test[i] 是 parallel translation），确保跨语言一致性。`split_ratio=0` 时行为完全不变。

### 任务 B: 服务器部署确认

grep 输出确认 `split_ratio`/`split_seed`/`train_indices`/`eval_indices` 均存在于服务器文件中（20 处匹配）。

`--help` 输出：
```
--split_ratio SPLIT_RATIO
                    If > 0, split test data into train/eval. E.g., 0.7 = 70% train, 30% eval
--split_seed SPLIT_SEED
                    Random seed for train/eval split (ensures reproducibility across languages)
```

文件已部署到两个路径：
- `/root/xling_calib_direction/code/extract_activations_large.py`
- `/root/xling_calib_direction/extract_activations_large.py`

---
