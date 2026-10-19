# diagnose plan 002

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_plan_002_20260521T114903_result.json`
- **Structured JSON:** [`1b3c52df2e335044e322.json`](../../sessions/1b/1b3c52df2e335044e322.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

确认了，脚本中不存在 `--gpu_id` 参数。

## 诊断结论

### 失败根因

启动命令缺少 **`--model_name`** 必选参数。argparse 直接报错退出，EXIT_CODE=2。

完整命令：
```bash
python -u code/extract_activations.py \
  --model_path /root/autodl-tmp/models/Llama4-Scout-W4A16/RedHatAI/Llama-4-Scout-17B-16E-Instruct-quantized___w4a16/ \
  --layers 0,4,8,12,16,20,24,28,32,36,40,44,47 \
  --languages en,zh,ar,hi,sw,ko,es,fr,de,ru,tr,bn,ja,pt,vi,te,id,pl,nl,uk \
  --output_dir /root/autodl-tmp/activations/llama4_scout/ \
  --gpu_id 0   # ← 脚本不认识此参数
```

缺少：`--model_name llama4_scout_w4a16`（或类似短名称）

额外问题：`--gpu_id 0` 不是合法参数（脚本用的是 `--device_map`），但 argparse 先因 `--model_name` 缺失而退出，还没来得及报这个错。

### 模型下载状态

完整。14 个 safetensors shard 全部存在，总计 61GB。

### 修复方案

重新提交时命令改为：
```bash
python -u code/extract_activations.py \
  --model_path /root/autodl-tmp/models/Llama4-Scout-W4A16/RedHatAI/Llama-4-Scout-17B-16E-Instruct-quantized___w4a16/ \
  --model_name llama4_scout_w4a16 \
  --layers 0,4,8,12,16,20,24,28,32,36,40,44,47 \
  --languages en zh ar hi sw ko es fr de ru tr bn ja pt vi te id pl nl uk \
  --output_dir /root/autodl-tmp/activations/llama4_scout/ \
  --device_map auto
```

变更点：
1. **加上 `--model_name llama4_scout_w4a16`**
2. **`--gpu_id 0` → `--device_map auto`**（或删除，默认就是 auto）
3. **`--languages` 用空格分隔**（nargs="+" 需要空格分隔，不是逗号）— 当前逗号写法会被 argparse 视为一个整体字符串，虽然不会报错退出，但下游加载数据集时会失败

---
