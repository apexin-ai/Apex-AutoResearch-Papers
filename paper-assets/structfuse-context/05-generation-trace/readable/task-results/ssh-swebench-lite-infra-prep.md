# ssh swebench lite infra prep

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_swebench_lite_infra_prep_20260513T223449_result.json`
- **Structured JSON:** [`15427376f78701cdd09a.json`](../../sessions/15/15427376f78701cdd09a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。以下是总结。

---

## 环境准备状态

| 项目 | 状态 |
|------|------|
| swebench 4.1.0 | ✅ 已安装 |
| sb-cli 0.1.5 | ✅ 已安装 |
| SWE-bench Lite 数据集 | ✅ 300 instances, 12 repos, 已存 `/root/autodl-tmp/swebench/swebench_lite` |
| Retrieval 评估脚本 | ✅ `evaluation/eval_swebench.py` 完整可用, dry-run 通过 |
| 端到端评估框架 | ⚠️ `scripts/eval_swebench.py` 有 4 个 placeholder 待实现 |
| Docker | ❌ 不可用 (AutoDL 限制) |

## 数据集分布
django 114 | sympy 77 | matplotlib 23 | scikit-learn 23 | pytest 17 | sphinx 16 | astropy 6 | requests 6 | pylint 6 | xarray 5 | seaborn 4 | flask 3

## "还差什么" 清单

1. **Docker 替代方案** — patch 验证需用 sb-cli 云端或 Modal, 需注册账号
2. **Qwen3.6-27B 模型** — ~55GB 需下载到 `/root/autodl-tmp/models/`, 且需等 GPU 空闲
3. **端到端脚本** — 4 个 placeholder 函数 (retriever 加载, LLM 推理, patch 生成, 验证)
4. **11 repos 预 clone** — 避免评估时 clone 瓶颈
5. **GPU 释放** — M2 训练完成后才能跑真实评估 (预计 May 17-18)

## 评估方案

评估方案已写入 `artifacts/plan003_swebench_eval_plan.md`。核心路径: **先跑 retrieval-only (Recall@k/MRR, 已就绪), 再跑端到端 (Qwen3.6-27B Agentless 风格 + sb-cli 验证)**。总计 ≤40h GPU, 在预算内。

---
