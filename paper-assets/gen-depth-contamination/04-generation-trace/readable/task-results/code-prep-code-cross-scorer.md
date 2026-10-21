# code prep code cross scorer

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep-code-cross-scorer_20260519T062648_result.json`
- **Structured JSON:** [`19b845173baa8589327e.json`](../../sessions/19/19b845173baa8589327e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 验证完毕，一切正常。

---

## 实验方案

### 完整命令

```bash
bash /root/autodl-tmp/gen-depth-contamination/scripts/exp_code_qwen1b5_pythia_scorer.sh
```

脚本内容已写入服务器，核心逻辑：
1. symlink `data/exp_code_qwen1b5/depth_{0..5}.jsonl` → `data/exp_code_qwen1b5_pythia_scorer/`
2. `--skip_generation` 跳过文本生成，只用 Pythia-1.4B 做 feature extraction + analysis
3. `--model_path` 直接指向 Pythia-1.4B（因为 skip_generation 后不需要 generator）

### 预计耗时
- Dry-run 实测：depth_0 (5500 samples, batch_size=8) 约 90 秒
- 6 个 depth × 90s ≈ **9 分钟** feature extraction + analysis（几乎忽略不计）
- 总计约 **10-12 分钟**，< 0.2 GPU-hours

### 数据路径确认
| 项目 | 路径 |
|------|------|
| 输入数据 | `data/exp_code_qwen1b5/depth_{0..5}.jsonl` (5500 × 6 = 33000 行) |
| Scorer 模型 | `/root/autodl-tmp/.hf_cache/models--EleutherAI--pythia-1.4b/snapshots/fedc38a16eea3bd36a96b906d78d11d2ce18ed79` |
| 输出 features | `data/exp_code_qwen1b5_pythia_scorer/features.csv` |
| 输出结果 | `results/exp_code_qwen1b5_pythia_scorer/` (pairwise_auc.json, summary.txt 等) |
| GPU | cuda:0 (空闲, Pythia-1.4B 仅需 ~2.8 GB) |

### 潜在风险
- **无风险**：Pythia-1.4B 已在本地缓存，无需下载；TRANSFORMERS_OFFLINE=1 确保不会尝试网络请求
- Pythia tokenizer (GPT-NeoX) 与 Qwen tokenizer 不同，token 边界会不一致。这是正确的行为（cross-family scorer 就是要用不同 tokenizer），但 surprisal 绝对值会不同于 Qwen scorer 的结果，AUC 相对排序才是关键指标

可以直接 `submit_training_job` 或手动 `bash scripts/exp_code_qwen1b5_pythia_scorer.sh` 启动。

---
