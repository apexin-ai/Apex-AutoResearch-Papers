// Vanilla 4PL IRT without contamination parameter gamma
// P(y_ij = 1) = c_j + (d_j - c_j) * inv_logit(a_j * (theta_i - b_j))

data {
  int<lower=1> N_models;
  int<lower=1> N_items;
  array[N_models, N_items] int<lower=0, upper=1> y;
}

parameters {
  vector[N_models] theta;
  vector<lower=0>[N_items] a;
  vector[N_items] b;
  vector<lower=0.001, upper=0.999>[N_items] c;
  vector<lower=0.001, upper=0.999>[N_items] d;
}

model {
  theta ~ std_normal();
  a ~ lognormal(0, 0.5);
  b ~ std_normal();
  c ~ beta(5, 20);
  d ~ beta(20, 5);

  for (i in 1:N_models) {
    for (j in 1:N_items) {
      real eta = a[j] * (theta[i] - b[j]);
      real p = c[j] + (d[j] - c[j]) * inv_logit(eta);
      y[i, j] ~ bernoulli(p);
    }
  }
}

generated quantities {
  array[N_models] real calibrated_score;
  for (i in 1:N_models) {
    real total = 0.0;
    for (j in 1:N_items) {
      real eta = a[j] * (theta[i] - b[j]);
      real p = c[j] + (d[j] - c[j]) * inv_logit(eta);
      total += p;
    }
    calibrated_score[i] = total / N_items;
  }

  vector[N_models * N_items] log_lik;
  {
    int idx = 0;
    for (i in 1:N_models) {
      for (j in 1:N_items) {
        idx += 1;
        real eta = a[j] * (theta[i] - b[j]);
        real p = c[j] + (d[j] - c[j]) * inv_logit(eta);
        log_lik[idx] = bernoulli_lpmf(y[i, j] | p);
      }
    }
  }
}
