# research feature extraction code

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_feature-extraction-code_20260514T232106_result.json`
- **Structured JSON:** [`f45679d381086ae3148d.json`](../../sessions/f4/f45679d381086ae3148d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研完毕。汇总如下：

---

## 调研结果

### 1. 特征提取脚本

| 脚本 | 用途 | 关键参数 |
|------|------|----------|
| `extract_features.py` | MVP 单模型（pythia-2.8b）特征提取 | `--input`, `--output`, `--batch-size`, `--device`, `--dry-run` |
| `extract_features_multi.py` | **多生成器批量提取（已就绪）** | `--model-name`（增量单模型）, `--output`, `--batch-size`, `--device`, `--dry-run` |

**计算的特征（7 维）**：
- 参考模型特征（5）：`entropy_mean`, `entropy_std`, `entropy_min`, `entropy_max`, `tail_decay`
- 表面特征（2）：`ttr`（type-token ratio）, `hapax_ratio`

输出列：`model_name, seed_id, depth, entropy_mean, entropy_std, entropy_min, entropy_max, tail_decay, ttr, hapax_ratio`

### 2. 参考模型 Pythia-410M

- 路径：`/root/autodl-tmp/models/pythia-410m/models--EleutherAI--pythia-410m/snapshots/9879c9b5f8bea9051dcb0e68dff21493d67e9d4f/`
- 状态：**可用**，含 `model.safetensors`, `config.json`, `tokenizer.json` 等完整文件

### 3. 已有 features 输出

| 文件 | 行数 | 内容 |
|------|------|------|
| `data/features.csv` | 4609 条 | MVP 阶段 pythia-2.8b 的完整特征（id/depth/seed_id 索引） |
| `data/features_all.csv` | 20 条 | 多模型格式，仅含 pythia-2.8b（10 条）+ pythia-1b（10 条），**dry-run 测试产物** |

### 4. 是否需要修改脚本

**`extract_features_multi.py` 已经支持多模型批量提取**，无需修改。它：
- 硬编码了生成器列表：`["pythia-2.8b", "pythia-1b", "olmo-2-1b", "qwen3-1.7b", "qwen3-0.6b"]`
- 支持增量模式（`--model-name` 单独跑某个生成器）
- 支持去重、合并已有数据
- 但**只使用单张 GPU**（`--device cuda:0`），不支持原生 4 卡并行

若需 4 卡并行，方案是**手动分拆 4 个进程，每个指定不同 `--device` + `--model-name`**：

### 5. 建议启动命令模板（4 卡并行）

```bash
cd /root/gen-depth-fingerprint

# 方案：5 个生成器分配到 4 张卡（qwen3 两个小模型合一张）
nohup python extract_features_multi.py --model-name pythia-2.8b --device cuda:0 --batch-size 16 > /tmp/feat_pythia28.log 2>&1 &
nohup python extract_features_multi.py --model-name pythia-1b --device cuda:1 --batch-size 16 > /tmp/feat_pythia1b.log 2>&1 &
nohup python extract_features_multi.py --model-name olmo-2-1b --device cuda:2 --batch-size 16 > /tmp/feat_olmo.log 2>&1 &
nohup python extract_features_multi.py --model-name qwen3-1.7b --device cuda:3 --batch-size 16 > /tmp/feat_qwen17.log 2>&1 &
# qwen3-0.6b 等第一轮空出的卡再跑，或串行追加
```

注意：每个进程都会独立加载一份 Pythia-410M 参考模型（~800MB fp16），4 卡各自加载一份，显存无压力。增量模式会自动合并到 `data/features_all.csv`，但**并发写同一个 CSV 会冲突**——需要先各自写独立文件再 merge，或者串行执行合并步骤。

---
