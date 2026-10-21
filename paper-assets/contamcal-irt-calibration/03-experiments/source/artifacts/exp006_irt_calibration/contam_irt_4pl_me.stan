// 4PL+γ IRT with measurement error on exposure
// P(y_ij = 1) = c_j + (d_j - c_j) * inv_logit(a_j * (theta_i - b_j) + gamma * tau_ij)
// exposure_ij ~ N(tau_ij, sigma_e^2) where tau_ij is latent true exposure

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
  vector<lower=0.001, upper=0.999>[N_items] c;
  vector<lower=0.001, upper=0.999>[N_items] d;
  real gamma;
  matrix[N_models, N_items] tau;
  real<lower=1e-4> sigma_e;
}

model {
  // Priors
  theta ~ std_normal();
  a ~ lognormal(0, 0.5);
  b ~ std_normal();
  c ~ beta(5, 20);
  d ~ beta(20, 5);
  gamma ~ std_normal();
  sigma_e ~ normal(0, 0.5);

  // Latent exposure prior (weakly informative)
  to_vector(tau) ~ std_normal();

  // Measurement error model
  to_vector(exposure) ~ normal(to_vector(tau), sigma_e);

  // Likelihood
  for (i in 1:N_models) {
    for (j in 1:N_items) {
      real eta = a[j] * (theta[i] - b[j]) + gamma * tau[i, j];
      real p = c[j] + (d[j] - c[j]) * inv_logit(eta);
      y[i, j] ~ bernoulli(p);
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
      real p_clean = c[j] + (d[j] - c[j]) * inv_logit(eta_clean);
      total += p_clean;
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
        real eta = a[j] * (theta[i] - b[j]) + gamma * tau[i, j];
        real p = c[j] + (d[j] - c[j]) * inv_logit(eta);
        log_lik[idx] = bernoulli_lpmf(y[i, j] | p);
      }
    }
  }
}
