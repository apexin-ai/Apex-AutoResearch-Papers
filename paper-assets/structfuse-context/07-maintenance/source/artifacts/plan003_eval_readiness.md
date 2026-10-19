# Plan 003: SWE-bench Lite 评估就绪报告

> 生成时间: 2026-05-14
> 服务器: bjb1-42106 (2× RTX PRO 6000 Blackwell, 98GB each)

---

## 1. 就绪检查清单

| # | 项目 | 状态 | 备注 |
|---|------|------|------|
| 1 | StructFuseRetriever import | ✓ | evaluation/eval_swebench.py 可正常导入 |
| 2 | swebench | ✓ | 4.1.0 |
| 3 | sb-cli | ✓ | 0.1.5 |
| 4 | vLLM | ✓ | 0.18.1（≥0.17.0 required for Qwen3.6） |
| 5 | SWE-bench Lite 数据集 | ✓ | 300 instances，HF cache 可离线加载（`HF_DATASETS_OFFLINE=1`） |
| 6 | 12 repos bare clone | ✓ | `/root/autodl-tmp/swebench/repos/`，单下划线命名，两个脚本均兼容 |
| 7 | bare repo checkout 测试 | ✓ | django clone + checkout 正常 |
| 8 | M2 Qwen checkpoint | ✓ | `best_by_recall_at_1` (6.2GB) + `best_by_val_loss` 均存在 |
| 9 | M2 StarCoder checkpoint | ✓ | `best_by_recall_at_1` (6.1GB) + `best_by_val_loss` 均存在 |
| 10 | retrieval eval 脚本 | ✓ | `evaluation/eval_swebench.py` — dry-run 已通过 |
| 11 | end-to-end eval 脚本 | ✓ | `scripts/eval_swebench.py` — 所有函数已实现（generate_patch 支持 mock/API） |
| 12 | Qwen3.6-27B 模型下载 | ✗ | 未下载，需 ~60GB（BF16）或 ~30GB（FP8） |
| 13 | openai pip 包（API模式） | ✓ | 2.24.0 |
| 14 | 磁盘空间 | ✓ | 97GB 可用（250GB 总量） |
| 15 | 网络代理 | ⚠ | HF 直连不可达，需 `source /etc/network_turbo` 或用 `HF_DATASETS_OFFLINE=1` |

---

## 2. Eval 命令

### 环境准备（所有命令前置）

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/structfuse-context
export HF_DATASETS_OFFLINE=1
```

### Stage A: Retrieval-Only（无需 LLM，无需额外 GPU）

评估 retriever 在 SWE-bench Lite 上的 Recall@k / MRR。

```bash
# === Qwen backbone, best_by_recall_at_1 ===
python evaluation/eval_swebench.py \
    --checkpoint-path /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1 \
    --output-dir /root/autodl-tmp/structfuse/eval_results/swebench_retrieval/qwen_recall \
    --repo-cache-dir /root/autodl-tmp/swebench/repos \
    --top-k 1,5,10,20 \
    --swebench-split lite

# === StarCoder backbone, best_by_recall_at_1 ===
python evaluation/eval_swebench.py \
    --checkpoint-path /root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42/best_by_recall_at_1 \
    --output-dir /root/autodl-tmp/structfuse/eval_results/swebench_retrieval/starcoder_recall \
    --repo-cache-dir /root/autodl-tmp/swebench/repos \
    --top-k 1,5,10,20 \
    --swebench-split lite

# === Qwen backbone, best_by_val_loss ===
python evaluation/eval_swebench.py \
    --checkpoint-path /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_val_loss \
    --output-dir /root/autodl-tmp/structfuse/eval_results/swebench_retrieval/qwen_valloss \
    --repo-cache-dir /root/autodl-tmp/swebench/repos \
    --top-k 1,5,10,20 \
    --swebench-split lite

# === StarCoder backbone, best_by_val_loss ===
python evaluation/eval_swebench.py \
    --checkpoint-path /root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42/best_by_val_loss \
    --output-dir /root/autodl-tmp/structfuse/eval_results/swebench_retrieval/starcoder_valloss \
    --repo-cache-dir /root/autodl-tmp/swebench/repos \
    --top-k 1,5,10,20 \
    --swebench-split lite
