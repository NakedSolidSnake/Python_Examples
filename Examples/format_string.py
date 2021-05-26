ssr_list = []
ssr_str = '"family": {}, "codes":"{}"'

for i in range(64):
    ssr = ssr_str.format(i, "FFFFFFFFFFFFFFFF")
    ssr_list.append(ssr)
	# ssr_list.append(ssr)

print(ssr_list)





