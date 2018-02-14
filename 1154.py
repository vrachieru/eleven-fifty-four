# This mess is based on the Gibbons spigot generator of pi digits
# http://www.cs.ox.ac.uk/people/jeremy.gibbons/publications/spigot.pdf

q, r, t, k, n, l, p, d, c = 1, 0, 1, 1, 3, 3, 0, -2, 0

while c != 11:
    if 4 * q + r - t < n * t:
        if p * 10 + n == 54:
            c += 1
        q, r, t, k, n, l, p, d = (10 * q, 10 * (r - n * t), t, k, (10 * (3 * q + r)) // t - 10 * n, l, n, d + 1)
    else:
        q, r, t, k, n, l = (q * k, (2 * q + r) * l, t * l, k + 1, (q * (7 * k + 2) + r * l) // (t * l), l + 2)

print (d == 1154)