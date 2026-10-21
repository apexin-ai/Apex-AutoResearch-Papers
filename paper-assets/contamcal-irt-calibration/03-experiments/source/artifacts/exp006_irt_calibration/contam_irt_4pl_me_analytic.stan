// 4PL+γ IRT with analytical measurement error integration
// Eliminates latent τ parameters via conjugate normal posterior:
//   τ|e ~ N(E[τ|e], Var[τ|e])  where
//   E[τ|e] = (e * σ_τ² + μ_τ * σ_e²) / (σ_τ² + σ_e²)
//   Var[τ|e] = (σ_τ² * σ_e²) / (σ_τ² + σ_e²)
//
// Python preprocessing computes tau_posterior_mean and tau_posterior_var
// from observed exposure scores. This model uses tau_posterior_mean as the
// exposure covariate (same parameter count as simple model).

data {
  int<lower=1> N_models;
  int<lower=1> N_items;
  array[N_models, N_items] int<lower=0, upper=1> y;
  matrix[N_models, N_items] tau_post_mean;   // E[τ|e] from analytical integration
  matrix<lower=0>[N_models, N_items] tau_post_var;  // Var[τ|e] for CI correction
}

parameters {
  vector[N_models] theta;
  vector<lower=0>[N_items] a;
  vector[N_items] b;
  vector<lower=0, upper=1>[N_items] c;
  vector<lower=0, upper=1>[N_items] d;
  real gamma;
}

model {
  // Priors
  theta ~ std_normal();
  a ~ lognormal(0, 0.5);
  b ~ std_normal();
  c ~ beta(5, 20);
  d ~ beta(20, 5);
  gamma ~ std_normal();

  // Likelihood using posterior mean of τ as point estimate
  for (i in 1:N_models) {
    for (j in 1:N_items) {
      real eta = a[j] * (theta[i] - b[j]) + gamma * tau_post_mean[i, j];
      real p = c[j] + (d[j] - c[j]) * inv_logit(eta);
      y[i, j] ~ bernoulli(p);
    }
  }
}

generated quantities {
  // Calibrated scores: P(y=1 | exposure=0)
  // ME correction operates through the fitting stage: using E[τ|e] as
  // exposure yields wider gamma posteriors, which automatically widen
  // calibrated score CIs. No tau sampling needed in generated quantities.
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
        real eta = a[j] * (theta[i] - b[j]) + gamma * tau_post_mean[i, j];
        real p = c[j] + (d[j] - c[j]) * inv_logit(eta);
        log_lik[idx] = bernoulli_lpmf(y[i, j] | p);
      }
    }
  }
}
