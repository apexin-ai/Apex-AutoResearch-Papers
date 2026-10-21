// 2PL + gamma contamination parameter
// P(y_ij = 1) = inv_logit(a_j * (theta_i - b_j) + gamma * exposure_ij)
// No guessing (c) or upper asymptote (d) parameters

data {
  int<lower=1> N_models;
  int<lower=1> N_items;
  array[N_models, N_items] int<lower=0, upper=1> y;
  matrix[N_models, N_items] exposure;
}

parameters {
  vector[N_models] theta;
  vector<lower=0>[N_items] a;
  vector[N_items] b;
  real gamma;
}

model {
  theta ~ std_normal();
  a ~ lognormal(0, 0.5);
  b ~ std_normal();
  gamma ~ std_normal();

  for (i in 1:N_models) {
    for (j in 1:N_items) {
      real eta = a[j] * (theta[i] - b[j]) + gamma * exposure[i, j];
      y[i, j] ~ bernoulli_logit(eta);
    }
  }
}

generated quantities {
  // Calibrated scores: P(y=1 | exposure=0)
  array[N_models] real calibrated_score;
  for (i in 1:N_models) {
    real total = 0.0;
    for (j in 1:N_items) {
      real eta_clean = a[j] * (theta[i] - b[j]);
      total += inv_logit(eta_clean);
    }
    calibrated_score[i] = total / N_items;
  }

  vector[N_models * N_items] log_lik;
  {
    int idx = 0;
    for (i in 1:N_models) {
      for (j in 1:N_items) {
        idx += 1;
        real eta = a[j] * (theta[i] - b[j]) + gamma * exposure[i, j];
        log_lik[idx] = bernoulli_logit_lpmf(y[i, j] | eta);
      }
    }
  }
}