```

预计时间：每个 checkpoint ~30-60 min（300 instances × repo checkout + encoding），4 runs 共 ~2-4h，使用 1 张 GPU。

### Stage B: End-to-End（Retriever + LLM Agent）

需先启动 vLLM 服务（见下方方案），然后：

```bash
# 在 GPU 1 上启动 vLLM（见 Section 3）
# 然后在另一个终端：

export STRUCTFUSE_LLM_BACKEND=api
export STRUCTFUSE_LLM_API_BASE=http://localhost:8000/v1
export STRUCTFUSE_LLM_API_KEY=[REDACTED]
export STRUCTFUSE_LLM_MODEL=Qwen/Qwen3.6-27B

# 用最佳 retriever checkpoint
python scripts/eval_swebench.py \
    --retriever-checkpoint /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1 \
    --strategy random \
    --top-k 10 \
    --agent-model Qwen/Qwen3.6-27B \
    --swebench-dataset princeton-nlp/SWE-bench_Lite \
    --output-dir /root/autodl-tmp/structfuse/eval_results/swebench_e2e/qwen_recall_qwen36 \
    --repo-cache-dir /root/autodl-tmp/swebench/repos
```

预计时间：300 instances × ~30s/instance（LLM 推理）≈ 2.5-4h。

---

## 3. Qwen3.6-27B 部署方案

### 方案 A: 本地 vLLM 部署（推荐）

**硬件需求：**
- BF16：单卡 ~54GB weights + KV cache → 1× RTX PRO 6000 (98GB) 完全足够
- FP8：单卡 ~30GB weights → 更充裕
- 当前服务器 2 卡配置：1 卡跑 vLLM，1 卡跑 retriever

**模型下载（需 `source /etc/network_turbo` 或用 ModelScope）：**
```bash
# HuggingFace（需代理）
source /etc/network_turbo
export HF_HOME=/root/autodl-tmp/.hf_cache
huggingface-cli download Qwen/Qwen3.6-27B --local-dir /root/autodl-tmp/models/Qwen3.6-27B

# 或 ModelScope（国内 CDN，更快）
pip install modelscope
python -c "from modelscope import snapshot_download; snapshot_download('Qwen/Qwen3.6-27B', cache_dir='/root/autodl-tmp/models/Qwen3.6-27B')"
```

**存储需求：** ~60GB（BF16）或 ~30GB（FP8）。当前 97GB 可用，BF16 下载后剩 ~37GB 足够。

**启动命令：**
```bash
CUDA_VISIBLE_DEVICES=1 vllm serve /root/autodl-tmp/models/Qwen3.6-27B \
    --max-model-len 65536 \
    --reasoning-parser qwen3 \
    --language-model-only \
    --enable-prefix-caching \
    --port 8000
