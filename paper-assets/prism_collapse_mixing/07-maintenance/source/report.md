# Handover — 2026-05-16

> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。

## 运行中
（无）

## 待处理
（无）

## 近期结论
- **mvp_collapse_decoupling_v2** (failed): 在迭代合成训练中，collapse 信号（entropy/spectral rank/diversity）与 validation loss 脱钩——loss 稳定/改善而 collapse 信号下降，表明 loss 无法捕获 collapse 退化。（v2: OOM 修复后延续运行） ← 基于 mvp_collapse_decoupling
  [gen2_progress_check](/api/workspace-files/projects/prism_collapse_mixing/artifacts/mvp_collapse_decoupling_v2/report/gen2_progress_check.md)
- **mvp_collapse_decoupling** (failed): 在迭代合成训练中，collapse 信号（entropy/spectral rank/diversity）与 validation loss 脱钩——loss 稳定/改善而 collapse 信号下降，表明 loss 无法捕获 collapse 退化

## 趋势
成功 0 / 负向 0 / 失败 2 / 共 2

## 下一步
（无活跃 idea，请通过 ideas.md 添加）

## 资源状态
rtx6000-diagprobe: 空闲 cuda:0, cuda:1

## 告警
- mvp_collapse_decoupling: 训练失败 — unknown
- mvp_collapse_decoupling_v2: 训练失败 — unknown
