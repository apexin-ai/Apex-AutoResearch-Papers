# code exp gemma27b c4

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_gemma27b_c4_20260524T082950_result.json`
- **Structured JSON:** [`21f3d774c80f01b83318.json`](../../sessions/21/21f3d774c80f01b83318.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

一切就绪。以下是完整报告：

---

## 环境与数据状态

| 项目 | 状态 |
|------|------|
| **模型** | Gemma-2-27B 已下载 (102GB at `/root/autodl-tmp/.hf_cache/google/gemma-2-27b/`) |
| **GPU** | 4× RTX PRO 6000 Blackwell 98GB，全部空闲 |
| **磁盘** | `/root/autodl-tmp` 101GB 可用 |
| **深度链数据** | 已生成完毕 (`data/exp_gemma27b_c4/depth_{0-5}.jsonl`, 5K docs × 6 depths) |
| **自评特征** | 已提取 (`data/exp_gemma27b_c4/features.csv`, 30K rows) |
| **Cross-scorer 特征** | 已提取 (`data/exp_gemma27b_c4_qwen_scorer/features.csv`, 30K rows) |

## 已有实验结果

**Self-scorer (Gemma-27B)** — K\*=2:
| Pair | AUC | 判定 |
|------|-----|------|
| 0v1 | 0.9695 | 可区分 |
| 1v2 | 0.6196 | 可区分 (>0.60) |
| 2v3 | 0.5388 | 不可区分 |
| 3v4 | 0.5069 | ~random |
| 4v5 | 0.5124 | ~random |

**Cross-scorer (Qwen-1.5B-Instruct)** — K\*=1:
| Pair | AUC | 判定 |
|------|-----|------|
| 0v1 | 0.8874 | 可区分 |
| 1v2 | **0.5894** | 不可区分 (<0.60) |
| 2v3 | 0.5150 | ~random |

## 缺失部分

Bootstrap CI + 置换检验尚未计算。1v2 cross-scorer AUC=0.5894 距阈值 0.60 很近，bootstrap CI 可能横跨 0.60 — 这是 K\*=2 vs K\*=1 的关键判定。

## 新脚本

已创建 `scripts/run_gemma27b_depth.py`，支持以下模式：

```bash
# 完整流程（生成 + 自评 + cross-score + bootstrap CI）
python scripts/run_gemma27b_depth.py

# 跳过生成和 cross-scoring，直接跑 bootstrap CI（推荐，因为数据已有）
python scripts/run_gemma27b_depth.py --skip_generation --skip_cross_scoring

# 只跑 cross-scorer 的 bootstrap CI
python scripts/run_gemma27b_depth.py --cross_only --skip_cross_scoring

# 只跑 self-scorer 的 bootstrap CI
python scripts/run_gemma27b_depth.py --skip_generation --self_only
```

**推荐运行方式**：数据和特征已齐全，直接跑 bootstrap CI 即可，无需重新生成，预计 5-10 分钟：

```bash
cd /root/autodl-tmp/gen-depth-contamination
python scripts/run_gemma27b_depth.py --skip_generation --skip_cross_scoring
```

## 注意

旧脚本 `run_gemma27b_c4.sh` 的 Phase 2 cross-scoring 因传了无效参数 `--seed 42` 而失败（run_pipeline.py 不支持该参数）。Cross-scorer 结果是后来由其他途径补跑的。新脚本已修正这个问题。

---
