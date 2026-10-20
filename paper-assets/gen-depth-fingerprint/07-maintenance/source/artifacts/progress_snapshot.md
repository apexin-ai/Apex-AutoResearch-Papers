# 实验进度快照 — 2026-05-15

## 总览

| 实验 | 进度 | ETA | GPU | 状态 |
|------|------|-----|-----|------|
| plan-014 (Qwen3-8B) | 815/996 (82%) | ~49 min | cuda:0 75% | ✅ 正常 |
| plan-005-cont (Pythia-2.8B continuation) | 78/995 (8%) | ~1h50m | cuda:1 63% | ✅ 正常 |
| plan-005-elab (Pythia-2.8B elaboration) | 72/995 (7%) | ~2h18m | cuda:2 64% | ✅ 正常 |
| plan-005-rewrite (Pythia-2.8B rewriting) | 72/995 (7%) | ~2h02m | cuda:3 64% | ✅ 正常 |

## GPU 利用率

| GPU | 利用率 | 显存占用 |
|-----|--------|----------|
| cuda:0 | 75% | 16473 / 32607 MiB (50.5%) |
| cuda:1 | 63% | 6193 / 32607 MiB (19.0%) |
| cuda:2 | 64% | 6213 / 32607 MiB (19.0%) |
| cuda:3 | 64% | 6213 / 32607 MiB (19.0%) |

## 磁盘

| 分区 | 用量 | 剩余 |
|------|------|------|
| / (根) | 7.5G / 30G (25%) | 23G |
| /root/autodl-tmp (数据盘) | 123G / 250G (50%) | 128G |

## 详细信息

### plan-014 (Qwen3-8B 生成)
- **PID**: 134817 (nohup)，已运行 3h20m，状态 S (sleeping)
- **速度**: ~15-17s/it
- **日志**: `/tmp/gen_large_model.log`
- **输出文件**:
  - `data/qwen3-8b/generations_shard0.jsonl`: 416 行（当前写入中）
  - `data/qwen3-8b/generations_recovered.jsonl`: 3679 行（历史恢复）
  - `data/qwen3-8b/generations_shard0_recovered.jsonl`: 3679 行（历史恢复）
- **注意**: 有少量 seeds 因 empty output 被跳过（seed 611/619/622/637 等），不影响整体

### plan-005-cont (Pythia-2.8B continuation prompt)
- **tmux**: plan-005-cont
- **速度**: ~7-9s/it
- **输出**: `data/pythia-2.8b-continuation/generations_shard0.jsonl` — 396 行 (~5 行/seed)

### plan-005-elab (Pythia-2.8B elaboration prompt)
- **tmux**: plan-005-elab
- **速度**: ~8-9s/it
- **输出**: `data/pythia-2.8b-elaboration/generations_shard0.jsonl` — 373 行 (~5 行/seed)

### plan-005-rewrite (Pythia-2.8B inspired_rewriting prompt)
- **tmux**: plan-005-rewrite
- **速度**: ~8-9.5s/it
- **输出**: `data/pythia-2.8b-inspired_rewriting/generations_shard0.jsonl` — 373 行 (~5 行/seed)

## 异常检查
- ❌ 无 GPU 掉卡
- ❌ 无 OOM 错误
- ❌ 磁盘空间充足
- ⚠️ plan-014: 少量 seeds 产生空输出被跳过（正常行为）
- ⚠️ plan-005 三个实验日志显示 `Model loaded on cuda:0` — 因各 tmux session 设了 CUDA_VISIBLE_DEVICES，实际分别对应物理 GPU 1/2/3
