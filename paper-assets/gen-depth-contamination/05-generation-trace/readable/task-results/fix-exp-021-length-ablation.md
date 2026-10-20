# fix exp 021 length ablation

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_exp_021_length_ablation_20260516T071052_result.json`
- **Structured JSON:** [`041b34b41bb477ca2d2e.json`](../../sessions/04/041b34b41bb477ca2d2e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完美运行。汇报：

1. **本地 C4 数据**: `/root/autodl-tmp/gen-depth-contamination/data_exp016_qwen_base/depth_0.jsonl`，5000 行。已复制到 `data/exp_021_length_{128,256,512}/` 三个目录。

2. **脚本修改**: 未改脚本文件本身。通过两个环境变量 `HF_DATASETS_OFFLINE=1` + `TRANSFORMERS_OFFLINE=1` 阻断所有 HF 网络调用。`prepare_seed_data` 检测到 depth_0.jsonl 已存在，自动跳过了 HF streaming。

3. **submit_training_job**: 成功，PID 20982，tmux session `exp_021_length_ablation`，日志 `~/runs/gen-depth-contamination/exp_021_length_ablation.log`。

4. **启动验证**:
   - nvidia-smi: cuda:3 有 python 进程（PID 20992，24MiB 初始占用，模型加载中）
   - 日志确认：模型加载完成 → seed data 跳过（"already exists with enough samples — skipping"）→ depth chain generation 已开始（"Generating depth 1 (5000 docs, batch_size=16)"）
   - 当前正在跑 length=128, depth 1，共 313 个 batch

---
