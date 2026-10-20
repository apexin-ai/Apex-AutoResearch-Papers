# ssh prepare next pipeline

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_prepare-next-pipeline_20260515T172851_result.json`
- **Structured JSON:** [`c39568c1fad88bb83a75.json`](../../sessions/c3/c39568c1fad88bb83a75.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已跑到 Layer 4，代码完全正常运行，不需要继续等完整 33 层。以下是验证结论：

---

## 验证结果

### Part 1: goal_classification dry-run — **通过**

- `--probe_type goal_classification` 已在 choices 中
- 9 个 task、412 条轨迹、33 层 × dim=4096
- dry-run 结果（3 epochs）：
  - Layer 0: acc=0.18（接近 9 类随机 0.11）
  - Layer 1: acc=0.97, F1=0.87
  - Layer 2-3: acc=1.00, F1=1.00（完美分类）
- 后台仍在跑剩余层（PID 632743），已确认无报错

### Part 2: analyze_goal_probes.py — **存在且可用**

- 5342 bytes，`--help` 输出正常
- 参数：`--trained_dir`, `--untrained_dir`, `--dino_dir`, `--acc_gate`, `--gap_gate`

### Part 3: DINO 提取准备 — **就绪**

- checkpoint 存在：`/root/autodl-tmp/vla-ssd/checkpoints/dinov2-large/`（model.safetensors + config.json）
- `extract_dinov2.py --help` 正常
- 待执行命令：
```bash
python scripts/extract_dinov2.py \
  --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ \
  --output_dir /root/autodl-tmp/vla-ssd/features/dinov2_libero_goal/ \
  --model_path /root/autodl-tmp/vla-ssd/checkpoints/dinov2-large \
  --gpu 0
```

### 注意事项

- GPU 0 当前 85% 利用率（正在跑提取任务），DINO 提取需等 GPU 0 空闲后执行
- `trained_libero_goal/` 有 8 个 h5 文件（9 个 task 但 `put_the_wine_bottle_on_top_of_the_cabinet` 在 feature 里有但不在文件列表——实际在 scan 时被检测到了 9 个 task，说明可能嵌入在某个 h5 中或还在提取中）
- 无 blocker，所有代码验证通过

---
