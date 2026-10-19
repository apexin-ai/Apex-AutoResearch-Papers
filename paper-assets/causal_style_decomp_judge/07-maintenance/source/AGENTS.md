## 当前项目
当前绑定项目：**causal_style_decomp_judge**

## 按需查阅
- 项目配置：`load_project_config("causal_style_decomp_judge")` 或 `load_project_config("causal_style_decomp_judge", section="execution")`
- 知识文件：`read_project_file(file=...)` 读取项目文件（ROADMAP.md/memory.md/ideas.md/report.md 等）
- 路线图：`read_roadmap()` 读取研究方向和短期任务
- 产出目录：`/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/`（写文件后用 `register_artifact` 注册）

## 用户自定义规则（必须遵守）
### 审稿规则

- **[EMNLP 2026]** “EMNLP 2026 通过 ARR 统一审稿，Main/Findings 不分开投稿（不是两个Track），Long/Short 也走同一审稿系统，Overall Assessment的评分标准如下：5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle（需大幅修改，可在下一周期完成），1.5 = Resubmit after next cycle（需大幅修改，无法在下一周期完成），1 = Do not resubmit（需完全重做或与*ACL无关）”
- **[EMNLP 2026]** EMNLP 2026 restricts long paper submissions to a strict 8-page limit for main text, with unlimited space for references. Mandatory limitations and optional ethical considerations do not count towards this page limit, provided they do not contain excessive additional content.

### 写作规则

- **[EMNLP 2026]** Limitations 章节只需要写一小段，覆盖 3 个点左右就可以了，不需要写得很长
- **[EMNLP 2026]** ARR Responsible NLP Checklist在OpenReview的submission form里面（由用户手动填写），而不是在论文pdf里面
- **[EMNLP 2026]** 一篇文章只能有一个limitations section，放在正文里面，appendix不能有 limitations section
- **[EMNLP 2026]** abstract 不要超过 200 words

> 以上规则由用户配置，优先级等同于硬约束。违反会被 Reviewer 标记。

## Worker 操作规范

### ssh-env-setup

# 远程服务器环境搭建规范

## 核心原则

**先探测，再安装。** 不要假设服务器上什么都没有——很多包已经装好了。安装前必须走 discovery 流程。

**镜像快速路径**：连接服务器后，先用 `detect_image` 检测是否为预置镜像。如果是已知镜像且版本匹配，跳过基础环境搭建（Phase 1-4），直接安装项目特有依赖。未检测到镜像时走传统流程。

**aml-train 镜像使用 conda 环境**（不是 venv）。环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`。pip/python 在 `/root/miniconda3/bin/` 下。**不要假设 .venv 存在，不要创建 venv。**

## Phase 1: 环境探测（用 ssh_read_only）

连接到服务器后，第一步永远是收集信息，不要直接装东西：

```bash
# 1. Python 环境
which python3 && python3 --version
pip3 --version 2>/dev/null || echo "NO_PIP"

# 2. CUDA 环境
nvidia-smi --query-gpu=name,memory.total,driver_version --format=csv,noheader 2>/dev/null || echo "NO_GPU"
nvcc --version 2>/dev/null | grep "release" || echo "NO_NVCC"

# 3. 包管理器
ls -d /opt/miniconda3 ~/miniconda3 ~/.conda 2>/dev/null || echo "NO_CONDA"
ls -d .venv venv env 2>/dev/null || echo "NO_VENV"
pip3 list --format=freeze 2>/dev/null | grep -iE "torch|transformers|flash" || echo "NO_ML_PKGS"

# 4. PEP 668 检查
python3 -c "import sysconfig; print(sysconfig.get_path('stdlib'))" 2>/dev/null
ls /usr/lib/python*/EXTERNALLY-MANAGED 2>/dev/null && echo "PEP668_MANAGED" || echo "PEP668_OK"
```

根据探测结果决定安装策略，不要猜。

## Phase 2: 环境策略选择

根据 Phase 1 结果选择**一个**策略，不要混用：

| 探测结果 | 策略 | 说明 |
|----------|------|------|
| 项目目录有 `.venv/` | 用它：`source .venv/bin/activate` | 最优先 |
| 有 conda 且有写权限 | `conda activate base` 或创建专属 env | 次优先 |
| PEP668_MANAGED + 无 venv | 创建 venv：`python3 -m venv .venv && source .venv/bin/activate` | 不要用 --break-system-packages |
| PEP668_OK（无保护） | 直接 `pip install`（旧系统） | 仍建议 venv |

**决不混用 conda install + pip install 到同一环境。** 选了 pip 就全用 pip。

## Phase 3: PyTorch 安装

### CUDA 版本映射（2025-2026 常用）

先从 `nvcc --version` 或 `nvidia-smi` 获取 CUDA 版本，然后匹配：

| CUDA 版本 | PyTorch pip index URL | 推荐 torch 版本 |
|-----------|----------------------|-----------------|
| 11.8 | `https://download.pytorch.org/whl/cu118` | ≥ 2.0 |
| 12.1 | `https://download.pytorch.org/whl/cu121` | ≥ 2.1 |
| 12.4 | `https://download.pytorch.org/whl/cu124` | ≥ 2.4 |
| 12.6 | `https://download.pytorch.org/whl/cu126` | ≥ 2.6 |

