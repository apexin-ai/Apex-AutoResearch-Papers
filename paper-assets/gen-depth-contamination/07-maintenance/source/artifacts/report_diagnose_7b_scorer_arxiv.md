# 诊断报告: exp_7b_scorer_arxiv

## 结论：实验已成功完成，非崩溃

"进程死亡5次"为**误报**。最近一次运行（2026-05-20 20:34–21:14）正常跑完全部流程，日志末尾输出 `Pipeline complete.`。

## 误报根因

脚本 `run_7b_scorer_arxiv.py` **未写 sentinel 文件、未接入 W&B**。监控系统依赖这两个信号判断实验状态，缺失即判定为崩溃。之前的多次"崩溃"可能也是同样原因（进程正常结束但无完成信号）。

## 实验结果

产出文件已生成：
- `/root/autodl-tmp/gen-depth-contamination/results/exp_7b_scorer_arxiv/all_results.json`
- `/root/autodl-tmp/gen-depth-contamination/results/exp_7b_scorer_arxiv/summary.txt`

```
Config                          K*     0v1 AUC     1v2 AUC     2v3 AUC
----------------------------------------------------------------------
pythia_arxiv__qwen1.5b            3  0.9872       0.7938       0.6544
olmo_arxiv__qwen1.5b              1  0.9954       0.5182       0.4956
pythia_arxiv__qwen7b              3  0.9844       0.7987       0.6551
olmo_arxiv__qwen7b                1  0.9941       0.5089       0.4920

pythia_arxiv: K*(1.5B)=3, K*(7B)=3 -> MATCH
olmo_arxiv:   K*(1.5B)=1, K*(7B)=1 -> MATCH
```

假设验证：7B scorer 与 1.5B scorer 在 arXiv 数据上给出相同的 K* 值。

## 环境状态

- GPU: 4x RTX 4090 D (24GB)，当前空闲
- 数据目录完整（exp_025_pythia_arxiv, exp_arXiv_olmo 均含 depth_0-5.jsonl）
- 模型文件存在（Qwen2.5-1.5B-Instruct, Qwen2.5-7B）

## 建议

无需修复重跑。如需避免未来误报，可在脚本末尾添加 sentinel 文件写入：
```python
(OUT_RESULTS / "DONE.sentinel").write_text(f"completed {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
```
