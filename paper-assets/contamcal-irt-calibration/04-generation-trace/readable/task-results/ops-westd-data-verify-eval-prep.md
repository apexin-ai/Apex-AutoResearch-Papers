# ops westd data verify eval prep

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd-data-verify-eval-prep_20260518T065728_result.json`
- **Structured JSON:** [`f1656c216f9d09babb88.json`](../../sessions/f1/f1656c216f9d09babb88.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总结果如下：

---

## 任务 1: SFT 数据验证

### 文件清单 + 行数

| 文件 | 行数 | 大小 |
|------|------|------|
| `sft_dosage_000.jsonl` | 50,000 | 88MB |
| `sft_dosage_005.jsonl` | 50,826 | 89MB |
| `sft_dosage_025.jsonl` | 54,133 | 90MB |
| `sft_dosage_050.jsonl` | 58,266 | 92MB |
| `sft_dosage_100.jsonl` | 66,533 | 96MB |

### 辅助文件
- `data_meta.json` — 完整元数据（base 50K, contam 16533 总样本, benchmarks: arc_challenge=1172, gsm8k=1319, mmlu=14042）
- `data_meta_0pct.json` — d000 元数据（SlimOrca, 50K, seed=42）
- `contamination_labels_*.json` — 3 benchmarks × 4 dosages (d005/d025/d050/d100) = 12 个标签文件

### 数据完整性
- **dosage 齐全**: d000 (0%), d005 (5%), d025 (25%), d050 (50%), d100 (100%) — 5 个 level 全部到位
- **行数合理**: d000=50K base，每个 dosage 增量与污染比例一致（d005 +826, d025 +4133, d050 +8266, d100 +16533）
- **JSON 格式正确**: 抽样确认为 `{"messages": [{"role":..., "content":...}, ...]}` 标准 chat format
- **注意**: data_meta 里有 d050 dosage（50%），但 cqa1 上原始项目只提到 d000/d005/d025/d100。**d050 是 westd 新增还是遗漏待确认**

---

## 任务 2: Eval 脚本

| 脚本 | 功能 |
|------|------|
| `exp001/train_sft.py` | LoRA SFT 训练（peft + trl） |
| `exp001/evaluate.py` | Benchmark 评估（MMLU 5-shot, GSM8K 8-shot CoT, ARC-Challenge 25-shot, HumanEval pass@1），输出 per-item correctness matrix |
| `exp001/prepare_sft_data.py` | 构建 SFT 混合数据 |
| `exp001/rescore_gsm8k.py` | GSM8K 重新评分 |
| `exp002/compute_signals.py` | 信号提取主脚本 |
| `exp002/signals/s1_embedding.py` ~ `s4_selfcritique.py` | 4 种信号：embedding/minkpp/constat/selfcritique |
| `exp002/run_batch.py` | 批量信号计算 |
| `exp006/` | IRT 校准全套（2PL/4PL, baselines, ablation 等） |
| `exp008/` | Signal survival analysis |
| `scripts/gen_eval_matrix.py` | 生成 eval 结果汇总矩阵 |

**eval 脚本支持 7B/14B**: 配置文件已就绪（`configs/qwen25_7b.yaml`, `qwen25_14b.yaml`, `qwen25_14b_qlora.yaml`, `llama31_8b.yaml`），参数已针对大模型调整（14B: bs=1, grad_accum=16）。

---

## 任务 3: 环境就绪度

| 项目 | 状态 |
|------|------|
| Python | `/root/miniconda3/bin/python3` 3.12.3 — **不在 PATH 中**，需 `export PATH=/root/miniconda3/bin:$PATH` 或用绝对路径 |
| PyTorch | 2.8.0+cu128, CUDA available |
| GPU | 4× NVIDIA RTX PRO 6000 Blackwell (98GB VRAM each), **全部空闲**（0MB 使用） |
| 依赖 | peft, trl, transformers 均可导入 |
| CUDA | Driver 580.82.09, CUDA 13.0 |

---

## 关键问题

1. **模型下载未完成** — 3 个模型全部正在下载中（`download_all.sh` PID 5060 运行中），当前只有 config/tokenizer 文件，**无 .safetensors 权重文件**：
   - Qwen2.5-7B: 480MB / ~15GB（4 个 shard .incomplete）
   - Qwen2.5-14B: 3.6GB / ~28GB（8 个 shard .incomplete）
   - Mistral-7B-v0.3: 962MB / ~15GB（4 个 shard .incomplete）
   - 7B 之前下载超时重试过多次（dl_7b.log 显示 timeout errors）

2. **Python 不在 PATH** — 所有脚本用 `python3` 调用会失败，需要先 `conda init` 或设置 PATH

3. **d050 dosage** — westd 上有 d050 数据，需确认这是否是预期的（cqa1 原始设计里有 d000/d005/d025/d100，d050 可能是后来补充的）

---
