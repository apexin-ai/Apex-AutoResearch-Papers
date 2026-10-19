# ops anon repo integrity check

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_anon-repo-integrity-check_20260523T185637_result.json`
- **Structured JSON:** [`fe814de56a8472dad560.json`](../../sessions/fe/fe814de56a8472dad560.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 匿名仓库完整性核查报告

### 一致性对比

| 项目 | GitHub 远程 | 本地 (`/root/autodl-tmp/anon_repo/`) |
|------|------------|--------------------------------------|
| 文件数 | **99** | **99** |
| 最新 commit | `3d1671d` | `3d1671d` |
| 未推送 commit | — | **无** |

**两边完全一致。**

### Remote 配置
已确认为 HTTPS+token 格式（`https://[REDACTED]@github.com/...`），无需修改。

### 仓库根目录结构
```
.
├── README.md
├── requirements.txt
├── artifacts/
│   ├── run_stochastic_dominance.py
│   └── theorem1_proof.tex
├── docs/paper/
│   └── data/   (3 JSON 数据文件)
├── scripts/     (82 个实验/分析脚本)
└── src/         (12 个核心模块)
    ├── __init__.py
    ├── api_judge_service.py
    ├── attacks.py
    ├── config.py
    ├── correlation.py
    ├── eval_pipeline.py
    ├── judge_service.py
    ├── keff.py
    ├── panel_selection.py
    ├── panels.py
    ├── scaling.py
    ├── unified_data_loader.py
    └── utils.py
```

### 核心文件检查
- **README.md** ✓
- **requirements.txt** ✓
- **src/** 核心代码 (12 模块) ✓
- **scripts/** 实验脚本 (82 个) ✓
- **docs/paper/data/** 论文数据 ✓

### Git 状态
- 分支：`main`，与 `origin/main` 同步
- 工作区干净，无未提交修改
- 共 2 个 commit：`f9a3944` (Anonymous submission) → `3d1671d` (Fix K=5 epsilon sensitivity...)

**结论：匿名仓库本地与远程完全同步，结构完整，包含所有核心代码、README 和 requirements。**

---
