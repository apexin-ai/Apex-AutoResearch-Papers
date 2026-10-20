---
loop: 1
reason: max_wall_time
updated: '2026-05-15T22:17:36+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0, cuda:1（rtx6000-diagprobe）。当前 constraints.yaml 为空，尚未正式注册——Agent 提交训练时必须核对 CUDA_VISIBLE_DEVICES 在 [0,1] 内
- 合成数据必须每代自生成（standard model collapse 设定），不能用 Gen 0 模型一次性生成所有代的 synthetic data
- probe set (5000 samples) 来自 014_00000.parquet，training data 来自 000_00000.parquet——两者物理文件隔离保证零交集，不可混用
- Pass/Fail 阈值已预注册（D002）：|ρ| > 0.7 (Gen 0-1) → |ρ| < 0.5 (Gen 3)，单调退化 ≥15%，双 seed 一致。不可事后调整阈值

### 2. 🖥️ 基础设施快照
- 服务器：rtx6000-diagprobe（2× NVIDIA RTX PRO 6000 Blackwell, 98GB each）
- 工作目录：`/root/prism_collapse_mixing/`
- Python：`/root/miniconda3/bin/python`（conda base，Python 3.12）
- PyTorch：2.10.0+cu128
- HF cache：`/root/.cache/huggingface/hub/`（模型 `EleutherAI/pythia-410m-deduped` 已缓存）
- FineWeb parquets：`/root/autodl-tmp/fineweb_data/`（014 + 000 已下载）
- W&B：**未登录**（.netrc 不存在）。train.py 硬编码 `wandb.init()`，需 `WANDB_MODE=disabled` 或 API key
- 数据：`data/probe_set.jsonl` (5000行), `val_set.jsonl` (14881行), `real_pool.jsonl` (579255行/1.8GB)
- Gen 1 合成数据已生成：`synthetic/synthetic_gen1_seed42.jsonl` (335MB), `synthetic_gen1_seed137.jsonl` (336MB)
- 活跃进程：训练刚重启（日志仅 2 行 torch_dtype warning），PID 待确认。Registry 未注册新实验

### 3. 📊 当前状态
训练在 W&B 登录问题上崩溃后被重启。日志仅显示 `torch_dtype` deprecation 警告，GPU 有 1381 MiB 占用但 0% compute——可能在加载模型/数据阶段，也可能又挂了。**下一个"你"第一件事：检查 GPU 利用率和日志确认训练是否正常运行。**

Registry：
- `mvp_collapse_decoupling`: status=DONE (failed), wall_clock=8133s, gpu_hours=4.52。旧记录，训练重启后未注册新实验

信号文件：仅 Gen 0 × 2 seeds（seed42 + seed137，数值完全一致——正确，同一 base model）

### 4. 📋 待办
- **GPU 空闲 / 训练未运行** → 确认 W&B 问题修复状态，检查 train.py 是否 fallback `WANDB_MODE=disabled`，必要时催 Agent 修复并重启
- **Gen 1 训练完成** → 核实 `signals_gen1_seed{42,137}.json`，重点看 ρ(loss,entropy) 是否从 0.929 开始下降
- **Gen 3 完成** → 运行 pass/fail 判定：entropy |ρ| < 0.5 且均值单调退化 ≥15% 且双 seed 一致
- **Agent 声称 PASS** → 独立验证：读 per-example JSON，自行计算 ρ，核对与 Agent 报告是否一致
- **Agent 声称 FAIL** → 检查是否有实现 bug 导致假阴性（特别是 spectral rank 在 Gen 0 就 |ρ|=0.211，只有 entropy 能承载判定）

### 5. 🎯 战略上下文
- **核心科学问题**：collapse 信号是否包含 loss 无法捕获的退化信息？MVP 用 Pythia-410M 3 代迭代 50/50 混合验证
- **D001**: MVP 方案确定（Pythia-410M, 3代, 固定50/50）
- **D002**: 量化 pass/fail 阈值 + 2 seeds + 实验细节明确
- **关键发现**：Gen 0 基线 spectral_rank 与 loss 仅弱相关（|ρ|=0.211），无法满足 pass 条件中 "早期 |ρ| > 0.7" 要求。**MVP 判定实质上只看 entropy 一个信号**。这不是 bug，但缩窄了信息量
- **最容易判断错的事**：
  1. 不要因为 spectral_rank ρ 始终低就判 FAIL——pass 条件是 "≥1 信号"，entropy 单独 pass 即可
  2. transformers 版本较新，`dtype=` 是正确用法（非 `torch_dtype=`），别再建议改回去
  3. 不要套人类工时直觉——DDL 5/25 EMNLP ARR 距今 10 天，但 MVP 只需 2-3 天，算力充足
  4. train.py 已从 DDP 改为单卡训练——两个 seed 并行各用 1 卡，非 2 卡 DDP
