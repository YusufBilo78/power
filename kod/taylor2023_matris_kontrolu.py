"""Taylor & Dominguez-Garcia (2023, arXiv 2311.10880) ornegini dogrudan cozer.

Makalenin ekindeki karmasik->reel donusum matrisi
    M = [[r, -x], [r, x]]
olarak basilmis. Karmasik carpimin (r + jx)(mu + j nu) dogru reel karsiligi ise
    M = [[r, -x], [x, r]].
Bu script iki formu da ayni ayirma testiyle cozer ve kapali form sonuclarla karsilastirir.

Ayirma testi (sabit theta icin, konveks):
    sigma(theta) = min_{x} max(||lambda_0||^2, ||lambda_1||^2)
    theta ayirir  <=>  sigma(theta) >= 1
sigma(t*d) her yon d icin t'de monoton artan oldugundan, her yonde ikiye bolme ile
esik bulunur; yonler uzerinde minimum alinir.

Kapali formlar (pozitif bilesen blogu bilgi tasimaz: rakip i+ = e+ = 0 secer):
    standart form : |theta|min = 2 / |z- - zf|
    basili form   : |theta|min = sqrt(2) / max(|dr|, |dx|)

Calistirma:  python kod/taylor2023_matris_kontrolu.py
"""
import numpy as np
import cvxpy as cp

Z_MINUS = Z_PLUS = 30 + 35j


def m_standard(z):
    return np.array([[z.real, -z.imag], [z.imag, z.real]])


def m_printed(z):
    return np.array([[z.real, -z.imag], [z.real, z.imag]])


def sigma(theta, zf, M):
    e_m, e_p, i_p = cp.Variable(2), cp.Variable(2), cp.Variable(2)
    w = cp.Variable()
    r0 = cp.hstack([e_m - M(Z_MINUS) @ theta, e_p - M(Z_PLUS) @ i_p])
    r1 = cp.hstack([e_m - M(zf) @ theta, e_p - M(zf) @ i_p])
    cp.Problem(cp.Minimize(w), [cp.sum_squares(r0) <= w,
                                cp.sum_squares(r1) <= w]).solve(solver=cp.CLARABEL)
    return w.value


def min_theta(xf, M, n_dir=36, tol=1e-4):
    zf = 26 + 1j * xf
    best = np.inf
    for a in np.linspace(0, np.pi, n_dir, endpoint=False):  # sigma(-th) = sigma(th)
        d = np.array([np.cos(a), np.sin(a)])
        lo, hi = 0.0, 3.0
        while hi - lo > tol:
            mid = (lo + hi) / 2
            if sigma(mid * d, zf, M) >= 1:
                hi = mid
            else:
                lo = mid
        best = min(best, hi)
    return best


if __name__ == "__main__":
    print(f"{'xf':>4} {'standart (sayisal)':>19} {'2/|dz|':>8} {'basili (sayisal)':>17} {'sqrt2/max':>10}")
    for xf in (12, 25, 34, 35, 58):
        dz = Z_MINUS - (26 + 1j * xf)
        print(f"{xf:>4} {min_theta(xf, m_standard):>19.4f} {2 / abs(dz):>8.4f} "
              f"{min_theta(xf, m_printed):>17.4f} "
              f"{np.sqrt(2) / max(abs(dz.real), abs(dz.imag)):>10.4f}")
