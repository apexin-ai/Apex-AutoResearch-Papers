# ops verify anon repo

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-anon-repo_20260523T185707_result.json`
- **Structured JSON:** [`a8f4b641d70baab5e746.json`](../../sessions/a8/a8f4b641d70baab5e746.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
GitHub 文件数: 54, HEAD: c9ef6c5
本地文件数: 54, HEAD: c9ef6c5
一致性: ✅ 完全一致（文件数、commit hash 均匹配，文件列表逐一对应）
关键文件检查:
- 代码: ✅ (llama/train.py, mistral/train.py, qwen/train.py, src/person_fit.py 等)
- .tex: ✅ (main.tex + 14 个 sections/*.tex)
- figures: ✅ (fig_heatmap.pdf, fig_theta_scatter.pdf)
- bib: ✅ (references.bib)
- requirements: ✅ (requirements.txt)
- README: ✅ (README.md)
```

注：远程 tree API 返回 62 条包含 8 个目录节点（figures, llama, mistral, paper, paper/sections, qwen, scripts, src），实际文件（blob）54 个，与本地完全一致。最后推送时间 2026-05-23T18:51:40Z。

---
