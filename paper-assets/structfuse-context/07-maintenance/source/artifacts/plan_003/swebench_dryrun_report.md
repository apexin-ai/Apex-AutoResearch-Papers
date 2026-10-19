# SWE-bench Lite Dry-Run 预检报告

**日期**: 2026-05-14  
**服务器**: bjb1-42106 (2x RTX PRO 6000 96GB)

---

## 检查结果

### 1. SWE-bench 数据

| 项目 | 状态 | 详情 |
|------|------|------|
| SWE-bench Lite 数据集 | ✅ 就绪 | `/root/autodl-tmp/swebench/swebench_lite/` (dev: 23, test: 300 instances) |
| 数据来源 | ✅ | `princeton-nlp/SWE-bench_Lite` (已缓存为 Arrow 格式) |
| 预克隆仓库 | ✅ 就绪 | `/root/autodl-tmp/structfuse/swebench_repos/` (12 repos, 667MB) |

预克隆仓库列表：PyCQA/pylint, astropy/astropy, django/django, matplotlib/matplotlib, mwaskom/seaborn, pallets/flask, psf/requests, pydata/xarray, pytest-dev/pytest, scikit-learn/scikit-learn, sphinx-doc/sphinx, sympy/sympy

### 2. 评估脚本

| 脚本 | 状态 | 用途 |
|------|------|------|
| `evaluation/eval_swebench.py` | ✅ 就绪 | 检索评估 (Recall@k, MRR)，支持 dry-run 模式 |
| `scripts/eval_swebench_e2e.py` | ✅ 就绪 | 端到端评估 (检索 + LLM 修复 + resolve rate + bootstrap CI) |

两个脚本均支持 `--repo-cache-dir` 指向预克隆仓库。

- `eval_swebench.py`: 纯检索评估，**不需要 LLM API，不需要 docker**
- `eval_swebench_e2e.py`: 需要 LLM backend（默认 mock，可设为 API 模式）

### 3. LLM API 依赖

| 项目 | 状态 | 详情 |
|------|------|------|
| openai SDK | ✅ 已安装 | `/root/miniconda3/lib/python3.12/site-packages/openai` |
| anthropic SDK | ✅ 已安装 | |
| vllm | ✅ 已安装 | 可本地部署 LLM（但需等 GPU 空闲） |
| API Keys (env) | ❌ 未配置 | 无 OPENAI_API_KEY / ANTHROPIC_API_KEY / STRUCTFUSE_LLM_API_KEY |

**E2E 脚本 LLM 配置方式**（环境变量）：
- `STRUCTFUSE_LLM_BACKEND`: `mock`(默认) / `api`
- `STRUCTFUSE_LLM_API_BASE`: API endpoint URL（默认 `http://localhost:8000/v1`）
- `STRUCTFUSE_LLM_API_KEY`: API key
- `STRUCTFUSE_LLM_MODEL`: 模型名

### 4. Python 环境

| 项目 | 状态 | 详情 |
|------|------|------|
| Python | ✅ | 3.12 (conda base) |
| swebench 包 | ✅ 已安装 | `/root/miniconda3/lib/python3.12/site-packages/swebench` |
| torch/transformers 等 | ✅ | 项目依赖均已安装 |
| Docker | ❌ 不可用 | AutoDL 容器无 docker-in-docker |

> Docker 缺失不影响我们的评估流程：两个评估脚本均不依赖 docker，自行管理 repo checkout 和 patch 验证。SWE-bench 官方 `run_evaluation.py` 需要 docker（做沙箱化测试执行），但我们的脚本绕过了这一依赖。

### 5. 磁盘空间

| 分区 | 总量 | 可用 | 使用率 |
|------|------|------|--------|
| / (root) | 30G | 20G | 34% |
| /dev/sda2 (数据盘) | 879G | 817G | 3% |

空间充足。

### 6. M2 Checkpoints

| Checkpoint | 状态 |
|-----------|------|
| `m2_full_qwen/random_s42` | ✅ best_by_val_loss + best_by_recall_at_1 |
| `m2_full_qwen/random_s43` | ✅ best_by_val_loss + best_by_recall_at_1 |
| `m2_full_qwen/random_s44` | ✅ best_by_val_loss + best_by_recall_at_1 |
| `m2_full_starcoder/random_s42` | ✅ best_by_val_loss + best_by_recall_at_1 |
| `m2_full_starcoder/random_s43` | ✅ best_by_val_loss + best_by_recall_at_1 |
| `dataflow_aware_*` | ❌ 待 M2 训练产出 |

Checkpoint 格式已确认：`model.pt` + `training_config.json` + tokenizer 文件，与评估脚本兼容。

---

## 可执行性总结

### 现在可以做的（不等 M2）

1. **检索评估 (random baseline)**：用现有 `random_s42` checkpoint 跑 `eval_swebench.py`，验证端到端 pipeline 可用
   ```bash
   python eval_swebench.py \
       --checkpoint-path /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1 \
       --repo-cache-dir /root/autodl-tmp/structfuse/swebench_repos \
       --output-dir /root/autodl-tmp/structfuse/eval_results/swebench_random_baseline
   ```
   > 注意：M2 训练占用双 GPU，需等训练间歇或用 CPU（`--device cpu`，会很慢）

2. **Dry-run 验证**：零 GPU 开销，测试 pipeline 逻辑
   ```bash
   python eval_swebench.py --checkpoint-path mock --dry-run --num-instances 5
   ```

### 需要等 M2 完成后做的

1. 用 `dataflow_aware` best checkpoint 跑完整 300 instance 检索评估
2. E2E 评估（检索 + 修复）：
   - **方案 A (本地 LLM)**：用 vllm 部署 Qwen3.6-27B，设 `STRUCTFUSE_LLM_BACKEND=api`，`STRUCTFUSE_LLM_API_BASE=http://localhost:8000/v1`
   - **方案 B (外部 API)**：需配置 `STRUCTFUSE_LLM_API_KEY`

### 需要 Main Agent 操作的

| 操作 | 优先级 | 说明 |
|------|--------|------|
| 配置 LLM API Key | 🟡 中 | E2E 评估需要。如果用本地 vllm 部署则不需要外部 key，但需等 GPU 空闲 |
| Docker | ⚪ 低 | 当前评估脚本不依赖 docker，暂不需要 |

---

## 结论

**检索评估**所有前置条件已满足：数据、脚本、swebench 包、预克隆仓库全部就绪。M2 checkpoint 到手后可直接运行。

**E2E 评估**需要额外决策 LLM backend 方案（本地 vllm vs 外部 API）。建议 M2 训练完成后先跑检索评估，再根据 GPU 可用性决定 E2E 方案。
