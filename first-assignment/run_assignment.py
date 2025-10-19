import numpy as np

def ridge_weights(X, y, lam):
    """Closed-form ridge regression weights.
    X: (n,d), y: (n,)
    returns w of shape (d,)
    """
    d = X.shape[1]
    A = X.T @ X + lam * np.eye(d)
    b = X.T @ y
    w = np.linalg.solve(A, b)
    return w


def update_posterior(lambda0, sigma2, X_batch, y_batch, old_xx, old_xy):
    # old_xx is sum X^T X accumulated, old_xy is sum X^T y
    old_xx = old_xx + X_batch.T @ X_batch
    old_xy = old_xy + X_batch.T @ y_batch
    new_var_inv = lambda0 * np.eye(old_xx.shape[0]) + (1.0 / sigma2) * old_xx
    new_var = np.linalg.inv(new_var_inv)
    sigma_temp = lambda0 * sigma2 * np.eye(old_xx.shape[0]) + old_xx
    new_mean = np.linalg.solve(sigma_temp, old_xy)
    return new_var, new_mean, old_xx, old_xy


def active_learning(lambda0, sigma2, X_train, y_train, X_pool, k=10):
    d = X_train.shape[1]
    # start with empty measured set but incorporate existing training data
    old_xx = np.zeros((d, d))
    old_xy = np.zeros(d)
    # incorporate X_train, y_train as initial measured data
    old_xx += X_train.T @ X_train
    old_xy += X_train.T @ y_train
    var_inv = lambda0 * np.eye(d) + (1.0 / sigma2) * old_xx
    new_var = np.linalg.inv(var_inv)
    new_mean = np.linalg.solve(lambda0 * sigma2 * np.eye(d) + old_xx, old_xy)
    w_rr = new_mean

    pool = X_pool.copy()
    indices = list(range(pool.shape[0]))
    selected = []

    for _ in range(k):
        # predictive variance for each pool point = x^T new_var x
        # compute diagonal efficiently
        variances = np.einsum('ij,jk,ik->i', pool, new_var, pool)
        idx = int(np.argmax(variances))
        selected_idx = indices[idx]
        selected.append(selected_idx + 1)  # 1-based as in notebook
        x_sel = pool[idx:idx+1, :]
        y_sel = (x_sel @ w_rr).ravel()
        # update posterior with this newly measured point
        new_var, new_mean, old_xx, old_xy = update_posterior(lambda0, sigma2, x_sel, y_sel, old_xx, old_xy)
        w_rr = new_mean
        # remove selected from pool
        pool = np.delete(pool, idx, axis=0)
        indices.pop(idx)
    return w_rr, selected


if __name__ == '__main__':
    X_train = np.genfromtxt('X_train-2.csv', delimiter=',')
    y_train = np.genfromtxt('y_train-1.csv')
    X_test = np.genfromtxt('X_test.csv', delimiter=',')

    lam = 5.0
    sigma2 = 2.0

    w = ridge_weights(X_train, y_train, lam)
    print('Ridge weights (first 10):', np.round(w[:10], 6))

    w_rr, selected = active_learning(lam, sigma2, X_train, y_train, X_test, k=10)
    print('First 10 selected measurement indices (1-based):', selected)
    print('Posterior mean weights (first 10):', np.round(w_rr[:10], 6))
