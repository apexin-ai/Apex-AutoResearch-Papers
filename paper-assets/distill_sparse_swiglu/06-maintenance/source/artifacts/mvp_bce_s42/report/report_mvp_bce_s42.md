# 实验报告: mvp_bce_s42

## 状态: 训练成功完成

- EXIT_CODE=0，跑满 1000/1000 steps
- 训练耗时：~25 min 31 sec（19:58:15 → 20:23:46 CST）
- 服务器：westd-34887, GPU 0

## 训练配置

| 参数 | 值 |
|------|-----|
| 模型 | Llama 3.1 8B（冻结） |
| Predictor | rank-128 MLP |
| 可训练参数 | 75,960,320 / 8,030,261,248 (0.946%) |
| Loss 类型 | BCE |
| 数据集 | WikiText-103 train |
| Batch size | 4 |
| Seq length | 2048 |
| LR | 1e-3 (cosine → 0) |
| Sparsity target | 0.5 |
| Seed | 42 |

## Loss 曲线

| Step | Total Loss | BCE Loss | Reg Loss | Sparsity | LR |
|------|-----------|----------|----------|----------|-----|
| 100 | 0.6711 | 0.6628 | 0.0082 | 0.582 | 1.00e-03 |
| 200 | 0.6570 | 0.6505 | 0.0066 | 0.566 | 9.70e-04 |
| 300 | 0.6498 | 0.6440 | 0.0057 | 0.557 | 8.83e-04 |
| 400 | 0.6464 | 0.6409 | 0.0055 | 0.555 | 7.50e-04 |
| 500 | 0.6473 | 0.6417 | 0.0056 | 0.556 | 5.87e-04 |
| 600 | 0.6445 | 0.6394 | 0.0051 | 0.551 | 4.13e-04 |
| 700 | 0.6435 | 0.6383 | 0.0051 | 0.551 | 2.50e-04 |
| 800 | 0.6442 | 0.6392 | 0.0051 | 0.551 | 1.17e-04 |
| 900 | 0.6423 | 0.6372 | 0.0051 | 0.551 | 3.02e-05 |
| 1000 | 0.6430 | 0.6379 | 0.0051 | 0.551 | 0.00e+00 |

**最终 loss：0.6430**（BCE=0.6379, Reg=0.0051）

Loss 从 0.6711 降至 0.6430（降幅 4.2%）。Step 400 后基本收敛，plateau 在 ~0.643。Sparsity 从初始 0.582 收敛到 0.551（目标 0.5）。

## Checkpoint

- 路径：`/root/distill_sparse_swiglu/checkpoints/mvp_bce_s42/predictor_bce.pt`
- 大小：145 MB

## Eval 脚本

训练过程未执行 eval。Eval 脚本已就绪：

- 路径：`/root/distill_sparse_swiglu/src/evaluate.py`
- 功能：TEAL 全局分配 + WikiText-2 / C4 perplexity 评测（dense baseline + sparse）
- 运行命令：
  ```bash
  python src/evaluate.py \
    --checkpoint /root/distill_sparse_swiglu/checkpoints/mvp_bce_s42/predictor_bce.pt \
    --sparsity_target 0.5 --gpu 0
  ```

## Warnings

- HF Hub 未认证请求警告（无影响）
- 无 error / exception / traceback