**不要猜版本号。** 如果不确定可用版本：
```bash
pip index versions torch --index-url https://download.pytorch.org/whl/cu121 2>/dev/null | head -3
```

安装命令：
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu{CUDA_SHORT}
```

### 大包超时处理

PyTorch wheel 约 500MB-2GB，默认 SSH 超时可能不够。策略：

```bash
# 方法 1: nohup + 轮询（推荐）
nohup pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121 > /tmp/pip_install.log 2>&1 &
echo $!  # 记录 PID

# 后续用 ssh_read_only 轮询
cat /tmp/pip_install.log | tail -5
ps -p <PID> -o pid= 2>/dev/null && echo "STILL_RUNNING" || echo "DONE"
```

```bash
# 方法 2: 加大 pip 超时
pip install --timeout 300 torch ...
```

## Phase 4: 验证（必须执行）

安装后必须验证，不要假设成功：

```bash
python3 -c "
import torch
print(f'torch={torch.__version__}, cuda={torch.cuda.is_available()}, gpus={torch.cuda.device_count()}')
if torch.cuda.is_available():
    for i in range(torch.cuda.device_count()):
        print(f'  GPU {i}: {torch.cuda.get_device_name(i)} ({torch.cuda.get_device_properties(i).total_mem // 1024**3}GB)')
"
```

验证失败的常见原因：
- `torch.cuda.is_available()` 返回 False → CUDA 版本和 torch 不匹配，重装正确版本
- `ImportError: libcudnn` → 缺 cuDNN，装 `nvidia-cudnn-cu1x`
- GPU 数量不对 → 检查 `CUDA_VISIBLE_DEVICES` 环境变量

## Phase 5: 项目依赖

基础环境就绪后，安装项目依赖：

```bash
# 优先用 requirements.txt / pyproject.toml
pip install -r requirements.txt  # 或 pip install -e .

