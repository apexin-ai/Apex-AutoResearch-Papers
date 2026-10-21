# 72B Backbone Scaling 数据收集状态

**检查时间**: 2026-05-18 05:32 (UTC+8)

## 汇总表

| # | Task | 13313 eps | 14838 eps (raw/unique) | 合计 (去重) | 完成? |
|---|------|-----------|----------------------|-------------|-------|
| 1 | chemistry-mix | 20 | 0 | 20 | Y |
| 2 | find-animal | 20 | 0 | 20 | Y |
| 3 | find-non-living-thing | 20 | 0 | 20 | Y |
| 4 | freeze | 20 | 0 | 20 | Y |
| 5 | grow-fruit | 20 | 20/20 | 20 | Y |
| 6 | identify-life-stages-1 | 20 | 20/20 | 20 | Y |
| 7 | identify-life-stages-2 | 20 | 40/20 | 20 | Y |
| 8 | inclined-plane-determine-angle | 20 | 37/20 | 20 | Y |
| 9 | lifespan-longest-lived | 9 | 20/20 | 20 | Y |
| 10 | lifespan-longest-lived-then-shortest-lived | 0 | 20/20 | 20 | Y |
| 11 | measure-melting-point-unknown-substance | 0 | 16/16 (eps 0-15) | **16** | **N (缺4)** |

**总计: 10/11 tasks 已完成, 1 task 还差 4 episodes**

## 服务器状态

### westb-13313 (2x RTX 5090)

**GPU 状态:**
| GPU | 型号 | 利用率 | 显存 |
|-----|------|--------|------|
| 0 | RTX 5090 | 0% | 32089/32607 MiB |
| 1 | RTX 5090 | 0% | 32089/32607 MiB |

**活跃进程:**
- **PID 617494** (GPU 0+1, tp=2): `episode_level_collection.py` 跑全部 11 个 task, 当前在 **lifespan-longest-lived ep 9**
  - 已完成 8 tasks (chemistry-mix -> inclined-plane-determine-angle), 各 20 eps
  - 当前 lifespan-longest-lived: 9/20
  - 剩余: 11 eps (当前 task) + 20 (lifespan-longest-lived-then-shortest-lived) + 20 (measure-melting-point) = **51 eps**
  - tmux session: `backbone-scaling-70b`

### westb-14838 (4x RTX PRO 6000 Blackwell 96GB)

**GPU 状态:**
| GPU | 利用率 | 显存 |
|-----|--------|------|
| 0 | 0% | 0/97887 MiB (空闲) |
| 1 | 100% | 87255/97887 MiB |
| 2 | 55% | 87377/97887 MiB |
| 3 | 0% | 0/97887 MiB (空闲) |

**活跃进程:**
- **PID 69734** (GPU 1, tp=1): 主收集进程, tasks grow-fruit -> measure-melting-point, 当前在 **measure-melting-point ep 17** - 存活
- **PID 540230** (GPU 2, CUDA_VISIBLE_DEVICES=2): 补充收集 measure-melting-point eps 15-19 - 存活
- PID 20369: reflexion_baseline 7B (无关进程, 非 72B 收集)

**关于之前的 PID:**
- cuda:0 PID 321045: **已死** (GPU 0 空闲, 0 MiB)
- cuda:1 PID 69734: **存活** (确认在跑)
- cuda:2 PID 321159: **已死**, 被新进程 PID 540230 (05:31 启动) 替代

## 数据质量备注

1. **14838 有重复行**: identify-life-stages-2 (40 行, 20 unique), inclined-plane-determine-angle (37 行, 20 unique). 所有 unique episode range 均为 [0-19], 去重后数据完整。
2. **两台服务器重叠 tasks** (grow-fruit, identify-life-stages-1/2, inclined-plane-determine-angle): 均使用 `--seed 42`, 重叠部分大概率是相同数据。
3. **14838 GPU 1 和 GPU 2 同时写 measure-melting-point**: 可能产生 ep 15-19 的重复行, 需后处理去重。

## 缺失数据与预估

**唯一缺口: measure-melting-point-unknown-substance (差 4 eps: 16-19)**

预估完成时间:
- **14838 GPU 1** (主进程): 当前 ep 17, 每 ep ~171s, 剩余 ~3 eps -> **~8 min**
- **14838 GPU 2** (补充): 正在跑 eps 15-19, 预计 **~10-15 min** 内完成
- **13313**: 还需先完成 lifespan-longest-lived (11 eps) + lifespan-longest-lived-then-shortest-lived (20 eps), 然后才到 measure-melting-point -> **~3.5 小时** (但 14838 会更早完成)

**结论: measure-melting-point 预计 ~10-15 分钟内由 14838 完成, 届时全部 11 tasks 数据齐全。**
