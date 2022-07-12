# avg 求平均值
awk '{sum += $1; count+=1;} END{ print sum/count}'

# sum 求和
awk '{sum += $1;} END{ print sum}'


# group_avg 分组求平均值，按照第1列聚合，第2列求平均值
#!/bin/bash
awk 'NR>0{
    arr[$1]   += $2
    count[$1] += 1
}
END{
    for (a in arr) {
        print a "\t" arr[a] / count[a]
    }
}'

# group_sum 分组求和，按照第1列聚合，第2列求和
#!/bin/bash
awk 'NR>0{
    sums[$1]   += $2
    count[$1] += 1
}
END{
    for (key in sums) {
        print key "\t" sums[key] "\t" count[key]
    }
}'