# 常用 ML 依赖补装
pip install transformers datasets einops accelerate wandb
```

flash-attention 特殊处理（编译型包）：
```bash
# 需要匹配的 CUDA toolkit，编译耗时 5-15 分钟
pip install flash-attn --no-build-isolation
# 如果编译失败，试预编译版本
pip install flash-attn --no-build-isolation 2>/dev/null || pip install flash-attn-wheels
```

## ssh_read_only vs ssh_execute 使用规则

| 操作 | 用哪个工具 |
|------|-----------|
| 检查环境（python --version, nvidia-smi, pip list） | `ssh_read_only` |
| 读文件内容、查日志 | `ssh_read_only` |
| 安装包（pip install, conda install） | `ssh_execute` |
| 创建/修改文件、启动进程 | `ssh_execute` |
| 运行实验脚本 | `ssh_execute` |

**原则：能用 read_only 就用 read_only，只有要改变服务器状态时才用 execute。**

## AutoDL 专项注意事项

AutoDL 实例有一系列特殊约束，5 个项目反复踩坑，必须遵守：

### 磁盘
- **根分区只有 ~30GB，严禁存大文件。** 模型、数据集、HF cache 全部放数据盘 `/root/autodl-tmp/`
- 设置 `HF_HOME=/root/autodl-tmp/.hf_cache`，否则 HF 默认缓存到根分区导致磁盘满
- 下载模型时用 `--local-dir /root/autodl-tmp/models/<name>`，不要用默认路径

### 网络
- pip install / git clone 前必须 `source /etc/network_turbo` 启用代理加速，否则 pypi.nvidia.com 504 超时、GitHub TLS 断连
- HF 下载设 `HF_HUB_DISABLE_XET=1`，xet_get 在 AutoDL 上返回 401
- **SSL 证书**：`network_turbo` 的代理使用自签名证书，Python 默认 SSL 验证会失败。必须设置 `REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt` 和 `SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt`，否则 HF 下载、datasets 加载等全部报 SSL 错误
- **大模型下载优先用 ModelScope**：AutoDL 代理下载 HuggingFace 大文件极慢（~200KB/s），改用 ModelScope 国内 CDN 速度快很多。`pip install modelscope && python -c "from modelscope import snapshot_download; snapshot_download('Qwen/Qwen2.5-7B-Instruct', cache_dir='/root/autodl-tmp/.hf_cache')"`

### SSH
- **AutoDL 实例重启后 SSH 端口会变。** 连接失败时不要反复重试，应提示用户去控制台查新端口并更新 `~/.ssh/config`

## 经验沉淀

- [2026-04-05] Worker 首次连接服务器时，先用一条 ssh_read_only 组合命令完成全部探测，减少 SSH 往返次数
- [2026-04-05] 遇到 PEP 668 时创建 venv 而非 --break-system-packages，避免污染系统 Python
- [2026-04-05] PyTorch 大包安装用 nohup 后台执行 + 轮询方式，避免 SSH 超时导致安装中断
- [2026-04-05] conda 环境和 pip 不要混用——如果项目用 pip，就全部用 pip
- [2026-04-09] sync_code 前确保本地 commit 已 push 到 remote，否则服务器 git pull 拉不到最新代码
- [2026-04-09] venv 创建后用 `which python` 验证路径指向正确的 venv python，不要假设系统 PATH 正确

## 更多 Skills（按需加载）

执行相关任务前，先 Read 对应 skill 获取环境配置和最佳实践。

- **paper-writing-norms** — 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md`
- **check-training-status** — 当用户问训练进度/实验状态/查状态时使用。用专用工具查看训练状态，禁止 ssh_execute。  →  `/home/ubuntu/agent-ml-research/skills/global/check-training-status.skill.md`
- **rebuttal** — 撰写和优化学术 rebuttal——逐条回应审稿意见，生成 response letter。当收到审稿意见、需要写 rebuttal、回复 reviewer 评论时使用。关键词：rebuttal、审稿意见、reviewer response、author response、meta-review、AC 意见。  →  `/home/ubuntu/agent-ml-research/skills/global/rebuttal.skill.md`
- **review-reviewer-session-start** — Review Reviewer session 启动初始化——检查论文格式、编译状态、材料清单。Review Reviewer 角色 session 启动时自动使用。  →  `/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md`
- **reference-audit** — 引用验证与审计——检查 bib 条目完整性、引用真实性、格式一致性。写论文、审查论文、提交前检查引用时使用。关键词：citation verification、引用检查、bib 审计、fake citation、引用格式。  →  `/home/ubuntu/agent-ml-research/skills/global/reference-audit.skill.md`
- **accelerate-distributed** — HuggingFace Accelerate 分布式训练指南——4行代码实现多GPU/DeepSpeed/FSDP/混合精度。多GPU训练时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/accelerate-distributed.skill.md`
- **draw-paper-figure** — 生成学术论文级 matplotlib 图表——按 narrative_intent + design_notes 设计，从 pattern 库选用技法，远程 SSH 执行输出 PDF/PNG  →  `/home/ubuntu/agent-ml-research/skills/global/draw-paper-figure.skill.md`
- **experiment-analysis** — 实验结果分析框架——统计显著性检验、消融分析、baseline 对比、可视化建议。分析实验结果或撰写论文 Results 部分时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/experiment-analysis.skill.md`
- **hf-hub** — HuggingFace Hub CLI (hf) — 下载/上传模型和数据集、管理缓存、搜索论文和模型。涉及 HuggingFace 资源操作时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/hf-hub.skill.md`
- **latex-paper** — ML 顶会论文 LaTeX 写作全流程——Claim-Evidence 方法论、引用防幻觉、顶会模板速查、投稿工程链、会议转投。写论文/投稿时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md`
- **lm-eval-harness** — lm-evaluation-harness 模型评估指南——MMLU/GSM8K/HumanEval 等 60+ 学术基准测试。评估模型质量、对比实验时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/lm-eval-harness.skill.md`
- **ml-experiment-guide** — 跨项目 ML 实验避坑指南——从多个项目沉淀的通用踩坑经验与最佳实践。当 Worker 准备写实验代码、或排查实验问题时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/ml-experiment-guide.skill.md`
- **paper-banana** — 用 PaperBanana 生成高品质学术概念图（架构/流程/framework）。统计图不要用 PaperBanana，用 draw-paper-figure。需要 GOOGLE_API_KEY。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-banana.skill.md`
- **paper-image-extractor** — 从论文 PDF 或 arXiv 源码包提取图表——优先 arXiv 原始图片，回退 PDF 解析。用户说"提取图"/"抽图"/"extract figures"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-image-extractor.skill.md`
- **peft-lora** — PEFT/LoRA/QLoRA 参数高效微调指南——LoRA 配置选择、QLoRA 量化训练、Adapter 管理与合并。微调大模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/peft-lora.skill.md`
- **research-news** — 每日论文推荐——搜索 arXiv 最新论文，按相关性/新颖性/影响力评分，生成推荐列表。Director 说"有什么新论文"/"最近进展"/"research news"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/research-news.skill.md`
- **trl-training** — TRL (Transformer Reinforcement Learning) 训练指南——SFT/DPO/GRPO/KTO 配置与最佳实践。训练或对齐语言模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/trl-training.skill.md`
- **wandb-guide** — W&B 查询最佳实践——如何高效使用 fetch_wandb_metrics / compare_wandb_runs / get_best_wandb_run 分析实验结果。分析实验指标时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/wandb-guide.skill.md`
- **LLM Judge Style Bias — Research Landscape** — 从10篇论文蒸馏的LLM-as-Judge风格偏差研究领域隐性经验：实验设计共识、方法趋势、竞品定位、研究空白  →  `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/skills/projects/causal_style_decomp_judge/distilled-research.skill.md`
- **LLM Judge Style Bias — Writing Patterns** — 从8篇深度精读论文蒸馏的叙事策略、图表设计共识、投稿编排经验  →  `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/skills/projects/causal_style_decomp_judge/distilled-writing.skill.md`
