# SparseTSF ETTm1 Horizon-96 MSE Formal Task

This task uses the official SparseTSF model from `lss-1138/SparseTSF` and the original ETTm1 split for multivariate long-term forecasting with `seq_len=720` and `pred_len=96`.

The paper anchor is the ICML 2024 official SparseTSF result on ETTm1 horizon 96: MSE `0.314`. The budget baseline uses the official ETTm1 linear script hyperparameters but only trains for 1 epoch. The score is normalized as `(budget_baseline_mse - agent_mse) / (budget_baseline_mse - 0.314)`.
