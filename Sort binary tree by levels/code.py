def tree_by_levels(node):
    res = []
    lst = [node]
    while lst:
        new = []
        for i in lst:
            if not i:
                continue
            res.append(i.value)
            if i.left:
                new.append(i.left)
            if i.right:
                new.append(i.right)
        lst = new
    return res
