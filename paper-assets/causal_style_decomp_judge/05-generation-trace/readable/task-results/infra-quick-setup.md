# infra quick setup

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_quick_setup_20260520T092912_result.json`
- **Structured JSON:** [`b082e36f71d430408b7f.json`](../../sessions/b0/b082e36f71d430408b7f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 pip 依赖验证通过。

## 产出汇报

| 项目 | 状态 | 详情 |
|------|------|------|
| **pip 依赖** | ✅ | bert-score, openai, scipy, pandas, seaborn, matplotlib, datasets, tqdm 全部就绪；vllm 后台安装中 (PID 9272) |
| **NLI 模型** | ⏳ 下载中 | `cross-encoder/nli-deberta-v3-large` via hf-mirror，73% (1.19G/1.62G)，~13 min 完成，PID 8957 |
| **Qwen3-32B** | ⏳ 下载中 | ModelScope CDN，shard 8/17 at 38%，PID 8822 |
| **代码部署** | ✅ | 8 文件完整：`__init__.py`, `data_prep.py`, `counterfactual_gen.py`, `content_verification.py`, `judge_scoring.py`, `ate_analysis.py`, `requirements.txt`, `run_mvp.sh` |
| **数据准备** | ✅ | 100 条记录 → `data/mvp_samples.jsonl`（GPTInst:28, GPTOut:21, Manual:12, Neighbor:39） |
| **GPU** | ✅ | 4× RTX PRO 6000 Blackwell (96GB each)，torch=2.8.0+cu128，CUDA 可用 |
| **磁盘** | ✅ | `/root/autodl-tmp` 250GB，已用 18GB，剩余 233GB |

**修复记录**：`data_prep.py` BASE_URL 修正为 `Dataset/LLMBar/Adversarial/{subset}/dataset.json`（原路径 404），本地和服务器已同步。

**后台进程一览**：
- NLI 下载 PID 8957（~13 min）
- Qwen3 下载 PID 8822（预计数小时）
- vllm 安装 PID 9272

---
