# Seed=123 训练状态检查 — 2026-05-14

## GPU 状态
| GPU | 利用率 | 显存占用 | 状态 |
|-----|--------|----------|------|
| cuda:0 (RTX PRO 6000 Blackwell) | 51% | 71641/97887 MiB | ✅ 正常训练 |
| cuda:1 (RTX PRO 6000 Blackwell) | 58% | 28745/97887 MiB | ✅ 正常训练 |

## tmux Sessions
- `chain_cuda0_s123` — 创建于 09:58:34，运行 uncurated→rgds→random50 串行链
- `medium_external_seed123` — 创建于 11:11:15，运行 external_only
- `auto_cuda1` — 创建于 11:19:40，等待 cuda:1 空闲后跑 random50

## 实验进度

### cuda:0 — uncurated seed=123 (chain_cuda0_s123)
- **当前**: Gen 6/7，训练阶段 [3/5]
- **已完成 Gen**: 0–5（6 个 gen 完成）
- **每 Gen 耗时**: Gen 0 = 957s, Gen 1–5 ≈ 740s
- **预估剩余**: Gen 6 剩余训练+评估 ~5min + Gen 7 全程 ~12min ≈ **~17 min** 完成 uncurated
- **chain 后续**: uncurated 完成后自动启动 rgds (7 gen ≈ 90min)，再 random50 (7 gen ≈ 90min)
- **uncurated 预计完成**: ~12:20 CST
- **整条 chain 预计完成**: ~15:20 CST

### cuda:1 — external_only seed=123 (medium_external_seed123)
- **当前**: Gen 0/7，训练阶段 [3/5]（首个 gen 进行中）
- **已完成 Gen**: 无
- **预估每 Gen 耗时**: Gen 0 ≈ 1000s（含初始化），后续 ~800–900s（external_only 有 submodular selection 开销）
- **预估剩余**: ~7 个 gen × ~850s ≈ **~100 min**
- **预计完成**: ~13:50 CST

### auto_cuda1 — random50 seed=123 等待中
- Flag 文件 `/tmp/random50_seed123_on_cuda1` **不存在**
- auto_cuda1 正在等待 external_only 在 cuda:1 上完成
- 预计 external 完成后自动启动 random50（7 gen ≈ 90min）
- **注意**: 如果 chain_cuda0_s123 先跑完 uncurated+rgds 到 random50 阶段，可能与 auto_cuda1 抢 random50。需确认脚本逻辑是否有互斥机制

## 异常
- ⚠️ **无异常**。两块 GPU 均正常运行，无 OOM、无进程挂起。
- ℹ️ cuda:0 显存占用 73%（71.6GB），cuda:1 仅 29%（28.7GB），差异正常——uncurated 不做 selection 所以用全量数据训练，external_only 做 submodular selection 后只用 50% 数据。
