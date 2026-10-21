// Vanilla 2PL IRT (no gamma, no log_lik for memory efficiency)
data {
  int<lower=1> N_models;
  int<lower=1> N_items;
  array[N_models, N_items] int<lower=0, upper=1> y;
}

parameters {
  vector[N_models] theta;
  vector<lower=0>[N_items] a;
  vector[N_items] b;
}

model {
  theta ~ std_normal();
  a ~ lognormal(0, 0.5);
  b ~ std_normal();

  for (i in 1:N_models) {
    for (j in 1:N_items) {
      real eta = a[j] * (theta[i] - b[j]);
      y[i, j] ~ bernoulli_logit(eta);
    }
  }
}

generated quantities {
  array[N_models] real calibrated_score;
  for (i in 1:N_models) {
    real total = 0.0;
    for (j in 1:N_items) {
      real eta_clean = a[j] * (theta[i] - b[j]);
      total += inv_logit(eta_clean);
    }
    calibrated_score[i] = total / N_items;
  }
}
