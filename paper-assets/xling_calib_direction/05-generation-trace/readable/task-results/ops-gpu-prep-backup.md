# ops gpu prep backup

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_prep_backup_20260520T203335_result.json`
- **Structured JSON:** [`6742c1907cc4ec7c14e5.json`](../../sessions/67/6742c1907cc4ec7c14e5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息收集完毕，以下是三部分结果。

---

## Part 1: 备份状态

| 目录 | 文件数 | 大小 | 采样验证 |
|------|--------|------|----------|
| activations (mvp_001) | 48 .pt | 9.1G | OK (14042×3584) |
| activations_mvp002 | 42 .pt | 7.9G | OK (14042×3584) |
| activations_mvp003 | 54 .pt | 12G | OK (14042×4096) |
| probes_mvp001/002/003 | 9+8+10 | — | — |
| results_mvp001/002/003 | 5+4+5 | — | — |

**备份完成**: `/root/autodl-tmp/xling_backup/`，总计 **29G**，9 个子目录。所有采样 .pt 文件 `torch.load` 验证通过。

---

## Part 2: 磁盘空间 & 大模型可行性

### 磁盘

| 分区 | 总量 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| 根 `/` | 30G | ~30G | **620M** | **98%** |
| 数据盘 `/root/autodl-tmp/` | 350G | ~60G | **~290G** | 17% |

已有模型：Qwen2.5-7B (15G) + Llama-3.1-8B (15G) = 30G

**根分区告急（620M）**，后续所有大文件必须放数据盘。

### 大模型估算

| 模型 | 总参数 | FP16 磁盘 | INT8 磁盘 | INT4 磁盘 | INT8 VRAM | INT4 VRAM |
|------|--------|-----------|-----------|-----------|-----------|-----------|
| Qwen3-235B-A22B | 235B (22B active MoE) | ~470G | ~235G | ~120G | ~240G | ~125G |
| Llama 4 Scout 17B-16E | 109B (17B active MoE) | ~218G | ~110G | ~55G | ~115G | ~60G |

VRAM 预算：4× RTX 6000 PRO 96GB = **384GB**

### 可行性判定

| 模型 | FP16 | INT8 | INT4 |
|------|------|------|------|
| **Qwen3-235B** 磁盘 | 不够(290G<470G) | 勉强(290G>235G) | 够(290G>>120G) |
| **Qwen3-235B** VRAM | 不够(384G<470G) | 够(384G>240G) | 够(384G>>125G) |
| **Llama 4 Scout** 磁盘 | 够(290G>218G) | 够 | 够 |
| **Llama 4 Scout** VRAM | 不够(384G<218G+overhead) | 够(384G>115G) | 够 |

**注意**：`output_hidden_states=True` 会缓存所有层 hidden state。Qwen3 有 **94 层**（vs 当前 Qwen2.5-7B 的 28 层），隐藏维度约 **30720**（MoE 路由后）。单个样本全层 hidden state 可能占 ~20GB+，会显著增加 VRAM 峰值。

### 推荐量化方案

**bitsandbytes INT8/INT4**（最简单，改一行加载代码）：
- 已装 `accelerate`，只需 `pip install bitsandbytes`
- Qwen3-235B → **INT4** (`load_in_4bit=True`)，VRAM ~125G，4 GPU 充裕
- Llama 4 Scout → **INT8** (`load_in_8bit=True`)，VRAM ~115G，2 GPU 即可
- 两个模型可分别跑（不能同时加载）

---

## Part 3: 代码适配清单

现有 `extract_activations.py`（203 行）的模型加载：
```python
# L130-131: 当前加载方式
model = AutoModelForCausalLM.from_pretrained(
    args.model, torch_dtype=dtype, device_map="auto", trust_remote_code=True)
# L174: 逐样本推理
out = model(**inputs, output_hidden_states=True)
```

### 必须改动

| 文件 | 改动项 | 原因 |
|------|--------|------|
| `extract_activations.py` | 添加 `--load_in_8bit` / `--load_in_4bit` 参数 | 量化加载 |
| `extract_activations.py` | `BitsAndBytesConfig` + `quantization_config=` | bitsandbytes 集成 |
| `extract_activations.py` | **用 register_forward_hook 替代 `output_hidden_states=True`** | 94 层全缓存会 OOM，hook 只抓指定层 |
| `extract_activations.py` | `--max_length` 参数（当前硬编码 4096） | 不同模型 context 不同 |
| `extract_activations.py` | 抽取后 `.cpu()` 并 `del` 中间结果 | 大模型显存紧张 |
| `run_plan_001.sh` | 层索引（Qwen3: 94 层，采样如 0,10,20,30,47,60,70,80,93） | 层数不同 |
| `run_plan_002.sh` | 层索引（Scout: ~48 层） | 层数不同 |

### 无需改动

| 文件 | 原因 |
|------|------|
| `train_probe.py` | 只处理 .pt 文件，与模型大小无关 |
| `transfer_eval.py` | 同上 |
| `analyze_results.py` | 同上 |

### 需要安装的包

```bash
pip install bitsandbytes  # 量化（目前未安装）
# accelerate 已装 (1.13.0)
# flash-attn 未装（可选，加速推理但不影响正确性）
```

### 关键风险

1. **hidden_dim 变化**：Qwen3-235B hidden_dim ~4096 或 8192（MoE 专家之间共享），需确认实际维度后调整 probe 输入维度
2. **output_hidden_states 显存炸裂**：94 层 × batch × seq_len × hidden_dim → 必须用 hook 方案
3. **根分区 620M**：任何临时文件/日志都可能撑爆根盘，所有输出必须指向 `/root/autodl-tmp/`

---