```

`--max-model-len 65536` 足够覆盖 SWE-bench 场景（issue ~1K + 10 files × 5K = ~50K tokens），同时控制 KV cache 内存。

**优点：** 零边际成本，可反复调参，无 API 延迟
**缺点：** 需要下载模型（~60GB），占用 1 张 GPU

### 方案 B: API 调用

| 供应商 | 模型 | Input $/1M | Output $/1M | 备注 |
|--------|------|-----------|-------------|------|
| DashScope (阿里云) | qwen3.5-27b | $0.086 | $0.688 | 最便宜，国内低延迟 |
| OpenRouter | Qwen3.6-27B | $0.32 | $3.20 | 多 provider 路由 |
| Fireworks | Qwen3.6 Plus | $0.50 | $3.00 | 含 cached input $0.10/1M |

**300 instances 成本预估（DashScope）：**
- 每 instance input ≈ 40K tokens（issue + top-10 files）
- 每 instance output ≈ 2K tokens（patch）
- 总 input: 12M tokens → $1.03
- 总 output: 0.6M tokens → $0.41
- **总计: ~$1.44**（OpenRouter ~$5.76，Fireworks ~$7.80）

**优点：** 无需下载模型，不占 GPU，立即可用
**缺点：** 需 API key，受网络限制（需 `source /etc/network_turbo`），每次 re-run 有成本

### 推荐

**方案 A（本地 vLLM）**。理由：
1. 2× 98GB GPU 完全够用，一卡 retriever 一卡 LLM
2. 零边际成本，可反复调参（top-k, prompt template）
3. vLLM 0.18.1 已装好，无额外依赖
4. 避免 AutoDL 网络不稳定影响 API 调用
5. 本地推理延迟更低，300 instances 预计 2.5h（vs API 可能受限速）

如果需要快速跑通验证 pipeline 正确性，可先用方案 B（DashScope，$1.44），跑 10-20 instances smoke test。

---

## 4. 资源需求

### GPU 分配

| 阶段 | GPU 需求 | 预计时间 | 说明 |
|------|---------|---------|------|
| Stage A: Retrieval | 1× GPU（retriever 推理） | ~2-4h（4 checkpoints） | 可串行跑，单卡即可 |
| Stage B: End-to-End | 2× GPU（1 vLLM + 1 retriever） | ~2.5-4h | 两卡并行 |
| 模型下载 | 0 GPU | ~30min | 受网络带宽限制 |

### 磁盘

| 项目 | 大小 | 路径 |
|------|------|------|
| Qwen3.6-27B 模型（BF16） | ~60GB | /root/autodl-tmp/models/Qwen3.6-27B |
| eval 结果输出（6 runs） | ~1GB | /root/autodl-tmp/structfuse/eval_results/ |
| repo checkout 临时文件 | ~5-10GB | eval output_dir/_repos/ |
| **总计新增** | **~70GB** | 当前可用 97GB，剩余 ~27GB |

### API Key（仅方案 B）

- DashScope: 阿里云 API key
- OpenRouter: OpenRouter API key
- 方案 A 不需要任何 key

---

## 5. 依赖清单

| 包 | 版本 | 状态 | 用途 |
|----|------|------|------|
| torch | ≥2.0 | ✓ 已装 | retriever 推理 |
| transformers | ≥4.40 | ✓ 已装 | 模型加载 |
| datasets | ≥2.0 | ✓ 已装 | SWE-bench 数据加载 |
| numpy | any | ✓ 已装 | bootstrap CI |
| tqdm | any | ✓ 已装 | 进度条 |
| swebench | 4.1.0 | ✓ 已装 | SWE-bench 工具 |
| sb-cli | 0.1.5 | ✓ 已装 | SWE-bench CLI |
| vllm | 0.18.1 | ✓ 已装 | LLM 推理服务 |
| openai | 2.24.0 | ✓ 已装 | API 模式 generate_patch |

安装缺失依赖（如需）：
```bash
pip install openai
```

---

## 6. 风险和 Blockers

| 风险 | 严重性 | 缓解措施 |
|------|--------|---------|
| HF 网络不可达 | 中 | 已有本地 cache，用 `HF_DATASETS_OFFLINE=1`；下载模型时 `source /etc/network_turbo` |
| Qwen3.6-27B 下载慢 | 中 | 优先用 ModelScope CDN；或用 FP8 版本（30GB vs 60GB） |
| 磁盘空间紧张（下载后剩 ~27GB） | 低 | repo checkout 临时文件可在 eval 间清理；或用 FP8 省 30GB |
| bare repo fetch 特定 commit 失败 | 低 | bare clone 包含完整历史，checkout 应直接成功；已通过 django 验证 |
| generate_patch 默认 mock 模式 | 无 | Stage A 不需要 LLM；Stage B 需设置 `STRUCTFUSE_LLM_BACKEND=api` |
| M2 训练仍在进行中 | 阻断 | 需等最终 checkpoint 产出完成后再跑 Stage A |
| ~~openai 包未安装~~ | ~~低~~ | ✓ 已装 2.24.0，无风险 |

---

## 7. 执行建议

1. **M2 训练完成后 → 立即跑 Stage A**（retrieval-only），无需下载任何额外模型
2. Stage A 跑的同时 → **后台下载 Qwen3.6-27B**（用第 2 张卡空闲期间不冲突）
3. Stage A 结果出来后 → 选最佳 retriever checkpoint → **跑 Stage B**
4. 如果只需要 retrieval 指标（Recall@k, MRR）来写论文，Stage A 即可，Stage B 是 bonus
