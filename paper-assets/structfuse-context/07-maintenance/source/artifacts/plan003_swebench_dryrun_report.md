# SWE-bench Lite Dry-Run 验证报告

**日期**: 2026-05-14  
**服务器**: bjb1-42106 (2x NVIDIA RTX PRO 6000 Blackwell, 98GB each)

---

## 1. Eval 脚本

| 脚本 | 路径 | 用途 |
|------|------|------|
| 检索评测 | `/root/structfuse/evaluation/eval_swebench.py` | Recall@k, MRR（retrieval-only） |
| E2E 评测 | `/root/structfuse/scripts/eval_swebench_e2e.py` | 检索 → LLM agent → patch → 测试验证 |

**检索评测关键参数**:
- `--checkpoint-path`: checkpoint 目录（含 model.pt + training_config.json）
- `--num-instances`: 限制评测 instance 数（0=全部）
- `--repo-cache-dir`: 预 clone 的 repo 缓存目录
- `--dry-run`: mock retriever + mock 数据，无需 GPU
- `--top-k`: Recall@k 的 k 值（默认 1,5,10,20）

**E2E 评测关键参数**:
- `--retriever-checkpoint`, `--strategy`, `--max-instances`, `--repo-cache-dir`
- LLM backend 通过环境变量控制：
  - `STRUCTFUSE_LLM_BACKEND=mock`（默认，返回空 patch）
  - `STRUCTFUSE_LLM_BACKEND=api` + `STRUCTFUSE_LLM_API_BASE` + `STRUCTFUSE_LLM_API_KEY` + `STRUCTFUSE_LLM_MODEL`

## 2. Checkpoint 路径

```
/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1/
├── model.pt              (6.2 GB)
├── training_config.json
├── tokenizer.json / tokenizer_config.json / vocab.json / merges.txt
├── added_tokens.json / special_tokens_map.json / chat_template.jinja
```

**训练配置**:
- 基座模型: `/root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B`（已存在）
- LoRA: r=16, use_lora=true
- proj_dim: 256
- hard_negative_strategy: random
- max_seq_length: 2048

同目录下还有其他 checkpoint:
- `m2_full_qwen/random_s42/best_by_val_loss`
- `m2_full_qwen/random_s43/best_by_recall_at_1`, `best_by_val_loss`
- `m2_full_starcoder/random_s42/best_by_recall_at_1`, `best_by_val_loss`

## 3. 依赖状态

**全部已安装**，无需额外安装：

| 包 | 版本 |
|----|------|
| torch | 2.10.0+cu128 |
| transformers | 4.57.6 |
| peft | 0.19.0 |
| datasets | 4.8.4 |
| accelerate | 1.13.0 |
| flash-attn | 2.8.3 |
| vllm | 0.18.1 |
| openai | 2.24.0 |
| faiss-cpu | 1.13.2 |
| rank-bm25 | 0.2.2 |
| einops | 0.8.2 |

## 4. API Key 需求

| 模式 | 需要 API Key |
|------|-------------|
| 检索评测 (eval_swebench.py) | **不需要** |
| E2E mock 模式 (默认) | **不需要** |
| E2E api 模式 | 需要 `STRUCTFUSE_LLM_API_KEY` + `STRUCTFUSE_LLM_API_BASE` |

## 5. Dry-Run 结果

### Mock dry-run (eval_swebench.py --dry-run)
- **状态**: ✅ 通过
- SWE-bench Lite dataset 从 HF cache 加载成功（300 instances）
- Mock retriever 正常运行
- 输出格式正确（per_instance_results.jsonl + summary.json）

### Real checkpoint dry-run (eval_swebench.py + 真实 checkpoint)
- **模型加载**: ✅ 成功
  - Base model (2 shards): ~1.6s
  - model.pt (6.2 GB): ~15s
  - 总初始化: ~20s
- **推理速度**: ~1.75 instances/s（2 instances in 1.14s，不含 repo checkout 时间）
- **Repo checkout**: ❌ **失败 — 阻塞问题**

## 6. 🚨 阻塞问题：Partial Clone Repos

**问题描述**:

预 clone 到 `/root/autodl-tmp/structfuse/swebench_repos/` 的 12 个 repo 都是 `--filter=blob:none` partial clone。eval 脚本将它们 `git clone` 到临时工作目录后，新 clone 的 repo 的 `origin` 指向本地 cache 目录（不是 GitHub），导致 `git checkout <base_commit>` 时无法获取缺失的 blob 文件。

**错误信息**:
```
error: unable to read sha1 file of .circleci/config.yml (941fc59be...)
error: unable to read sha1 file of .gitattributes (c9e0d8c60...)
```

**影响**: 两个 eval 脚本的 repo checkout 逻辑都有此问题，所有 instance 都会 `clone_failed`。

**修复方案**（按推荐顺序）:

1. **修改 eval 脚本的 `setup_repo` / `checkout_repo`**：clone 后将 origin URL 重设为 GitHub：
   ```python
   subprocess.run(["git", "remote", "set-url", "origin", f"https://github.com/{repo}.git"], cwd=repo_dir)
   ```
   然后 checkout 前做 `git fetch origin <commit> --depth=1`

2. **直接在 cache repo 上 checkout**（不二次 clone）：省去 clone 步骤，直接在 `/root/autodl-tmp/structfuse/swebench_repos/astropy__astropy` 中 checkout。需要 `git fetch origin <commit>` 以获取 blob。网络代理需启用 (`source /etc/network_turbo`)

3. **重新 clone 为完整 repo**：当前 partial clone 共 667 MB，完整 clone 预估 10-20 GB。磁盘剩余 44 GB，可行但耗时。

## 7. 资源估算（300 instances，修复 repo 问题后）

### 检索评测 (eval_swebench.py)
- 模型加载: ~20s（一次）
- 每 instance: repo checkout ~3s + 文件收集 ~1s + 编码推理 ~2s ≈ 6s
- **总计: 约 30-40 分钟**
- GPU 显存: 单卡，预估 <10 GB（3B 模型 + LoRA）
- 磁盘: 需要存放 checkout 的 repo 工作目录，约 2-5 GB

### E2E 评测 (eval_swebench_e2e.py)
- 检索部分同上
- LLM agent patch generation: **取决于 backend**
  - mock 模式: 极快（空 patch），仅测 pipeline
  - API 模式: 每 instance ~30-60s（取决于模型和 API 延迟）
  - **300 instances API 模式: 约 3-5 小时 + API 费用**

## 8. 其他注意事项

- **HF Dataset 加载慢**: 即使有本地 cache，`datasets` 库仍尝试 HEAD 请求检查更新。建议设 `HF_DATASETS_OFFLINE=1` 避免超时
- **网络代理**: 需 `source /etc/network_turbo` + SSL cert 环境变量
- **SSH 超时**: MCP SSH 工具 30s 超时，长时间运行需 nohup 后台执行
- **Resume 支持**: eval_swebench.py 支持断点续跑（per_instance_results.jsonl 追加模式）
