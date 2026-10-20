# exp-002 Signal Pipeline — Code Status Report

## 文件清单 (1844 行 Python)

| 文件 | 行数 | 状态 | 功能 |
|------|------|------|------|
| compute_signals.py | 284 | ✅ Complete | 主入口，CLI，信号调度，merge |
| signal_embedding.py | 204 | ✅ Complete | S1: Embedding cosine similarity (FAISS) |
| signal_minkpp.py | 255 | ✅ Complete | S2: Min-K++ membership inference |
| signal_constat.py | 118 | ✅ Complete | S3: ConStat accuracy gap |
| signal_selfcritique.py | 255 | ✅ Complete | S4: Self-Critique entropy collapse |
| aggregate_rrf.py | 226 | ✅ Complete | RRF fusion + ablation baselines |
| run_batch.py | 257 | ✅ NEW | Batch orchestration (9 tasks) |
| test_dryrun.py | 135 | ✅ Complete | Dry-run test v1 |
| test_dryrun_v2.py | 110 | ✅ Complete | Dry-run test v2 (offline) |

## 本次修改

### 1. run_batch.py (新建，257 行)
- 定义 task matrix: 0.5B × {d000, d005, d100} × {mmlu, gsm8k, arc_challenge} = 9 tasks
- D016 合规: Min-K++ ref model = d000 fine-tuned model (非裸基座)
- ConStat 自动跳过（paraphrase eval 未就绪时）
- 支持 `--skip-completed` (默认)、`--print-only`、`--only` 过滤
- 生成 batch_report JSON

### 2. Offline mode fix (4 files)
所有信号模块 + compute_signals.py 添加:
```python
os.environ.setdefault("HF_DATASETS_OFFLINE", "1")
os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")
```
修复 AutoDL 上 HuggingFace 连接超时导致 datasets 加载挂起的问题。

## Dry-run 验证结果

### 直接运行 (compute_signals.py)
- d005/arc_challenge, 3 items, GPU 1
- Embedding: PASS (300 training segments, FAISS search ~0.5s)
- Min-K++: PASS (target + ref model loaded, logprobs computed)
- Self-Critique: PASS (generate + critique ~8s)
- Merge: PASS (3 items merged)
- 总耗时: ~23 seconds

### Batch 运行 (run_batch.py)
- d005 × {arc_challenge, gsm8k}, dry-run, GPU 1
- 2/2 tasks PASS
- 总耗时: ~56 seconds

### 输出格式验证
```json
{
  "index": 0,
  "benchmark": "arc_challenge",
  "s1_embedding": 0.384,
  "s2_minkpp": 0.355,
  "s3_constat": null,
  "s4_selfcritique": -0.920
}
```

## 生产运行命令

```bash
# Preview
python run_batch.py --model-size 0.5B --gpu 3 --print-only

# Dry-run (5 items each)
python run_batch.py --model-size 0.5B --gpu 3 --dry-run

# Full run
python run_batch.py --model-size 0.5B --gpu 3

# Single dosage
python run_batch.py --model-size 0.5B --gpu 3 --only d005 --only-benchmarks mmlu
```

预计生产运行时间: 每 task ~10-20 min (embedding bottleneck on MMLU 14K items), 总计 ~1.5-3 GPU-hours

## 前置依赖
- ✅ SFT checkpoints: d000/d005/d100 均已就绪
- ✅ SFT data: sft_dosage_{000,005,100}.jsonl
- ✅ Contamination labels: contamination_labels_{benchmark}_{dosage}.json
- ⏳ Paraphrase eval results: 未就绪 (ConStat 信号暂跳过)
- ✅ Python packages: torch, transformers, datasets, peft, faiss, sentence-transformers, sklearn

## 服务器路径
- 代码: /root/contamcal-irt-calibration/exp002/
- 输出: /root/autodl-tmp/exp002/signals/{model_id}/
