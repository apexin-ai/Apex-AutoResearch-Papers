# Handover — 2026-05-16

> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。

## 运行中
（无）

## 待处理
- gold-deep-analysis-r5（准备中）
- e5-large-seed42（准备中）
- d075-e5large-s42: 补跑 E5-large encoder probe seed 42（原 multiseed JSON 数据为编造），修复数据完整性问题（准备中）

## 近期结论
- **llm-judge-gold-r5** (success): —
  [llm-judge-gold-summary](/api/workspace-files/projects/agent_progress_probe/artifacts/llm-judge-gold-r5/data/summary_content.txt)
- **reverse-transfer-oh-to-swe** (success): —
  [reverse_transfer_oh_to_swe_results](/api/workspace-files/projects/agent_progress_probe/artifacts/reverse-transfer-oh-to-swe/data/reverse_transfer_results.txt)
- **encoder-ablation-probe-bgem3** (success): —
  [bgem3_multiseed_test_results](/api/workspace-files/projects/agent_progress_probe/artifacts/encoder-ablation-probe-bgem3/data/bgem3_multiseed_test_results.txt)

## 趋势
成功 68 / 负向 10 / 失败 1 / 共 89
best_epoch: 5 ↑（近 3 次 success）
test_macro_f1: 0.9413 ↑（近 3 次 success）

## 下一步
（无活跃 idea，请通过 ideas.md 添加）

## 资源状态
bjb2-23165: 空闲 cuda:0, cuda:1

## 告警
- encoder-ablation: 已被终止 — unknown
- outcome-bp-3seed-s42: 已被终止 — unknown
- encoder-ablation-probe: 已被终止 — unknown
- encoder-ablation-probe-e5: 已被终止 — unknown
- encoder-ablation-probe-bge-m3: 已被终止 — unknown
- ablation-lf-holdout: 已被终止 — unknown
- data-scaling: 训练失败 — unknown
- twv-no-temporal-sigma2: 已被终止 — unknown
- conf2-subset-v2: 已被终止 — unknown
- gold_dryrun_v1: 已被终止 — unknown
- gold_dryrun_v2: 已被终止 — unknown
