# Plan 003: SWE-bench Lite 端到端评估方案

> 日期: 2026-05-14 | 状态: 基础设施就绪，等待 M2 训练完成

## 1. 目标

在 SWE-bench Lite (300 instances) 上评估 StructFuse 训练的检索模型，衡量 **retrieval quality** 和 **end-to-end resolve rate**。

对比 3 strategies × best checkpoint:
- `random` (baseline)
- `embedding_distance`
- `dataflow_aware`

## 2. 服务器环境现状

| 项目 | 状态 |
|------|------|
| 硬件 | 2× RTX PRO 6000 96GB (Blackwell), 均在跑 M2 训练 |
| 磁盘 | root: 22GB free / autodl-tmp: 100GB free |
| Python | conda base, Python 3.x |
| ML 栈 | torch 2.10+cu128, transformers 4.57.6, vllm 0.18.1, peft 0.19, datasets 4.8.4 |
| swebench | **4.1.0 已安装** |
| sb-cli | **0.1.5 已安装** |
| Docker | **不可用** (AutoDL 容器内无 Docker daemon) |
| 数据集 | **SWE-bench Lite 已下载** → `/root/autodl-tmp/swebench/swebench_lite` (300 instances, 12 repos) |

## 3. 现有代码资产

### 3.1 Retrieval 评估 (完整可用)
**`/root/structfuse/evaluation/eval_swebench.py`**
- 功能: 文件级检索评估 (Recall@k, MRR)
- 流程: clone repo → 收集 .py 文件 → StructFuseRetriever encode → cosine rank → 与 gold patch 文件对比
- 支持: dry-run, resume, batch encoding
- StructFuseRetriever: 加载 model.pt + training_config.json, mean-pool + projection, 截断 12000 chars

### 3.2 端到端框架 (有 placeholder)
**`/root/structfuse/scripts/eval_swebench.py`**
- 功能: retrieval → LLM agent → patch → verify → resolve rate + bootstrap CI
- 状态: `load_retriever()`, `retrieve_top_k_files()`, `generate_patch()`, `verify_patch()` 均为 **PLACEHOLDER**
- 需要: 实现 LLM agent 调用, patch 验证

### 3.3 Checkpoint 目录
```
/root/autodl-tmp/structfuse/checkpoints/
├── m2_full_qwen/
│   └── random_s42/
│       ├── best_by_val_loss/
│       └── best_by_recall_at_1/
└── m2_full_starcoder/
    └── random_s42/
        ├── best_by_val_loss/
        └── best_by_recall_at_1/
```
训练完成后预期:
```
m2_full_qwen/{random,embedding_distance,dataflow_aware}_s{42,123,7}/best_by_{val_loss,recall_at_1}/
```
每个 checkpoint 包含: `model.pt`, `training_config.json`, tokenizer files

### 3.4 模型架构
- Backbone: Qwen2.5-Coder-3B (bi-encoder)
- LoRA on q_proj, v_proj (r=16, alpha=32)
- Projection: hidden → 256-dim, L2 normalized
- InfoNCE loss with weighted positives (dataflow distance)

## 4. 评估流水线设计

### Stage A: Retrieval-Only 评估 (可立即执行)

```
[SWE-bench instance] → clone repo@base_commit → 收集 .py 文件
                     → StructFuse encode(issue, files)
                     → cosine similarity rank
                     → Recall@{1,5,10,20}, MRR
```

**已有完整代码** (`evaluation/eval_swebench.py`)，训练完成后直接跑:
```bash
python evaluation/eval_swebench.py \
    --checkpoint-path /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/dataflow_aware_s42/best_by_recall_at_1 \
    --swebench-split lite \
    --output-dir /root/autodl-tmp/structfuse/eval_results/qwen_dataflow_s42_recall
```

每 strategy 每 seed 一次，共 3 strategies × 3 seeds × 2 checkpoints = 18 runs (可并行)。

**资源**: 主要是 CPU (git clone) + 少量 GPU (encoding)。每 instance ~30s encoding + ~60s clone = ~90s。300 instances ≈ 7.5h per run。

