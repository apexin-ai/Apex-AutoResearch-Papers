# westd-10894 Health Check — 2026-05-26 ~10:20 UTC

## 磁盘

| 分区 | 容量 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| / (根) | 30G | 15G | 16G | 48% |
| /root/autodl-tmp/ | 250G | 216G | 35G | 87% |

Checkpoints 总占用: **194G**

**磁盘已从 100% 恢复到 87%**，相比 05-26 04:30 UTC 的满盘状态释放了约 34G。

## GPU 状态

| GPU | 实验 | PID | 显存占用 | GPU利用率 |
|-----|------|-----|----------|----------|
| cuda:0 | cutoff_45k_s2_v2 | 4294 | 62200/97887 MiB | 99% |
| cuda:1 | mvp_occ_s3_v2 | 33897 | 62194/97887 MiB | 99% |
| cuda:2 | full_occ_ln_s3_v2 | 34102 | 62194/97887 MiB | 41% |
| cuda:3 | ablation_occ_detach_s3_v2 | 34443 | 62194/97887 MiB | 89% |

4 个 GPU 全部在线，进程 PID 与预期一致。cuda:2 利用率偏低 (41%)，可能是 checkpoint saving 的瞬时波动。

## 实验进度

| 实验 | Step | 总Step | 进度 | 速度 | 剩余时间 | 预计完成 (UTC) |
|------|------|--------|------|------|----------|---------------|
| cutoff_45k_s2_v2 | 36345 | 50005 | 73% | ~1.07 it/s | ~3.5h | ~14:00 |
| mvp_occ_s3_v2 | 25152 | 50005 | 50% | ~1.08 it/s | ~6.4h | ~16:40 |
| full_occ_ln_s3_v2 | 25061 | 50005 | 50% | ~1.07 it/s | ~6.5h | ~16:50 |
| ablation_occ_detach_s3_v2 | 25000 | 50005 | 50% | ~1.07 it/s | ~6.5h | ~16:50 |

最新 loss 值:
- cutoff_45k_s2_v2: step 36300, occ=0.0102, action=0.0767
- mvp_occ_s3_v2: step 25100, occ=0.0093, action=0.0698
- full_occ_ln_s3_v2: step 25000, occ=0.0107, action=0.0898
- ablation_occ_detach_s3_v2: step 25000 (日志截断于此)

3 个 _v2 实验于 04:42 UTC 重启后已稳定运行 ~5.5h，无异常。

## 磁盘风险评估

**结论: 中等风险，建议清理。**

当前运行的 4 个实验各保留 2 个 checkpoint (30G each)，总计 120G。实验采用滚动保留策略，不会无限增长。剩余 35G 在正常情况下足够撑到实验完成。

**但是**：如果 4 个实验同时触发 checkpoint saving（写入新 ckpt + 尚未删除旧 ckpt 的瞬间），瞬时磁盘需求可能增加 60G (4x15G)，超过 35G 可用空间，导致再次磁盘满。

## 可安全清理的旧 Checkpoint

以下 checkpoint 满足条件：实验已完成（非 RUNNING/PREPARING）、无 RUNNING/PREPARING 实验以其为 parent 依赖：

| Checkpoint | 大小 | Registry 状态 | 清理理由 |
|------------|------|---------------|----------|
| full_occ_ln_s1 | 15G | DONE/success, eval DONE/negative | 无后续依赖 |
| full_occ_ln_s2 | 15G | DONE/success, eval DONE/negative | 无后续依赖 |
| vanilla_retrain_s0 | 15G | DONE/success, eval DONE/success | 无后续依赖 |
| ablation_occ_detach_s0_retrain | 15G | DONE/success, eval DONE/success | 无后续依赖 |
| cutoff_15k_s1 | 463M | DONE/success, eval DONE/success | 无后续依赖 |

**可释放总计: ~60.5G** -> 清理后可用空间达 ~95G，消除磁盘风险。

**不可清理:**
- full_occ_ln_s0 (15G): full_occ_ln_s4 (PREPARING) 依赖其 checkpoint 作为 resume 起点
- 所有 RUNNING 实验的 checkpoint 目录

## 建议

1. **优先清理 full_occ_ln_s1 + full_occ_ln_s2** (+30G)，立即消除瞬时磁盘满风险
2. 如需更大缓冲，继续清理 vanilla_retrain_s0 + ablation_occ_detach_s0_retrain (+30G)
3. vanilla_s2_train.log (938K) 可一并清理
