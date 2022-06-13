frameworks=[
    ["django" , "python" , 4],
    ["flask" ,"python",3],
    ["spring","javascript",5],
    ["express","javascript",4,
    ["angular","typescript",4]]
]

ret=[fw for fw in frameworks if fw[1]=="python"]
print(ret)

rating_gt_3=[ar for ar in frameworks if ar[2]>3]
print(rating_gt_3)