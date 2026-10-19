# infra westd14391 setup plan

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_westd14391-setup-plan_20260523T215451_result.json`
- **Structured JSON:** [`0f16c6b5b2479df6deae.json`](../../sessions/0f/0f16c6b5b2479df6deae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

从日志中提取了完整的 westd-41302 数据目录和脚本信息。已收集齐全部信息，可以输出报告。

---

## 数据需求

### steering_experiment.py 输入文件

| 文件 | 用途 | Steering 必须 |
|------|------|:---:|
| `en_activations.pt` | 训练 probe 提取 steering direction | **是** |
| `en_conflict_test_verified.jsonl` | 评估 steering 效果的测试样本 | **是** |
| `probe_results.json` | 如果不指定 `--peak_layer` 则自动读取 peak layer | 可选（可用 `--peak_layer` 跳过） |
| `en_conflict_train*.jsonl` | collect_activations 的输入 | 仅重新生成 activations 时 |
| 其他 `de_*/zh_*` 文件 | 跨语言 probe/steering | L12/L14 不需要 |

### data/llama31/ 目录（westd-41302 上的完整内容）

```
en_activations.pt        ← 关键，估算 ~200-400 MB
de_activations.pt        ← 本次不需要
zh_activations.pt        ← 本次不需要
en_conflict_test.jsonl
en_conflict_test_verified.jsonl   ← 关键
en_conflict_train.jsonl
en_conflict_train_verified.jsonl
de_conflict_*.jsonl, zh_conflict_*.jsonl  ← 本次不需要
probe_results.json + bootstrap 变体
probe_weights/
steering_results/         ← 已有 L13/L18/L28 结果
各种分析 JSON
```

**Steering 必须文件**：`en_activations.pt` + `en_conflict_test_verified.jsonl`（+ 脚本）

## 模型需求

| 项目 | 值 |
|------|------|
| 路径 (westd-14391) | `/root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct` |
| 大小 | **15 GB**（已在 westd-14391 上） |
| 下载 | **不需要，已存在** |

## L13 参数参考（成功实验，p=0.0009）

```bash
CUDA_VISIBLE_DEVICES=3 OMP_NUM_THREADS=1 python src/steering_experiment.py \
  --model /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct \
  --data_dir data/llama31 \
  --peak_layer 13 \
  --alphas -20 -10 -5 5 10 20 \
  --position last \
  --output_suffix _L13_last
```

- **alphas**: `-20, -10, -5, 5, 10, 20`（最佳 α=-20, p=0.0009; α=5, p=0.002）
- **position**: `last`（all-position 结果完全相同）
- **测试样本**: 136 条
- **probe 精度**: 76.1%

## 代码需求

### Python 脚本

| 文件 | 来源 | 状态 |
|------|------|------|
| `src/steering_experiment.py` | westd-41302 生成，~365 行 | **本地不存在，需从 westd-41302 取或重新生成** |
| `src/collect_activations.py` | `artifacts/clkc_code/src/` | 本地有 |
| `src/train_probe.py` | `artifacts/clkc_code/src/` | 本地有 |
| 其他 5 个 .py | `artifacts/clkc_code/src/` | 本地有（steering 不直接需要） |

### Python 包依赖

```
torch, transformers, numpy, scipy, scikit-learn, matplotlib, tqdm
```

## 磁盘状况 (westd-14391)

| 分区 | 总量 | 已用 | 可用 |
|------|------|------|------|
| 根分区 `/` | 30 GB | 13 GB | 18 GB |
| 数据盘 `/root/autodl-tmp/` | 250 GB | 31 GB | **220 GB** |

## 关键阻塞与建议

1. **westd-41302 不在 SSH 工具可用列表中**。无法直接 scp 数据。需要：
   - 用户手动从 westd-41302 传 `en_activations.pt` + `en_conflict_test_verified.jsonl` + `steering_experiment.py`
   - 或在 westd-14391 上用 `collect_activations.py` 重新生成 `en_activations.pt`（需 ~10-20 分钟 GPU 时间，需要先传 JSONL 训练数据）

2. **steering_experiment.py 不在本地**。日志中保留了完整的前 100 行和 argparse 部分，但中间部分（steering hook、generation、evaluation 逻辑）缺失。需从 westd-41302 获取完整文件。

3. **建议传输方案**：如果 westd-41302 还能访问，`scp` 整个 `/root/clkc_mech_interp/` 到 westd-14391（数据盘 220GB 空间充足）。如果不能，最小路径是传 JSONL 数据（25MB）+ 重写 steering 脚本 + 重新生成 activations。

---
