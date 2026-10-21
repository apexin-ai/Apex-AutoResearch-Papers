// 2PL+γ IRT model (for baseline 2: single-signal)
// P(y_ij = 1) = inv_logit(a_j * (theta_i - b_j) + gamma * exposure_ij)

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
  // Priors
  theta ~ std_normal();
  a ~ lognormal(0, 0.5);
  b ~ std_normal();
  gamma ~ std_normal();

  // Likelihood
  for (i in 1:N_models) {
    for (j in 1:N_items) {
      y[i, j] ~ bernoulli_logit(a[j] * (theta[i] - b[j]) + gamma * exposure[i, j]);
    }
  }
}

generated quantities {
  // Calibrated scores: P(y=1 | exposure=0)
  array[N_models] real calibrated_score;
  for (i in 1:N_models) {
    real total = 0.0;
    for (j in 1:N_items) {
      total += inv_logit(a[j] * (theta[i] - b[j]));
    }
    calibrated_score[i] = total / N_items;
  }

  // Log-likelihood for LOO-CV
  vector[N_models * N_items] log_lik;
  {
    int idx = 0;
    for (i in 1:N_models) {
      for (j in 1:N_items) {
        idx += 1;
        log_lik[idx] = bernoulli_logit_lpmf(y[i, j] | a[j] * (theta[i] - b[j]) + gamma * exposure[i, j]);
      }
    }
  }
}