### Stage B: End-to-End 评估 (需要实现)

```
[SWE-bench instance] → Stage A retrieval → top-k files
                     → 拼接 prompt (issue + retrieved files)
                     → Qwen3.6-27B 生成 patch
                     → 验证 patch → resolve rate
```

#### B1: LLM Agent (Agentless-style)

**推荐方案: Agentless Lite 风格**
- 不用复杂 agent loop, 单轮生成
- 输入: issue text + top-k retrieved files (来自 StructFuse)
- 输出: unified diff patch
- 重试: 采样 N 个 candidate patches, 选最优

**Agent LLM: Qwen3.6-27B**
- 最新 (2026-04-22), Apache 2.0
- 262K context window, 77.2 on SWE-bench Verified
- vllm 0.18.1 已安装, 可本地推理
- 显存需求: ~60GB (FP16), 单卡 96GB 足够
- **注意**: 训练占满两张卡期间不能用, 需训练完成后

**Prompt 设计** (参考 Agentless):
```
You are a software engineer. Given the following GitHub issue and relevant source files,
generate a patch that fixes the issue.

## Issue
{problem_statement}

## Relevant Files
{for each file in top_k_files:}
### {file_path}
```python
{file_content (truncated to fit context)}
```

## Instructions
Generate a unified diff patch that fixes the issue. Only modify the minimum necessary code.
Output the patch in the following format:
```diff
--- a/path/to/file.py
+++ b/path/to/file.py
@@ ... @@
...
```
```

#### B2: Patch 验证

**核心问题: 服务器无 Docker**

SWE-bench 官方 harness 需要 Docker 来运行测试验证。AutoDL 容器内嵌套 Docker 不可行。

**方案对比**:

| 方案 | 优点 | 缺点 | 推荐度 |
|------|------|------|--------|
| A: sb-cli 云端评估 | 官方验证, 结果可信 | 需注册/可能收费, 网络依赖 | ★★★★ |
| B: Modal 云端评估 | swebench 内置支持 | 需 Modal 账号 + API key | ★★★ |
| C: 另一台有 Docker 的机器 | 完全控制 | 需要额外机器 | ★★★ |
| D: 仅做 retrieval 评估 | 零依赖, 可立即执行 | 无 resolve rate | ★★★ (先行) |
| E: 简化验证 (apply patch + lint) | 轻量 | 不等价于跑测试 | ★ |

**推荐路径**: **D → A**
1. 先跑 Stage A retrieval-only (无依赖, 论文最核心指标)
2. 然后用 sb-cli 或 Modal 提交 patches 做官方验证

## 5. 执行计划

### Phase 1: 训练完成前 (现在 → May 17-18)

- [x] 安装 swebench 4.1.0, sb-cli 0.1.5
- [x] 下载 SWE-bench Lite 数据集 (300 instances, 12 repos, 已验证完整)
- [x] Dry-run retrieval 评估通过 (5 mock instances, pipeline 正常)
- [ ] 完善 `scripts/eval_swebench.py` — 实现 LLM agent 集成 (placeholder → real)
- [ ] 注册 sb-cli 或 Modal 账号 (解决 Docker 问题)
- [ ] 预 clone SWE-bench repos (300 instances 涉及 11 repos) → 存到 `/root/autodl-tmp/swebench/repos/`

### Phase 2: Retrieval 评估 (M2 训练完成后, ~May 18)

对 best checkpoint 跑 retrieval:
```bash
# 每 strategy 跑一次, 3 strategies × best-by-recall_at_1
for strategy in random embedding_distance dataflow_aware; do
  python evaluation/eval_swebench.py \
    --checkpoint-path /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/${strategy}_s42/best_by_recall_at_1 \
    --swebench-split lite \
    --output-dir /root/autodl-tmp/structfuse/eval_results/swebench_qwen_${strategy}
done
```

预计: 3 runs × ~7.5h = ~22.5h (可 2 runs 并行用两张卡 → ~15h)

### Phase 3: End-to-End 评估 (May 18-19)

