DCOL Feature-Based Training Code (src/dcol_train.py)

架构: 19-dim → MLP(128→64) → projection(32) + classification(4)
Loss: L_DCOL = L_attractive + L_repulsive + λ*L_CE (N-pair contrastive, margin按深度差缩放)
Dry-run: 20k samples, 2 epoch, loss 1.53→1.25, acc 73.9%
评估: 4-class acc+CI, 3-class d1-d3, per-class recall, pairwise AUC, confusion matrix, t-SNE/PCA
CLI: argparse (--data_dirs, --epochs, --alpha, --beta, --lambda_ce, etc.)
服务器路径: /root/autodl-tmp/recursive_gen_depth_est/src/dcol_train.py