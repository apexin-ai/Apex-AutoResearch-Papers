# bjb1-42106 状态检查 — 2026-05-13 16:30 CST

## GPU 状态
| GPU | 显存使用 | 利用率 | 占用进程 |
|-----|---------|--------|---------|
| 0 | 24227/97887 MiB | 100% | PID 27234 (plan_013_starcoder) |
| 1 | 22781/97887 MiB | 100% | PID 29302 (m2_embed_verify) |

## 实验 1: m2_embed_verify (cuda:1, PID 29302)

**状态: ⚠️ 运行中但 wrapper 已死**

- PID 29302 存活，运行时间 01:51:07
- 当前训练: **random strategy, epoch 2, step 1300**（Qwen2.5-Coder-3B）
- 原始 wrapper (run_m2_embed_verify.sh) 已被 kill（EXIT_CODE=129），PID 29302 作为孤儿进程存活
- stdout 通过 pipe 输出到 `random_s42.log`（最后更新 16:29:21，正常写入）

### eval 指标
| checkpoint | val_loss | R@1 | R@5 | R@10 |
|-----------|----------|-----|-----|------|
| eval@500 (best) | **0.4834** | 0.5357 | 0.9808 | 1.0 |
| eval@1000 | 0.5451 | 0.5348 | 0.9765 | 1.0 |

eval@1000 未改善（patience 1/3）。random 训练接近完成（epoch 2 后半段）。

### ⚠️ 问题
- wrapper 死亡后，random 完成时 **embedding 和 dataflow 策略不会自动启动**
- `embedding_s42.log` 和 `dataflow_s42.log` 仅有模型加载日志（来自之前被 kill 的 wrapper），无训练数据

## 实验 2: plan_013_starcoder (cuda:0, PID 23798/27234)

**状态: ✅ 正常运行**

- Wrapper PID 23798 存活（03:01:47），Python PID 27234 存活（02:02:20）
- random strategy **已完成**（14:25:48）
- 当前训练: **embedding_distance strategy, epoch 2, step 1000**（starcoder2-3b）

### eval 指标
| checkpoint | val_loss | R@1 | R@5 | R@10 |
|-----------|----------|-----|-----|------|
| eval@500 (best) | **0.5140** | 0.4800 | 0.9826 | 1.0 |
| eval@1000 | 待出 | — | — | — |

eval@1000 即将产出。embedding 完成后 wrapper 会自动尝试 dataflow（此前 OOM 过）。

### dataflow retry 脚本
`/root/structfuse/run_plan013_dataflow_retry.sh` 已就绪，降参数（batch=2, neg=3）避免 OOM。

## flash-attn
- **已安装**: flash_attn 2.8.3
- 编译进程 PID 12207 已结束

## 需要处理的事项
1. **m2_embed_verify**: random 即将完成，需要手动启动 embedding 和 dataflow 策略（wrapper 已死）
2. **plan_013_starcoder**: embedding 正常运行中，关注 eval@1000 结果；embedding 完成后观察 dataflow 是否 OOM
3. 两个实验的 random 策略结果对比：Qwen2.5-Coder-3B 的 R@1（0.5357）优于 starcoder2-3b（starcoder eval@500 val_loss=0.5140 vs Qwen 的 0.4834）
