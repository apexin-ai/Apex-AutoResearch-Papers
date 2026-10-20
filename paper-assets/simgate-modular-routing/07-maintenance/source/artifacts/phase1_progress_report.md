# Phase 1 进度报告 — 2026-05-13 14:55 UTC

## GPU0 (boil, melt, change-the-state-of-matter-of)
- 进程状态: **alive** (PID 20296, 运行 28 分钟)
- 当前任务: `boil` (第 1/3 个 task)
- 当前进度: Episode 2/20，[C] oracle-routing 运行中
- 已完成 episode:
  - Ep 0: [A]=-100.0, [B]=0.0, [C]=0.0 (int=27/det=3)
  - Ep 1: [A]=0.0, [B]=0.0, [C]=0.0 (int=30/det=0)
  - Ep 2: [A]=2.0, [B]=3.0, [C]=运行中
- 已完成 task: 无（boil 仍在进行）
- episodes.jsonl: 2 行 (93KB)

## GPU1 (chemistry-mix-paint-secondary-color, grow-plant)
- 进程状态: **alive** (PID 55775, 运行 7 分钟)
- 当前任务: `chemistry-mix-paint-secondary-color` (第 1/2 个 task)
- 当前进度: Episode 1/20，[B] always-deterministic 运行中
- 已完成 episode:
  - Ep 0: [A]=-100.0, [B]=0.0, [C]=0.0 (int=27/det=3)
  - Ep 1: [A]=20.0, [B]=运行中
- 已完成 task: 无
- episodes.jsonl: 1 行 (38KB)

## 资源
| GPU | 型号 | 显存占用 | 利用率 |
|-----|------|----------|--------|
| GPU0 | RTX 5090 | 15729 / 32607 MiB (48%) | 0% (推理间隙) |
| GPU1 | RTX 5090 | 15601 / 32607 MiB (48%) | 79% |

## 已产出文件
```
results/mvp/
├── phase0_validation.json
├── phase0_validation_v2.json
├── boil/
│   └── episodes.jsonl (2 行, 93KB)
└── chemistry-mix-paint-secondary-color/
    └── episodes.jsonl (1 行, 38KB)
```
无 summary.json（任何 task 均未完成全部 20 episodes）

## 预估
- 每个 episode 3 种 mode 合计约 8-10 分钟
- GPU0: 60 episodes 总量 (20×3 tasks), 已完成 2 → 预计还需 ~5-7 小时
- GPU1: 40 episodes 总量 (20×2 tasks), 已完成 1 → 预计还需 ~4-5 小时

## 初步信号观察
- Episode 0 的 always-internal [A] 均为 -100.0（首次加载模型时可能有初始化问题）
- 后续 episode 分数有改善：boil Ep2 [A]=2.0 [B]=3.0; mix-paint Ep1 [A]=20.0
- Oracle routing 目前大量选择 internal modality（int=27-30/det=0-3），deterministic 几乎未被选中