1. 用 vllm 启动 Qwen3.6-27B 推理服务 (单卡)
2. 对每个 strategy 的 top-10 retrieved files, 生成 patches
3. 用 sb-cli submit 提交验证

预计: 300 instances × 3 strategies × ~2min/instance = ~30h (单卡推理)

### Phase 4: 结果分析

- 3 strategies resolve rate + 95% bootstrap CI
- Retrieval recall vs resolve rate 相关性分析
- 按 repo/difficulty 分层分析

## 6. 依赖清单

### 已就绪 ✓
- [x] swebench 4.1.0
- [x] sb-cli 0.1.5
- [x] torch, transformers, vllm, peft, datasets
- [x] SWE-bench Lite 数据集 (已下载验证: 300 instances, 12 repos)
- [x] evaluation/eval_swebench.py (retrieval 评估脚本)

### 待完成 ✗
- [ ] **Docker 替代方案**: 注册 sb-cli 或 Modal 账号
- [ ] **Qwen3.6-27B 模型**: 需下载 (~60GB) 到 `/root/autodl-tmp/models/`
- [ ] **端到端脚本完善**: `scripts/eval_swebench.py` 的 4 个 placeholder 函数
- [ ] **Repo 预 clone**: 11 repos 预先 clone 到数据盘
- [ ] **sb-cli 认证**: 需要注册 + API key
- [ ] **GPU 空闲**: 等 M2 训练完成释放 GPU

### 磁盘空间估算
| 项目 | 大小 |
|------|------|
| SWE-bench Lite 数据集 | ~5 MB |
| 11 repos clone (sparse) | ~2-5 GB |
| Qwen3.6-27B 模型 (FP16) | ~55 GB |
| 评估输出 (per-instance results) | ~100 MB |
| 总计 | ~60 GB |
| autodl-tmp 剩余 | 100 GB → 充足 |

## 7. 时间/资源估算

| 阶段 | GPU 需求 | 时间 | 备注 |
|------|---------|------|------|
| Stage A: Retrieval (3 strategies) | 1 GPU (~4GB) | ~15-22h | clone 是瓶颈, 可预缓存 |
| Stage B: LLM 推理 (900 instances) | 1 GPU (~60GB) | ~30h | Qwen3.6-27B via vllm |
| Stage B: Patch 验证 (900 patches) | 0 (cloud) | ~数小时 | sb-cli 提交 |
| 结果分析 | 0 | ~2h | |
| **总计** | **≤40h GPU** | **~2-3天** | 在 40h budget 内 |

## 8. 风险和备选方案

| 风险 | 影响 | 缓解 |
|------|------|------|
| sb-cli 不免费或有限额 | 无法验证 patches | 用 Modal ($30 credit), 或仅报 retrieval metrics |
| Qwen3.6-27B 太大放不下 | 无法本地推理 | 用 Qwen3.6-27B-GPTQ/AWQ 量化版, 或 Qwen3-14B |
| Retrieval 质量太差 | Resolve rate 低 | 增大 top-k (10→20), 结合 BM25 hybrid |
| Clone repos 失败 (AutoDL 网络) | 部分 instance 跳过 | 预 clone + 重试, 用 `source /etc/network_turbo` |
| GPU 不够 (训练未完成) | 时间线推迟 | Stage A retrieval GPU 需求小, 可与训练共存 |

## 9. 论文中的呈现

### 核心 Table: SWE-bench Lite Retrieval
| Strategy | Recall@1 | Recall@5 | Recall@10 | MRR |
|----------|----------|----------|-----------|-----|
| Random (baseline) | - | - | - | - |
| Embedding distance | - | - | - | - |
| Dataflow-aware | - | - | - | - |

### 可选 Table: End-to-End Resolve Rate
| Strategy | Resolve Rate | 95% CI |
|----------|-------------|--------|
| Random | - | - |
| Embedding distance | - | - |
| Dataflow-aware | - | - |
| BM25 (reference) | - | - |

Retrieval 指标是论文核心主张的直接证据; resolve rate 是锦上添花 (证明 retrieval 改善传导到下游)。
