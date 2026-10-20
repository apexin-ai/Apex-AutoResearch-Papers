# Archive Report — irt_personfit_contam

**Date**: 2026-05-26 04:42 UTC  
**Server**: westd-35694 (root)

## 1. 活跃进程检查

- **GPU**: 4x NVIDIA RTX PRO 6000 Blackwell (96GB each), 全部空闲, 0% utilization, 无 GPU 进程
- **Python 进程**: 无活跃训练进程（仅系统服务: JupyterLab, TensorBoard, autopanel）
- **结论**: 可安全回收

## 2. 归档子目录

归档根: `/root/irt_personfit_contam_archive/`

| 子目录 | 大小 | 内容 |
|--------|------|------|
| `checkpoints/` | 20G | pilot(11G), llama(4.5G), mistral(2.7G), arcc(948M), post_rl(445M) |
| `code/` | 111M | anon_repo(.git), ConStat(.git), irt_personfit_contam, ctrl_contam_{pilot,llama,mistral,arcc}, post_rl_contam, standalone scripts, baseline/constat comparison |
| `data/` | 111M | pilot/llama/mistral/post_rl contamination training data (clean/contam splits at 5/15/25/50%) |
| `results/` | 40M | experiment results, wandb_pilot, logs, standalone JSON results |
| `paper/` | 712K | figures |

## 3. 归档总大小

**20G**

## 4. Tarball

未生成（确认 S3 权限不足后中止了 tar 进程）。

## 5. S3 上传

**失败** — IAM 用户权限不足。

```
User: arn:aws:iam::297645381734:user/agent-ml-be-backup
Error: not authorized for s3:PutObject or s3:ListBucket on s3://agent-ml-manager-backups-emnlp
```

**需要操作**: 为 IAM 用户 `agent-ml-be-backup` 添加以下权限:
- `s3:PutObject` on `arn:aws:s3:::agent-ml-manager-backups-emnlp/project-archive/irt_personfit_contam/*`
- `s3:ListBucket` on `arn:aws:s3:::agent-ml-manager-backups-emnlp`

## 6. S3 验证

N/A

## 备注

- 原始数据保留在 `/root/autodl-tmp/`（未删除）
- 归档副本在 `/root/irt_personfit_contam_archive/`
