from typing import Tuple, Dict


# kws and factors are tuples with same size, prices is dict {limit: price}
def cost(kws: Tuple[float, float], factors: Tuple[float, float],
         prices: Dict[float, float]) -> float:
    payment = 0.0
    limits = sorted(prices.keys())
    common = sum(kws)
    factor = sum([kws[i] / common * factors[i] for i in range(len(kws))])
    unpaid = common - limits[0]  # if limits[0] > 0
    i = 0

    def pay_for(kws: float) -> None:
        nonlocal payment, unpaid
        payment += kws * prices[limits[i - 1]] * factor
        unpaid -= kws

    for i in range(1, len(limits)):
        arange = limits[i] - limits[i - 1]
        pay_for(unpaid if unpaid < arange else arange)
        if unpaid <= 0:
            break
    if unpaid > 0:
        payment += unpaid * prices[limits[i]] * factor
    return payment / 100  # to hryvnia
